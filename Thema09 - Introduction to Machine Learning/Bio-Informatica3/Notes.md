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
+ **Homozygous deletion**: Zero copies; Deleting both allels in knockout
+ **Hemizygous deletion**: One copy is deleted and one copy remains

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
+ Protein -> amino acid sequMag ik straks iemandence

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

## Notes
### Hidden Markov Model *(p.181-184)*

### Protein classification techniques
+ **Edman Degredation**: Breaking the peptide bonds to get individual amino acids. <br>
+ **SDS-PAGE**: jfhdgkjf <br>
+ **MALDI-TOF**: Tube filled with protein gets blasted by UV laser. Smaller bits fly out, detector meet de tijd. <br>
+ **PRIDE at EBI**: database for mass spectrometry

### Protein structures
#### Domain and motifs (Primary structure)
According to [InterPro](https://interpro-documentation.readthedocs.io/en/latest/faq.html#what-are-entry-types) definitions:
+ **Domain**: Distinct functional, structural or sequence units in biological context.
+ **Family**: The common evolutionary origin by related functions, structure or sequence.
+ **Homologous Superfamily**: Common evolutionary origin by related structure, but not sequence.
+ **Repeat**: Short sequence repeated within protein.
+ **Site**: Active site, Binding site, Conserved site, PTM site (post-trans mod)

Post-translational modifications are physical features (also for classification).

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

### Functional genomics
Differences in phenotype, but with same genomics: **(fig 14.1 ~ p.636)**
natural / experimental
+ DNA: SNPs; epigenomics / knockout collections transgenic animals
+ RNA: transcriptome profiling (RNA-seq) / RNA; siRNA
+ Protein: protein localization; protein-protein interactions; pathways / chemical modifications

8 model organisms to learn functional genomics: **(p.638)**
+ E. coli (Bacteria): Small, operons, easy to work with
+ Sccharomyces cerevisiae (Yeast): A lot of orthologues and paralogues
+ Arabidopsis thaliana (Plant): Big genome
+ Caenorhabditis elegans (Nematode): 
+ Drosophila melanogaster (Fruitfly): Linkage maps and recombination
+ Danio rerio (Zebrafish): Short reproduction time; Embryo is transparent (visualization transgenes)
+ Mus musculus (Mouse): Short reproduction time; ~10.000 knockout genes
+ Humans: Not a model per se; Nature plays big roles on diseases, radiation, etc.

#### Reverse genetic screens
+ Large number of genes is systematically inhibited one by one (knockout, gene trapping, etc.). (Which phenotype comes forward from a different genotype?)
+ **Knockout**: **p.653**
+ **RNA silencing**: **p.662**
+ **Genetic footprinting**: **Figure 14.15 ~ p.661**

#### Forward genetic screens
+ Starting point is phenotype. (Can a mutation lead to a different phenotype?)
+ **Chemical mutagenesis**: **p.665**

#### Protein-protein interactions *(p.672)*
+ **Co-immunoprecipitation**: Specific antibodies directed against a protein are used to precipitate the protein along with any associated binding partners.
+ **Affinity chromatography**: a cDNA construct encodes a protein of interest in frame with glutathione S-transferase (GST) or some other tag. A resin to which glutathione is covalently attached is incubated with a GST fusion protein, and it binds to the resin along with any binding partners. Irrelevant proteins are eluted and then the specific binding complex is eluted and its protein content is identified.
+ **Cross-linking**:
+ Skip last 3

*Yeast two-hybrid system*

#### From Pairwise Interactions to Protein Networks *(p.678)*
+ Assessment
+ choice
+ experimental
+ variation
+ categories

### Molecular Phylogeny and Evolution
#### Molecular Clock Hypothesis (p.250)

#### Positive and Negative Selection
+ More synonymous than non-synonymous: **Negative**
+ More non-synonymous than synonymous: **Positive**
+ Both equals: Neutral

#### Neutral Theory of Molecular Evolution
+ The main cause of evolutionary change (or variability) due to random drift of mutant alleles.

#### Consider using DNA, RNA or protein
Depending on what 

#### Properties of Trees
+ **OTU**: Operational Taxonomic Unit; Unit of the genome to base the tree on.
+ **Clade**: Groups of organisms including the common ancestor.
+ **Node**: Species that split into more branches.
+ **Edge**: The branch between nodes.
+ **Extant**: The leafs of the tree that are alive.
+ **Inferred/Internal node**: Do not have to be alive, sometimes based on calculations and not alignment.
+ **Bifurcating internal node**: Tree splits into two.
+ **Multifurcating internal node**: Tree splits into three or more.
+ **Outgroup tree root**: Taxon that's distantly related to the other OTUs.
+ **Mid tree root**: The longest edge contains the most mutations.

[//]: # (TODO niet extant?)

+ Neighbor-joining tree styles: Rectangular, topology only, UPGMA, radial
+ Rectangular style: Branch lengths show 
+ UPGMA tree: Always contains a root

#### Type of Trees
##### Species Trees or Gene/Protein Trees

##### DNA, RNA, Protein-Based Trees

[//]: # (TODO p.269 fig.7.15)

##### Five Stages of Phylogenetic Analysis (p.271)
+ Step 1: Sequence Acquisition
+ Step 2: Multiple Sequence Alignment
+ Step 3: Models of substitution
  + Divergence
  + Hamming: $D = n/N$; For alignment length *N* with *n* mutations, *D* is the divergence.
  + Jukes and Cantor: $D = \minus{3}\over{4}ln(1\minus{4}\over{3}p)$
+ Step 4: Tree-Building Methods
  + Distance-Based: Using one of named distance equations to build a distance matrix. (UPGMA and neighbor-joining)
  + Character-Based: Looks at the alignment columns and creates all the possible trees (exhaustively), returning the best tree possible. (Maximum parsimony and likelihood)
+ Step 5: Bootstrapping
  + Random values from columns 
