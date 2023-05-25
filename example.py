import requests

url = 'https://mralidev.pythonanywhere.com/post/posts/'

url1 = 'https://bozor.com/uz/products_all/Grechka/grechka-qop/'

response = requests.request("GET", url1)
print(response.json())
