
import requests
import re
from bs4 import BeautifulSoup as bs
import logging
import sys
from urllib.parse import urlparse, urlunparse
from PyPDF2 import PdfReader as pdfr
import io

from requests.exceptions import MissingSchema, InvalidSchema

logging.basicConfig(
    stream=sys.stdout,
    level=logging.DEBUG,
    format="%(asctime)s-%(levelname)s:%(message)s"
)

logger = logging.getLogger(__name__)


def is_not_bull(a):
    return a.get('href') not in ('/', '#') and not re.match(r'^tel:', a.get('href')) and not re.match(r'^mail:', a.get('href')) and not re.match(r'^mailto:', a.get('href'))

def is_onsite(a, site):
    if not urlparse(a.get('href')).netloc or urlparse(a.get('href')).netloc == urlparse(site):
        return True
    return False

def add_netloc(a, site):
    link = a.get('href')
    parsed_link = urlparse(link)
    parsed_site = urlparse(site)
    if not parsed_link.netloc:
        a['href'] = urlunparse(
            (
                parsed_site.scheme,
                parsed_site.netloc,
                parsed_link.path,
                parsed_link.params,
                '',
                ''
            )
        )
    return a

def is_not_seen(a, seen):
    if a.get('href') in seen:
        return False
    return True

def is_check(a, site, seen):
    if is_not_bull(a) and is_onsite(a, site) and is_not_seen(a, seen):
        return True
    return False

def is_to_save(a):
    text = a.get_text()
    if re.match(r'.*KII.*', text, flags=re.I) or re.match(r'.*karta.*', text, flags=re.I) or re.match(r'.*kluczowe.*inwestorów.*', text, flags=re.I):
        return True
    return False

def dfs(link):
    """

    :param link: valid url
    :return: list of <a> tags from all pages found on site
    """
    seen = set()
    def dfs_(a):
        if not isinstance(a, str):
            link_ = a.get('href')
        else:
            link_ = a
        seen.add(link_)
        logger.info(f"trying {link_}")
        try:
            resp = requests.get(link_)
            if resp.status_code != 200: # noqa
                logger.warning(f"GET {link_} failed with code: {resp.status_code}")
                return []
            logger.debug(f"GET {link_} content-type: {resp.headers.get('Content-Type')}")
            if resp.headers.get("Content-Type", "").__contains__("text/html"):
                soup = bs(resp.content)
                found_as = soup.find_all("a", href=True, recursive=True)
                to_check_as = [add_netloc(a, link) for a in found_as if is_check(a, link, seen)]
                for a in to_check_as:
                    if is_not_seen(a, seen):
                        dfs_(a)

            elif resp.headers.get("Content-Type", "").__contains__("application/pdf"):
                if is_to_save(a):
                    if len(pdfr(io.BytesIO(resp.content)).pages) == 2:
                        with open(f'../data/raw/{a.get("href").split("/")[-1]}', 'wb') as file:
                            for chunk in resp.iter_content(chunk_size=1024):
                                file.write(chunk)

            else:
                logger.warn(f"unhandled content-type: {resp.headers.get('Content-Type')}")
        except (MissingSchema, InvalidSchema) as exc:
            logger.warning(f"GET {link_} failed with {exc}")


    dfs_(link)


if __name__ == "__main__":
    with open('linki', 'r') as file:
        linki = file.read().split('\n')

    for link in linki:
        dfs(link)