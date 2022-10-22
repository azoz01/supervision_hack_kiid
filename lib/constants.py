from pathlib import Path

SECTIONS_NAMES = [
    "cele i polityka inwestycyjna",
    "profil ryzyka i zysku",
    "opłaty",
    "wyniki osiągnięte w przeszłości",
    "informacje praktyczne",
]
PARSED_PDFS_FRAME_COLUMNS = ["filename", "raw_text", "intro"]
PARSED_PDFS_FRAME_COLUMNS.extend(SECTIONS_NAMES)

SPLIT_TOKEN = "<SPLIT_TOKEN>"

DATA_PATH = Path("data")
RAW_KIIDS_DIR = Path("data/raw")
PARSED_KIIDS_DIR = Path("data/parsed")
TEMPORARY_PATH = Path("temp")

KEY_PHRASES_DICT = {
    'Kluczowe informacje dla inwestorów': 'intro',
    'Niniejszy dokument zawiera kluczowe informacje dla inwestorów dotyczące tego funduszu. Nie są to materiały marketingowe. Dostarczenie tych informacji jest wymogiem prawnym mającym na celu ułatwienie zrozumienia charakteru i ryzyka związanego z inwestowaniem w ten fundusz. Przeczytanie niniejszego dokumentu jest zalecane inwestorowi, aby mógł on podjąć świadomą decyzję inwestycyjną.' : 'intro',
    'Niniejsze kluczowe informacje dla inwestorów są aktualne na dzień': 'informacje praktyczne',
    'Fundusz otrzymał zezwolenie na prowadzenie działalności w': 'raw_text',
    'Zalecenie: niniejszy fundusz może nie być odpowiedni dla inwestorów, którzy planują wycofać swoje środki w ciągu': 'cele i polityka inwestycyjna',
    'może zostać pociągnięta do odpowiedzialności za każde oświadczenie zawarte w niniejszym dokumencie, które wprowadza w błąd, jest niezgodne ze stanem faktycznym lub niespójne z odpowiednimi częściami prospektu emisyjnego UCITS.': 'informacje praktyczne',
    'Opłaty jednorazowe pobierane przed lub po dokonaniu inwestycji': 'opłaty',
    'Opłata za subskrypcję': 'raw_text',
    'Opłata za umorzenie': 'opłaty',
    'Opłaty pobierane z funduszu w ciągu roku': 'opłaty',
    'Opłaty bieżące': 'opłaty',
    'Opłaty pobierane z funduszu w określonych warunkach szczególnych': 'raw_text',
    'Opłata za wyniki': 'opłaty',
    'Cele i polityka inwestycyjna': 'cele i polityka inwestycyjna',
    'Profil ryzyka i zysku': 'profil ryzyka i zysku',
    'Opłaty': 'opłaty',
    'Wyniki osiągnięte w przeszłości': 'wyniki osiągnięte w przeszłości',
    'Informacje praktyczne': 'informacje praktyczne	'
    }