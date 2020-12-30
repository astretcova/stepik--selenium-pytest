import xmltodict
import requests

response = requests.get('http://www.cbr.ru/scripts/XML_daily.asp')
xml = xmltodict.parse(response.text)
for x in xml['ValCurs']['Valute']:
    if x['CharCode'] == 'HKD':
        print(x['Value'])
        break


response = requests.get('http://jsonplaceholder.typicode.com/users')
json = response.json()
org, net = [], []
for x in json:
    domain = x['email'].split('.')[-1]
    if domain == 'org':
        org.append(x['name'])
    if domain == 'net':
        net.append(x['name'])
print('org: ', ', '.join(org))
print('net:', ', '.join(net))
