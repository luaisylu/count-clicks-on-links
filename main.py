import os
import argparse


import requests
from urllib.parse import urlparse


def shorten_link(arguments, headers):
  site_link_shortening = "https://api-ssl.bitly.com/v4/shorten"
  payload = {"long_url": arguments}
  response = requests.post(site_link_shortening, json=payload, headers=headers)
  response.raise_for_status()                         
  return response.json()["id"]


def count_clicks(arguments, headers):
  parsed_link = urlparse(arguments)
  url = f"https://api-ssl.bitly.com/v4/bitlinks/{parsed_link.netloc}{parsed_link.path}/clicks/summary"
  response = requests.get(url, headers=headers)
  response.raise_for_status()
  return response.json()["total_clicks"]


def check_bitlink(arguments, headers):
  parsed_link = urlparse(arguments)
  url = f"https://api-ssl.bitly.com/v4/bitlinks/{parsed_link.netloc}{parsed_link.path}"
  response = requests.get(url, headers=headers)
  return response.ok

  
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--url', help='Введите ссылку: ')
    arguments = parser.parse_args()
    parsed_link = urlparse(arguments.url)
    if parsed_link.scheme:
        arguments = arguments.url
    else:
        arguments = f"http://{arguments.url}"
      
    link_without_scheme = f"{parsed_link.netloc}{parsed_link.path}"

    bitly_token = os.getenv("BITLY_TOKEN")
    headers = {"Authorization" : "Bearer {}".format(bitly_token)}        
    try:
        if check_bitlink(link_without_scheme, headers):
    	    print("По вашей ссылке прошли ", 
                  count_clicks(link_without_scheme, headers), 
                  "раз(а)")
        else:
            link_short = shorten_link(arguments, headers)
            print("Битлинк ", link_short) 
    except requests.exceptions.HTTPError:
        print("Ошибка")


if __name__ == "__main__":
	main()
