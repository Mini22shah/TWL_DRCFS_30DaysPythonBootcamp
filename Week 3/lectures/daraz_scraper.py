# Goto daraz site for a specific product
# Fetch it's current price
# Write that price to a file every 60 seconds

# Request the daraz product page using requests module
# Parse the html string using bs4
# Find the element that contains the price
# Convert the price into integer
# Write the price in a file




# import bs4
# import requests

# def reuest_site(url: str) -> str:
#     return requests.get(url).text

# def parse_html(unparsed_html: str) -> bs4.BeautifulSoup:
#     return bs4.BeautifulSoup(unparsed_html,"html.parser")


# def get_price_from_soup(soup: bs4.BeautifulSoup) -> float:
#     price_element = soup.find('span', class_="price-wrapper")
#     neplai_price = price_element


# def write_price_to_file(price: float , filename: str) -> None:

# def main():
#     website_url="https://www.daraz.com.np/products/gorilla-tripod-with-mobile-clips-for-camera-and-mobile-i105521575-s1027285559.html?spm=a2a0e.11779170.flashSale.5.287d2d2brIeWOn"
#     file_path = "data.txt"
#     html_str = request_site(website_url)


