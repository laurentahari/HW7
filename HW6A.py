from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urlopen(url, context=ctx).read()

soup = BeautifulSoup(html, "html.parser")

total=0
tags = soup('span')
for tag in tags:
    y=str(tag)
    x= re.findall("[0-9]+",y)
    for i in x:
        i=int(i)
        total=total+i
print (total)

#print(soup.prettify())


"""
# Retrieve all of the anchor tags
tags = soup('span')
total= 0
number = 0
for tag in tags:
    num = re.findall("[0-9]+")
    for i in num:
        number = number +int(i)
    total = total + number
    number = 0
print (total)

    # Look at the parts of a tag
    print('TAG:', tag)
    print('URL:', tag.get('href', None))
    print('Contents:', tag.contents[0])
    print('Attrs:', tag.attrs)

"""
