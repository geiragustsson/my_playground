from bs4 import BeautifulSoup
from urllib.request import urlopen

url_root = "https://inside.nov.com/CAPS/SPS/HR/DK/Employeehandbook/Pages/"
url_page = "https://inside.nov.com/CAPS/SPS/HR/DK/Employeehandbook/Pages/SmokingPolicy.aspx"

content = urlopen(url_page).read()

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