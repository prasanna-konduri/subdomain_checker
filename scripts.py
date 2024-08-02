from subdomain_checker import SubdomainChecker

if __name__=="__main__":

    domain_name = "herovired.com"

    try:
        subchecker = SubdomainChecker(domain_name)
        subchecker.run()
    except Exception as e:
        print(f"Exception occurred..{e}")
    except KeyboardInterrupt:
        print("Exiting...")