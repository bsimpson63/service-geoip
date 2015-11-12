# service-geoip

start the service: `baseplate-serve --debug example.ini`

query an IP: `python3 -m reddit_service_geoip.geoip_thrift.remote -h localhost:9090 get_country 127.0.0.1`
