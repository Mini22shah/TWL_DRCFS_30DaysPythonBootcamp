import requests
import bs4

def requests_url(website_url:str):
    html_unparsed_string = requests.get(website_url).text
    return html_unparsed_string

def html_parse(html_string:str):
    soup = bs4.BeautifulSoup(html_string,'html.parser')
    return soup

def get_details(soup:bs4.BeautifulSoup):
    
    name = soup.find('span',class_ ='base').text
    
    price =soup.find('span',class_ = 'price').text
    return name,price

def main():
    website_url = 'https://www.sastodeal.com/lnspirion-15-gaming-series-g5-i7-11800h-16gb-8x2-512gb-15-6-120hz-250nits-r-sd-dlpts-033.html'

    html_string = requests_url(website_url)
    soup = html_parse(html_string)
    name,price = get_details(soup)

    print(name)
    print(price)

if __name__ == '__main__':
    main()


