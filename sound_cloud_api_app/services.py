import soundcloud,sys


class SingletonType(type):
    def __call__(cls,*args,**kwargs):  # @NoSelf
        try:
            return cls.__instance
        except AttributeError:
            cls.__instance = super(SingletonType, cls).__call__(*args, **kwargs)
            return cls.__instance

class SoundCloudApiService:
    __metaclass__ = SingletonType
    
    def __init__(self):
        self.client_id = '2255e5d6063b906993b59e4831b9c7e9'
        self.client_secret = '1b30faa4afd71e103b76c1e7a71f25d3'
        self.redirect_uri = 'http://127.0.0.1:8000/soundcloud/api_data'
    
    def get_connection(self):
        try:
            client = soundcloud.Client(client_id = self.client_id,client_secret=self.client_secret,redirect_uri=self.redirect_uri)
        except:
            raise Exception(sys.exc_info()[1])   
        else:
            return client

# class_dict = {'SoundCloudApiService':SoundCloudApiService}
         
class SoundCloudApiFactory():   
    __metaclass__  = SingletonType
    
    def __init__(self):
        self.instance = SoundCloudApiService()
        
    def get_api_connection(self):
        return self.instance.get_connection()
    
    def get_authorize_url(self):
        return self.get_api_connection().authorize_url()
        