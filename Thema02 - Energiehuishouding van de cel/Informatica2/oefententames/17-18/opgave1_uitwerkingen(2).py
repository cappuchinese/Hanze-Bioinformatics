#!/usr/bin/env python3

#opgave 1A

first_name = "hier je voornaam"
last_name = "hier je achternaam"


def print_name(surname, given_name):
    print("Dit zijn de antwoorden van", given_name, surname)


print_name(given_name=first_name, surname=last_name)
#indien keywordargumenten in functie definitie: 2p


#opgave 1B

#herschrijf onderstaande functie naar een functie met oneindig veel argumenten [5p]
def print_all(a,b,c,d):
    print(a, end=' ')
    print(b, end=' ')
    print(c, end=' ')
    print(d, end=' ')

print_all("1B:", 2,"primes", [251,257])

#################################################
#solution
def print_alla(*arg):
    for i in args:
        print(i, end=' ')


#################################################


#opgave 1C

# herschrijf de onderstaand code naar een generator function die
# ook op de juiste manier aangeroepen wordt[5p]

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

# in te vullen code:

# vul de onderstaand code aan zodat generator_primer een generator function wordt [5p]
def generate_primer(primerlength):
    dna = "ATCG"
    #genereer hier een random primers (doe dat een primerlength aantal keer)
    
    # roep op de juiste manier aan [5p]
    # programmeer op deze regel een for loop die de generate_primer functie aanroept met de primerlength
    print(base, end='')


#################################################

#solution
def generate_primer(primerlength):
    dna = "ATCG"
    for i in range(primerlength):
        yield random.choice(dna)

for base in generate_primer(10):
    print(base, end='')


#################################################



#opgave 1D

rna = ["AUCGUC", "CGUCA", "GCAUC", "ACCUUGC", "CACACUU", "UUCAG", "AGGGG"]
list_comprehension = [i.replace("U", "T") for i in rna if i.startswith("A")]
print(list_comprehension)
# basis voor comprehension en werkend: vb [i for i in rna]: 4p
# comprehension werkend voor U>T: +3p
# comprehension werkend if i.startswith: +3p

# combi map/filter werkend en helemaal goed: 6p
# comprehension werkend maar code kan efficienter: 8p
