from bs4 import BeautifulSoup
import requests
import re
import pandas as pd
import numpy as np

def get_soup(url: str) -> BeautifulSoup:
    html = requests.get(url)
    soup = BeautifulSoup(html.text)
    return soup

def get_summary(soup: BeautifulSoup) -> pd.DataFrame:

    links_regex = re.compile('^#.*$')

    # first table on the page
    summary_table = soup.find_all("table", {"class": "sample"})[0]
    links_to_sections = summary_table.find_all("a", {'href' : links_regex})

    # section in html doc + full name of fund connected with it
    sections = list(map(lambda link: link['href'], links_to_sections))
    funds_names = list(map(lambda link: link.text, links_to_sections))

    df = pd.DataFrame(data={'section': sections, 'fund_name': funds_names})
    return df

def get_full_df(soup: BeautifulSoup, summary_df: pd.DataFrame) -> pd.DataFrame:
    
    def _extract_df(section: str) -> pd.DataFrame:

        country_id_regex = re.compile('Identyfikator krajowy: (PLTFI.{6})')

        link_before_section = soup.find("a", {"name": section[1:]})

        header = link_before_section.findNext("h4").text
        country_id = link_before_section.findNext(text=country_id_regex)

        html_df_wrappers = link_before_section.findNext(
            "div", {"class": "table-responsive"}
        )
        html_table = html_df_wrappers.find("table")

        df = pd.read_html(str(html_table))[0]

        df["towarzystwo"] = header
        df["identyfikator_krajowy"] = country_id[-11:]

        return df

    dfs = summary_df['section'].apply(_extract_df)

    full_df = pd.DataFrame()

    for df in dfs:
        full_df = pd.concat([full_df, df])

    return full_df

def main(
    url: str = 'https://www.knf.gov.pl/podmioty/Podmioty_rynku_kapitalowego/Fundusze_Inwestycyjne/TFI_i_FI',
    out: str = './../data/knf_funds.pkl'
):
    soup = get_soup(url)
    summary = get_summary(soup)

    df = get_full_df(soup, summary)

    df.to_pickle(out)


if __name__ == "__main__":
    main(
        
    )
