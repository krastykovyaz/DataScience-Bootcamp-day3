#!/usr/bin/env python
import bs4
from time import sleep
import requests
import sys


class ErrorStatusCode(Exception):
    pass


def get_page(url):
    try:
        # sleep(5)
        resp = requests.get(url)
    except:
        raise ConnectionError

    if resp.status_code == 200:
        return resp.text
    else:
        raise ErrorStatusCode


def parse_html(html, ticket, table_field):
    soup = bs4.BeautifulSoup(html, "html.parser")
    if not soup.find('span', text=f"Symbols similar to '{ticket.lower()}'") is None:
        print('Invalid ticket')
        raise ValueError
    all_rows = soup.find_all('span')
    for i, row in enumerate(all_rows):
        if row.text == table_field:
            valid_row_id = i
            break
    else:
        print('Invalid table field')
        raise ValueError
    table_data = [row.text for row in all_rows[valid_row_id + 1:valid_row_id + 6]]
    return tuple([table_field] + table_data)


def main():
    try:
        if len(sys.argv) != 3:
            sys.exit()
        ticket, table_field = sys.argv[1:]
        url = f'https://finance.yahoo.com/quote/{ticket}/financials'
        try:
            html = get_page(url)
        except ConnectionError:
            sys.exit()
        try:
            table_data = parse_html(html, ticket, table_field)
        except ValueError:
            sys.exit()
        print(table_data)
    except:
        sys.exit()


if __name__ == '__main__':
    main()
