import requests


class API_CLIENT:
    def __init__(self,base_url,username,password) -> None:
        self.base_url = base_url
        self.username = username
        self.password = password
        self.token = None
        self.header = {"Content-Type": "application/json"}
    def login(self):
        login_url = f"{self.base_url}/login"
        responce = requests.post(login_url,auth=(self.username,self.password))
        responce.raise_for_status()
        self.token = responce.json()['token']
        self.header["Authorization"] = f"Bearer {self.token}"
        print("Login successful, token acquired.")
    
    def get(self,endpoint):
        url = f"{self.base_url}\{endpoint}"
        responce = requests.get(url=url,headers=self.header)
        responce.raise_for_status()
        return responce.json()

    
    def put(self,endpoint,payload):
        url = f"{self.base_url}\{endpoint}"
        responce = requests.put(url=url,headers=self.header,json=payload)
        responce.raise_for_status()
        return responce.json
    
    
        
    