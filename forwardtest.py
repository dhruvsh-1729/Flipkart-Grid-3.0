import requests
from requests.models import requote_uri

UrlForward="http://192.168.0.106/Forward"
Urlsleft="http://192.168.0.106/sleft"
Urlsright="http://192.168.0.106/sright"
UrlLeft="http://192.168.0.106/Left"
UrlRight="http://192.168.0.106/Right"
UrlFlip="http://192.168.0.106/Flip"
UrlStop="http://192.168.0.106/Stop"


r=requests.get(url=UrlForward)
# for i in range(0,6):
#     r=requests.get(url=UrlForward)
# r=requests.get(url=UrlFlip)
# r=requests.get(url=UrlRight)
# for i in range(0,9):
#     r=requests.get(url=Urlsright)

# for i in range(0,6):
#     r=requests.get(url=UrlForward)
# r=requests.get(url=UrlFlip)
# r=requests.get(url=UrlLeft)
# for i in range(0,9):
#     r=requests.get(url=Urlsleft)

# i=0
# while i<3:
#     for i in range(0,6):
#     r=requests.get(url=UrlForward)
#     r=requests.get(url=UrlFlip)  
# r=requests.get(url=UrlRight)
# for i in range(0,9):
#     r=requests.get(url=Urlsright)

# for i in range(0,6):
#     r=requests.get(url=UrlForward)
# r=requests.get(url=UrlFlip)
# r=requests.get(url=UrlLeft)
# for i in range(0,9):
#     r=requests.get(url=Urlsleft)




        