import requests


class MijnAfvalWijzerClient:
    BASE_API = 'https://api.mijnafvalwijzer.nl/webservices/appsinput'

    def __init__(self, api_key: str):
        self.api_key = api_key
        if not self.api_key:
            raise Exception("No API key provided")

    def get_data(self, zip_code: str = "", house_number: str = "", add_on: str = ""):
        url_parameters = {
            'apikey': self.api_key,
            'method': 'postcodecheck',
            'street': '',
            'toevoeging': add_on,
            'huisnummer': house_number,
            'postcode': zip_code,
            'app_name': 'afvalwijzer',
            'platform': 'phone',
            'afvaldata': '{4}',
            'langs': 'nl',
        }
        response = requests.get(self.BASE_API, params=url_parameters)
        if response.status_code == 200:
            data = response.json()
            if data.get('ophaaldagen') and data['ophaaldagen']['response'] == 'OK':
                return data['ophaaldagen']['data']
        return None
