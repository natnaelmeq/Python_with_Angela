import requests
from datetime import datetime

USERNAME = "natiman123"
TOKEN = "kfdlfjldjfldhflædfhd58f8888"
GRAPHID = "graph1"

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"

}
# response= requests.post(url=pixela_endpoint,json=user_params)
# print(response.text)


graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id":GRAPHID ,
    "name": "Go to Gym",
    "unit": "KM",
    "type": "float",
    "color": "sora"
}

headers = {
    "X-USER-TOKEN": TOKEN
}
# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

#Create new pixel

create_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPHID}"

today = datetime.now()
print(today.strftime("%Y%m%d"))

create_pixel_params ={
    "date": today.strftime("%Y%m%d"),
    "quantity": "2",
}

response_pixel = requests.post(url=create_pixel_endpoint,json=create_pixel_params,headers=headers)


