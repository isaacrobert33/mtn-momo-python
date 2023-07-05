from utils import SANDBOX_URL
from api_requestor import APIRequestor
import uuid

class UserProvisioning(object):
    def __init__(self, sub_key, ref_id=None) -> None:
        self.url = SANDBOX_URL+f"/apiuser"
        self.ref_id = ref_id
        
        self.requestor = APIRequestor(sub_key=sub_key)
    
    def create_user(self, callback=""):
        data = {
            "providerCallbackHost": callback
        }
        self.ref_id = uuid.uuid4().__str__()
        headers = {
            "X-Reference-Id": self.ref_id,
        }
        response = self.requestor.request("post", url=self.url, data=data, headers=headers)
        if response[1] == 201:
            return True
        else:
            return False
    
    @property
    def user(self, ref_id=None):
        url = self.url+f"/{ref_id if ref_id else self.ref_id}"
        response = self.requestor.request("get", url=url)
        return response[0]
    
    @property
    def api_key(self, ref_id=None):
        url = self.url+f"/{ref_id if ref_id else self.ref_id}/apikey"
        response = self.requestor.request("post", url=url)
        return response[0].get("apiKey")

    
# # 
# user = UserProvisioning(sub_key="7f58138a101041f2b26d4bb04c3d02e1", ref_id="46223256-8e88-4982-ab45-b502c97cd32d")
# print(user.api_key)
