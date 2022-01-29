def vraag1(my_list):
    return list(filter(lambda x: x%3 == 0 and x<30, my_list))


def vraag2():
    l1 = [1, 2, 3]
    l2 = [4, 5, 6]
    return list(map(lambda x: x[0] + x[1], zip(l1, l2)))


def vraag3():
    import re
    rna = 'AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGAAAAAAAA'
    pat = "AUG[AUGC]{30,1000}A{5,10}"
    return re.match(pat, rna)


class MRNAError(RuntimeError):
    def __init__(self, str):
        super().__init__(str)


class MRNA:
    def __init__(self, str):
        if self.check_rna(str):
            self.rna = str
        else:
            MRNAError("The string is not valid mRNA")

    def __str__(self):
        chunks = "".join([self.rna[x:x+3] + "-" for x in range(0, len(self.rna), 3)])
        return chunks

    def check_rna(self, str):
        for i in str:
            if i not in ["A", "C", "G", "U"]:
                return False

        if len(str) % 3 != 0:
            return False

        return True


print(vraag1([0,1,1,2,3,6,8,12,21,28,34,55]))
print(vraag2())
print(vraag3())

try:
  obj = MRNA('ACAGGUGCAACA')
  assert (type(obj) == MRNA)

  print(obj)

  obj2 = MRNA('FOOBAR')

except AssertionError:
  print ('Het object is niet van het goede type')
except NameError:
  print ('De klasse heeft niet de juiste naam')
except MRNAError:
  print ('De string is geen valide mRNA')