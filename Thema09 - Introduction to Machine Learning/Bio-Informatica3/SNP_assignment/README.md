# SNP reproduction assignment
This program allows the user to input any Multiple Sequence Alignment (MSA) and add a mutation to a given position, which will return the new score of that position. For this example an MSA of the myoglobin protein is used.

```
python3 SNP.py [-h] -f file [-matrix {45,50,62,80,90}] [-out] [-p position] [-m mutation]
options:
  -h, --help            show this help message and exit
  -f file               Path to the MSA (MultiFASTA only) [REQUIRED]
  -matrix {45,50,62,80,90}
                        BLOSUM matrix for calculating. Options: [45, 50, 62, 80, 90](Default = 62)
  -out                  Option for creating an output file. If not given, scores will print in terminal
  -p position           Position of the mutation. If none is given, the scores of every position will be given
  -m mutation           The amino acid mutation of given position.
```

The options `position` and `mutation` can only be used together. The program will abort if only one of the option is given. After the initial terminal run, the program will ask for new mutations. Since there are different run options, all the possible combinations are explained below.

## Run examples
To create an output CSV, add the `-out` option. The results will print in the terminal if this option is not added.

```bash
python3 SNP.py -f msa.txt
```
Calculates all the scores from the MSA. When the user inputs a new mutation in the second phase of the program, the score of that position will be overwritten.

```bash
python3 SNP.py -f msa.txt -p 3 -m A
```
Calculates the score of `position 3` with `mutation A` added. The mutations given in the second phase will be appended to the results if it takes place on a different position.
