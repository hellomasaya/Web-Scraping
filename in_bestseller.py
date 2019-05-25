import bs4
#from urllib.request import urlopen as uReq
import requests
from bs4 import BeautifulSoup as soup

first = open('in_book.csv', 'w')
first.write('Name' + ";" + 'URL' + ";" + 'Author' + ";" + 'Price' +
            ";" + 'Number of Ratings' + ";" + 'Average Rating' + "\n")
for i in range(1, 6):
    #page = ("https://www.amazon.com/best-sellers-books-Amazon/zgbs/books/")
    #client = uReq(page)
    p_html = requests.get(
        'https://www.amazon.in/gp/bestsellers/books/ref=zg_bs_pg_{0}?ie=UTF8&pg={0}'.format(i)).text
    # client.close()

    p_soup = soup(p_html, "html.parser")

    main = p_soup.findAll("div", {"class": "zg_itemImmersion"})
    # contain=main[0]

    for contain in main:
        wrap = contain.find("div", {"class": "zg_itemWrapper"})
        section = wrap.find(
            "div", {"class": "a-section a-spacing-none p13n-asin"})
        try:
            start_name = section.find(
                "div", {"class": "p13n-sc-truncate p13n-sc-line-clamp-1"})
            name = start_name.text.strip()
            ans_name = name
        except Exception as e:
            ans_name = "Not Available"

        first.write(str(ans_name) + ";")
        # print(ans_name)

        try:
            url = "https://www.amazon.in" + section.a["href"]
            ans_url = url
        except Exception as e:
            ans_url = "Not Available"

        first.write(str(ans_url) + ";")
        # print(ans_url)

        try:
            start_author = section.find(
                "span", {"class": "a-size-small a-color-base"})
            author = start_author.text.strip()
            ans_author = author
        except Exception as e:
            ans_author = "Not Available"

        first.write(str(ans_author) + ";")
        # print(ans_author)

        try:
            start_price = section.find("span", {"class": "p13n-sc-price"})
            price = start_price.text.strip()
            ans_price = price
        except Exception as e:
            ans_price = "Not Available"

        first.write(str(ans_price) + ";")
        # print(ans_price)

        try:
            start_number = section.find(
                "a", {"class": "a-size-small a-link-normal"})
            number = start_number.text.strip()
            ans_number = number
        except Exception as e:
            ans_number = "Not Available"

        first.write(str(ans_number) + ";")
        # print(ans_number)

        try:
            start_rating = section.find("span", {"class": "a-icon-alt"})
            rating = start_rating.text.strip()
            ans_rating = rating
        except Exception as e:
            ans_rating = "Not Available"

        first.write(str(ans_rating) + "\n")
        # print(ans_rating)

first.close()


# print(author)
# print(price)

# print(rating)
