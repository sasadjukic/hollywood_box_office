
from bs4 import BeautifulSoup
import requests

class BoxOfficeMojo:

    def __init__(self):
        self.URL = 'https://www.boxofficemojo.com/'
        response = requests.get(self.URL)
        web_site = response.text
        self.soup = BeautifulSoup(web_site, 'html.parser')

    def __repr__(self) -> str:
        return self.URL

    def scrape_all_titles(self) -> list:
        self.all_titles = self.soup.select('td', class_='a-link-normal')
        return self.all_titles

    def scrape_headers(self) -> list:
        self.all_h2 = self.soup.select('div h2')
        return self.all_h2

def get_headers(h2: list) -> list:

    header_container = []
    for headers in h2:
        headers.text.split('\n')
        text = headers.text.strip()
        header_container.append(text.upper())

    return header_container

def display_daily_boxoffice(titles: list, header: list) -> None:
    print(f"\n{header.ljust(50, '.')}")
    for title in titles[40:50]:
        title.text.split('\n')
        info = title.text.strip()
        print(info)

def display_weekend_boxoffice(weeknd_titles: list, weeknd_header: list) -> None:
    print(f"\n{weeknd_header.ljust(50, '.')}")
    for title in weeknd_titles[51:73]:
        title.text.split('\n')
        weeknd_info = title.text.strip()
        if weeknd_info != 'false' and weeknd_info != 'true':
            if weeknd_info != '2' and weeknd_info != '3':
                if weeknd_info != '4' and weeknd_info != '5':
                    print(weeknd_info)

def display_usa_yearly(usa_titles: list, usa_header: list) -> None:
    print(f"\n{usa_header.ljust(50, '.')}")
    for title in usa_titles[101:119]:
        title.text.split('\n')
        usa_info = title.text.strip()
        if usa_info != '-' and usa_info != '2':
            if usa_info != '3' and usa_info != '4':
                if usa_info != '5':
                    print(usa_info)

def display_worldwide_yearly(world_titles: list, world_header: list) -> None:
    print(f"\n{world_header.ljust(50, '.')}")
    for title in world_titles[121:]:
        title.text.split('\n')
        world_info = title.text.strip()
        if world_info != '-' and world_info != '2':
            if world_info != '3' and world_info != '4':
                if world_info != '5':
                    print(world_info)

def main():
    webscraper = BoxOfficeMojo()
    all_titles = webscraper.scrape_all_titles()
    headers = webscraper.scrape_headers()
    all_headers = get_headers(headers)
    display_daily_boxoffice(all_titles, all_headers[0])
    display_weekend_boxoffice(all_titles, all_headers[1])
    display_usa_yearly(all_titles, all_headers[3])
    display_worldwide_yearly(all_titles, all_headers[4])

if __name__ == '__main__':
    main()

