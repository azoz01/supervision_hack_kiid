from pathlib import Path

SECTIONS_NAMES = [
    "cele i polityka inwestycyjna",
    "profil ryzyka i zysku",
    "opłaty",
    "wyniki osiągnięte w przeszłości",
    "informacje praktyczne",
]
PARSED_PDFS_FRAME_COLUMNS = ["id", "filename", "raw_text", "intro"]
PARSED_PDFS_FRAME_COLUMNS.extend(SECTIONS_NAMES)

SPLIT_TOKEN = "<SPLIT_TOKEN>"
TEAM_NAME = "Pomysłowi_Inżynierowie_Wielkich_Okazji"
TEAM_ID = 2

DATA_PATH = Path("data")
RAW_KIIDS_DIR = DATA_PATH / "raw"
PARSED_KIIDS_DIR = DATA_PATH / "parsed"
TEMPORARY_PATH = Path("temp")
FINAL_DATA_DIR = DATA_PATH / "final"
META_FILE_PATH = FINAL_DATA_DIR / (TEAM_NAME + "_KIID_META.csv")
KIID_WYRAZENIA = FINAL_DATA_DIR / (TEAM_NAME + '_KIID_WYRAZENIA.csv')
KNF_DATA = DATA_PATH / "knf_funds.pkl"
BAG_OF_WORDS_RAW_PATH = FINAL_DATA_DIR / (TEAM_NAME + "_KIID_BAGOFWORDS_S.csv")
BAG_OF_WORDS_NORM_PATH = FINAL_DATA_DIR / (
    TEAM_NAME + "_KIID_BAGOFWORDS_N.csv"
)
KIID_DATA_PATH = FINAL_DATA_DIR / (TEAM_NAME + "_KIID_DANE.csv")


KEY_PHRASES_DICT = {
    "Kluczowe informacje dla inwestorów": "intro",
    "Niniejszy dokument zawiera kluczowe informacje dla inwestorów dotyczące tego funduszu. Nie są to materiały marketingowe. Dostarczenie tych informacji jest wymogiem prawnym mającym na celu ułatwienie zrozumienia charakteru i ryzyka związanego z inwestowaniem w ten fundusz. Przeczytanie niniejszego dokumentu jest zalecane inwestorowi, aby mógł on podjąć świadomą decyzję inwestycyjną.": "intro",
    "Niniejsze kluczowe informacje dla inwestorów są aktualne na dzień": "informacje praktyczne",
    "Fundusz otrzymał zezwolenie na prowadzenie działalności w": "raw_text",
    "Zalecenie: niniejszy fundusz może nie być odpowiedni dla inwestorów, którzy planują wycofać swoje środki w ciągu": "cele i polityka inwestycyjna",
    "może zostać pociągnięta do odpowiedzialności za każde oświadczenie zawarte w niniejszym dokumencie, które wprowadza w błąd, jest niezgodne ze stanem faktycznym lub niespójne z odpowiednimi częściami prospektu emisyjnego UCITS.": "informacje praktyczne",
    "Opłaty jednorazowe pobierane przed lub po dokonaniu inwestycji": "opłaty",
    "Opłata za subskrypcję": "raw_text",
    "Opłata za umorzenie": "opłaty",
    "Opłaty pobierane z funduszu w ciągu roku": "opłaty",
    "Opłaty bieżące": "opłaty",
    "Opłaty pobierane z funduszu w określonych warunkach szczególnych": "raw_text",
    "Opłata za wyniki": "opłaty",
    "Cele i polityka inwestycyjna": "cele i polityka inwestycyjna",
    "Profil ryzyka i zysku": "profil ryzyka i zysku",
    "Opłaty": "opłaty",
    "Wyniki osiągnięte w przeszłości": "wyniki osiągnięte w przeszłości",
    "Informacje praktyczne": "informacje praktyczne",
}

GENERATED_COLUMNS = [
    "NAZWA_SUBFUNDUSZU",
    "NAZWA_FUNDUSZU",
    "ISIN",
    "IDENTYFIKATOR_KRAJOWY",
    "NUMER_RFI",
    "PODMIOT_ZARZADZAJACY",
    "DATA_AKTUALIZACJI_KIID",
    "KATEGORIE_JEDNOSTEK_UCZESTNICTWA",
    "CEL_INWESTYCYJNY",
    "POLITYKA_INWESTYCYJNA",
    "MINIMALNY_POZIOM_INWESTYCJI_UDZIALOWE",
    "MAKSYMALNY_POZIOM_INWESTYCJI_UDZIALOWE",
    "MINIMALNY_POZIOM_INWESTYCJI_DLUZNE",
    "MAKSYMALNY_POZIOM_INWESTYCJI_DLUZNE",
    "MAKSYMALNY_POZIOM_INWESTYCJI_TYTULY_UCZESTNICTWA",
    "CZESTOTLIWOSC_ZBYWANIA_I_ODKUPOWANIA_JEDNOSTEK_UCZESTNICTWA",
    "CZY_FUNDUSZ_WYPLACA_DYWIDENDE",
    "BENCHMARK",
    "ZALECANY_OKRES_INWESTYCJI",
    "PROFIL_RYZYKA_I_ZYSKU",
    "SRRI",
    "OPLATY",
    "OPLATA_ZA_NABYCIE",
    "OPLATA_ZA_ODKUPIENIE",
    "OPLATY_BIEZACE",
    "OPLATY_ZA_WYNIKI",
    "WYNIKI_OSIAGNIETE_W_PRZESZLOSCI",
    "STOPA_ZWROTU_2012",
    "STOPA_ZWROTU_2012_BENCHMARK",
    "STOPA_ZWROTU_2013",
    "STOPA_ZWROTU_2013_BENCHMARK",
    "STOPA_ZWROTU_2014",
    "STOPA_ZWROTU_2014_BENCHMARK",
    "STOPA_ZWROTU_2015",
    "STOPA_ZWROTU_2015_BENCHMARK",
    "STOPA_ZWROTU_2016",
    "STOPA_ZWROTU_2016_BENCHMARK",
    "STOPA_ZWROTU_2017",
    "STOPA_ZWROTU_2017_BENCHMARK",
    "STOPA_ZWROTU_2018",
    "STOPA_ZWROTU_2018_BENCHMARK",
    "STOPA_ZWROTU_2019",
    "STOPA_ZWROTU_2019_BENCHMARK",
    "STOPA_ZWROTU_2020",
    "STOPA_ZWROTU_2020_BENCHMARK",
    "STOPA_ZWROTU_2021",
    "STOPA_ZWROTU_2021_BENCHMARK",
    "DATA_PIERWSZEJ_WYCENY",
    "DEPOZYTARIUSZ",
    "KRS_TOWARZYSTWA",
    "NIP_TOWARZYSTWA",
    "SIEDZIBA_TOWARZYSTWA",
    "KAPITAL_ZAKLADOWY_TOWARZYSTWA",
    "WALUTA_KAPITALU_ZAKLADOWEGO_TO-WARZYSTWA",
    "CZY_ESG",
    "TYP_FUNDUSZU"
]