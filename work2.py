import asyncio
import requests
from tqdm import tqdm 
from concurrent.futures import ProcessPoolExecutor
import re 

url = "http://google.com" # Or  url = input("Enter a valid url")
request_count = 5

regex = re.compile(
        r'^(?:http|ftp)s?://' 
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|' 
        r'localhost|' 
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'
        r'(?::\d+)?' 
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)


if re.match(regex, url) is  None :
    raise ValueError("Enter a valid url")

def request_url():
    requests.get(url)

async def responses(tasks):
    responses = [await f for f in tqdm(asyncio.as_completed(tasks), total=len(tasks))] # progress bar for  responses 
    return responses

if __name__ == "__main__":
    executor = ProcessPoolExecutor(2)
    loop = asyncio.new_event_loop()
    tasks = []
    for i in tqdm(range(request_count)):  # progress bar for  processes 
        task = loop.run_in_executor(None, request_url)
        tasks.append(task)
        
    asyncio.gather(*tasks)
    r = loop.run_until_complete(responses(tasks))

