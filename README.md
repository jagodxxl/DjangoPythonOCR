**Spis treści:**

\1. pdf2jpg.py

\2. ocr\_core3.py

\3. correct\_skew\_old.py

\4. img\_crop.py

\5. fakt\_morele.py

\6. search\_txt\_6.py

\7. angle\_detection.py

\8. rotate.py

**pdf2jpg.py**

**OPIS:**

*Skrypt, który dzieli wielostronicowy plik pdf na osobne strony i zapisuje w formacie JPG w wybranym*

*folderze.*

**KOMENDA DO WYWOŁANIA SKRYPTU:**

sudo python3 pdf2jpg.py FV-Example.pdf images

**LEGENDA:**

pdf2jpg.py - nasz skrypt,

FV-Example.pdf - nasz pdf, którego chcemy podzielić,

images - folder, do którego zrzucane są nasze podzielone zdjęcia.


**Użyte biblioteki:**

Os

Sys

**ocr\_core3.py**

**OPIS:**

*Skrypt, który odczytuje zadaną ilość linii od dołu.*

**KOMENDA DO WYWOŁANIA SKRYPTU:**

python3 ocr\_core3.py image4.jpg images 2

**LEGENDA:**

ocr\_core3.py - nasz skrypt,

image4.jpg - przykładowe zdjęcie, które zostało wcześniej podzielone z pdf'a, z niego są

odczytywane linie - wyrazów,

images - przykładowy folder z naszymi podzielonymi zdjęciami,

"2" - liczba linii wyświetlonych od dołu.

**Użyte biblioteki:**

Os

Sys

**correct\_skew\_old.py**

**OPIS:**

*Skrypt, który prostuje zakrzywione zdjęcie. Skrypt po użyciu wyświetla nam zakrzywione i poprawione*

*zdjęcie, oraz pokazuje w konsoli o jaki kąt zdjęcie zostało obrócone. Każde poprawione zdjęcie*

*zapisywane jest z końcówką “\_r. Wyjście ze skryptu klawiszem „Esc”.*

**KOMENDA DO WYWOŁANIA SKRYPTU:**

sudo python correct\_skew\_old.py --image images/images0.jpg

**LEGENDA:**

correct\_skew\_old.py - skrypt,

images - przykładowy folder z naszymi podzielonymi zdjęciami, które są zakrzywione,

image0.jpg - przykładowe zdjęcie, które zostało wcześniej podzielone z pdf'a i jest

zakrzywione.


**Użyte biblioteki:**

NumPy

Argparse

OpenCV

**img\_crop.py**

**OPIS:**

*Skrypt, który wycina zadaną ilość pikseli od dołu, po czym wyciąga maksymalną ilość znaków z tego*

*obszaru. Takie zdjęcie jest potem zapisywane w podanym katalogu z końcówką “\_crop”.*

**KOMENDA DO WYWOŁANIA SKRYPTU:**

sudo python3 img\_crop.py images/image0.jpg 150

**LEGENDA:**

img\_crop.py - skrypt,

images/image0.jpg - ścieżka zdjęcia, które nas interesuje,

150 - ilość pikseli od dołu, które wycinamy i zarazem wyświetlamy.

**Użyte biblioteki:**

Sys

Pillow

Pytesseract

**fakt\_morele.py**

**Opis:**

*Skrypt, który wyświetla konkretne obszary z faktury z Morele. Przykładowe koordynaty różnych pól są*

*na stałe wpisane w skrypt. Np. text1 – wyświetla dane z pierwszego prostokąta takie jak: sprzedawca,*

*adres, NIP, nr rejestrowy BDO. Odczytany tekst jest zapisywany w podanym folderze z końcówką*

*“\_frag1”.*

**KOMENDA DO WYWOŁANIA SKRYPTU:**

sudo python3 fakt\_morele.py images/image5\_r.jpg

**LEGENDA:**

fakt\_morele.py - skrypt,

images/image5\_r.jpg - ścieżka zdjęcia, które nas interesuje.





**DODATKOWA LEGENDA:**

text1 - prostokąt z danymi Sprzedawca, Adres, NIP, Nr rejestrowy BDO,

text2 - prostokąt, który wyświetla nr faktury,

text3 - prostokąt, który wyświetla dwie daty: 2019-11-07 oraz 2019-11-06,

text4 - prostokąt z danymi Nabywca, Adres, NIP,

text5 - prostokąt z danymi Odbiorcy,

text6 - prostokąt z danymi Razem do zapłaty razem z kwotą.

**Użyte biblioteki:**

Sys

Pillow

Pytesseract


**search\_txt\_6.py**

**OPIS:**

*Skrypt, który znajduje współrzędne zadanego tekstu.*

**KOMENDA DO WYWOŁANIA SKRYPTU:**

sudo python3 search\_txt\_6.py -i images2/image1\_r.jpg -t 'co szukam' -s 2

**LEGENDA:**

search\_txt\_6.py - skrypt,

images2/image1\_r.jpg

t - odpowiada za wyrazy, które ma szukać,

'co szukam' - tutaj wpisujemy wyrazy, które nas interesują,

-s 2 - dodatkowa opcja, która pozwala nam na wyświetlenie np. 2 następnych wyrazów, po

tych, które wpisaliśmy w ‘co szukam’.


**Użyte biblioteki:**

Argparse

Pytesseract

OpenCV

**angle\_detection.py**

**OPIS:**

*Skrypt, który informuje nas o tym, w jakiej pozycji znajduje się zdjęcie, o jaki kąt jest pochylony oraz czy*

*znajduje się w pozycji pionowej lub poziomej.*

**KOMENDA DO WYWOŁANIA SKRYPTU:**

sudo python3 angle\_detection.py -i images/image3.jpg

**LEGENDA:**

angle\_detection.py - nasz skrypt,

images/image3.jpg - ścieżka zdjęcia.


**Użyte biblioteki:**

Pytesseract

CV2

Argparse

Re (regular expression)

Numpy

Imutils


**rotate.py**

**OPIS:**

*Skrypt, który odwraca nam zdjęcie o podaną ilość stopni. Takie odwrócone zdjęcie jest zapisywane w*

*podanym katalogu z "rotate" i z podaną ilością stopni, o które odwróciliśmy. Dla przykładu, jak*

*odwróciliśmy zdjęcie o 90 stopni, to nowe, obrócone zdjęcie będzie miało dodaną końcówkę*

*"\_rotate.90."*

**KOMENDA DO WYWOŁANIA SKRYPTU:**

sudo python3 rotate.py -i images/image3.jpg -a 90

**LEGENDA:**

rotate.py - nasz skrypt,

images/image3.jpg - ścieżka zdjęcia,

-a 90 - parametr, który odpowiada za obrócenie zdjęcia w stopniach.


**Użyte biblioteki:**

PyTesseract

OpenCV

Argparse

Re (regular expression)

Numpy

Imutils

