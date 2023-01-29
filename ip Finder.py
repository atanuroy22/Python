import requests

linkurl = "https://api.techniknews.net/ipgeo/"
ip = input("Enter ip....")
try:
    respond = requests.get(linkurl+ip).json()
    print(respond)
except:
    print("Try another ip.....")    