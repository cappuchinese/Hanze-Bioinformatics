# Introduction Data Mining
Naam: Lisa Hu <br>
Docent: Dave Langers <br>
Datum: 2022-09

## Table of contents
1. [Termen](#termen)
2. [Basis ML](#basis-ml)
3. [Classificatie methoden](#classificatie-methoden)
4. 

## Termen
+ **Overfitting**: Model bevat meer parameters dan de data kan verantwoorden.
<img src="https://miro.medium.com/max/640/1*dl4EiM_Io0_5jYtxRfTGhQ.png">

+ **Forward pruning**: Geen takken bij nodes.
+ **Backward pruning**: Geen nodes en subtrees.
+ **A priori**: Onvoorwaardelijke kans; aantallen van totaal.
+ **A posteriori**: Voorwaardelijke kans; Kans van voorwaarde.

## Basis ML
ML-algoritmen presteren beter als ze op meer data kunnen trainen ("ervaring")

+ Typen Machine Learning:
  1. **Supervised**: Alle data is gelabelt, de uitkomsten zijn gegeven.
  2. **Unsupervised**: Data is niet gelabelt, computer moet zelf uitvogelen.
+ Typen variabelen:
  + Categorisch/kwalitatief
    + Nominaal: Labels (Plaatsen)
    + Ordinaal: Labels met volgorde (Kleding S/M/L)
  + Numeriek/kwantitatief
    + Interval: Getallen met vaste tussenwaarden (Datum)
    + Ratio: Getallen met nulpunt/verhouding (Lengte, dubbel zo lang)

|             | supervised                      | unsupervised                       |
|-------------|---------------------------------|------------------------------------|
| categorisch | classificatie <br/>(bijv. tree) | clustering <br/>(bijv. k-means)    |
| numeriek    | regressie <br/>(bijv. lineair)  | dimensie reductie <br/>(bijv. PCA) |

## Entropie
$$\sum_{i=1}^{n} -p_{i} \cdot log(p_{i})$$
+ In recursie:
  + H<sub>in</sub>: De entropie van de eerste tak (*a priori*)
  + H<sub>uit</sub> = *&sum; \<kans van de mogelijke staat> &sdot; \<entropie van de mogelijke staat>* over de tweede tak (*a posteriori*)
  + H<sub>gain</sub> &or; &Delta;H = H<sub>in</sub> &minus; H<sub>uit</sub>
  + H<sub>split</sub>: Entropie over de kansen dat het de `uit` staten kan worden
  + Gain ratio = H<sub>gain</sub> &minus; H<sub>split</sub>

Zie Table 4.7, p.141

## Classificatie methoden
### Rules
#### ZeroR
+ Voorspelt uitkomst op basis van wat het meeste voorkomt.
+ Kijkt niet naar variabelen

#### OneR
+ Kijkt naar 1 variabele die het meeste informatie geeft in relatie tot voorspelling.
+ Bij categorisch: Voor elke variabele een `ZeroR` test voor elke mogelijke waarde.
+ Bij numeriek: Waarden sorteren, punten proberen te vinden om data te splitsen (buckets)
+ Missing values worden gezien als een apart attribuut.

### Trees
#### ID3
+ Gebruikt *information gain* (H<sub>gain</sub>)
+ Kan niet omgaan met missing values en numerieke data.
  + Met een filter omzetten naar nominaal
  + Ook filter voor missing values (`ReplaceMissingValues`)
+ Kan niet gevisualiseerd worden

#### J48
+ Gebruikt *gain ration*
+ Past *backward pruning* toe
  + In WEKA: `unpruned` optie.

## Cross-validation
Met wat voor data test je je algoritme?
+ **Resubstitutie**: Evaluatie op trainingsdata.
+ **Seperate testdata**: Evaluatie op afzonderlijke testdata.
+ **Holdout**: Splits de data op in trainingsdata en testdata.
+ **Repeated holdout**: Verhouding in trainingsdata en testdata veranderen voor elke instance.
+ **nfold cross-validation**: Partities van de data gebaseerd op *n*-voud.
+ **Leave One Out**: Cross validation waarbij *n* de hoeveelheid observaties aangeeft. Het algoritme wordt voor elke instance toegepast, waarbij alle andere instances gelden als trainingsdata en de gekozen als enkel-item testdata.
+ **Bootstrap**: *Random sampling with replacement*; Een bootstrap sample is ongeveer 2/3e originele data. Deze samples kunnen dan als soort vervanging gebruikt worden in de sets.

## Bayes
+ **Formule van Bayes**: $P(A|B) = {{P(B|A) \cdot P(A)} \over {P(B)}}$
+ **Naive Bayes**: $P(C|A_{n}) = {{P(A_{n}|C) \cdot P(C)} \over {P(A_{n})}}$
  + $P(A_{n}|C) \cdot P(C) = L_{C}$ (likelyhood)
  + $P(A_{n})$ = P(...) = $L_{C1} + L_{C2}$<br><br>
+ In WEKA (nominal data):
  + Telt vanaf 1 zodat berekeningen nooit 0 bevatten (*laplace estimator*).
  + In kleine dataset valt het misschien op, in grote dataset niet te merken.

## Nearest neighbor
+ Simpel en effectief, maar langzaam
+ Lazy learning: Neighbor is de kortste euclidische afstand tussen de training instance en test instance.
+ In WEKA: IBk
+ 

## Attribute selection
+ Single attribute evaluation (ranking)
  + Bijv. OneR accuracy (InfoGain, GainRatio)
+ Attribute subset selectioon
  + CFS: Correlation-based feature selection (scheme independent)
  + Wrapper (Scheme dependent)
