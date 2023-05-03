import requests

url = "https://api.geoapify.com/v1/geocode/reverse?lat=52.51894887928074&lon=13.409808180753316&type=postcode&lang=en&format=json&apiKey=c79a00754b0046f2b25219b796bb9625"
          
response = requests.get(url)
print(response.json())