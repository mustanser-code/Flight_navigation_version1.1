import requests
import config
# now i have to make class to fetch data from server using get().
class flightextractor:
    def __init__(self,url):
        self.url = url
        print(self.url)
    def get_data(self):
        #catching server request 
        try:
            response = requests.get(self.url)
            if response.status_code == 200:
                print("successFull!")
                return response.json()
        except Exception as E:
            print("Error!",E)
        
raw = flightextractor(config.url)
data = raw.get_data()
print(data)
