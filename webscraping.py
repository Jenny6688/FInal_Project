import csv
import urllib.request
from bs4 import BeautifulSoup


# DOWNLOAD_URL = "https://www.amazon.com/Adventure-Players-Average-Playtime-Minutes/dp/B00U26V4VQ/ref=sr_1_2?crid=2DRD3QX1SMEHM&keywords=catan&qid=1701898336&sprefix=catan%2Caps%2C143&sr=8-2"
# DOWNLOAD_URL = "https://www.amazon.com/Seafarers-Expansion-Strategy-Playtime-Studio/dp/B0BCL7C7QV/ref=pd_bxgy_img_d_sccl_1/143-4569472-5379124?pd_rd_w=iS3v7&content-id=amzn1.sym.839d7715-b862-4989-8f65-c6f9502d15f9&pf_rd_p=839d7715-b862-4989-8f65-c6f9502d15f9&pf_rd_r=90KC35DR0R78NMWV3YN5&pd_rd_wg=0y6CJ&pd_rd_r=4acea434-f0ae-45bf-8674-e843845ffd62&pd_rd_i=B0BCL7C7QV&psc=1"
# DOWNLOAD_URL = "https://www.amazon.com/Amazon-Essentials-Waisted-Burgundy-XX-Large/dp/B097RQ7M3L/ref=sr_1_1_ffob_sspa?crid=1SIQQU2Q8S3K2&keywords=dress&qid=1701900127&sprefix=dres%2Caps%2C150&sr=8-1-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&psc=1"
# DOWNLOAD_URL = "https://www.amazon.com/Ferrero-Rocher-Confections-Collection-Valentines/dp/B07W6TR96W/ref=sr_1_2_sspa?crid=1ELEO1ERPMEVJ&keywords=chocolate&qid=1701900386&sprefix=chocolate%2Caps%2C153&sr=8-2-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&psc=1"
# DOWNLOAD_URL = "https://www.amazon.com/Plunder-Pirates-Life-Board-Game/dp/B083S1R2Z1/ref=sr_1_34?keywords=board+game&qid=1701902505&sr=8-34"
# DOWNLOAD_URL = "https://www.amazon.com/Secret-Hitler/dp/B01JKD4HYC/ref=sr_1_29?keywords=board+game&qid=1701902505&sr=8-29" 
DOWNLOAD_URL = "https://www.amazon.com/Czech-Games-00031CGE-Codenames/dp/B014Q1XX9S/ref=pd_bxgy_img_d_sccl_1/136-6692807-8557869?pd_rd_w=yXvTC&content-id=amzn1.sym.839d7715-b862-4989-8f65-c6f9502d15f9&pf_rd_p=839d7715-b862-4989-8f65-c6f9502d15f9&pf_rd_r=5RN95EDHJXC7N7TDNGBM&pd_rd_wg=MCi3K&pd_rd_r=3ed55677-57d0-4c97-bfed-7faac560fda5&pd_rd_i=B014Q1XX9S&psc=1"

def download_page(url):
    """
    Download the entire page given an URL
    """
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    }
    request = urllib.request.Request(url, headers=headers)
    return urllib.request.urlopen(request)


# print(download_page(DOWNLOAD_URL).read())


def parse_html(html):
    """
    Analyze the html page, find the information and return the move list of tuples (title, year)
    """

    soup = BeautifulSoup(html, features="html.parser")
    # print(soup.prettify())
    price_info = soup.find("div", attrs={"id":"corePriceDisplay_desktop_feature_div"})

    try:
        list_pirce = price_info.find("span", attrs={"class":"a-size-small a-color-secondary aok-align-center basisPrice"})
        original_price_element = list_pirce.find("span", attrs={"aria-hidden": "true"})
        original_price = original_price_element.get_text() if original_price_element else None
        print(original_price)
    except:
        list_pirce = price_info.find("span", attrs={"class": "a-price aok-align-center reinventPricePriceToPayMargin priceToPay"})
        original_price = list_pirce.find("span", attrs={"aria-hidden": "true"}).get_text() if list_pirce else None
        print(original_price)
    
    
    new_price = price_info.find("span", attrs={"class": "a-price aok-align-center reinventPricePriceToPayMargin priceToPay"})
    discounted_price = new_price.find("span", attrs={"aria-hidden": "true"}).get_text() if new_price else None
    print(discounted_price)

    percent_off_element = price_info.find("span", attrs={"class": "a-size-large a-color-price savingPriceOverride aok-align-center reinventPriceSavingsPercentageMargin savingsPercentage"})
    percent_off = percent_off_element.get_text() if percent_off_element else None
    print(percent_off)




def main():
    url = DOWNLOAD_URL

    html = download_page(url)
    price_check = parse_html(html)
    return price_check
  


if __name__ == "__main__":
    main()