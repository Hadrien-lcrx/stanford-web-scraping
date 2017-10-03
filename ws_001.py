# Number of datasets currently listed on data.gov

from bs4 import BeautifulSoup
import requests

### Getting the webpage and a response object
r = requests.get('http://www.data.gov/')

### Creating soup object
soup = BeautifulSoup(r.content, 'html.parser')
number = soup.html.select('small > a')

for s in number:
	s = s.text
	if 'datasets' in s:
		number = str(s[0:8])
		print('Number of datasets:', number)