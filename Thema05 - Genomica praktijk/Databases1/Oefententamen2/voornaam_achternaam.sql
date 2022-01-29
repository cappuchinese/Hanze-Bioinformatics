-- studentnr:
-- voornaam:
-- tussenvoegsels:
-- achternaam:

/*
vraag 1:
    • Voer het script 2021Tdatabases1.sql uit en geef als antwoorden de query die je zou gebruiken om de vragen te beantwoorden, dus niet het resultaat van de query!
    • Gebruik (tenzij er expliciet iets anders gevraagd wordt) de 'join-syntax' om tabellen aan
      elkaar te koppelen; het maken van een carthesisch produkt gevolgd door het filteren van de overtollige tupels m.b.v. de where-clausule wordt fout gerekend.
    • Overtollige joins worden fout gerekend, net als overtollige subqueries.
    • Voer de query uit in de mysql client, dat voorkomt slordigheidsfouten.
    • Verzamel de antwoorden in je tekstbestand zoals boven aangegeven.
*/

-- 1a (2 pnt): Geef de initialen en de achternamen van de scientists op alfabetische volgorde van achternaam.

-- 1b (4 pnt): Welke alignments zijn gevonden in de experimenten waar Drs. Herber aan meegewerkt heeft? Geef de id ‘s van de alignments.

-- 1c (4 pnt): Idem, maar gebruik nu de WHERE syntax in plaats van de JOIN om eerst een carthesisch product te maken.

-- 1d (5 pnt): Wat is de gemiddelde score van alle alignments?

-- 1e (5 pnt): Wat is/zijn de id’s van de querysequences waarvan PWTQRFFESFGDLSTPDAVMGNPKVKAHGK een deelsequentie is.

-- 1f (5 pnt): Zijn er experimenten waarvan onbekend is wanneer ze uitgevoerd zijn? Geef de ids in aflopende volgorde (van groot naar klein dus).

-- 1g (5 pnt): Bij welke experimenten heeft BSc. Wedema een BLOSUM62 matrix gebruikt?  Geef alleen de id van de experimenten.

-- 1h (5 pnt): Welke experimenten hebben alignments die gelijk zijn aan de hoogste alignment score? Geef alleen de id van de experimenten.

-- 1i (5 pnt): Laat per wetenschapper zien aan hoeveel experimenten (z|h)ij meegewerkt heeft. Geef alleen de fam_name en het aantal experimenten. Sorteer op achternaam van de wetenschapper op alfabetische volgorde.


/*
vraag 2: 
    • Gebruik voor deze vraag de database die je krijgt door het uitvoeren van 2021Tdatabases1.sql.
    • Geef als antwoorden de queries die je zou gebruiken om de vragen te beantwoorden, dus NIET het antwoord zelf!
    • Gebruik (tenzij er expliciet iets anders gevraagd wordt) de 'join-syntax' om tabellen aan elkaar te koppelen; het maken van een carthesisch product gevolgd door het filteren van de overtollige tupels m.b.v. de where-clausule wordt fout gerekend. 
    • Voer de queries uit in de mysql client, dat voorkomt slordigheidsfouten.Het gebruik van overtollige joins en subqueries is ook fout.
*/

-- 2a (5 pnt): Er is een fout gemaakt bij het invoeren van M. Herber. Voor zijn titel is abusievelijk MSc. ingevoerd terwijl dat Drs. zou moeten zijn. Geef de query die deze fout herstelt.

-- 2b (5 pnt): In de database kunnen nu wetenschappers zonder achternaam (fam_name) ingevoerd worden. Geef de query om de database zo aan te passen dat fam_name een verplicht veld wordt.

-- 2c ( pnt): Omdat D.Stapel gefraudeerd heeft moeten hij en zijn experimenten uit de database verwijderd worden. Geef de benodigde queries in de goede volgorde. Lukt het niet om een query op te stellen, dan kun je een deel van de punten verdienen door in plaats van de query zelf een korte omschrijving te geven van wat de query moet doen.  


/* 
VERGEET NIET VRAAG 3 TE MAKEN!

succes!

Arne

*/
