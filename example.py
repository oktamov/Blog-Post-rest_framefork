import requests

url = 'http://127.0.0.1:8000/post/posts/5/'

response = requests.request("GET", url)
print(response.json())
