from bs4 import BeautifulSoup
from urllib.request import urlopen

url = "http://andriki.is/2018/05/25/folkid-sem-veit-hvernig-thu-munt-ferdast-arid-2040"

content = urlopen(url).read()

soup = BeautifulSoup(content, 'html.parser')

soup_dic = {}
soup_dic["parser"] = soup.declared_html_encoding
soup_dic["prettified"] = soup.prettify()
article = soup.find("section", attrs={"role":"main"})
soup_dic["article"] = article
soup_dic["article_text"] = article.text.strip()

print(soup_dic["article_text"])

#print(soup.title.string)
#print(soup.p)
#print(soup.a)