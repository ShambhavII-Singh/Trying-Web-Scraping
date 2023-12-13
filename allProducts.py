import requests #to fetch web page
from bs4 import BeautifulSoup #to web scrape

#need to iterate through the pages of this website
base_url = "https://www.carlroth.com/de/de/life-science/mikrobiologie/c/web_folder_260553?q=%3Apopularity-desc&page="
#final answer
all_products = [] 

#iterate through each page
for i in range(47):
    page = requests.get(base_url + str(i)) #create complete url
    soup = BeautifulSoup(page.content,"html.parser") #scraping object

    page_products = [] #all results of this page

    products = soup.select("div.product-item") #get content of each cell of product grid as a list

    #iterate  through each product for its details
    for product in products:
        #store as a dictionary with labels
        information = {
            "name" : product.select("div.details > a.name")[0].text.strip(), #product nam
            "purity_level" : product.select("div.details > div.purityLevel")[0].text.strip(), #subheading
            "small_text" : product.select("div.details > div.small-text")[0].text.strip().replace("\n\t\t\t\t\t\t\t",""), #grey text
            "synonyms" : product.select("div.details > div.synonyms")[0].text.strip(), #grey text
            "stock_status" : product.select("div.bottom-container > div.stockstatus")[0].text.strip().replace("\xa0"," "), #beside marker
            "price" : product.select("div.bottom-container > div.price")[0].getText().strip().replace("\xa0"," ").replace("\n\t\t\t\t\t\t\t","") #product price
        }
        page_products.append(information) #append in page products

    page_products = page_products[:len(page_products)//3:] #appended thrice for some reason so slice out
    all_products.add(page_products) #add in cumilative list

print(all_products)
