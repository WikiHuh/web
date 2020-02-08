import urllib.request
from bs4 import BeautifulSoup
import time
import json

start = time.time()
#wikihow sitemap (contains links to all articles)
url = "http://wikihow.com/sitemap.xml"

request = urllib.request.Request(url)
xml = urllib.request.urlopen(request).read()

soup = BeautifulSoup(xml, "xml")

urls = []
locs = soup.find_all('loc')

for link in locs:
    urls.append(link.string)

# out = open('img_data.json', 'a')
# out.write("[")

# for i in range(100):
#     head_urls = urls[(50 * i) : (50 * (i + 1))]

#     for link in head_urls:
#         # make a request to each of the article urls
#         request = urllib.request.Request(link)

#         # save the contents in this variable
#         html = urllib.request.urlopen(request).read()

#         # create new bs object
#         html_soup = BeautifulSoup(html, 'html.parser')

#         title_element = html_soup.find('h1', class_="firstHeading")
#         title = title_element.a.string

#         # getting all of the list elements (li tags) that contain images
#         image_containers = html_soup.find_all('li', class_="hasimage")

#         # loop through all of the li's containing images
#         for item in image_containers:
#             img = item.find('img')

#             record = {'plays': 0, 'skips': 0}
#             if 'data-src' in img.attrs:
#                 record['title'] = title
#                 record['img_url'] = img['data-src']
#                 json.dump(record, out)
#                 out.write(",")
#             elif 'src' in img.attrs:
#                 record['title'] = title
#                 record['img_url'] = img['src']
#                 json.dump(record, out)
#                 out.write(",")


# end = time.time()
# out.write("]")
# print(end - start)