import requests
import time
from prettytable import PrettyTable
from subdomain_list import SubdomainList

class SubdomainChecker:
    def __init__(self,domain_name:str):
        self.domain_name = domain_name
        self.subdomains_list = SubdomainList(self.domain_name).subdomainsList
        self.status_list = []
        

    def run(self):
         while True:
            self.checkSubdomainsStatus()
            self.printTable()
            time.sleep(1)

    def checkSubdomainsStatus(self):
        print('checking Subdomains Status...')

        for subdomain in self.subdomains_list:
             status = self.checkSubdomainStatus(subdomain)
             self.status_list.append((subdomain,status))


    def checkSubdomainStatus(self,subdomain):
        
        try:
            res = requests.get(subdomain)
            if res.status_code == 200:
                status = "Up"
            else:
               status = "Down" 
        except ConnectionError:
                status = "Down"

        return status
    
    def printTable(self):
        status_table = PrettyTable(["Subdomain Name","Status"]) 
        status_table.add_rows(self.status_list)
        print(status_table)
        self.status_list = []
    


      
            
            
