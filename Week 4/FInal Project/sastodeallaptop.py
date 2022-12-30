import requests
import bs4
import pandas as pd 

def request_url(website_url:str):
    html_unparsed_string = requests.get(website_url).text
    return html_unparsed_string

def html_parse(html_string:str):
    soup = bs4.BeautifulSoup(html_string,'html.parser')
    return soup

def get_details(soup:bs4.BeautifulSoup):
    
    product_name =[]
    product_price = []

    product_details = {
        
        "Product_name":product_name,
        "Product_price":product_price
        
    }
    container_name= soup.find_all('strong',class_ ='product name product-item-name')
    container_price = soup.find_all('span',class_ = 'price')

    for ele_name,ele_price  in zip(container_name,container_price):
        name = ele_name.text
        price = ele_price.text

        product_name.append(name)
        product_price.append(price)
    # print(product_details)
    mini = pd.DataFrame(product_details)     
    print(mini)  


    


def main():
    website_url = 'https://www.sastodeal.com/electronic/laptops.html'
    html_string= request_url(website_url)
    soup = html_parse(html_string)
    get_details(soup)

    

if __name__ == '__main__':
    main()

