# broaderPredicate_uberon

## Overview


## RIKEN BioResource SPARQL endpoint
https://knowledge.brc.riken.jp/sparql  


## SPARQL query example
### Additional file 1
[Example_1_Additional_file_1.txt](https://github.com/kushidat/broaderPredicate_uberon/blob/main/Example1_Additional_file_1.txt)  
Explain: Federated SPARQL query for Alzheimer's disease  

### Additional file 2 
[Example2_Additional_file_2.txt](https://github.com/kushidat/broaderPredicate_uberon/blob/main/Example2_Additional_file_2.txt)  
Explain: Centralized SPARQL query for Alzheimer's disease  

### Additional file 3
[Example3_Additional_file_3.txt](https://github.com/kushidat/broaderPredicate_uberon/blob/main/Example3_Additional_file_3.txt)  
Explain: Federated SPARQL query for Melanoma (umls:C0025202)  

### Additional file 4
[Example4_ Additional_file_4.txt](https://github.com/kushidat/broaderPredicate_uberon/blob/main/Example4_Additional_file_4.txt )  
Explain: Centralized SPARQL query for Melanoma (umls:C0025202)   

### Additional file 5
[tsv2rdf_uberonKgx_to_uberon_broader20230723.py](#https://github.com/kushidat/broaderPredicate_uberon/blob/main/tsv2rdf_uberonKgx_to_uberon_broader20230723.py)  
Explain: This is a python script for converting the latest uberon_kgx_tsv_edge.tsv from the kg-uberon webpage in the KG-OBO project (https://kg-hub.berkeleybop.io/kg-obo/uberon/) to two ttl format files includes subject_broader_object_from_BFO_0000050.ttl (Additional file 6) and subject_broader_object_from_subClassOf.ttl (Additional file 7).  

### Additional file 6
[subject_broader_object_from_BFO_0000050.ttl](https://github.com/kushidat/broaderPredicate_uberon/blob/main/subject_broader_object_from_BFO_0000050.ttl)  
Explain: This is a turtle file converted from the latest uberon_kgx_tsv_edge.tsv in the kg-uberon webpage in the KG-OBO project (https://kg-hub.berkeleybop.io/kg-obo/uberon/). This file includes the borader predicate’s relationships among terms created from the BFO:0000050 (pratOf) relations in the uberon_kgx_tsv_edge.tsv in the kg-uberon.  

### Additional file 7
[subject_broader_object_from_subClassOf.ttl](https://github.com/kushidat/broaderPredicate_uberon/blob/main/subject_broader_object_from_subClassOf.ttl)  
Explain: This is a turtle file converted from the latest uberon_kgx_tsv_edge.tsv in the kg-uberon webpage in the KG-OBO project (https://kg-hub.berkeleybop.io/kg-obo/uberon/). This file includes the borader predicate’s relationships among terms created from the rdfs:subClassOf relations in the uberon_kgx_tsv_edge.tsv in the kg-uberon.  

### Additional file 8
[Example5_Additional_file_8.txt](https://github.com/kushidat/broaderPredicate_uberon/blob/main/Example5_Additional_file_8.txt)  
Explain: Centralized query for Melanoma (umls:C0025202) using broader predicate    


## Reference
https://github.com/tarcisiotmf/swat4hcls
