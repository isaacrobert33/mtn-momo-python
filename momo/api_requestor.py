import requests

class APIRequestor(object):
    def __init__(self, sub_key, headers={}) -> None:
        self.headers = {
            "Ocp-Apim-Subscription-Key":  sub_key,
            "Content-Type": "application/json",
            "Host": "sandbox.momodeveloper.mtn.com",
            **headers
        }
    
    def request(self, method, url, data=None, **kwargs):
        response = getattr(requests, method)(
            url, data, headers={**self.headers, **kwargs.get("headers", {})}
        )
        try:
            response_json = response.json()
        except:
            return
        
        return response_json, response.status_code
    
