# HMMER assignment

To search potential other sequences, a model needs to be build first:
```
hmmbuild --amino myoglobin.hmm ../msa.txt
```

`seqdb` is an argument in `hmmsearch` which accepts a file containing all the potential sequences hmmsearch is allowed to match with the HMM model given. Since we do not have a file with such quantities of sequences to match it with, the online tool will be used.

[This tool](https://www.ebi.ac.uk/Tools/hmmer/search/hmmsearch) asks for various types of inputs and in this case the `myoglobin.hmm` file will be uploaded. This HMM will be matched with the `Reference Proteomes` database. `new_sequences.txt` shows the chosen sequences and the link to it. For the sake of time, only two sequences were chosen.

The final step is to check these sequences in the PFAM database. For this, [InterPro](https://www.ebi.ac.uk/interpro/) was used. The search was successful as both sequences were marked as myoglobin sequences.
