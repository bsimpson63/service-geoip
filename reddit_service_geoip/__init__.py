import logging

from baseplate import make_metrics_client, config, diagnostics
from baseplate.integration.thrift import BaseplateProcessorEventHandler

from .geoip_thrift import GeoipService
from .geoip_thrift.ttypes import GeoIpRecord

from geoip2.database import Reader
from geoip2.errors import AddressNotFoundError


logger = logging.getLogger(__name__)


class Handler(GeoipService.ContextIface):
    def __init__(self, city_db_path):
        # maxmind docs recommend reusing a Reader across requests
        self.reader = Reader(city_db_path)

    def is_healthy(self, context):
        return True

    def get_country(self, context, ip_address):
        # TODO: add anonymous info (tor/ec2/rackspace/etc)
        try:
            response = self.reader.city(ip_address)
        except AddressNotFoundError:
            country_code = ""
            country_name = ""
        else:
            country_code = response.country.iso_code
            country_name = response.country.name

        return GeoIpRecord(
            country_code=country_code,
            country_name=country_name,
        )


def make_processor(app_config):
    cfg = config.parse_config(app_config, {
        "city_db_path": config.String,
    })

    metrics_client = make_metrics_client(app_config)

    agent = diagnostics.DiagnosticsAgent()
    agent.register(diagnostics.LoggingDiagnosticsObserver())
    agent.register(diagnostics.MetricsDiagnosticsObserver(metrics_client))

    handler = Handler(cfg.city_db_path)
    processor = GeoipService.ContextProcessor(handler)
    event_handler = BaseplateProcessorEventHandler(logger, agent)
    processor.setEventHandler(event_handler)

    return processor
