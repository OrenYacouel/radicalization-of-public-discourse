
openai_api_key ="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"


class bot:
    def __init__(self, apikey, api_secret, access_token, access_token_secret, bearer_token ):
        self.apikey = apikey
        self.api_secret = api_secret
        self.bearer_token = bearer_token
        self.access_token = access_token
        self.access_token_secret = access_token_secret

     
    def print(self):
        print("API Key: " + self.apikey)
        print("API Secret: " + self.api_secret)
        print("Bearer Token: " + self.bearer_token)
        print("Access Token: " + self.access_token)
        print("Access Token Secret: " + self.access_token_secret)

    
barakadizibros = bot('HLn10AtYu9sDWYblZzRWAxde2', 'oqCf888MJ3tiIhfQhoowlfPFsUlK5i9mpMT69Jz8Lu03o2GCSS', 'AAAAAAAAAAAAAAAAAAAAAMa4ngEAAAAABcqzY2E6cphd%2BbOxfkNmOAEuonc%3DyiXYzUj4Gasb4WiZV7Ms6XI84otl5DE4f38XGfVbuphINHLDVr', '1660304001278042113-Hq29VDJl21yqkS2gf8dm9A9EQbhURO', 'isSBPy38K4H9jiuHj4Ov0bBNdSTejLayvgm6oNRDoIzvX')
