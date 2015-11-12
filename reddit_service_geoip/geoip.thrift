include "baseplate.thrift"

struct GeoIpRecord {
  1: required string country_code;
  2: required string country_name;
}

service GeoipService extends baseplate.BaseplateService {
  GeoIpRecord get_country(1:string ip_address),
}
