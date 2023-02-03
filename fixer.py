import requests

url = "https://data.fixer.io/api/"

# firstCur = input("First currency: ")
# secondCur = input("Second currency: ")

# amount = float(input("The amount that you want to convert: "))

response = requests.get(url)
jsonresponse = response.json()


print(jsonresponse)