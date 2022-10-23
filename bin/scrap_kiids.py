import requests
import re
from bs4 import BeautifulSoup as bs
import logging
import sys
from urllib.parse import urlparse, urlunparse
from PyPDF2 import PdfReader as pdfr
import io
import multiprocessing.dummy as mp


from requests.exceptions import MissingSchema, InvalidSchema

logging.basicConfig(
    stream=sys.stdout,
    level=logging.INFO,
    format="%(asctime)s-%(levelname)s:%(message)s"
)

logger = logging.getLogger(__name__)


def is_not_bull(a):
    return a.get('href') not in ('/', '#') and not re.findall(r'^tel:', a.get('href')) and not re.findall(r'^mail:', a.get('href')) and not re.findall(r'^mailto:', a.get('href'))

def is_onsite(a, site):
    #logger.debug(f"href netloc is: {urlparse(a.get('href')).netloc} site netloc is: {urlparse(site).netloc}")
    if len(a.get('href')) > 0 and a.get('href')[0] == '/':
        return True
    if site.__contains__(urlparse(a.get('href')).netloc):
        return True
    if a.get('href').__contains__(site):
        return True
    if site == '.'.join(urlparse(a.get('href')).netloc.split('.')[1:]):
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
    #logger.error(a.get('href'))
    if is_not_bull(a) and is_onsite(a, site) and is_not_seen(a, seen):
        return True
    return False

def is_to_save(a):
    text = a.get_text()
    if re.findall(r'.*KII.*', text, flags=re.I|re.DOTALL) or re.findall(r'.*karta.*', text, flags=re.I|re.DOTALL) or re.findall(r'.*kluczowe.*inwestorów.*', text, flags=re.I|re.DOTALL):
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
                logger.error(f"found file at: {a.get('href')}")
                if is_to_save(a):
                    if len(pdfr(io.BytesIO(resp.content)).pages) == 2:
                        filename = re.findall(r'(?<=filename=\")(.*)(?=\")',resp.headers.get("Content-Disposition", ""))
                        if len(filename)>0:
                            filename = filename[0]
                        else:
                            filename = a.get('href').split('/')[-1]
                        with open(f'../data/raw/{filename}', 'wb') as file:
                            for chunk in resp.iter_content(chunk_size=1024):
                                file.write(chunk)

            else:
                logger.warn(f"unhandled content-type: {resp.headers.get('Content-Type')}")
        except (MissingSchema, InvalidSchema) as exc:
            logger.warning(f"GET {link_} failed with {exc}")


    dfs_(link)


if __name__ == "__main__":
    pool = mp.Pool(32)
    with open('linki', 'r') as file:
        linki = file.read().split('\n')
    pool.map(dfs, linki)
    pool.close()
    pool.join()