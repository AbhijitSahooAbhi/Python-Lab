

import requests

def fetch_and_write_data(url, filename):

  try:
    response = requests.get(url)
    response.raise_for_status()  

    with open(filename, 'w') as f:
      f.write(response.text)
    print(f"Data fetched successfully and written to {filename}")
  except requests.exceptions.RequestException as e:
    print(f"Error fetching data from {url}: {e}")


if __name__ == "__main__":
  url = "https://www.google.com"  
  filename = "fetched_data.txt"
  fetch_and_write_data(url, filename)
