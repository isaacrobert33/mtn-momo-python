import base64
SANDBOX_URL="https://sandbox.momodeveloper.mtn.com/v1_0"


def get_auth(user, apiKey):
    creds = f'{user}:{apiKey}'
    enc = base64.b64encode(creds.encode("utf-8")).decode("utf-8")
    return enc
