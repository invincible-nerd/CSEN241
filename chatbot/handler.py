import datetime
import requests

def handle(req):

    if req=="name":
        print("My name is CSEN241 Chatbot!")
        return "My name is CSEN241 Chatbot!"
    elif req=="time":
        now = datetime.datetime.now()
        time=now.strftime("%Y-%m-%d %H:%M:%S")
        print(time)
        return time     
    else:
        figlet_url = "http://10.62.0.5:8080/function/figlet"
        response = requests.post(figlet_url, data="Hello, World!")
        return response.text
    

# req="n"
# if req=="name":
#     s="My name is CSEN241 Chatbot!" 
# elif req=="time":
#     now = datetime.datetime.now()
#     s=now.strftime("%Y-%m-%d %H:%M:%S")
# else:
#     s="hhh"
# print(s)            