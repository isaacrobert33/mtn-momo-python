

class Remittances(object):
    """
    An Object representing the Remittance Product of the MoMo API. 
    Remit funds to local recipients from the diaspora with ease.
    """

    @property
    def product_url(cls):
        return "/remittances/v1_0/"
    
