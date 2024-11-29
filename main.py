import whois

def Domain_Info(link):
    domain= whois.whois(url)
    print(f"Server : {domain.whois_server}")
    print(f"Exp Date : {domain.expiration_date}")
    print(f"Name : {domain.name}")
    print(f"Organization : {domain.org}")
    print(f"State : {domain.state}")
    print(f"City : {domain.city}")
    print(f"Country : {domain.country}")

url = input("Enter URL with .com or anything\n")

try:
    domain= whois.whois(url)
except:
    print("Domain is available")

else:
    print("Domain is already purchased\n")
    print("Doamin Info is as follow:-\n")
    Domain_Info(url)