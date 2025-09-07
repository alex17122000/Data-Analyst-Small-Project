POC Overview

A manufacturing company is modernizing its Procurement systems, but struggles with a messy supplier database full of duplicates and outdated records. Leadership is pushing for a clear cost-saving strategy and is interested in sustainability, but resources are limited.
They’re testing two solutions: a strong-performing newcomer and a reputable legacy provider. A decision will be made next quarter.

Tasks:

1. Entity Resolution
Select the best company match (from up to 5 suggestions per row). If none are accurate, leave it unmatched or find the correct one manually.

2. Data QC
Review the matched company data. Highlight any missing or inconsistent fields. Cleaning is optional.

3. Summary
Document your process and insights. Focus on your logic, not just the tools used.

----------------------------------

Procesul de gandire (POC Veridion)

Am inceput cu o abordare de tip fuzzy matching intre input_company_name si company_name. A functionat decent, dar am realizat ca nu este suficient pentru a identifica entitatea corecta in toate cazurile, asa ca am creat un scor compus care include mai multi factori relevanti:
•	Numele companiei
•	Tara
•	Orasul
•	Website-ul
•	LinkedIn-ul

Apoi m-am gandit ca nu este corect ca un camp necompletat sa penalizeze scorul, asa ca am modificat logica: daca input_main_country lipseste, nu penalizez scorul, ba chiar adaug puncte ca sa nu dezavantajez entitatea. (M-am gandit ca, daca toate campurile se potrivesc inafara de unul singur, entitatea va fi mult dezavantajata, desi cel mai probabil este un MATCH.)
Am adaugat si o coloana numita score_justification pentru a documenta clar de ce fiecare companie a primit scorul respectiv (ex: "Fuzzy: 41.5p | Country: +20p (missing input)", etc).

Verificarea calitatii datelor
Apoi am vrut sa verific daca datele pe care le-am selectat ca "MATCHED" sunt si calitativ utile. M-am intrebat:
Cate companii au website? Cate au venituri sau coduri de industrie? Merita aceasta baza de date livrata clientului?
Am construit o analiza de Quality Control (QC) care masoara gradul de completitudine pentru fiecare camp relevant si genereaza un raport CSV.
Am  tratat si cazurile in care coloanele nu exista (de exemplu, dupa merge(), unele coloane devin *_x sau *_y).

Cand am recitit cerinta, am observat si partea de documentatie si mi-am dat seama ca nu am citit initial instructiunile legate de API. Am vazut ca Veridion ofera un API care intoarce un scor de incredere si un ID unic pentru fiecare companie.
Totusi, nu am primit o cheie de autentificare si am presupus ca ideea challenge-ului este sa lucrez fara API, folosind doar fisierele puse la dispozitie.

 Ce am invatat din acest proiect:
•	Cum sa construiesc un scor personalizat de potrivire a entitatilor, adaptat la scenarii reale
•	Cum sa evaluez datele nu doar pentru acuratete, ci si pentru utilitatea practica
•	Sa citesc intotdeauna documentatia inainte 

