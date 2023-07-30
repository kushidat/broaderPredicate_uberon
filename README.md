# broaderPredicate_uberon

## Overview

## SPARQL query example
Additional file 1  
Example_1_Additional_file_1.txt
Query Example 1
Example 1: Federated SPARQL query for Alzheimer's disease
SPARQL endpoint: https://knowledge.brc.riken.jp/sparql
Example_1_Additional_file_1.txt
https://github.com/kushidat/broaderPredicate_uberon/blob/main/Example1_Additional_file_1.txt 

Additional file 2
Query Example 2
Example 2: Centralized SPARQL query for Alzheimer's disease 
SPARQL endpoint: https://knowledge.brc.riken.jp/sparql
Example2_Additional_file_2.txt
https://github.com/kushidat/broaderPredicate_uberon/blob/main/Example2_Additional_file_2.txt 
 
Additional file 3
Query Example 3
Example 3: Federated SPARQL query for Melanoma (umls:C0025202)
SPARQL endpoint: https://knowledge.brc.riken.jp/sparql
Example3_Additional_file_3.txt
https://github.com/kushidat/broaderPredicate_uberon/blob/main/Example3_Additional_file_3.txt

Additional file 4
Query Example 4
Example 4: Centralized SPARQL query for Melanoma (umls:C0025202)
SPARQL endpoint: https://knowledge.brc.riken.jp/sparql
Example4_ Additional_file_4.txt
https://github.com/kushidat/broaderPredicate_uberon/blob/main/Example4_Additional_file_4.txt 

Additional file 5
tsv2rdf_uberonKgx_to_uberon_broader20230723.py
This is a python script for converting the latest uberon_kgx_tsv_edge.tsv from the kg-uberon webpage in the KG-OBO project (https://kg-hub.berkeleybop.io/kg-obo/uberon/) to two ttl format files includes subject_broader_object_from_BFO_0000050.ttl (Additional file 6) and subject_broader_object_from_subClassOf.ttl (Additional file 7).
#https://github.com/kushidat/broaderPredicate_uberon/blob/main/tsv2rdf_uberonKgx_to_uberon_broader20230723.py

Additional file 6
subject_broader_object_from_BFO_0000050.ttl
This is a turtle file converted from the latest uberon_kgx_tsv_edge.tsv in the kg-uberon webpage in the KG-OBO project (https://kg-hub.berkeleybop.io/kg-obo/uberon/). This file includes the borader predicate’s relationships among terms created from the BFO:0000050 (pratOf) relations in the uberon_kgx_tsv_edge.tsv in the kg-uberon.
https://github.com/kushidat/broaderPredicate_uberon/blob/main/subject_broader_object_from_BFO_0000050.ttl

Additional file 7
subject_broader_object_from_subClassOf.ttl
This is a turtle file converted from the latest uberon_kgx_tsv_edge.tsv in the kg-uberon webpage in the KG-OBO project (https://kg-hub.berkeleybop.io/kg-obo/uberon/). This file includes the borader predicate’s relationships among terms created from the rdfs:subClassOf relations in the uberon_kgx_tsv_edge.tsv in the kg-uberon.
https://github.com/kushidat/broaderPredicate_uberon/blob/main/subject_broader_object_from_subClassOf.ttl 

Additional file 8
Query Example 5
Example 5: Centralized query for Melanoma (umls:C0025202) using broader predicate
SPARQL endpoint: https://knowledge.brc.riken.jp/sparql
Example5_Additional_file_8.txt
https://github.com/kushidat/broaderPredicate_uberon/blob/main/Example5_Additional_file_8.txt 
![image](https://github.com/kushidat/broaderPredicate_uberon/assets/1106622/9eeab200-2b95-4ce0-890e-aa29af439087)


reeference:
https://github.com/tarcisiotmf/swat4hcls
