# Bioinformatics 3
Lecturer: Ronald Wedema (WERD)<br>
Name: Lisa Hu <br>
Date: 2022-09

# Table of content
1. [Glossary](#glossary)
2. [Class assignments](#class-assignments)
3. [Notes](#notes)

## Glossary
+ **Curation** : Database entry checks
+ **Redundancy** : How much double code it contains (Lower is more single code)
+ **Motif** : 3D-structure that appear different, evolutionary unrelated molecules. Unrelated to sequence.
+ **Classical structural biology**: Know what it does/what it's involved with, but don't know what it looks like. (Prions)
+ **Structural genomics**: Predicting the structure and predict function, based on genomics. (Homology)

## Class assignments
### Which protein databases are used a lot recently?
+ Description of the database
+ What kind of information can be found?
+ Level of curation
+ Redundancy

#### PIR-PSD
+ Protein sequences
+ Superfamily classification
+ Expert curation

#### Alphafold Protein Structure Database
+ Best reviewed database at the moment
+ Protein structure and sequence
+ Structure based on AI

#### EMBL-EBI
+ Alphafold and 3D structures
+ Protein -> amino acid sequence

#### UniProt
+ Computational & expert curated
+ Universal information

#### PDB
+ Crystal structures
+ Search based on experimental method, X-ray resolution and organism

#### CATH
+ Classification:
  + Classes
  + Architecture: Orientation of secundary structure
  + Topology: Fold families, non-homologous
  + Superfamily: Common ancestor, homologous

#### SCOP
+ Classification:
  + Protein type: Groups folds and IUPRs into four groups: soluble, membrane, fibrous and intrinsically disordered.
  + Classes: Brings together folds and IUPRs.
  + IUPR (Intrinsically Unstructured Protein Region): Organises superfamiles or protein regions that do not adopt globular folded structure.
  + Fold: Composition of the secondary structures. Attribute of superfamily, but different distinct structural features can belong to a different fold.
  + Superfamily: More distant related protein domains based on common structural features.
  + Family: Related with clear evidence for their evolutionary origin.
+ Manual and computational inspection
+ Structural en functional relations of proteins in PDB

#### Dali Domain Dictionary
+ Protein structure comparison
+ Input PDB
+ Returns structural information dendogram

### GO terms for human beta globin on three levels of organization


## Notes
### Which techniques are used on proteins to classify them?
**Edman Degredation**: Afbreken van eerste aminozuur <br>
**SDS-PAGE**: jfhdgkjf <br>
**MALDI-TOF**: Tube filled with protein gets blasted by UV laser. Smaller bits fly out, detector meet de tijd. <br>
**PRIDE at EBI**: database for mass spectrometry

### 1. Domain and motifs
According to [InterPro](https://interpro-documentation.readthedocs.io/en/latest/faq.html#what-are-entry-types) definitions:
+ **Domain**: Distinct functional, structural or sequence units in biological context.
+ **Family**: The common evolutionary origin by related functions, structure or sequence.
+ **Homologous Superfamily**: Common evolutionary origin by related structure, but not sequence.
+ **Repeat**: Short sequence repeated within protein.
+ **Site**: Active site, Binding site, Conserved site, PTM site (post-trans mod)

Post-translational modifications are physical  zijn fysische eigenschappen, ook voor klassificatie.

### 2. Different structures
#### Three levels of organization for GO terms 
1. Localization
2. Biological process
3. Molecular function

#### Secundary structure
+ Secondary structure prediction from DSSP database -> DSSP code
+ Ramachandran plot

#### Tertiary structure
Protein folding main approaches:
1. X-ray crystallography
   + used to determine 80% of structures
   + requires high protein concentration
   + requires crystals
   + able to trace amino acid side chains
   + earliest structure solved was myoglobin
2. NMR
   + Magnetic field applied to proteins in solution
   + largest structures: 350 amino acids (40kD)
   + does not require crystallization
3. Prediction
   1. Homology modelling (comparative modelling). This is most useful when a template (protein of interest) can be matched to proteins of known structures. (<50% sequence recognition)
   2. Fold recognition (threading). A target sequence lacks identifiable sequence matches end yet may have folds in common with proteins of knows structure. (<35%)
   3. Ab initio prediction (template-free modelling). (<20%)

#### 3.

#### 4.

### Which tools are used for protein localisation?

### Protein functions

