from api_requestor import APIRequestor
from utils import get_auth
import uuid

class Remittances(object):
    """
    An Object representing the Remittance Product of the MoMo API. 
    Remit funds to local recipients from the diaspora with ease.
    """
    BASE_URL = "https://sandbox.momodeveloper.mtn.com/remittance"
    BASE_URL_V1 = "https://sandbox.momodeveloper.mtn.com/remittance/v1_0"
    SCOPE = "remittance"

    def __init__(self, sub_key, user_id, api_key, target_env="sandbox", **kwargs):
        headers = {
            "Authorization": get_auth(user_id, api_key),
            "X-Target-Environment": target_env,
            **kwargs
        }
        self.auth_req_id = kwargs.get("auth_req_id")
        self.MSISDN = kwargs.get("msisdn")
        self.request = APIRequestor(sub_key=sub_key, headers=headers).request

    @property
    def access_token(self):
        url = f"{self.BASE_URL}/token"
        response = self.request("post", url)
        self.token_data = response[0]
        return self.token_data["access_token"] if response[1] == 200 else None
    
    @property
    def oauth2_token(self):
        url = f"{self.BASE_URL}/oauth2/token/"
        data = {
            "grant_type": "urn:openid:params:grant-type:ciba",
            "auth_req_id": self.auth_req_id
        }
        response = self.request("post", url, data)
        self.oauth_token_data = response[0]
        return self.oauth_token_data["access_token"] if response[1] == 200 else None

    
    def bc_authorize(self, msisdn=None):
        url = f"{self.BASE_URL}/v1_0/bc-authorize"
        data = {
            "login_hint": f"ID:{msisdn if msisdn else self.MSISDN}",
            "scope": self.SCOPE,
            "access_type": "online"
        }
        response = self.request("post", url, data=data)
        return response[0]
    
    @property
    def get_account_balance(self, currency=None):
        url = f"{self.BASE_URL_V1}/account/balance" if not currency else f"{self.BASE_URL_V1}/account/balance/{currency}"
        response = self.request("get", url)
        return response[0]
    
    def get_basic_user_info(self, msisdn=None):
        url = f"{self.BASE_URL_V1}/accountholder/msisdn/{msisdn if msisdn else self.MSISDN}/basicuserinfo"
        response = self.request("get", url)
        return response[0]
    
    def get_transfer_status(self, reference_id):
        url = f"{self.BASE_URL_V1}/transfer/{reference_id}"
        response = self.request("get", url)
        return response[0]
    
    def get_user_info_with_consent(self):
        url = f"{self.BASE_URL}/oauth2/v1_0/userinfo"
        response = self.request("get", url)
        return response[0]
    
    def transfer(self, amount: int, currency: str, externalId: str, partyId: str, message: str="", note: str=""):
        url = f"{self.BASE_URL_V1}/transfer"
        externalId = f"tranx_{uuid.uuid4().__str__()}" if not externalId else externalId
        data = {
            "amount": amount,
            "currency": currency,
            "externalId": externalId,
            "payee": {
                "partyIdType": "MSISDN",
                "partyId": partyId
            },
            "payerMessage": message,
            "payeeNote": note
        }
        response = self.request("post", url, data)
        return True if response[1] == 202 else False
    
    def validate_account_holder_status(self, holder_id_type, holder_id):
        url = f"{self.BASE_URL_V1}/accountholder/{holder_id_type}/{holder_id}/active"
        response = self.request("get", url)
        return True if response[1] == 202 else False


    
