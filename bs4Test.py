import requests
import bs4

req = requests.get("https://usm.maine.edu")

soup = bs4.BeautifulSoup (req.text, "html.parser")

print("web page title: ", soup.title.string)
print("-" * 50)
print("")
#show all <p> blocks

for p in soup.select("p"):
    print(p.string)
    print("---")