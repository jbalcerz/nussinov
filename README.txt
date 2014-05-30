nussinov
========

 Implementacja algorytmu Nussinov do obliczania struktury drugorzędowej DNA i RNA


przykłady użycia:

python main.py -h
python main.py
python main.py -i exampleInput.txt 
python main.py -i exampleInput.txt -o output1.txt
python main.py -r GGGGGAAAACCCCC 
python main.py -r GGGGGAAAACCCCC -o output2.txt


TODO:
    - napisać testy funkcjonalności głównego skryptu typu "black box", 
      jak coś się znajdzie - naprawić
    - przygotować ok. 10-20 (od prostych do skomplikowanych) ciągów RNA do testów
      i przeprowadzić testy, naprawić jeśli się coś wali, dodać testy wydajnościowe
    - uruchomić automatyczną dokumentację kodu, dopisać dokumentację w kodzie
    - przygotować kod dla różnych platform i potestowac je (sprawdzić jak to 
      smiga dla różnych wersji znacznika nowej linii na różnych platformach)
    - przygotować wersje executable dla różnych platform
    - porównać wyniki testów z innymi aplikacjami i zawrzec to w końcowym sprawozdaniu
    - napisać dokumentacje końcową ok. 4 strony (zawierająca podsumowanie i wyniki badań), 
      koniecznie opisać która wersja algorytmu traceback została użyta



Odnośnie szczegółów: 
1. jako że Panowie chcą aplikację w Pythonie, to chciałbym, aby w prosty i wygodny sposób można było wprawadzać ciągi znaków zarówno "z palca", jak i z plików. 
2. Chciałbym również, aby aplikacja była dostarczna z szeregiem testów, które weryfikują poprawność działania algorytmu. 
3. Pod uwagę będę brał również jakość dostarczonego kodu (czytelność, poprawność względem "sztuki programowania"). 
4. W zależności od zakresu prac, oczekuję również pewnych testów wydajnościowych.
5. Polecam (chociaż nie jest to wymogiem ścisłym) automatyczną dokumentację kodu.
