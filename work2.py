import asyncio
import requests
from tqdm import tqdm
from concurrent.futures import ProcessPoolExecutor
import re

regex = re.compile(
        r'^(?:http|ftp)s?://' 
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|' 
        r'localhost|' 
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'
        r'(?::\d+)?' 
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)

request_count = 1000

url = "http://google.com" # Or  url = input("Enter a valid url")
if re.match(regex, url) is  None :
    raise ValueError("Enter a valid url")

def request_url():
    requests.get(url)
    print("Done")

if __name__ == "__main__":
    executor = ProcessPoolExecutor(2)
    loop = asyncio.get_event_loop()
    for i in tqdm(range(request_count +1)):
        loop.run_in_executor(executor, request_url)
