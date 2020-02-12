import bs4

xml_str = """
<xml>
	<item>Apples</item>
	<item>Bananas</item>
</xml>
"""

soup = bs4.BeautifulSoup(xml_str, "lxml")