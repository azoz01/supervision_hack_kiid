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
        df["identyfikator_krajowy_funduszu"] = country_id[-11:]

        return df

    def _restructure_funds_df(df: pd.DataFrame) -> pd.DataFrame:

        fund_regex = re.compile(" (fundusz)(e|y|)", re.IGNORECASE)
        subfind_start_regex = re.compile(".*wydzielone.subfundusze.*", re.IGNORECASE)

        new_df = pd.DataFrame(
            columns=["fundusz", "subfundusz", "indentyfikator_krajowy", "nr_w_rejestrze"]
        )

        is_subfund = False
        curr_fund = ""

        for index, row in df.iterrows():

            if subfind_start_regex.search(row["fundusz"]):
                is_subfund = True
                continue

            if not is_subfund:
                curr_fund = row["fundusz"]

            if is_subfund:
                if bool(fund_regex.search(row["fundusz"])):
                    is_subfund = False

            new_row = pd.DataFrame()

            if is_subfund:
                new_row = pd.DataFrame(
                    {
                        "fundusz": [curr_fund],
                        "subfundusz": [row["fundusz"]],
                        "indentyfikator_krajowy": [row["identyfikator krajowy"]],
                        "nr_w_rejestrze": [row["nr w rejestrze funduszy inwestycyjnych"]],
                    }
                )
            else:
                new_row = pd.DataFrame(
                    {
                        "fundusz": [row["fundusz"]],
                        "subfundusz": [None],
                        "indentyfikator_krajowy": [row["identyfikator krajowy"]],
                        "nr_w_rejestrze": [row["nr w rejestrze funduszy inwestycyjnych"]],
                    }
                )
            new_df = new_df.append(new_row, ignore_index=True)

        new_df['towarzystwo'] = df['towarzystwo']
        new_df["identyfikator_krajowy_funduszu"] = df["identyfikator_krajowy_funduszu"]

        return new_df

    dfs = summary_df['section'].apply(_extract_df)

    full_df = pd.DataFrame()

    for df in dfs:
        n_df = _restructure_funds_df(df)
        full_df = pd.concat([full_df, n_df])

    return full_df

def clear_data(df: pd.DataFrame) -> pd.DataFrame:
    is_id_valid = df['nr_w_rejestrze'].apply(lambda x: len(str(x)) in (3, 4) )

    df = df[is_id_valid]

    return df

def main(
    url: str = 'https://www.knf.gov.pl/podmioty/Podmioty_rynku_kapitalowego/Fundusze_Inwestycyjne/TFI_i_FI',
    out: str = './../data/knf_funds.pkl'
):
    soup = get_soup(url)
    summary = get_summary(soup)

    df = get_full_df(soup, summary)

    df = clear_data(df)

    df.to_pickle(out)


if __name__ == "__main__":
    main(
        
    )
