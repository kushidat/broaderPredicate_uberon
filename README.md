#

## Overview
The RIKEN BioResource Research Center (BRC) is exploring the model organisms which are expected to be available for medical science research by executing the SPARQL queries for the RIKEN bioresource Knowledge graph integrated with the Bgee, a gene expression database, the Orthologous MAtrix (OMA, an orthology database), the DisGeNET, a human gene-disease association, Mouse Genome Informatics (MGI), UniProt, and four disease ontologies stored in the RIKEN BioResource MetaDatabase. This page shares the SPARQL query examples and the related data.

## Reference
https://github.com/tarcisiotmf/swat4hcls

## SPARQL endpoint
  - RIKEN BioResource SPARQL endpoint: https://knowledge.brc.riken.jp/sparql  
  - Bgee SPARQL endpoint: https://www.bgee.org/sparql/

____

## SPARQL query examples and the related data
### Additional file 1 (SPARQL query example 1-1)  
[Example_1-1_Additional_file_1.txt](https://github.com/kushidat/broaderPredicate_uberon/blob/main/Example1-1_Additional_file_1.txt)  
Description: A federated SPARQL query for Alzheimer's disease using DisGeNET and one subquery    
Search parameters:  
  - Federated (F) or Centralized (C): F
  - Sections: All
  - Disease: Alzheimer's disease (umls:C0002395)
  - GDA: DisGeNET (https://www.disgenet.org/)
  - Anatomical parts: prefrontal cortex (UBERON:0000451)
  - Confidence Level: high
  - Expression Level: > 99
  - No. of subqueries: 1
  - Property paths: No

The average runtime (10 times):  
- 59 seconds [Execution date: 4 August 2023]  
- 44 seconds [Execution date: 10 August 2023]  
  
Results:  
| Query approach | No. of mice | RIKEN Mouse IDs | No. of genes![image] | Ensembl Gene IDs | Gene labels |
|:---|:---:|:---|:---:|:---|:---:|
|Example 1-1: Federated query for AD | 21 | RBRC06342,RBRC06343,<br>RBRC06344,RBRC10041,<br>RBRC10042,RBRC10700,<br>RBRC10701,RBRC10043,<br>RBRC11518,RBRC03298,<br>RBRC03388,RBRC03389,<br>RBRC03390,RBRC03391,<br>RBRC03418,RBRC03419,<br>RBRC03420,RBRC03421,<br>RBRC03422,RBRC03423,<br>RBRC00052 | 2 | ENSG00000130203,<br>ENSG00000142192 | APOE,<br>APP |  

_____

### Additional file 2 (SPARQL query example 2-1)  
[Example2-1_Additional_file_2.txt](https://github.com/kushidat/broaderPredicate_uberon/blob/main/Example2-1_Additional_file_2.txt)  
Description: A centralized SPARQL query for Alzheimer's disease using DisGeNET and one subquery     
Search parameters:  
  - Federated (F) or Centralized (C): C
  - Sections: All
  - Disease: Alzheimer's disease (umls:C0002395)
  - GDA: DisGeNET (https://www.disgenet.org/)
  - Anatomical parts: prefrontal cortex (UBERON:0000451)
  - Confidence Level: high
  - Expression Level: > 99
  - No. of subqueries: 1
  - Property paths: No
    
The average runtime (10 times): 
  - 40 seconds [Execution date: 4 August 2023]
    
Results:  
| Query approach | No. of mice | RIKEN Mouse IDs | No. of genes | Ensembl Gene IDs | Gene labels |
|:---|:---:|:---|:---:|:---|:---:|
|Example 2-1: Centralized query for AD | 21 | RBRC06342,RBRC06343,<br>RBRC06344,RBRC10041,<br>RBRC10042,RBRC10700,<br>RBRC10701,RBRC10043,<br>RBRC11518,RBRC03298,<br>RBRC03388,RBRC03389,<br>RBRC03390,RBRC03391,<br>RBRC03418,RBRC03419,<br>RBRC03420,RBRC03421,<br>RBRC03422,RBRC03423,<br>RBRC00052 | 2 | ENSG00000130203,<br>ENSG00000142192 | APOE,<br>APP |  

____

### Additional file 3 (SPARQL query example 3-1)  
[Example3-1_Additional_file_3.txt](https://github.com/kushidat/broaderPredicate_uberon/blob/main/Example3-1_Additional_file_3.txt)  
Description: A federated SPARQL query for melanoma using DisGeNET and one subquery  
Search parameters:  
  - Federated (F) or Centralized (C): F
  - Sections: All
  - Disease: melanoma (umls:C0025202) 
  - GDA: DisGeNET (https://www.disgenet.org/)
  - Anatomical parts: skin of body (UBERON:0002097)
  - Confidence Level: high
  - Expression Level: > 99
  - No. of subqueries: 1
  - Property paths: No
    
The average runtime (10 times):  
- 38 seconds [Execution date: 4 August 2023]    
- 21 seconds [Execution date: 10 August 2023]  


Results:  
| Query approach | No. of mice | RIKEN Mouse IDs | No. of genes![image] | Ensembl Gene IDs | Gene labels |
|:---|:---:|:---|:---:|:---|:---:|
|Example 3-1: Federated query for melanoma | 18 | RBRC10866,RBRC01088,<br>RBRC02449,RBRC02450,<br>RBRC02451,RBRC02460,<br>RBRC02464,RBRC02466,<br>RBRC02473,RBRC02475,<br>RBRC02479,RBRC02481,<br>RBRC02484,RBRC02485,<br>RBRC02487,RBRC02488,<br>RBRC02586,RBRC11578 | 1 | ENSG00000174775 | HRAS |  

____

### Additional file 4 (SPARQL query example 4-1)  
[Example4-1_ Additional_file_4.txt](https://github.com/kushidat/broaderPredicate_uberon/blob/main/Example4-1_Additional_file_4.txt )  
Description: A centralized SPARQL query for melanoma using DisGeNET and one subquery   
Search parameters:  
  - Federated (F) or Centralized (C): C
  - Sections: All
  - Disease: melanoma (umls:C0025202) 
  - GDA: DisGeNET (https://www.disgenet.org/)
  - Anatomical parts: skin of body (UBERON:0002097)
  - Confidence Level: high
  - Expression Level: > 99
  - No. of subqueries: 1
  - Property paths: No
    
The average runtime (10 times): 
  - 20 seconds [Execution date: 4 August 2023]
     
Results:  
| Query approach | No. of mice | RIKEN Mouse IDs | No. of genes![image] | Ensembl Gene IDs | Gene labels |
|:---|:---:|:---|:---:|:---|:---:|
|Example 4-1: Centralized query for melanoma | 18 | RBRC10866,RBRC01088,<br>RBRC02449,RBRC02450,<br>RBRC02451,RBRC02460,<br>RBRC02464,RBRC02466,<br>RBRC02473,RBRC02475,<br>RBRC02479,RBRC02481,<br>RBRC02484,RBRC02485,<br>RBRC02487,RBRC02488,<br>RBRC02586,RBRC11578 | 1 | ENSG00000174775 | HRAS |  

____

### Additional file 5 (SPARQL query example 1-2)  
[Example1-2_Additional_file_5.txt](https://github.com/kushidat/broaderPredicate_uberon/blob/main/Example1-2_Additional_file_5.txt)  
Description: A federated SPARQL query for Alzheimer's disease using DisGeNET and two subqueries   
Search parameters:  
  - Federated (F) or Centralized (C): F
  - Sections: All
  - Disease: Alzheimer's disease (umls:C0002395)
  - GDA: DisGeNET (https://www.disgenet.org/)
  - Anatomical parts: prefrontal cortex (UBERON:0000451)
  - Confidence Level: high
  - Expression Level: > 99
  - No. of subqueries: 2
  - Property paths: No

The average runtime (10 times): 
  - 48 seconds [Execution date: 4 August 2023]
    
Results:  

____

### Additional file 6 (SPARQL query example 2-2)  
[Example2-2_Additional_file_6.txt](https://github.com/kushidat/broaderPredicate_uberon/blob/main/Example2-2_Additional_file_6.txt)  
Description: A centralized SPARQL query for Alzheimer's disease using DisGeNET and two subqueries   
Search parameters:  
  - Federated (F) or Centralized (C): C
  - Sections: All
  - Disease: Alzheimer's disease (umls:C0002395)
  - GDA: DisGeNET (https://www.disgenet.org/)
  - Anatomical parts: prefrontal cortex (UBERON:0000451)
  - Confidence Level: high
  - Expression Level: > 99
  - No. of subqueries: 2
  - Property paths: No

The average runtime (10 times): 
  - 12 seconds [Execution date: 4 August 2023]
    
Results:  

____

### Additional file 7 (SPARQL query example 3-2)  
[Example3-2_Additional_file_7.txt](https://github.com/kushidat/broaderPredicate_uberon/blob/main/Example3-2_Additional_file_7.txt)  
Description: A federated SPARQL query for melanoma using DisGeNET and two subqueries  
Search parameters:  
  - Federated (F) or Centralized (C): F
  - Sections: All
  - Disease: melanoma (umls:C0025202)
  - GDA: DisGeNET (https://www.disgenet.org/)
  - Anatomical parts: skin of body (UBERON:0002097)
  - Confidence Level: high
  - Expression Level: > 99
  - No. of subqueries: 2
  - Property paths: No

The average runtime (10 times):  
- 42 seconds [Execution date: 4 August 2023]   
  
Results:  

____

### Additional file 8 (SPARQL query example 4-2)  
[Example4-2_Additional_file_8.txt](https://github.com/kushidat/broaderPredicate_uberon/blob/main/Example4-2_Additional_file_8.txt)  
Description: A centralized SPARQL query for melanoma using DisGeNET and two subqueries  
Search parameters:  
  - Federated (F) or Centralized (C): C
  - Sections: All
  - Disease: melanoma (umls:C0025202)
  - GDA: DisGeNET (https://www.disgenet.org/)
  - Anatomical parts: skin of body (UBERON:0002097)
  - Confidence Level: high
  - Expression Level: > 99
  - No. of subqueries: 2
  - Property paths: No

The average runtime (10 times): 
  - 42 seconds [Execution date: 4 August 2023]
    
Results:  

____

### Additional file 9 (SPARQL query example 1-3)  
[Example1-3_Additional_file_9.txt](https://github.com/kushidat/broaderPredicate_uberon/blob/main/Example1-3_Additional_file_9.txt)  
Description: A federated SPARQL query for Alzheimer's disease using DisGeNET and three subqueries  
Search parameters:  
  - Federated (F) or Centralized (C): F
  - Sections: All
  - Disease: Alzheimer's disease (umls:C0002395)
  - GDA: DisGeNET (https://www.disgenet.org/)
  - Anatomical parts: prefrontal cortex (UBERON:0000451)
  - Confidence Level: high
  - Expression Level: > 99
  - No. of subqueries: 3
  - Property paths: No

The average runtime (10 times): 
  - 47 seconds [Execution date: 4 August 2023]
    
Results:  

____

### Additional file 10 (SPARQL query example 2-3)  
[Example2-3_Additional_file_10.txt](https://github.com/kushidat/broaderPredicate_uberon/blob/main/Example2-3_Additional_file_10.txt)  
Description: A centralized SPARQL query for Alzheimer's disease using DisGeNET and three subqueries  
Search parameters:  
  - Federated (F) or Centralized (C): C
  - Sections: All
  - Disease: Alzheimer's disease (umls:C0002395)
  - GDA: DisGeNET (https://www.disgenet.org/)
  - Anatomical parts: prefrontal cortex (UBERON:0000451)
  - Confidence Level: high
  - Expression Level: > 99
  - No. of subqueries: 3
  - Property paths: No

The average runtime (10 times):   
  - 28 seconds [Execution date: 4 August 2023]
    
Results:  

____

### Additional file 11 (SPARQL query example 3-3)  
[Example3-3_Additional_file_11.txt](https://github.com/kushidat/broaderPredicate_uberon/blob/main/Example3-3_Additional_file_11.txt)  
Description: A federated SPARQL query for melanoma using DisGeNET and three subqueries  
Search parameters:  
  - Federated (F) or Centralized (C): F
  - Sections: All
  - Disease: melanoma (umls:C0025202)
  - GDA: DisGeNET (https://www.disgenet.org/)
  - Anatomical parts: skin of body (UBERON:0002097)
  - Confidence Level: high
  - Expression Level: > 99
  - No. of subqueries: 3
  - Property paths: No

The average runtime (10 times): 
  - 40 seconds [Execution date: 4 August 2023]
    
Results:  

____

### Additional file 12 (SPARQL query example 4-3)  
[Example4-3_Additional_file_12.txt](https://github.com/kushidat/broaderPredicate_uberon/blob/main/Example4-3_Additional_file_12.txt)  
Description: A centralized SPARQL query for Alzheimer's disease using DisGeNET and three subqueries.    
Search parameters:  
  - Federated (F) or Centralized (C): C
  - Sections: All
  - Disease: melanoma (umls:C0025202)
  - GDA: DisGeNET (https://www.disgenet.org/)
  - Anatomical parts: skin of body (UBERON:0002097)
  - Confidence Level: high
  - Expression Level: > 99
  - No. of subqueries: 3
  - Property paths: No

The average runtime (10 times): 
  - 40 seconds [Execution date: 4 August 2023]
    
Results:  

____

### Additional file 13 (SPARQL query example 5-0)  
[Example5-0_ Additional_file_13.txt](https://github.com/kushidat/broaderPredicate_uberon/blob/main/Example5-0_Additional_file_13.txt )  
Description: A centralized SPARQL query of Sections 1 through 3 for Alzheimer's disease using DisGeNET and without the subquery.  
Search parameters:  
  - Federated (F) or Centralized (C): C
  - Sections: 1, 2, and 3
  - Disease: Alzheimer's disease (umls:C0002395)
  - GDA: DisGeNET (https://www.disgenet.org/)
  - Anatomical parts: Not specified
  - Confidence Level: high
  - Expression Level: > 99
  - No. of subqueries: 0
  - Property paths: No
    
The average runtime (10 times): 
  - 51 seconds [Execution date: 4 August 2023]
    
Results:

____

### Additional file 14 (SPARQL query example 5-1) 
[Example5-1_ Additional_file_14.txt](https://github.com/kushidat/broaderPredicate_uberon/blob/main/Example5-1_Additional_file_14.txt )  
Description: A centralized SPARQL query of Sections 1 through 3 for Alzheimer's disease using DisGeNET and one subquery.  
Search parameters:  
  - Federated (F) or Centralized (C): C
  - Sections: 1, 2, and 3
  - Disease: Alzheimer's disease (umls:C0002395)
  - GDA: DisGeNET (https://www.disgenet.org/)
  - Anatomical parts: Not specified
  - Confidence Level: high
  - Expression Level: > 99
  - No. of subqueries: 1
  - Property paths: No
 
The average runtime (10 times): 
  - 2 seconds [Execution date: 4 August 2023]
    
Results:  

____

### Additional file 15 (SPARQL query example 5-2)  
[Example5-2_ Additional_file_15.txt](https://github.com/kushidat/broaderPredicate_uberon/blob/main/Example5-2_Additional_file_15.txt )  
Description: A centralized SPARQL query of Sections 1 through 3 for Alzheimer's disease using DisGeNET and two subqueries.  
Search parameters:  
  - Federated (F) or Centralized (C): C
  - Sections: 1, 2, and 3
  - Disease: Alzheimer's disease (umls:C0002395)
  - GDA: DisGeNET (https://www.disgenet.org/)
  - Anatomical parts: Not specified
  - Confidence Level: high
  - Expression Level: > 99
  - No. of subqueries: 2
  - Property paths: No
        
The average runtime (10 times): 
  - 2 seconds [Execution date: 4 August 2023]
    
Results:  

____

### Additional file 16 (SPARQL query example 6-0)  
[Example6-0_ Additional_file_16.txt](https://github.com/kushidat/broaderPredicate_uberon/blob/main/Example6-0_Additional_file_16.txt )  
Description: A centralized SPARQL query of Sections 1 through 3 for melanoma using DisGeNET and without the subquery.  
Search parameters:  
  - Federated (F) or Centralized (C): C
  - Sections: 1, 2, and 3
  - Disease: melanoma (umls:C0025202)
  - GDA: DisGeNET (https://www.disgenet.org/)
  - Anatomical parts: Not specified
  - Confidence Level: high
  - Expression Level: > 99
  - No. of subqueries: 0
  - Property paths: No
    
The average runtime (10 times): 
  - 77 seconds [Execution date: 4 August 2023]
    
Results:  

____

### Additional file 17 (SPARQL query example 6-1)  
[Example6-1_ Additional_file_17.txt](https://github.com/kushidat/broaderPredicate_uberon/blob/main/Example6-1_Additional_file_17.txt )  
Description: A centralized SPARQL query of Sections 1 through 3 for melanoma using DisGeNET and one subquery.  
Search parameters:  
  - Federated (F) or Centralized (C): C
  - Sections: 1, 2, and 3
  - Disease: melanoma (umls:C0025202)
  - GDA: DisGeNET (https://www.disgenet.org/)
  - Anatomical parts: Not specified
  - Confidence Level: high
  - Expression Level: > 99
  - No. of subqueries: 1
  - Property paths: No

The average runtime (10 times): 
  - 2 seconds [Execution date: 4 August 2023]
    
Results:  

____

### Additional file 18 (SPARQL query example 6-2)  
[Example6-2_ Additional_file_18.txt](https://github.com/kushidat/broaderPredicate_uberon/blob/main/Example6-2_Additional_file_18.txt )  
Description: A centralized SPARQL query of Sections 1 through 3 for melanoma using DisGeNET and two subqueries.  
Search parameters:  
  - Federated (F) or Centralized (C): C
  - Sections: 1, 2, and 3
  - Disease: melanoma (umls:C0025202)
  - GDA: DisGeNET (https://www.disgenet.org/)
  - Anatomical parts: Not specified
  - Confidence Level: high
  - Expression Level: > 99
  - No. of subqueries: 2
  - Property paths: No
    
The average runtime (10 times): 
  - 2 seconds [Execution date: 4 August 2023]
    
Results:  

____

### Additional file 19 (SPARQL query example 7)  
[Example7_ Additional_file_19.txt](https://github.com/kushidat/broaderPredicate_uberon/blob/main/Example7_Additional_file_19.txt )  
Description: A federated SPARQL query of Section 4 (Bgee) for the "prefrontal cortex" using DisGeNET.  
Search parameters:  
  - Federated (F) or Centralized (C): F
  - Sections: 4 (Bgee data)
  - Disease: Not specified
  - GDA: DisGeNET (https://www.disgenet.org/)
  - Anatomical parts: prefrontal cortex (UBERON:0000451)
  - Confidence Level: high
  - Expression Level: > 99
  - No. of subqueries: 0
  - Property paths: No
    
The average runtime (10 times):  
- 29 seconds [Execution date: 4 August 2023]
- 10 seconds [Execution date: 10 August 2023]  
  
Results:  

____

### Additional file 20 (SPARQL query example 8)  
[Example8_ Additional_file_20.txt](https://github.com/kushidat/broaderPredicate_uberon/blob/main/Example8_Additional_file_20.txt )  
Description: A federated SPARQL query of Section 4 (Bgee) for the "skin of body" using DisGeNET.  
Search parameters:  
  - Federated (F) or Centralized (C): F
  - Sections: 4 (Bgee data)
  - Disease: Not specified
  - GDA: DisGeNET (https://www.disgenet.org/)
  - Anatomical parts: skin of body (UBERON:0002097)
  - Confidence Level: high
  - Expression Level: > 99
  - No. of subqueries: 0
  - Property paths: No
    
The average runtime (10 times): 
  - 29 seconds [Execution date: 4 August 2023]
    
Results:  

____

### Additional file 21 (SPARQL query example 9)  
[Example9_ Additional_file_21.txt](https://github.com/kushidat/broaderPredicate_uberon/blob/main/Example9_Additional_file_21.txt )  
Description: A centralized SPARQL query of Section 4 (Bgee) for the "prefrontal cortex" using DisGeNET.  
Search parameters:  
  - Federated (F) or Centralized (C): C
  - Sections: 4 (Bgee data)
  - Disease: Not specified
  - GDA: DisGeNET (https://www.disgenet.org/)
  - Anatomical parts: prefrontal cortex (UBERON:0000451)
  - Confidence Level: high
  - Expression Level: > 99
  - No. of subqueries: 0
  - Property paths: No
    
The average runtime (10 times): 
  - 9 seconds [Execution date: 4 August 2023]
    
Results:  

____

### Additional file 22 (SPARQL query example 10)  
[Example10_ Additional_file_22.txt](https://github.com/kushidat/broaderPredicate_uberon/blob/main/Example10_Additional_file_22.txt )  
Description: A centralized SPARQL query of Section 4 (Bgee) for the "skin of body" using DisGeNET.  
Search parameters:  
  - Federated (F) or Centralized (C): C
  - Sections: 4 (Bgee data)
  - Disease: Not specified
  - GDA: DisGeNET (https://www.disgenet.org/)
  - Anatomical parts: skin of body (UBERON:0002097)
  - Confidence Level: high
  - Expression Level: > 99
  - No. of subqueries: 0
  - Property paths: No
    
The average runtime (10 times): 
  - 11 seconds [Execution date: 4 August 2023]
    
Results:  

____


### Additional file 23 (Python script)
[tsv2rdf_uberonKgx_to_uberon_broader20230723.py](https://github.com/kushidat/broaderPredicate_uberon/blob/main/tsv2rdf_uberonKgx_to_uberon_broader20230723.py)  
Description: This is a Python script for converting the latest **uberon_kgx_tsv_edge.tsv** from the [kg-uberon webpage](https://kg-hub.berkeleybop.io/kg-obo/uberon/) in the [KG-OBO project](https://github.com/Knowledge-Graph-Hub/kg-obo) of the [KG-Hub](https://kghub.org/) to two ttl format files includes [subject_broader_object_from_BFO_0000050.ttl](https://github.com/kushidat/broaderPredicate_uberon/blob/main/subject_broader_object_from_BFO_0000050.ttl)  (Additional file 24) and [subject_broader_object_from_subClassOf.ttl](https://github.com/kushidat/broaderPredicate_uberon/blob/main/subject_broader_object_from_subClassOf.ttl) (Additional file 25).  We loaded both turtle files as the graph <http://metadb.riken.jp/db/uberonRDF_broader_fromKGX> to the [RIKEN Bioresource MetaDabase](https://knowledge.brc.riken.jp/sparql) to enable executing a transitive search for the Uberon terms.

<img width="1411" alt="a_partOf_image_additional_file_5" src="https://github.com/kushidat/broaderPredicate_uberon/assets/1106622/80973097-c5aa-4c4d-b2f4-2be24d7ee046">

____

### Additional file 24 (RDF data)  
[subject_broader_object_from_BFO_0000050.ttl](https://github.com/kushidat/broaderPredicate_uberon/blob/main/subject_broader_object_from_BFO_0000050.ttl)  
Description: This is a turtle file converted from the latest uberon_kgx_tsv_edge.tsv in the [kg-uberon webpage](https://kg-hub.berkeleybop.io/kg-obo/uberon/) in the [KG-OBO project](https://github.com/Knowledge-Graph-Hub/kg-obo) of the [KG-Hub](https://kghub.org/). In this file, the BFO:0000050 (pratOf) relations among the Uberon terms were converted to <http://purl.org/rbrc/resource/broader> relations among them.

Sample:  
![sample_subject_broader_object_from_BFO_0000050_02](https://github.com/kushidat/broaderPredicate_uberon/assets/1106622/bb4c6e13-cdb5-4d9d-9895-7d59a08fde41)

____

### Additional file 25 (RDF data)  
[subject_broader_object_from_subClassOf.ttl](https://github.com/kushidat/broaderPredicate_uberon/blob/main/subject_broader_object_from_subClassOf.ttl)  
Description: This is a turtle file converted from the latest uberon_kgx_tsv_edge.tsv in the [kg-uberon webpage](https://kg-hub.berkeleybop.io/kg-obo/uberon/) in the [KG-OBO project](https://github.com/Knowledge-Graph-Hub/kg-obo) of the [KG-Hub](https://kghub.org/). In this file, the rdfs:subClassOf relations among the Uberon terms were converted to <http://purl.org/rbrc/resource/broader> relations among them.  

Sample:  
![sample_subject_broader_object_from_subClassOf_02](https://github.com/kushidat/broaderPredicate_uberon/assets/1106622/a967b103-4698-4ff7-b92e-897debbe5fde)

____

### Overview of Converting the uberon.owl to the turtle file using the “broader” predicate.  (Image file)  
[image_additional_file_5.tiff](https://github.com/kushidat/broaderPredicate_uberon/blob/main/image_additional_file_5.tiff)  
Title: Overview of Converting the uberon.owl to the turtle file using the “broader” predicate.  
Description: A path between the “skin of limb” ([UBERON_0001419](http://purl.obolibrary.org/obo/UBERON_0001419)) to the “skin of body” ([UBERON_0002097](http://purl.obolibrary.org/obo/UBERON_0002097)) in the uberon.owl (A) and that in the graph <http://purl.org/rbrc/resource/broader> within the RIKEN Bioresource MetaDatabase (B). The diagrams were created using https://www.kanzaki.com/works/2009/pub/graph-draw.  

![image_additional_file_5](https://github.com/kushidat/broaderPredicate_uberon/assets/1106622/190dc9ca-167e-48ba-ad7f-f6bc95b4025d)  

____

### Additional file 26 (SPARQL query example 11-1)  
[Example11-1_Additional_file_26.txt](https://github.com/kushidat/broaderPredicate_uberon/blob/main/Example11-1_Additional_file_26.txt)      
Description: A centralized query for melanoma using DisGeNET and the uberonRDF-KGX
  
Search parameters:  
  - Federated (F) or Centralized (C): C
  - Sections: All
  - Disease: melanoma (umls:C0025202) 
  - GDA: DisGeNET (https://www.disgenet.org/)
  - Anatomical parts: skin of body (UBERON:0002097)
  - Confidence Level: high
  - Expression Level: > 99
  - No. of subqueries: 1
  - Property paths: Yes
    
The average runtime (10 times): 
  - 67 seconds [Execution date: 4 August 2023]
    
Results:  
| Query approach | No. of mice | RIKEN Mouse IDs | No. of genes | Ensembl Gene IDs | Gene labels |  No. of anatomical entities | Uberon IDs | Anatomical entity labels |
|:---|:---:|:---|:---:|:---|:---:|:---:|:---|:---|
|Example 11-1: Centralized query for melanoma using the broader predicate| 21 | RBRC11578,<br>RBRC02473,<br>RBRC02481,<br>RBRC02449,<br>RBRC02488,<br>RBRC02464,<br>RBRC02485,<br>RBRC02484,<br>RBRC10866,<br>RBRC02466,<br> RBRC02479,<br>RBRC02450,<br>RBRC02586,<br>RBRC02460,<br>RBRC02451,<br> RBRC02475,<br>RBRC01088,<br>RBRC02487,<br>RBRC-AES1453,<br>RBRC02300,<br>RBRC02301 | 2 | ENSG00000174775 | HRAS,<br>PTEN | 8 | UBERON:0000014,<br>UBERON:0001511,<br>UBERON:0003532,<br>UBERON:0001416,<br>UBERON:0001419,<br>UBERON:0002097,<br>UBERON:0003531,<br>UBERON:0004263,<br> | zone of skin,<br>skin of leg,<br>hindlimb skin,<br>skin of abdomen,<br>skin of limb,<br>skin of body,<br>forelimb skin,<br>upper arm skin |  

____


### Additional file 27 (SPARQL query example 11-2)  
[Example11-2_Additional_file_27.txt](https://github.com/kushidat/broaderPredicate_uberon/blob/main/Example11-2_Additional_file_27.txt)      
Description: A centralized query for melanoma using DisGeNET and the Ubergraph (Endpoint: https://ubergraph.apps.renci.org/sparql)   
Search parameters:  
  - Federated (F) or Centralized (C): C
  - Sections: All
  - Disease: melanoma (umls:C0025202) 
  - GDA: DisGeNET (https://www.disgenet.org/)
  - Anatomical parts: skin of body (UBERON:0002097)
  - Confidence Level: high
  - Expression Level: > 99
  - No. of subqueries: 1
  - Property paths: Yes
    
The average runtime (10 times): 
  - Transaction timed out (over 10 mins) [Execution date: 4 August 2023]
    
Results:  ND

____


### SPARQL query example 12  
[Example12.txt](https://github.com/kushidat/broaderPredicate_uberon/blob/main/Example12.txt)  
Description: A centralized query for Alzheimer's disease using MedGen  
Search parameters:  
  - Federated (F) or Centralized (C): C
  - Sections: All
  - Alzheimer's disease (umls:C0002395)
  - GDA: MedGen (https://www.ncbi.nlm.nih.gov/medgen/)
  - Anatomical parts: prefrontal cortex (UBERON:0000451)
  - Confidence Level: high
  - Expression Level: > 99
  - No. of subqueries: 1
  - Property paths: No
    
The average runtime (10 times): 
  - 67 seconds [Execution date: 4 August 2023]
    
Results:  0 cases  

____

### SPARQL query example 13  
[Example13.txt](https://github.com/kushidat/broaderPredicate_uberon/blob/main/Example13.txt)  
Description: A centralized query for Alzheimer's disease using MGI  
Search parameters:  
  - Federated (F) or Centralized (C): C
  - Sections: All
  - Alzheimer's disease (umls:C0002395)
  - GDA:MGI (https://www.informatics.jax.org/)  
  - Anatomical parts: prefrontal cortex (UBERON:0000451)
  - Confidence Level: high
  - Expression Level: > 99
  - No. of subqueries: 1
  - Property paths: No
    
The average runtime (10 times): 
  - 1 second [Execution date: 4 August 2023]
    
Results:  
| Query approach | No. of mice | RIKEN Mouse IDs | No. of genes![image] | Ensembl Gene IDs | Gene labels |
|:---|:---:|:---|:---:|:---|:---:|
|Example 13: Federated query for AD | 10 | RBRC10700,RBRC10701,<br>RBRC06344,RBRC10042,<br>RBRC10041,RBRC06342,<br>RBRC11518,RBRC06343,<br>RBRC10043,RBRC10368 | 2 | ENSG00000142192,<br>ENSG00000127445 | APP,<br>PIN1 |  

____

## Licence

BioResource MetaDatabase by RIKEN BRC is licensed under a [Creative Commons Attribution 4.0 International (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/)  
If you use data from this database, please be sure attribute this database as follows:  
"BioResource Metadatabase (https://knowledge.brc.riken.jp/) © RIKEN BRC licensed under CC Attribution 4.0 International".  

The Bioresource MetaDatabase integrates the BRC's research results using the following external datasets.  
OMA (Orthologs) licensed under [CC Attribution-Share Alike 2.5 (CC BY-SA 2.5)](https://creativecommons.org/licenses/by-sa/2.5/).  
Bgee (Gene expression) licensed under [CC0](https://creativecommons.org/publicdomain/zero/1.0/).  
DisGeNET (Disease-gene interaction) licensed under [Attribution-NonCommercial-ShareAlike 4.0 International](https://creativecommons.org/licenses/by-nc-sa/4.0/).  


