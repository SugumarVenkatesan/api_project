import requests,sys

class APIService:
    def __init__(self,api_url,api_params):
        self.api_url = api_url
        self.api_params = api_params
        
    def f1_api_services(self):
        try:
            api_data = requests.api.get(self.api_url,params=self.api_params)
            api_data = api_data.json()
            api_data = api_data['MRData']['StandingsTable']['StandingsLists'][0]
            api_data = api_data['DriverStandings']
        except IndexError:
            raise IndexError(sys.exc_info()[1])
        except:
            raise Exception(sys.exc_info()[1])
        else:
            return api_data
    
