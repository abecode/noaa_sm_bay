from bs4 import BeautifulSoup
soup = BeautifulSoup(open("out.html"), 'html.parser')
for x in soup.find_all('div'):
  if "class" in x.attrs and "row-forecast" in x['class']:
    print x.get_text()
