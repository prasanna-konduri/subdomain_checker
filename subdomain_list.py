import requests

class SubdomainList:
    def __init__(self,domain_name:str):
        self.domain_name = domain_name
        self.subdomainsFile = "assets/subdomains.txt" 
        self.subdomainsList =self.getALL()

    def getALL(self):

        print(f"Getting all sub domains for {self.domain_name}")  
        sub_domains_list = []
        sub_domains = self.getSubDomains()

        for subdomain in sub_domains:
            url = f"https://{subdomain}.{self.domain_name}"
            try:
                requests.get(url)
                sub_domains_list.append(url)
            except requests.ConnectionError:
                pass
        
        print(f"{len(sub_domains_list)} sub domains found")
        return sub_domains_list

    
    def getSubDomains(self):

        with open(self.subdomainsFile,'r') as file:
            name = file.read()
            sub_domains = name.splitlines()
            
        return sub_domains