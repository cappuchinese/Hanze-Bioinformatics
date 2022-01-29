#!/usr/bin/env python3

#IMPORTS
import random
import sys

#opgave 1A [5p]

first_name = "Lisa"
last_name = "Hu"


def print_name(surname, given_name):
    print("Dit zijn de antwoorden van", given_name, surname)


print_name(given_name=first_name, surname=last_name)


#opgave 1B [5p]

#herschrijf onderstaande print_all functie naar een functie
#met oneindig veel argumenten

def print_all(*a):
    for i in a:
        print(i, end=' ')

print_all("1B:", 2,"primes", [251,257])



#opgave 1C [10p]

#herschrijf de onderstaand code (zie in te vullen code) naar een generator function
#die ook op de juiste manier aangeroepen wordt

#originele code
def primer_list(primerlength):
    """
        The generate_primer function generates random primers
        """
    dna = "ATCG"
    primer = []
    for base in range(primerlength):
        random_base = random.choice(dna)
        primer.append(random_base)
    return "".join(primer)

print(primer_list(10))

#in te vullen code:

#vul de onderstaand code aan zodat generator_primer een generator function wordt
def generate_primer(primerlength):
    dna = "ATCG"
    #genereer hier een DNA letter (doe dat een primerlength aantal keer)
    
#roep op de juiste manier aan
#programmeer op deze regel een for loop die de generate_primer functie aanroept met de primerlength
    print(base, end='')


#opgave 1D [10p]

rna = ["AUCGUC", "CGUCA", "GCAUC", "ACCUUGC", "CACACUU", "UUCAG", "AGGGG"]
for i in rna:
    if i.startswith("A"):
        x = i.replace("U", "T")

list_comprehension = [x.replace("U", "T") for x in rna if x.startswith("A")]
print(list_comprehension)

