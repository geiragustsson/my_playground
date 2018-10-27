from bs4 import BeautifulSoup
from urllib.request import urlopen

url = "http://andriki.is/2018/05/25/folkid-sem-veit-hvernig-thu-munt-ferdast-arid-2040"

content = urlopen(url).read()

soup = BeautifulSoup(content, 'html.parser')

soup_dic = {}
soup_dic["parser"] = soup.declared_html_encoding
soup_dic["prettified"] = soup.prettify()
soup_dic["article"] = soup.find(id="content")

print(soup_dic["article"])

#print(soup.title.string)
#print(soup.p)
#print(soup.a)