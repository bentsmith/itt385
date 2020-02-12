import requests
import bs4

req = requests.get("https://usm.maine.edu")

soup = bs4.BeautifulSoup ( req.text, "html.parser")

print("Web page title:", soup.title.string)
print("-" * 50)
print("")

# find the div's with class "item-content"

for one_div in soup.select("div.item-content"):
    header = one_div.select("h2")
    details =  one_div.select("p")

    if (header[0].text is not None):
        print("Header:", header[0].string)

        for p in details:
            if p.text is not None:
                print("Details:", p.text)

        print("---")
        print("")