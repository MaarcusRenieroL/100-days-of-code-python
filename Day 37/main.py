import requests
TOKEN="d837cr28orcyoe8208r7tc"
USERNAME="marky1706"
pixela_endpoint="https://pixe.la/v1/users"
user_params={
    "token":TOKEN,
    "username":USERNAME,
    "agreeTermsOfService":"yes",
    "notMinor":"yes"
}
# response=requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint=f"{pixela_endpoint}/{USERNAME}/graphs"
graph_config={
    "id":"graph1",
    "name":"Cycling Graph",
    "unit":"Km",
    "type":"float",
    "color":"ajisai"
}

headers={
    "X-USER_TOKEN":TOKEN
}

response=requests.post(url=graph_endpoint, json=graph_config, headers=headers)
print(response.text)