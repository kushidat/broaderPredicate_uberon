#

## Overview
The RIKEN BioResource Research Center (BRC) is exploring the model organisms which are expected to be available for medical science research by executing the SPARQL queries for the RIKEN bioresource Knowledge graph integrated with the Bgee, a gene expression database, the Orthologous MAtrix (OMA, an orthology database), the DisGeNET, a human gene-disease association, Mouse Genome Informatics (MGI), UniProt, and four disease ontologies stored in the RIKEN BioResource MetaDatabase. This page shares the SPARQL query examples and the related data.

## RIKEN BioResource SPARQL endpoint
https://knowledge.brc.riken.jp/sparql  


## SPARQL query example
### Additional file 1
[Example_1_Additional_file_1.txt](https://github.com/kushidat/broaderPredicate_uberon/blob/main/Example1_Additional_file_1.txt)  
Explain: A federated SPARQL query for Alzheimer's disease (umls:C0002395) 

### Additional file 2 
[Example2_Additional_file_2.txt](https://github.com/kushidat/broaderPredicate_uberon/blob/main/Example2_Additional_file_2.txt)  
Explain: A centralized SPARQL query for Alzheimer's disease (umls:C0002395) 

### Additional file 3
[Example3_Additional_file_3.txt](https://github.com/kushidat/broaderPredicate_uberon/blob/main/Example3_Additional_file_3.txt)  
Explain: A federated SPARQL query for Melanoma (umls:C0025202)  

### Additional file 4
[Example4_ Additional_file_4.txt](https://github.com/kushidat/broaderPredicate_uberon/blob/main/Example4_Additional_file_4.txt )  
Explain: A centralized SPARQL query for Melanoma (umls:C0025202)   

### Additional file 5
#### [tsv2rdf_uberonKgx_to_uberon_broader20230723.py](https://github.com/kushidat/broaderPredicate_uberon/blob/main/tsv2rdf_uberonKgx_to_uberon_broader20230723.py)  
Explain: This is a Python script for converting the latest uberon_kgx_tsv_edge.tsv from the [kg-uberon webpage](https://kg-hub.berkeleybop.io/kg-obo/uberon/) in the [KG-OBO project](https://github.com/Knowledge-Graph-Hub/kg-obo) of the [KG-Hub](https://kghub.org/) to two ttl format files includes [subject_broader_object_from_BFO_0000050.ttl](https://github.com/kushidat/broaderPredicate_uberon/blob/main/subject_broader_object_from_BFO_0000050.ttl)  (Additional file 6) and [subject_broader_object_from_subClassOf.ttl](https://github.com/kushidat/broaderPredicate_uberon/blob/main/subject_broader_object_from_subClassOf.ttl) (Additional file 7).  

### Additional file 6
[subject_broader_object_from_BFO_0000050.ttl](https://github.com/kushidat/broaderPredicate_uberon/blob/main/subject_broader_object_from_BFO_0000050.ttl)  
Explain: This is a turtle file converted from the latest uberon_kgx_tsv_edge.tsv in the [kg-uberon webpage](https://kg-hub.berkeleybop.io/kg-obo/uberon/) in the [KG-OBO project](https://github.com/Knowledge-Graph-Hub/kg-obo) of the [KG-Hub](https://kghub.org/). This file includes the borader predicate’s relationships among terms created from the BFO:0000050 (pratOf) relations in the uberon_kgx_tsv_edge.tsv in the [kg-uberon](https://kg-hub.berkeleybop.io/kg-obo/uberon/).  

### Additional file 7
[subject_broader_object_from_subClassOf.ttl](https://github.com/kushidat/broaderPredicate_uberon/blob/main/subject_broader_object_from_subClassOf.ttl)  
Explain: This is a turtle file converted from the latest uberon_kgx_tsv_edge.tsv in the [kg-uberon webpage](https://kg-hub.berkeleybop.io/kg-obo/uberon/) in the [KG-OBO project](https://github.com/Knowledge-Graph-Hub/kg-obo) of the [KG-Hub](https://kghub.org/). This file includes the borader predicate’s relationships among terms created from the rdfs:subClassOf relations in the uberon_kgx_tsv_edge.tsv in the [kg-uberon](https://kg-hub.berkeleybop.io/kg-obo/uberon/).  

### Additional file 8
[Example5_Additional_file_8.txt](https://github.com/kushidat/broaderPredicate_uberon/blob/main/Example5_Additional_file_8.txt)  
Explain: A centralized query for Melanoma (umls:C0025202) using broader predicate    

## Licence
[Attribution 4.0 International (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/)

## Reference
https://github.com/tarcisiotmf/swat4hcls
