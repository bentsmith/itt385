import requests

req = requests.get("https://usm.maine.edu")

print("Server returned a status of", req.status_code)

if ((req.status_code >+ 200) and (req.status_code <= 299)):
    # we have data
    content = req.content.decode('utf-8')

    print(content[:200])
