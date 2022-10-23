---
marp: true
backgroundColor: #182458
---

![bg](1_tlo.png)
# <p  style="color:white; font-size=20px; text-align: left;"> Pomysłowi <br> Inżynierowie <br> Wielkich <br> Okazji  </p>

## <p  style="color:white; font-size=20px; text-align: left;"> #KarateKIID </p>

---
# <center style="color:white;">Problem</center>
<center><img src="2_kiid_1.png" width=400px></center>

---

# <center style="color:white;">Pobieranie danych</center>
<div style="color:white">
<ul>
    <li>Odwiedzenie jak największej liczby stron</li>
    <li>Algorytm DFS</li>
    <li>Niezależność od struktury strony</li>
    <li>~16000 plików w surowych danych</li>
    <li>~600 plików, które na pewno są KIIDami</li>
</ul>
</div>

---

# <center style="color:white;">Przetwarzanie PDFów</center>
<div style="color:white">
<ul>
    <li>Podział na sekcje</li>
    <li>Ekstrakcja danych z tabel za pomocą konwersji <em>PDF -> HTML</em> </li>
    <li>Potencjalnie analiza wykresu za pomocą AI</li>
    <li>Dane w takiej postaci są dużo prostsze w dalszej obróbce</li>
</ul>
</div>


---

# <center style="color:white;">Wyciąganie informacji z tekstu</center>
<div style="color:white">
<ul>
    <li>Spacy</li>
    <li>BeautifulSoup</em> </li>
    <li>Imputacja brakujących danych przy użyciu zewnętrznych źródeł</li>
</ul>
</div>


---
# <center style="color:white;">Bag of words</center>
<center><img src="4_bow.png" width=900px></center>

---

# <center style="color:white;">Weryfikacja wymaganych fraz
</center>
<div style="color:white">
<ul>
    <li>zmodyfikowany algorytm wyszukiwania najdłuższego wspólnego podciągu</li>
    <li>odporny na odmianę słów</li>
    <li>dodatkowo, tworzy intuicyjne wizualizacje pokazujące różnice między tekstami</li>
    <br>
    <img src="5_text.png">
</ul>
</div>

---

# <center style="color:white;">Nasze sukcesy
</center>
<div style="color:white">
<ul>
  <li>Bardzo dokładny scrapping niezależny od zmian w strukturze strony</li>
  <li>Poprawnie przeprowadzone Bag of Words</li>
  <li>Dobrze zorganizowany i rozszerzalny kod</li>
  <li>Poprawne wyciąganie wielu kolumn</li>
  <li>Korzystanie z zewnętrznych danych</li>
</ul>
</div>

---

# <center style="color:white;">Co pozostało do realizacji
</center>
<div style="color:white">
<ul>
  <li>Niepoprawne wyciąganie wartości dla niektórych kolumn np. "IDENTYFIKATOR_KRAJOWY"</li>
  <li>Optymalizacja procesu wyciągania danych z tekstu KIIDa</li>
  <li>Wyciąganie danych o opłatach z tabeli</li>
  <li>Wyciąganie danych o stopie zwrotu z wykresów</li>
</ul>
</div>
