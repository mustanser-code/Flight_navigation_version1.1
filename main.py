import config
from extractor import flightextractor
from transform import flight_transformer

    ## ========== ##
    ## Extract
    ## ========== ##
extractor = flightextractor(config.url)
data = extractor.get_data()
    ## ========== ##
    ## Extract
    ## ========== ##

transform =  flight_transformer(data)

clean = transform.transform()
print(f"Cleaned Data{clean}")
