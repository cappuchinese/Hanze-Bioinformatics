

class Nucliotides:

    def __init__(self):
        self.__nucs = ["Adenine","Cytosine","Guanine","Thymine"]
        self.__pyrimidines = {"Cytosine","Thymine"}
        self.__d = dict(Adenine="A",Cytosine="C",Guanine="G",Thymine="T")


    def number_listing(self):
        """
        Given this list: [“Adenine”,“Cytosine”,“Guanine”,“Thymine”], 
        what would be the most efficient code to produce this output:
        “1: Adenine”,
        “2: Cytosine”,
        “3: Guanine”,
        “4: Thymine”,
        """
        for i,n in enumerate(self.__nucs):
            print("{}: {}".format(i+1,n))

    def short(self):
        """
        Given the same list [“Adenine”,“Cytosine”,“Guanine”,“Thymine”], 
        how can you produce this output using the map() function:
        “[‘A’, ‘C’, ‘G’, ‘T’]”
        """
        return list(map(lambda x: self.__d[x], self.__nucs))


    def filter_pyrimidines(self):
        """
        Again given the same list ([“Adenine”,“Cytosine”,“Guanine”,“Thymine”]), 
        how can you produce this output using the filter() function:
        “[‘Cytosine’, ‘Thymine’]”
        """
        return list(filter(lambda x: x in self.__pyrimidines, self.__nucs))


class Somequiz:
    def q1(self):
        """    
        Given this list [1, -1, 3, 5, -6, -2, 0], 
        how can you produce this output as efficiently as possible:
        “[1, 1, 3, 5, 6, 2, 0]”
        """
        l = [1,-1,3,5,-6,-2,0]
        return list(map(abs, l))

    def q2(self):
        """
        Suppose you have a list of tuples, each with one or more numbers, like this:
        [(2,1,3),(1,5,3,1),(7,3,5),(6,8),(1,4,2)]

        Write code to obtain a list with…
        All the maximum values of these tuples.
        The averages of these tuples.
        Tuples containing only the odd numbers. 
        This one is tricky, but there are several ways to solve it!
        """
        l = [(2,1,3),(1,5,3,1),(7,3,5),(6,8),(1,4,2)]
        return list(map(lambda x: max(x), l))
   

    def q3(self):
        """
        Suppose you have a list of tuples, each with one or more numbers, like this:
        [(2,1,3),(1,5,3,1),(7,3,5),(6,8),(1,4,2)]
        Write code to obtain a list with the averages of these tuples.
        """
        l = [(2,1,3),(1,5,3,1),(7,3,5),(6,8),(1,4,2)]
        return list(map( lambda x: sum(x)/len(x), l))


    def q4(self):
        """
        Suppose you have a list of tuples, each with one or more numbers, like this:
        [(2,1,3),(1,5,3,1),(7,3,5),(6,8),(1,4,2)]

        Write code to obtain a list with…
        Tuples containing only the odd numbers.
        This one is tricky, but there are several ways to solve it!
        """
        l = [(2,1,3),(1,5,3,1),(7,3,5),(6,8),(1,4,2)]
        return [ tuple(y for y in x if y%2!=0) for x in l ]
    

        

class Seqreq:
    def __init__(self):
        self.seqrec = [
                    {'name':'FHIT human', 'accno':'NP|1234', 'seq':'MRTEHIILVC'},
                    {'name':'FHIT mouse', 'accno':'NP|2315', 'seq':'MKSEHLVLVC'},
                    {'name':'FHIT gorilla', 'accno':'NP|6645', 'seq':'MRTDWAILAC'},
                    {'name':'FHIT fruitfly', 'accno':'NP|9732', 'seq':'MKSDHVILVC'}
                 ]


    def sort_seqrec(self):
        """
        Write code that will print these records alphabetically by name
        """
        return sorted(self.seqrec, key=lambda x: x["name"])
        

    def sort_assession(self):
        """
         Write code that will print these records numerically by the accession number 
        (that is, everything after the “NP|”)
        output: 
         ## {'name': 'FHIT human', 'seq': 'MRTEHIILVC', 'accno': 'NP|1234'}
         ## {'name': 'FHIT mouse', 'seq': 'MKSEHLVLVC', 'accno': 'NP|2315'}
         ## {'name': 'FHIT gorilla', 'seq': 'MRTDWAILAC', 'accno': 'NP|6645'}
          ## {'name': 'FHIT fruitfly', 'seq': 'MKSDHVILVC', 'accno': 'NP|9732'}
        """
        return sorted(self.seqrec, key=lambda x: int(x["accno"][3:]) )

    def sort_molweight(self):
        """
        Write code that will print these records ordered by molecular weight. 
        You should first find the molecular weights of the amino acids on the internet 
        and put them in a dict. Again, this one is not very easy.
        """
        aaWeights = {
            'A':89.000, 'R':174.000, 'N':132.000, 'D':133.000, 'C':121.000,
            'Q':146.000, 'E':147.000, 'G':75.000, 'H':155.000, 'I':131.000,
            'L':131.000, 'K':146.000, 'M':149.000, 'F':165.000,'P':115.000,
            'S':105.000, 'T':119.000, 'W':204.000, 'Y':181.000, 'V':117.000
            }

        return sorted(self.seqrec, key=lambda x: sum(map(lambda x: aaWeights[x], x["seq"])))




     
nucs = Nucliotides()
nucs.number_listing()
print(nucs.short())
print(nucs.filter_pyrimidines())

quiz = Somequiz()
print(quiz.q1())
print(quiz.q2())
print(quiz.q3())
print(quiz.q4())

s = Seqreq()
print(s.sort_assession())
print(s.sort_molweight())
print(s.sort_seqrec())

