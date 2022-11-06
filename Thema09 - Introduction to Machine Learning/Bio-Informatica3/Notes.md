# Bioinformatics 3
Lecturer: Ronald Wedema (WERD)<br>
Name: Lisa Hu <br>
Date: 2022-09

# Table of content
1. [Glossary](#glossary)
2. [Class assignments](#class-assignments)
3. [Notes](#notes)
   + [Hidden Markov Model](#hidden-markov-model)
   + [Molecular Phylogeny and Evolution](#molecular-phylogeny-and-evolution)
   + [Proteins](#proteins)
   + [Functional Genomics](#functional-genomics)
4. [Guest classes](#guest-classes)

# Glossary
+ **Curation** : Database entry checks
+ **Redundancy** : How much double code it contains (Lower is more single code)
+ **Motif** : 3D-structure that appear different, evolutionary unrelated molecules. Unrelated to sequence.
+ **Classical structural biology**: Know what it does/what it's involved with, but don't know what it looks like. (Prions)
+ **Structural genomics**: Predicting the structure and predict function, based on genomics. (Homology)
+ **Homozygous deletion**: Zero copies; Deleting both allels in knockout
+ **Hemizygous deletion**: One copy is deleted and one copy remains

# Class assignments
## Which protein databases are used a lot recently?
+ Description of the database
+ What kind of information can be found?
+ Level of curation
+ Redundancy

### PIR-PSD
+ Protein sequences
+ Superfamily classification
+ Expert curation

### Alphafold Protein Structure Database
+ Best reviewed database at the moment
+ Protein structure and sequence
+ Structure based on AI

### EMBL-EBI
+ Alphafold and 3D structures
+ Protein -> amino acid sequence

### UniProt
+ Computational & expert curated
+ Universal information

### PDB
+ Crystal structures
+ Search based on experimental method, X-ray resolution and organism

### CATH
+ Classification:
  + Classes
  + Architecture: Orientation of secundary structure
  + Topology: Fold families, non-homologous
  + Superfamily: Common ancestor, homologous

### SCOP
+ Classification:
  + Protein type: Groups folds and IUPRs into four groups: soluble, membrane, fibrous and intrinsically disordered.
  + Classes: Brings together folds and IUPRs.
  + IUPR (Intrinsically Unstructured Protein Region): Organises superfamiles or protein regions that do not adopt globular folded structure.
  + Fold: Composition of the secondary structures. Attribute of superfamily, but different distinct structural features can belong to a different fold.
  + Superfamily: More distant related protein domains based on common structural features.
  + Family: Related with clear evidence for their evolutionary origin.
+ Manual and computational inspection
+ Structural en functional relations of proteins in PDB

### Dali Domain Dictionary
+ Protein structure comparison
+ Input PDB
+ Returns structural information dendogram

# Notes
## Hidden Markov Model
+ Generates a position-specific scoring system based on probability.
+ *States* are the different possibilities the model can follow.
+ *Transition functions* describe how to move from one state to another (mostly expressed as probabilities).
+ The lowest probability outcome is usually the best model.

## Molecular Phylogeny and Evolution
### Molecular Clock Hypothesis
+ By comparing the  over time for every given gene, the rate of molecular evolution is constant.
+ ${{n}\over{100}} = 1 - e^{-(m/100)}$
+ Rate varies among different organisms.
+ Main force guiding the clock molecular clock is selection. Clock varies among different genes and across different parts of individual gene.
+ Only applicable when a gene in question 

### Positive and Negative Selection
+ **Positive selection**: Selected traits in a population that enhance survival.
+ **Negative selection**: Mutated traits reduce fitness.
+ More synonymous than nonsynonymous: **Negative**
+ More nonsynonymous than synonymous: **Positive**
+ Both equals: Neutral

### Neutral Theory of Molecular Evolution
+ The main cause of evolutionary change (or variability) due to random drift of mutant alleles.
+ Most nonsynonymous mutations are deleterious -> not observed as substitutions in the population.

### Properties of Trees
+ Nodes represent taxonomic units.
  + **Node**: Species that split into more branches.
  + **Edge**: The branch between two nodes.
  + **OTU**: Operational Taxonomic Unit; Unit of the genome in *extant* species.
    + **Extant**: The leafs of the tree (alive).
+ **Clade**: Groups of organisms including the common ancestor.
+ **Inferred/Internal node**: Ancestral species; Do not have to be alive, sometimes based on calculations and not alignment.
  + **Bifurcating internal node**: Tree splits into two.
  + **Multifurcating internal node**: Tree splits into three or more.
+ Tree roots represent the most recent common ancestor of all the given sequences.
  + **Outgroup tree root**: Taxon that's distantly related to the other OTUs.
  + **Mid tree root**: The longest edge contains the most mutations.

### Species Trees vs. Gene/Protein Trees
+ **Speciation event**: The moment a single ancestral species diverge into multiple new species.
+ Analysis of molecular evolution can be complicated by the time two species diverge:
  1. The divergence of two genes from two species may have predated the speciation event -> may cause overestimation of branch lengths;
  2. The topology of gene tree may differ from species tree.

### DNA, RNA, or Protein-Based Trees
+ Protein pros: lower rate of substitutions in protein relative to DNA -> more appropriate for comparisons across widely divergent species.
+ DNA pros:
  + Allows study of synonymous and nonsynonymous mutations rated;
  + Include directly observed substitutions (single-nucleotide, sequential, and coincidental).
    + Single-nucleotide: only one of the observations;
    + Sequential: in the middle of the codon;
    + Coincidental: both observations are mutated;
  + Can also show mutations without producing a mismatch (parallel, convergent, and back);
    + Parallel: both observations are the same mutation;
    + Convergent: change from ancestral sequence mutated into the same descendant sequence;
    + Back: previous mutation mutated back to ancestral sequence.
  + Noncoding regions can be analyzed. Conservation differs greatly in different regions;
  + **Pseudogenes**: Nonfunctional DNA segments that resemble functional genes.
  + Rate of transitions and transversions.
+ Step matrices describe number of steps required to change from one to another.

### Five Stages of Phylogenetic Analysis
1. Sequence Acquisition
   + Selection of sequences for analysis
2. Multiple Sequence Alignment
   + Inspect alignment to be sure that all sequences are homologous. 
   + Lower the gap creation and/or gap extension penalties if distantly related sequences are aligned outside the block of others. 
   + The complete sequence is not known for many genes -> analyse portions.
   + Gaps could represent insertion or deletion that algorithms can't handle -> delete all the columns containing gaps.
3. Models of substitution
   + Divergence
   + Hamming: $D = n/N$; For alignment length *N* with *n* mutations, *D* is the divergence.
   + Jukes and Cantor: $D = -{{3}\over{4}}ln(1-{{4}\over{3}}p)$
4. Tree-Building Methods
   + Distance-Based: Using one of named distance equations to build a distance matrix. (UPGMA and neighbor-joining)
   + Character-Based: Looks at the alignment columns and creates all the possible trees (exhaustively), returning the best tree possible. (Maximum parsimony and likelihood)
5. Bootstrapping
   + Random values from columns

## Proteins
### Protein classification techniques
+ **Edman Degredation**: Breaking the peptide bonds to get individual amino acids. <br>
+ **SDS-PAGE**: jfhdgkjf <br>
+ **MALDI-TOF**: Tube filled with protein gets blasted by UV laser. Smaller bits fly out, detector meet de tijd. <br>
+ **PRIDE at EBI**: database for mass spectrometry

### Three levels of organization for GO terms 
1. Localization
2. Biological process
3. Molecular function

### Primary structure
According to [InterPro](https://interpro-documentation.readthedocs.io/en/latest/faq.html#what-are-entry-types) definitions:
+ **Domain**: Distinct functional, structural or sequence units in biological context.
+ **Family**: The common evolutionary origin by related functions, structure or sequence.
+ **Homologous Superfamily**: Common evolutionary origin by related structure, but not sequence.
+ **Repeat**: Short sequence repeated within protein.
+ **Site**: Active site, Binding site, Conserved site, PTM site (post-trans mod)

Post-translational modifications are physical features (also for classification).

### Secundary structure
+ Secondary structure prediction from DSSP database -> DSSP code
+ Ramachandran plot

### Tertiary structure
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

## Functional genomics
Differences in phenotype, but with same genomics: **(fig 14.1 ~ p.636)**
natural / experimental
+ DNA: SNPs; epigenomics / knockout collections transgenic animals
+ RNA: transcriptome profiling (RNA-seq) / RNA; siRNA
+ Protein: protein localization; protein-protein interactions; pathways / chemical modifications

### 8 model organism **(p.638)**
+ E. coli (Bacteria): Small, operons, easy to work with
+ Sccharomyces cerevisiae (Yeast): A lot of orthologues and paralogues
+ Arabidopsis thaliana (Plant): Big genome
+ Caenorhabditis elegans (Nematode): 
+ Drosophila melanogaster (Fruitfly): Linkage maps and recombination
+ Danio rerio (Zebrafish): Short reproduction time; Embryo is transparent (visualization transgenes)
+ Mus musculus (Mouse): Short reproduction time; ~10.000 knockout genes
+ Humans: Not a model per se; Nature plays big roles on diseases, radiation, etc.

### Reverse genetic screens
+ Large number of genes is systematically inhibited one by one (knockout, gene trapping, etc.). (Which phenotype comes forward from a different genotype?)
+ **Knockout**: **p.653**
+ **RNA silencing**: **p.662**
+ **Genetic footprinting**: **Figure 14.15 ~ p.661**

### Forward genetic screens
+ Starting point is phenotype. (Can a mutation lead to a different phenotype?)
+ **Chemical mutagenesis**: **p.665**

### Protein-protein interactions *(p.672)*
+ **Co-immunoprecipitation**: Specific antibodies directed against a protein are used to precipitate the protein along with any associated binding partners.
+ **Affinity chromatography**: a cDNA construct encodes a protein of interest in frame with glutathione S-transferase (GST) or some other tag. A resin to which glutathione is covalently attached is incubated with a GST fusion protein, and it binds to the resin along with any binding partners. Irrelevant proteins are eluted and then the specific binding complex is eluted and its protein content is identified.
+ **Cross-linking**:
+ Skip last 3

*Yeast two-hybrid system*

### From Pairwise Interactions to Protein Networks *(p.678)*
+ Assessment
+ choice
+ experimental
+ variation
+ categories

## Bacteria and Archea: Genome Analysis
### Classification Bacteria and Archaea
1. Morphology
   + Different forms of the cell
2. Genome size
   + 1 gene per kilobase
   + Obligate symbiont/parasite have smaller genome size than host associated or free-living
3. Lifestyle
   + Extracellular 
   + Facultatively intracellular
   + Extremophilic *
   + Epicellular bacteria *
   + Obligate intracellular and symbiotic *
   + Obligate intracellular and parasitic *<br>
   \* These tend to have smaller genome size
4. Relevance human disease
   + Some bacteria cause the same disease
5. Molecular phylogeny using rRNA
   + MSA of 16S and other small variants rRNA
   + Proteobacteria, Firmicutes, Actinabacteria, and Bacteroidetes are the only phyla easy to grow in a lab, which accounts for 90% of the known bacteria: Very unreliable, only 1% of all bacteria
6. Molecular phylogeny using other molecules

### The Human Microbiome
1. There are extraordinary bioinformatics challenges associated with these types of projects.
2. Most of the microbiome is bacterial.
3. There is no single reference microbiome due to between individuals.
4. Each body region does have characteristic bacteriall species within each hindividual, oftern occur in common between individuals.
5. ???????????????? TODO

### Analysis of Bactarial and Archaeal Genomes
#### Nucleotide Composition
+ GC has three hydrogen bonds, making is more stable in extreme heat.
+ Eukaryotic, archaeal and bacteria have different GC percentages (~60%, 20-35%, 20-66%).
+ GC can fluctuate within genome due to horizontal gene transfer.
+ Makes the work of bioinformatics harder. Which is the original gene?

#### Finding Genes
1. Open reading frames (ORF): Start to stop codon
2. Consensus for ribosome binding (Shine-Dalgarno): Short sequence that implies ribosome binding
3. Pattern of codon usage
4. Homology of putative gene to other genes
+ GLIMMER (a HMM) sequentially scans nucleotide sequences for particular kmers and estimates the probability of that pattern occuring in a real gene.

#### Gene annotation
+ Used to assign functions to genes and to reconstruct metabolic pathways or other higher levels of gene function.
+ RAST is an automated annotation webservice.

# Guest classes
## Molecular Dynamics (Tsjerk Wassenaar)
All biochemical systems are dynamic: everything is always moving.
+ DNA is boring: structure is not important.
+ mRNA is already more interesting: it folds itself and has different functions.
+ Proteins are the molecular machines, executing all the functions in an organism: structure is interesting.

### Molecular Dynamics Simulations
+ Simulations are done with Newton's laws of motion. Quantum mechanics is also possible, but is much more complex and expensive.
+ The amount of atoms calculated lies between ten thousands to millions.
+ A simulation can sometimes take 9 billion steps.
+ If all the positions and forces are known, the past and future can be predicted.

### Techniques
+ **Force field**
  + Contains functions to describe the interactions (e.a. interactions between polar and apolar parts).
  + Also contains functions describing bonds, angles and dihedrals.
  + Over 2 bonds is not predictable anymore, only with calculations.
+ **X-ray Crystallography**
  + Crystallizing proteins by stacking layers on top of each other.
+ **Electron Microscopy**
  + Freeze the parts and take loads of pictures.
  + Combine the pictures for analysis.
+ **Nucleaer Magnetic Resonance Spectroscopy**
  + Check the average distance between atoms.

### Simulation process
1. Structure
2. Topology
3. Solvation
4. Equilibration
5. Production
6. Analysis
    + Quality assurance (Validate the results)
    + Validation (Does it match the experimental data)
    + Prediction (What are the observations in further experiments)

+ There are different levels for the length of simulations. To up the efficiency, the same atoms are clustered to create "superatoms".
+ Cystosol is a good example of a simulation. It contains 35% water and the rest is RNA, proteins, sugars, etc.
+ Different kinds of membranes have different kinds of lipids. Humans have around 1000 different lipids.
+ New on the market: simulations on organelles instead of proteins.
