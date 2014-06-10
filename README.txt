nussinov
========

 Implementacja algorytmu Nussinov do obliczania struktury drugorzędowej DNA i RNA


przykłady użycia:

python main.py -h
python main.py
python main.py -r GGGGGAAAACCCCC 
python main.py -r GGGGGAAAACCCCC -o output1.txt
python main.py -i sequences/1.txt -o output2.txt


TODO:

Jerzy:
	- potestować działanie nowych funkcjonalności -minLoop -energyMatrix
	- stworzyc sprawko w LaTex
	- napisać wstęp, opis algorytmu, opis narzędzi
	- scalić dwie częśći sprawozadania
	- napisać komentarze w kodzie i zrobić automatyczną dokumentację kodu

Olek:
	- poprawić skrypty do testów jesli trzeba
	- napisać do sprawka:
		- teoretycznie o testach - jakie przeprowadziliśmy, 
		  ide danych testowych, skąd (dokładnie opisać źródło!)
		- co wnioskujesz z testów
		- porównanie z innymi programami
	- dokończyć wizualizację
	- przygotować releasy na różne platformy (napisać makefile?)

