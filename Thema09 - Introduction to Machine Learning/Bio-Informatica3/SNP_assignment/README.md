# SNP reproduction assignment
This program allows the user to input any Multiple Sequence Alignment (MSA) and add a mutation to a given position, which will return the new score of that position. For this example an MSA of the myoglobin protein is used.

```
python3 SNP.py [-h] -f file [-matrix {45,50,62,80,90}] [-out] [-p position] [-m mutation]
options:
  -h, --help            show this help message and exit
  -f file               Path to the MSA (MultiFASTA only) [REQUIRED]
  -matrix {45,50,62,80,90}
                        BLOSUM matrix for calculating. Options: [45, 50, 62, 80, 90](Default = 62)
  -out                  Option for creating an output file. If not given, scores will print in terminal.
  -p position           Position of the mutation. [REQUIRED]
  -m mutation           The amino acid mutation of given position. [REQUIRED]
```

## Run example
To create an output CSV, add the `-out` option. The results will print in the terminal if this option is not added.

```bash
python3 SNP.py -f ../msa.fasta -p 3 -m A
```
Calculates the score of `position 3` with `mutation A` added. The mutation will be named `M<position>` in the results (e.a. `M3`)

In the second phase of the program, it will ask for more mutations. Proceed to add as many mutations as wanted, but keep in mind that mutations for the same positions will not be stored and rather overridden.

See `output.csv` for an output example.
