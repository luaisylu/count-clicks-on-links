from urllib.parse import urlparse
import requests
import os


def shorten_link(link, headers):
  link_shortening = "https://api-ssl.bitly.com/v4/shorten"
  payload = {"long_url": link}
  response = requests.post(link_shortening, json=payload, headers=headers)
  response.raise_for_status()                         
  return response.json()["id"]


def count_clicks(link, headers):
  parsed_link = urlparse(link)
  url = "https://api-ssl.bitly.com/v4/bitlinks/{}{}/clicks/summary"
  clicks_url = url.format(parsed_link.netloc, parsed_link.path)
  response = requests.get(clicks_url, headers=headers)
  response.raise_for_status()
  return response.json()["total_clicks"]


def check_bitlink(link, headers):
  parsed_link = urlparse(link)
  url = "https://api-ssl.bitly.com/v4/bitlinks/{}{}"
  clicks_url = url.format(parsed_link.netloc,parsed_link.path)
  response = requests.get(clicks_url, headers=headers)
  return response.json()["archived"]


def main():
  link = input("Введите ссылку: ")
  bitly_token = os.getenv("BITLY_TOKEN")
  headers = {"Authorization" : "Bearer {}".format(bitly_token)}
  
  try:
    bitlink_check = check_bitlink
    print("По вашей ссылке прошли ", count_clicks(link, headers), "раз(а)")
  except requests.exceptions.HTTPError:
    link_short = shorten_link(link, headers)
    print("Битлинк ", link_short)


if __name__ == "__main__":
	main()
