#

## Overview
The RIKEN BioResource Research Center (BRC) is exploring the model organisms which are expected to be available for medical science research by executing the SPARQL queries for the RIKEN bioresource Knowledge graph integrated with the Bgee, a gene expression database, the Orthologous MAtrix (OMA, an orthology database), the DisGeNET, a human gene-disease association, Mouse Genome Informatics (MGI), UniProt, and four disease ontologies stored in the RIKEN BioResource MetaDatabase. This page shares the SPARQL query examples and the related data.

## Reference
https://github.com/tarcisiotmf/swat4hcls

## RIKEN BioResource SPARQL endpoint
https://knowledge.brc.riken.jp/sparql  


## SPARQL query examples and the ralated data
### Additional file 1 (SPARQL query example 1)  
[Example_1_Additional_file_1.txt](https://github.com/kushidat/broaderPredicate_uberon/blob/main/Example1_Additional_file_1.txt)  
Description: A federated SPARQL query for Alzheimer's disease using DisGeNET   
Search parameters:  
  - Federated or Centralized: Federated
  - Disease: Alzheimer's disease (umls:C0002395)
  - GDA: DisGeNET (https://www.disgenet.org/)
  - Anatomical parts: prefrontal cortex (UBERON:0000451)
  - Confidence Level: high
  - Expression Level: > 99
  - Property paths: No

The average runtime (10 times): 42 seconds  
Results:  
| Query approach | No. of mice | RIKEN Mouse IDs | No. of genes![image] | Ensembl Gene IDs | Gene labels |
|:---|:---:|:---|:---:|:---|:---:|
|Example 1: Federated query for AD | 21 | RBRC06342,RBRC06343,<br>RBRC06344,RBRC10041,<br>RBRC10042,RBRC10700,<br>RBRC10701,RBRC10043,<br>RBRC11518,RBRC03298,<br>RBRC03388,RBRC03389,<br>RBRC03390,RBRC03391,<br>RBRC03418,RBRC03419,<br>RBRC03420,RBRC03421,<br>RBRC03422,RBRC03423,<br>RBRC00052 | 2 | ENSG00000130203,<br>ENSG00000142192 | APOE,<br>APP |  


### Additional file 2 (SPARQL query example 2)  
[Example2_Additional_file_2.txt](https://github.com/kushidat/broaderPredicate_uberon/blob/main/Example2_Additional_file_2.txt)  
Description: A centralized SPARQL query for Alzheimer's disease using DisGeNET   
Search parameters:  
  - Federated or Centralized: Centralized
  - Disease: Alzheimer's disease (umls:C0002395)
  - GDA: DisGeNET (https://www.disgenet.org/)
  - Anatomical parts: prefrontal cortex (UBERON:0000451)
  - Confidence Level: high
  - Expression Level: > 99
  - Property paths: No
    
The average runtime (10 times): 40 seconds  
Results:  
| Query approach | No. of mice | RIKEN Mouse IDs | No. of genes![image] | Ensembl Gene IDs | Gene labels |
|:---|:---:|:---|:---:|:---|:---:|
|Example 2: Centralized query for AD | 21 | RBRC06342,RBRC06343,<br>RBRC06344,RBRC10041,<br>RBRC10042,RBRC10700,<br>RBRC10701,RBRC10043,<br>RBRC11518,RBRC03298,<br>RBRC03388,RBRC03389,<br>RBRC03390,RBRC03391,<br>RBRC03418,RBRC03419,<br>RBRC03420,RBRC03421,<br>RBRC03422,RBRC03423,<br>RBRC00052 | 2 | ENSG00000130203,<br>ENSG00000142192 | APOE,<br>APP |  

### Additional file 3 (SPARQL query example 3)  
[Example3_Additional_file_3.txt](https://github.com/kushidat/broaderPredicate_uberon/blob/main/Example3_Additional_file_3.txt)  
Description: A federated SPARQL query for Melanoma using DisGeNET  
Search parameters:  
  - Federated or Centralized: Federated
  - Disease: Melanoma (umls:C0025202) 
  - GDA: DisGeNET (https://www.disgenet.org/)
  - Anatomical parts: skin of body (UBERON:0002097)
  - Confidence Level: high
  - Expression Level: > 99
  - Property paths: No
    
The average runtime (10 times): 38 seconds  
Results:  
| Query approach | No. of mice | RIKEN Mouse IDs | No. of genes![image] | Ensembl Gene IDs | Gene labels |
|:---|:---:|:---|:---:|:---|:---:|
|Example 3: Federated query for Melanoma | 18 | RBRC10866,RBRC01088,<br>RBRC02449,RBRC02450,<br>RBRC02451,RBRC02460,<br>RBRC02464,RBRC02466,<br>RBRC02473,RBRC02475,<br>RBRC02479,RBRC02481,<br>RBRC02484,RBRC02485,<br>RBRC02487,RBRC02488,<br>RBRC02586,RBRC11578 | 1 | ENSG00000174775 | HRAS |  

### Additional file 4 (SPARQL query example 4)  
[Example4_ Additional_file_4.txt](https://github.com/kushidat/broaderPredicate_uberon/blob/main/Example4_Additional_file_4.txt )  
Description: A centralized SPARQL query for Melanoma using DisGeNET  
Search parameters:  
  - Federated or Centralized: Centralized
  - Disease: Melanoma (umls:C0025202) 
  - GDA: DisGeNET (https://www.disgenet.org/)
  - Anatomical parts: skin of body (UBERON:0002097)
  - Confidence Level: high
  - Expression Level: > 99
  - Property paths: No
    
The average runtime (10 times): 20 seconds  
Results:  
| Query approach | No. of mice | RIKEN Mouse IDs | No. of genes![image] | Ensembl Gene IDs | Gene labels |
|:---|:---:|:---|:---:|:---|:---:|
|Example 4: Centralized query for Melanoma | 18 | RBRC10866,RBRC01088,<br>RBRC02449,RBRC02450,<br>RBRC02451,RBRC02460,<br>RBRC02464,RBRC02466,<br>RBRC02473,RBRC02475,<br>RBRC02479,RBRC02481,<br>RBRC02484,RBRC02485,<br>RBRC02487,RBRC02488,<br>RBRC02586,RBRC11578 | 1 | ENSG00000174775 | HRAS | 

### Additional file 5 (A Python script)
[tsv2rdf_uberonKgx_to_uberon_broader20230723.py](https://github.com/kushidat/broaderPredicate_uberon/blob/main/tsv2rdf_uberonKgx_to_uberon_broader20230723.py)  
Description: This is a Python script for converting the latest **uberon_kgx_tsv_edge.tsv** from the [kg-uberon webpage](https://kg-hub.berkeleybop.io/kg-obo/uberon/) in the [KG-OBO project](https://github.com/Knowledge-Graph-Hub/kg-obo) of the [KG-Hub](https://kghub.org/) to two ttl format files includes [subject_broader_object_from_BFO_0000050.ttl](https://github.com/kushidat/broaderPredicate_uberon/blob/main/subject_broader_object_from_BFO_0000050.ttl)  (Additional file 6) and [subject_broader_object_from_subClassOf.ttl](https://github.com/kushidat/broaderPredicate_uberon/blob/main/subject_broader_object_from_subClassOf.ttl) (Additional file 7).  

![image_additional_file_5](https://github.com/kushidat/broaderPredicate_uberon/assets/1106622/5d259025-5ec9-46d0-8b4d-d1c360317054)

### Additional file 6 (RDF data)  
[subject_broader_object_from_BFO_0000050.ttl](https://github.com/kushidat/broaderPredicate_uberon/blob/main/subject_broader_object_from_BFO_0000050.ttl)  
Description: This is a turtle file converted from the latest uberon_kgx_tsv_edge.tsv in the [kg-uberon webpage](https://kg-hub.berkeleybop.io/kg-obo/uberon/) in the [KG-OBO project](https://github.com/Knowledge-Graph-Hub/kg-obo) of the [KG-Hub](https://kghub.org/). This file includes the borader predicate’s relationships among terms created from the BFO:0000050 (pratOf) relations in the uberon_kgx_tsv_edge.tsv in the [kg-uberon](https://kg-hub.berkeleybop.io/kg-obo/uberon/).  

![sample_subject_broader_object_from_BFO_0000050](https://github.com/kushidat/broaderPredicate_uberon/assets/1106622/3f407b1f-434f-41e7-a54e-d03da5e5a3b6)

### Additional file 7 (RDF data)  
[subject_broader_object_from_subClassOf.ttl](https://github.com/kushidat/broaderPredicate_uberon/blob/main/subject_broader_object_from_subClassOf.ttl)  
Description: This is a turtle file converted from the latest uberon_kgx_tsv_edge.tsv in the [kg-uberon webpage](https://kg-hub.berkeleybop.io/kg-obo/uberon/) in the [KG-OBO project](https://github.com/Knowledge-Graph-Hub/kg-obo) of the [KG-Hub](https://kghub.org/). This file includes the borader predicate’s relationships among terms created from the rdfs:subClassOf relations in the uberon_kgx_tsv_edge.tsv in the [kg-uberon](https://kg-hub.berkeleybop.io/kg-obo/uberon/).  

### Additional file 8 (SPARQL query example 5)  
[Example5_Additional_file_8.txt](https://github.com/kushidat/broaderPredicate_uberon/blob/main/Example5_Additional_file_8.txt)  
Description: A centralized query for Melanoma using DisGeNET and the property paths  
Search parameters:  
  - Federated or Centralized: Centralized
  - Disease: Melanoma (umls:C0025202) 
  - GDA: DisGeNET (https://www.disgenet.org/)
  - Anatomical parts: skin of body (UBERON:0002097)
  - Confidence Level: high
  - Expression Level: > 99
  - Property paths: Yes
    
The average runtime (10 times): 72 seconds  
Results:  
| Query approach | No. of mice | RIKEN Mouse IDs | No. of genes | Ensembl Gene IDs | Gene labels |  No. of anatomical entities | Uberon IDs | Anatomical entity labels |
|:---|:---:|:---|:---:|:---|:---:|:---:|:---|:---|
|Example 5: Centralized query for Melanoma using the broader predicate| 21 | RBRC11578,<br>RBRC02473,<br>RBRC02481,<br>RBRC02449,<br>RBRC02488,<br>RBRC02464,<br>RBRC02485,<br>RBRC02484,<br>RBRC10866,<br>RBRC02466,<br> RBRC02479,<br>RBRC02450,<br>RBRC02586,<br>RBRC02460,<br>RBRC02451,<br> RBRC02475,<br>RBRC01088,<br>RBRC02487,<br>RBRC-AES1453,<br>RBRC02300,<br>RBRC02301 | 2 | ENSG00000174775 | HRAS,<br>PTEN | 8 | UBERON:0000014,<br>UBERON:0001511,<br>UBERON:0003532,<br>UBERON:0001416,<br>UBERON:0001419,<br>UBERON:0002097,<br>UBERON:0003531,<br>UBERON:0004263,<br> | zone of skin,<br>skin of leg,<br>hindlimb skin,<br>skin of abdomen,<br>skin of limb,<br>skin of body,<br>forelimb skin,<br>upper arm skin |

### SPARQL query example 6  
[Example6](https://github.com/kushidat/broaderPredicate_uberon/blob/main/Example6.txt)  
Description: A centralized query for Alzheimer's disease using MedGen  
Search parameters:  
  - Federated or Centralized: Centralized
  - Alzheimer's disease (umls:C0002395)
  - GDA: MedGen (https://www.ncbi.nlm.nih.gov/medgen/)
  - Anatomical parts: prefrontal cortex (UBERON:0000451)
  - Confidence Level: high
  - Expression Level: > 99
  - Property paths: Yes
    
The average runtime (3 times): 67 seconds  
Results:  0 cases  

## Licence
[Attribution 4.0 International (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/)  
Copyright (c) 2023 Tatsuya Kushida (RIKEN BioResource Research Center (BRC))


