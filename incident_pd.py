import requests

url = 'http://127.0.0.1:8000/api/v1/details/'
headers = {'Authorization': 'Token 9684da15bece87f9bda579f5f705e3b5cc7ee158'}
r = requests.get(url, headers=headers)