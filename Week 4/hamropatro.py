#beautifulsopu4

#Goto a weather website
#Get the current temperature and weather for your local city
#print the current temperature and weather

#hit the website using requests modeule
#parse he htmlm retured by requests module using bs4 module

#fetch the current temperature and weather using the parsed html 
#print it

import requests
import bs4

def send_request(website_url: str) ->str:
    return requests.get(website_url).text
    # print(website_url)
    #get request pathauuxa 
    #raw string ma dinxa--> i.e.html


def parse_html_string(html_str: str) -> bs4.BeautifulSoup:
    soup = bs4.BeautifulSoup(html_str,'html.parser')
    #html string ho so we need to parse it 
    print('Working')
    return soup

def fetch_current_nepali_date(parsed_html: bs4.BeautifulSoup) ->str:
    #id kasari nikalni 
    print('Entered in function')
    top_element = parsed_html.find(id="top")
    #top element aaesake paxi 
    date_element = top_element.find('div',class_="date")
    current_date = date_element.span.string.removeprefix('\n')
    return current_date
    #string return garna ko lagi  


def main():
    print('stage 1')
    website="https://www.hamropatro.com/"
    print('stage 2')
    html_str = send_request(website)
    print('stage 3')
    parsed_html= parse_html_string(html_str)

    current_date = fetch_current_nepali_date(parsed_html)

    print(f"The current date is {current_date}.")

if __name__=='__main_':
    main()