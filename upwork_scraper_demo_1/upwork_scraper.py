import json
import os
import time

import httpx
from selectolax.parser import HTMLParser
from upwork_scraper_demo_1.helpers.json_cookie_manager import JsonCookieHandler
from fake_useragent import UserAgent
import simple_header as sh

base_url: str = "https://www.upwork.com/nx/search/jobs/"
cookies = JsonCookieHandler().cookies_file_to_dict()
headers = sh.get_dict(url=base_url, user_agent=UserAgent().random, cookies=cookies)


def get_html(url):
    response = httpx.get(url=base_url, cookies=cookies)
    try:
        response.raise_for_status()
    except httpx.HTTPError as e:
        print(e)

    html = HTMLParser(response.text)
    return html


def parse_link(html: HTMLParser):
    job_list = html.css(query="article.job-tile")
    for job in job_list:
        yield base_url + job.css_first("div.job-tile-header h2.job-tile-title a").attributes["href"],


def parse_page(html: HTMLParser) -> dict[str, str]:
    content = html.css_first(query="div.job-details-content")
    job_details = {
        "title": content.css_first(query="header.air3-card-section py-4x h1.m-0 h4").text_content.strip(),
        "description": content.css_first(query="div[data-test='Description'] p.text-body-sm").text_content.strip(),
    }
    return job_details


def convert_to_json(data: dict[str, str]) -> None:
    file_path = "./data_dump/jobs.json"

    if os.path.exists(file_path):
        with open("data.json", "a", encoding="utf-8") as f:
            json.dump(data, f, indent=4)

    else:
        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)


def main():
    html = get_html(base_url)
    job_item = {}
    time.sleep(7)
    links = parse_link(html)
    for link in links:
        job_page = get_html(link)
        time.sleep(2)
        job_details = parse_page(job_page)
        job_item = {
            "title": job_details["title"],
            "description": job_details["description"],
            "link": link,
        }
        time.sleep(4)

    convert_to_json(job_item)


if __name__ == "__main__":
    main()
