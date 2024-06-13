#

## Overview
The RIKEN BioResource Research Center (BRC) is exploring the model organisms which are expected to be available for medical science research by executing the SPARQL queries for the RIKEN bioresource Knowledge graph integrated with the Bgee, a gene expression database, the Orthologous MAtrix (OMA, an orthology database), the DisGeNET, a human gene-disease association, Mouse Genome Informatics (MGI), UniProt, and four disease ontologies stored in the RIKEN BioResource MetaDatabase. This page shares the SPARQL query examples and the related data.

## Reference
https://github.com/tarcisiotmf/swat4hcls  
[Querying the Bgee Knowledge Graph with SPARQL](https://www.bgee.org/support/tutorial-query-bgee-knowledge-graph-sparql)  

## SPARQL endpoint
  - RIKEN BioResource SPARQL endpoint: https://knowledge.brc.riken.jp/sparql
    - RDF Store: Virtuoso/07.20.3230 
  - Bgee SPARQL endpoint: https://www.bgee.org/sparql/
    - RDF Store: Virtuoso/07.20.3234 (Linux) x86_64-pc-linux-gnu

____

## SPARQL query examples, the query results, and the related data
### Additional file 1 (SPARQL query Example 1-1)  
[Example1-1_Additional_file_1.rq](https://github.com/kushidat/broaderPredicate_uberon/blob/main/Example1-1_Additional_file_1.rq)  
Description: A federated SPARQL query for Alzheimer's disease using DisGeNET and one subquery    
Search parameters:  
  - Federated (F) or Centralized (C): F
  - Sections: All
  - Disease: Alzheimer's disease (umls:C0002395)
  - GDA: DisGeNET (https://www.disgenet.org/)
  - Anatomical parts: prefrontal cortex (UBERON:0000451)
  - Confidence Level: high
  - [Expression Score](https://www.bgee.org/support/tutorial-gene-page#expression-and-reported-absence-of-expression): 0 - 100
  - Sex: any
  - No. of subqueries: 1
  - Property paths: No
  - Limit on the number of rows returned: 100 and No (all rows)

The average runtime (10 times) and the query results:  
- \> 600 sec / all rows [Execution date: 6 June 2024]
  -  [resultOfExample1-1.csv](https://github.com/kushidat/broaderPredicate_uberon/blob/main/resultOfExample1-1.csv)
  -  [resultOfExample1-1.xlsx](https://github.com/kushidat/broaderPredicate_uberon/blob/main/resultOfExample1-1.xlsx)  
- 112 sec / 100 rows [Execution date: 6 June 2024]  
- 44 sec / all rows, Expression Score: > 99 [Execution date: 10 August 2023]
- 59 sec / all rows, Expression Score: > 99 [Execution date: 4 August 2023] 

Statistics of results:  
| Query approach | No. of RIKEN mice | No. of genes | Gene labels (Ensembl Gene IDs) |
|:---|:---:|:---:|:---|
|Example 1-1: Federated query for AD | 55 | 14 | PICALM (ENSG00000073921)<br>PSEN1 (ENSG00000080815)<br>NPY (ENSG00000122585)<br>APOE (ENSG00000130203)<br>APP (ENSG00000142192)<br>PSEN2 (ENSG00000143801)<br>ACE (ENSG00000159640)<br>INSR (ENSG00000171105)<br>BCL2 (ENSG00000171791)<br>BDNF (ENSG00000176697)<br>MAPT (ENSG00000186868)<br>CD2AP (ENSG00000198087)<br>INS (ENSG00000254647)<br>Novel protein (ENSG00000288674) |  

_____

### Additional file 2 (SPARQL query Example 2-1)  
[Example2-1_Additional_file_2.rq](https://github.com/kushidat/broaderPredicate_uberon/blob/main/Example2-1_Additional_file_2.rq)  
Description: A centralized SPARQL query for Alzheimer's disease using DisGeNET and one subquery     
Search parameters:  
  - Federated (F) or Centralized (C): C
  - Sections: All
  - Disease: Alzheimer's disease (umls:C0002395)
  - GDA: DisGeNET (https://www.disgenet.org/)
  - Anatomical parts: prefrontal cortex (UBERON:0000451)
  - Confidence Level: high
  - [Expression Score](https://www.bgee.org/support/tutorial-gene-page#expression-and-reported-absence-of-expression): 0 - 100
  - Sex: any
  - No. of subqueries: 1
  - Property paths: No
  - Limit on the number of rows returned: 100 and No (all rows)  
    
The average runtime (10 times) and the query results:  
  - 307 sec / all rows [Execution date: 6 June 2024]
    - [resultOfExample2-1.csv](https://github.com/kushidat/broaderPredicate_uberon/blob/main/resultOfExample2-1.csv)
    - [resultOfExample2-1.xlsx](https://github.com/kushidat/broaderPredicate_uberon/blob/main/resultOfExample2-1.xlsx)  
  - 5 sec  / 100 rows [Execution date: 6 June 2024]
  - 40 sec / all rows, Expression Score: > 99 [Execution date: 4 August 2023] 

Statistics of results:  
| Query approach | No. of RIKEN mice | No. of genes | Gene labels (Ensembl Gene IDs) |
|:---|:---:|:---:|:---|
|Example 2-1: Centralized query for AD | 55 | 14 | PICALM (ENSG00000073921)<br>PSEN1 (ENSG00000080815)<br>NPY (ENSG00000122585)<br>APOE (ENSG00000130203)<br>APP (ENSG00000142192)<br>PSEN2 (ENSG00000143801)<br>ACE (ENSG00000159640)<br>INSR (ENSG00000171105)<br>BCL2 (ENSG00000171791)<br>BDNF (ENSG00000176697)<br>MAPT (ENSG00000186868)<br>CD2AP (ENSG00000198087)<br>INS (ENSG00000254647)<br>Novel protein (ENSG00000288674) |  

____

### Additional file 3 (SPARQL query Example 3-1)  
[Example3-1_Additional_file_3.rq](https://github.com/kushidat/broaderPredicate_uberon/blob/main/Example3-1_Additional_file_3.rq)  
Description: A federated SPARQL query for melanoma using DisGeNET and one subquery  
Search parameters:  
  - Federated (F) or Centralized (C): F
  - Sections: All
  - Disease: melanoma (umls:C0025202) 
  - GDA: DisGeNET (https://www.disgenet.org/)
  - Anatomical parts: skin of body (UBERON:0002097)
  - Confidence Level: high
  - [Expression Score](https://www.bgee.org/support/tutorial-gene-page#expression-and-reported-absence-of-expression): 0 - 100
  - Sex: any
  - No. of subqueries: 1
  - Property paths: No
  - Limit on the number of rows returned: 100 and No (all rows) 
    
The average runtime (10 times) and the query results:  
- \> 600 sec / all rows [Execution date: 6 June 2024]
  - [resultOfExample3-1.csv](https://github.com/kushidat/broaderPredicate_uberon/blob/main/resultOfExample3-1.csv)
  - [resultOfExample3-1.xlsx](https://github.com/kushidat/broaderPredicate_uberon/blob/main/resultOfExample3-1.xlsx)  
- \> 300 sec / 100 rows [Execution date: 6 June 2024]     
- 21 sec / all rows, Expression Score: > 99 [Execution date: 10 August 2023]
- 38 sec / all rows, Expression Score: > 99  [Execution date: 4 August 2023]

Statistics of results:  
| Query approach | No. of RIKEN mice | No. of genes | Gene labels (Ensembl Gene IDs) |
|:---|:---:|:---:|:---|
|Example 3-1: Federated query for melanoma | 102 | 14 | TYR (ENSG00000077498)<br>PPP6C (ENSG00000119414)<br>PIK3CA (ENSG00000121879)<br>BRCA2 (ENSG00000139618)<br>TP53 (ENSG00000141510)<br>AKT1 (ENSG00000142208)<br>ATM (ENSG00000149311)<br>KIT (ENSG00000157404)<br>TERT (ENSG00000164362)<br>CTNNB1 (ENSG00000168036)<br>PTEN (ENSG00000171862)<br>HRAS (ENSG00000174775)<br>MITF (ENSG00000187098)<br>NRAS (ENSG00000213281) |  


____

### Additional file 4 (SPARQL query Example 4-1)  
[Example4-1_ Additional_file_4.rq](https://github.com/kushidat/broaderPredicate_uberon/blob/main/Example4-1_Additional_file_4.rq)  
Description: A centralized SPARQL query for melanoma using DisGeNET and one subquery   
Search parameters:  
  - Federated (F) or Centralized (C): C
  - Sections: All
  - Disease: melanoma (umls:C0025202) 
  - GDA: DisGeNET (https://www.disgenet.org/)
  - Anatomical parts: skin of body (UBERON:0002097)
  - Confidence Level: high
  - [Expression Score](https://www.bgee.org/support/tutorial-gene-page#expression-and-reported-absence-of-expression): 0 - 100
  - Sex: any
  - No. of subqueries: 1
  - Property paths: No
  - Limit on the number of rows returned: 100 and No (all rows) 
    
The average runtime (10 times) and the query results:  
  - 502 sec / all rows [Execution date: 6 Jun 2024]
    - [resultOfExample4-1.csv](https://github.com/kushidat/broaderPredicate_uberon/blob/main/resultOfExample4-1.csv)
    - [resultOfExample4-1.xlsx](https://github.com/kushidat/broaderPredicate_uberon/blob/main/resultOfExample4-1.xlsx) 
  - 142 sec / 100 rows [Execution date: 6 Jun 2024] 
  - 20 sec / all rows, Expression Score: > 99 [Execution date: 4 August 2023]

Statistics of results:  
| Query approach | No. of RIKEN mice | No. of genes | Gene labels (Ensembl Gene IDs) |
|:---|:---:|:---:|:---|
|Example 4-1: Centralized query for melanoma | 102 | 14 | TYR (ENSG00000077498)<br>PPP6C (ENSG00000119414)<br>PIK3CA (ENSG00000121879)<br>BRCA2 (ENSG00000139618)<br>TP53 (ENSG00000141510)<br>AKT1 (ENSG00000142208)<br>ATM (ENSG00000149311)<br>KIT (ENSG00000157404)<br>TERT (ENSG00000164362)<br>CTNNB1 (ENSG00000168036)<br>PTEN (ENSG00000171862)<br>HRAS (ENSG00000174775)<br>MITF (ENSG00000187098)<br>NRAS (ENSG00000213281) |   

____

### Additional file 5 (SPARQL query Example 1-2)  
[Example1-2_Additional_file_5.rq](https://github.com/kushidat/broaderPredicate_uberon/blob/main/Example1-2_Additional_file_5.rq)  
Description: A federated SPARQL query for Alzheimer's disease using DisGeNET and two subqueries   
Search parameters:  
  - Federated (F) or Centralized (C): F
  - Sections: All
  - Disease: Alzheimer's disease (umls:C0002395)
  - GDA: DisGeNET (https://www.disgenet.org/)
  - Anatomical parts: prefrontal cortex (UBERON:0000451)
  - Confidence Level: high
  - [Expression Score](https://www.bgee.org/support/tutorial-gene-page#expression-and-reported-absence-of-expression): 0 - 100
  - Sex: any
  - No. of subqueries: 2
  - Property paths: No
  - Limit on the number of rows returned: 100 and No (all rows) 

The average runtime (10 times) and the query results:  
  - \> 600 sec / all rows [Execution date: 6 June 2024]
    - [resultOfExample1-2.csv](https://github.com/kushidat/broaderPredicate_uberon/blob/main/resultOfExample1-2.csv)
    - [resultOfExample1-2.xlsx](https://github.com/kushidat/broaderPredicate_uberon/blob/main/resultOfExample1-2.xlsx)  
  - \> 300 sec / 100 rows [Execution date: 6 June 2024]
  - 48 sec / all rows, Expression Score: > 99 [Execution date: 4 August 2023]  

Statistics of results:  
| Query approach | No. of RIKEN mice | No. of genes | Gene labels (Ensembl Gene IDs) |
|:---|:---:|:---:|:---|
|Example 1-2: Federated query for AD | 55 | 14 | PICALM (ENSG00000073921)<br>PSEN1 (ENSG00000080815)<br>NPY (ENSG00000122585)<br>APOE (ENSG00000130203)<br>APP (ENSG00000142192)<br>PSEN2 (ENSG00000143801)<br>ACE (ENSG00000159640)<br>INSR (ENSG00000171105)<br>BCL2 (ENSG00000171791)<br>BDNF (ENSG00000176697)<br>MAPT (ENSG00000186868)<br>CD2AP (ENSG00000198087)<br>INS (ENSG00000254647)<br>Novel protein (ENSG00000288674) |  

____

### Additional file 6 (SPARQL query Example 2-2)  
[Example2-2_Additional_file_6.rq](https://github.com/kushidat/broaderPredicate_uberon/blob/main/Example2-2_Additional_file_6.rq)  
Description: A centralized SPARQL query for Alzheimer's disease using DisGeNET and two subqueries   
Search parameters:  
  - Federated (F) or Centralized (C): C
  - Sections: All
  - Disease: Alzheimer's disease (umls:C0002395)
  - GDA: DisGeNET (https://www.disgenet.org/)
  - Anatomical parts: prefrontal cortex (UBERON:0000451)
  - Confidence Level: high
  - [Expression Score](https://www.bgee.org/support/tutorial-gene-page#expression-and-reported-absence-of-expression): 0 - 100  
  - Sex: any
  - No. of subqueries: 2
  - Property paths: No
  - Limit on the number of rows returned: 100 and No (all rows) 

The average runtime (10 times) and the query results:  
  - \> 600 sec / all rows [Execution date: 4 June 2024]
    - [resultOfExample2-2.csv](https://github.com/kushidat/broaderPredicate_uberon/blob/main/resultOfExample2-2.csv)
    - [resultOfExample2-2.xlsx](https://github.com/kushidat/broaderPredicate_uberon/blob/main/resultOfExample2-2.xlsx) 
  - 177 sec / 100 rows [Execution date: 4 June 2024]
  - 12 sec / all rows,  Expression Score: > 99 [Execution date: 4 August 2023]

Statistics of results:  
| Query approach | No. of RIKEN mice | No. of genes | Gene labels (Ensembl Gene IDs) |
|:---|:---:|:---:|:---|
|Example 2-2: Centralized query for AD | 55 | 14 | PICALM (ENSG00000073921)<br>PSEN1 (ENSG00000080815)<br>NPY (ENSG00000122585)<br>APOE (ENSG00000130203)<br>APP (ENSG00000142192)<br>PSEN2 (ENSG00000143801)<br>ACE (ENSG00000159640)<br>INSR (ENSG00000171105)<br>BCL2 (ENSG00000171791)<br>BDNF (ENSG00000176697)<br>MAPT (ENSG00000186868)<br>CD2AP (ENSG00000198087)<br>INS (ENSG00000254647)<br>Novel protein (ENSG00000288674) |  

____

### Additional file 7 (SPARQL query Example 3-2)  
[Example3-2_Additional_file_7.rq](https://github.com/kushidat/broaderPredicate_uberon/blob/main/Example3-2_Additional_file_7.rq)  
Description: A federated SPARQL query for melanoma using DisGeNET and two subqueries  
Search parameters:  
  - Federated (F) or Centralized (C): F
  - Sections: All
  - Disease: melanoma (umls:C0025202)
  - GDA: DisGeNET (https://www.disgenet.org/)
  - Anatomical parts: skin of body (UBERON:0002097)
  - Confidence Level: high
  - [Expression Score](https://www.bgee.org/support/tutorial-gene-page#expression-and-reported-absence-of-expression): 0 - 100  
  - Sex: any 
  - No. of subqueries: 2
  - Property paths: No
  - Limit on the number of rows returned: 100 and No (all rows) 

The average runtime (10 times) and the query results:  
  - \> 600 sec / all rows [Execution date: 6 June 2024]
    - [resultOfExample3-2.csv](https://github.com/kushidat/broaderPredicate_uberon/blob/main/resultOfExample3-2.csv)
    - [resultOfExample3-2.xlsx](https://github.com/kushidat/broaderPredicate_uberon/blob/main/resultOfExample3-2.xlsx)  
  - \> 300 sec / 100 rows [Execution date: 6 June 2024]
  - 42 sec / all rows, Expression Score: > 99 [Execution date: 4 August 2023]   

Statistics of results:  
| Query approach | No. of RIKEN mice | No. of genes | Gene labels (Ensembl Gene IDs) |
|:---|:---:|:---:|:---|
|Example 3-2: Federated query for melanoma | 102 | 14 | TYR (ENSG00000077498)<br>PPP6C (ENSG00000119414)<br>PIK3CA (ENSG00000121879)<br>BRCA2 (ENSG00000139618)<br>TP53 (ENSG00000141510)<br>AKT1 (ENSG00000142208)<br>ATM (ENSG00000149311)<br>KIT (ENSG00000157404)<br>TERT (ENSG00000164362)<br>CTNNB1 (ENSG00000168036)<br>PTEN (ENSG00000171862)<br>HRAS (ENSG00000174775)<br>MITF (ENSG00000187098)<br>NRAS (ENSG00000213281) |  

____

### Additional file 8 (SPARQL query Example 4-2)  
[Example4-2_Additional_file_8.rq](https://github.com/kushidat/broaderPredicate_uberon/blob/main/Example4-2_Additional_file_8.rq)  
Description: A centralized SPARQL query for melanoma using DisGeNET and two subqueries  
Search parameters:  
  - Federated (F) or Centralized (C): C
  - Sections: All
  - Disease: melanoma (umls:C0025202)
  - GDA: DisGeNET (https://www.disgenet.org/)
  - Anatomical parts: skin of body (UBERON:0002097)
  - Confidence Level: high
  - [Expression Score](https://www.bgee.org/support/tutorial-gene-page#expression-and-reported-absence-of-expression): 0 - 100  
  - Sex: any  
  - No. of subqueries: 2
  - Property paths: No
  - Limit on the number of rows returned: 100 and No (all rows) 

The average runtime (10 times) and the query results:  
  - \> 600 sec / all rows [Execution date: 6 June 2024]
    - [resultOfExample4-2.csv](https://github.com/kushidat/broaderPredicate_uberon/blob/main/resultOfExample4-2.csv)
    - [resultOfExample4-2.xlsx](https://github.com/kushidat/broaderPredicate_uberon/blob/main/resultOfExample4-2.xlsx)  
  - \> 300 sec / 100 rows [Execution date: 6 June 2024]
  - 42 sec / all rows, Expression Score: > 99 [Execution date: 4 August 2023]

Statistics of results:  
| Query approach | No. of RIKEN mice | No. of genes | Gene labels (Ensembl Gene IDs) |
|:---|:---:|:---:|:---|
|Example 4-2: Centralized query for melanoma | 102 | 14 | TYR (ENSG00000077498)<br>PPP6C (ENSG00000119414)<br>PIK3CA (ENSG00000121879)<br>BRCA2 (ENSG00000139618)<br>TP53 (ENSG00000141510)<br>AKT1 (ENSG00000142208)<br>ATM (ENSG00000149311)<br>KIT (ENSG00000157404)<br>TERT (ENSG00000164362)<br>CTNNB1 (ENSG00000168036)<br>PTEN (ENSG00000171862)<br>HRAS (ENSG00000174775)<br>MITF (ENSG00000187098)<br>NRAS (ENSG00000213281) |   

____

### Additional file 9 (SPARQL query Example 1-3)  
[Example1-3_Additional_file_9.rq](https://github.com/kushidat/broaderPredicate_uberon/blob/main/Example1-3_Additional_file_9.rq)  
Description: A federated SPARQL query for Alzheimer's disease using DisGeNET and three subqueries  
Search parameters:  
  - Federated (F) or Centralized (C): F
  - Sections: All
  - Disease: Alzheimer's disease (umls:C0002395)
  - GDA: DisGeNET (https://www.disgenet.org/)
  - Anatomical parts: prefrontal cortex (UBERON:0000451)
  - Confidence Level: high
  - [Expression Score](https://www.bgee.org/support/tutorial-gene-page#expression-and-reported-absence-of-expression): 0 - 100  
  - Sex: any  
  - No. of subqueries: 3
  - Property paths: No
  - Limit on the number of rows returned: 100 and No (all rows) 

The average runtime (10 times) and the query results:  
  - \> 600 sec / all rows [Execution date: 6 June 2024]
    - [resultOfExample1-3.csv](https://github.com/kushidat/broaderPredicate_uberon/blob/main/resultOfExample1-3.csv)
    - [resultOfExample1-3.xlsx](https://github.com/kushidat/broaderPredicate_uberon/blob/main/resultOfExample1-3.xlsx)   
  - \> 300 sec / 100 rows [Execution date: 6 June 2024]
  - 47 sec / all rows, Expression Score: > 99 [Execution date: 4 August 2023] 

Statistics of results:  
| Query approach | No. of RIKEN mice | No. of genes | Gene labels (Ensembl Gene IDs) |
|:---|:---:|:---:|:---|
|Example 1-3: Federated query for AD | 55 | 14 | PICALM (ENSG00000073921)<br>PSEN1 (ENSG00000080815)<br>NPY (ENSG00000122585)<br>APOE (ENSG00000130203)<br>APP (ENSG00000142192)<br>PSEN2 (ENSG00000143801)<br>ACE (ENSG00000159640)<br>INSR (ENSG00000171105)<br>BCL2 (ENSG00000171791)<br>BDNF (ENSG00000176697)<br>MAPT (ENSG00000186868)<br>CD2AP (ENSG00000198087)<br>INS (ENSG00000254647)<br>Novel protein (ENSG00000288674) |  

____

### Additional file 10 (SPARQL query Example 2-3)  
[Example2-3_Additional_file_10.rq](https://github.com/kushidat/broaderPredicate_uberon/blob/main/Example2-3_Additional_file_10.rq)  
Description: A centralized SPARQL query for Alzheimer's disease using DisGeNET and three subqueries  
Search parameters:  
  - Federated (F) or Centralized (C): C
  - Sections: All
  - Disease: Alzheimer's disease (umls:C0002395)
  - GDA: DisGeNET (https://www.disgenet.org/)
  - Anatomical parts: prefrontal cortex (UBERON:0000451)
  - Confidence Level: high
  - [Expression Score](https://www.bgee.org/support/tutorial-gene-page#expression-and-reported-absence-of-expression): 0 - 100  
  - Sex: any  
  - No. of subqueries: 3
  - Property paths: No
  - Limit on the number of rows returned: 100 and No (all rows) 

The average runtime (10 times) and the query results:  
  - \> 600 sec / all rows [Execution date: 6 June 2024]
    - [resultOfExample2-3.csv](https://github.com/kushidat/broaderPredicate_uberon/blob/main/resultOfExample2-3.csv)
    - [resultOfExample2-3.xlsx](https://github.com/kushidat/broaderPredicate_uberon/blob/main/resultOfExample2-3.xlsx) 
  - 196 sec / 100 rows [Execution date: 6 June 2024]
  - 28 sec / all rows, Expression Score: > 99 [Execution date: 4 August 2023]

Statistics of results:  
| Query approach | No. of RIKEN mice | No. of genes | Gene labels (Ensembl Gene IDs) |
|:---|:---:|:---:|:---|
|Example 2-3: Centralized query for AD | 55 | 14 | PICALM (ENSG00000073921)<br>PSEN1 (ENSG00000080815)<br>NPY (ENSG00000122585)<br>APOE (ENSG00000130203)<br>APP (ENSG00000142192)<br>PSEN2 (ENSG00000143801)<br>ACE (ENSG00000159640)<br>INSR (ENSG00000171105)<br>BCL2 (ENSG00000171791)<br>BDNF (ENSG00000176697)<br>MAPT (ENSG00000186868)<br>CD2AP (ENSG00000198087)<br>INS (ENSG00000254647)<br>Novel protein (ENSG00000288674) |  

____

### Additional file 11 (SPARQL query Example 3-3)  
[Example3-3_Additional_file_11.rq](https://github.com/kushidat/broaderPredicate_uberon/blob/main/Example3-3_Additional_file_11.rq)  
Description: A federated SPARQL query for melanoma using DisGeNET and three subqueries  
Search parameters:  
  - Federated (F) or Centralized (C): F
  - Sections: All
  - Disease: melanoma (umls:C0025202)
  - GDA: DisGeNET (https://www.disgenet.org/)
  - Anatomical parts: skin of body (UBERON:0002097)
  - Confidence Level: high
  - [Expression Score](https://www.bgee.org/support/tutorial-gene-page#expression-and-reported-absence-of-expression): 0 - 100  
  - Sex: any  
  - No. of subqueries: 3
  - Property paths: No
  - Limit on the number of rows returned: 100 and No (all rows) 

The average runtime (10 times) and the query results:  
  - \> 600 sec / all rows [Execution date: 6 June 2024]
    - [resultOfExample3-3.csv](https://github.com/kushidat/broaderPredicate_uberon/blob/main/resultOfExample3-3.csv)
    - [resultOfExample3-3.xlsx](https://github.com/kushidat/broaderPredicate_uberon/blob/main/resultOfExample3-3.xlsx) 
  - \> 300 sec / 100 rows [Execution date: 6 June 2024]
  - 40 sec / all rows, Expression Score: > 99 [Execution date: 4 August 2023]

Statistics of results:  
| Query approach | No. of RIKEN mice | No. of genes | Gene labels (Ensembl Gene IDs) |
|:---|:---:|:---:|:---|
|Example 3-3: Federated query for melanoma | 102 | 14 | TYR (ENSG00000077498)<br>PPP6C (ENSG00000119414)<br>PIK3CA (ENSG00000121879)<br>BRCA2 (ENSG00000139618)<br>TP53 (ENSG00000141510)<br>AKT1 (ENSG00000142208)<br>ATM (ENSG00000149311)<br>KIT (ENSG00000157404)<br>TERT (ENSG00000164362)<br>CTNNB1 (ENSG00000168036)<br>PTEN (ENSG00000171862)<br>HRAS (ENSG00000174775)<br>MITF (ENSG00000187098)<br>NRAS (ENSG00000213281) |  
 

____

### Additional file 12 (SPARQL query Example 4-3)  
[Example4-3_Additional_file_12.rq](https://github.com/kushidat/broaderPredicate_uberon/blob/main/Example4-3_Additional_file_12.rq)  
Description: A centralized SPARQL query for Alzheimer's disease using DisGeNET and three subqueries.    
Search parameters:  
  - Federated (F) or Centralized (C): C
  - Sections: All
  - Disease: melanoma (umls:C0025202)
  - GDA: DisGeNET (https://www.disgenet.org/)
  - Anatomical parts: skin of body (UBERON:0002097)
  - Confidence Level: high
  - [Expression Score](https://www.bgee.org/support/tutorial-gene-page#expression-and-reported-absence-of-expression): 0 - 100  
  - Sex: any  
  - No. of subqueries: 3
  - Property paths: No
  - Limit on the number of rows returned: 100 and No (all rows) 

The average runtime (10 times) and the query results:  
  - \> 600 sec / all rows [Execution date: 6 June 2024]
    - [resultOfExample4-3.csv](https://github.com/kushidat/broaderPredicate_uberon/blob/main/resultOfExample4-3.csv)
    - [resultOfExample4-3.xlsx](https://github.com/kushidat/broaderPredicate_uberon/blob/main/resultOfExample4-3.xlsx) 
  - \> 300 sec / 100 rows [Execution date: 6 June 2024]
  - 40 sec / all rows, Expression Score: > 99 [Execution date: 4 August 2023]

Statistics of results:  
| Query approach | No. of RIKEN mice | No. of genes | Gene labels (Ensembl Gene IDs) |
|:---|:---:|:---:|:---|
|Example 4-3: Centralized query for melanoma | 102 | 14 | TYR (ENSG00000077498)<br>PPP6C (ENSG00000119414)<br>PIK3CA (ENSG00000121879)<br>BRCA2 (ENSG00000139618)<br>TP53 (ENSG00000141510)<br>AKT1 (ENSG00000142208)<br>ATM (ENSG00000149311)<br>KIT (ENSG00000157404)<br>TERT (ENSG00000164362)<br>CTNNB1 (ENSG00000168036)<br>PTEN (ENSG00000171862)<br>HRAS (ENSG00000174775)<br>MITF (ENSG00000187098)<br>NRAS (ENSG00000213281) |   

____

### Additional file 13 (SPARQL query Example 5-0)  
[Example5-0_Additional_file_13.rq](https://github.com/kushidat/broaderPredicate_uberon/blob/main/Example5-0_Additional_file_13.rq)  
Description: A centralized SPARQL query of Sections 1 through 3 for Alzheimer's disease using DisGeNET and without the subquery.  
Search parameters:  
  - Federated (F) or Centralized (C): C
  - Sections: 1, 2, and 3
  - Disease: Alzheimer's disease (umls:C0002395)
  - GDA: DisGeNET (https://www.disgenet.org/)
  - Anatomical parts: Not specified
  - Confidence Level: Not specified
  - Expression Level: Not specified
  - No. of subqueries: 0
  - Property paths: No
  - Limit on the number of rows returned: 100 and No (all rows)
    
The average runtime (10 times) and the query results:  
  - 285 sec / all rows [Execution date: 6 June 2024]
    - [resultOfExample5-0.csv](https://github.com/kushidat/broaderPredicate_uberon/blob/main/resultOfExample5-0.csv)
    - [resultOfExample5-0.xlsx](https://github.com/kushidat/broaderPredicate_uberon/blob/main/resultOfExample5-0.xlsx)  
  - 283 sec / 100 rows [Execution date: 6 June 2024]
  - 51 sec / all rows [Execution date: 4 August 2023]

Statistics of results:  
| Query approach | No. of RIKEN mice | No. of genes | Gene labels (Ensembl Gene IDs) |
|:---|:---:|:---:|:---|
|Example 5-0: Centralized query for AD | 56 | 15 | PICALM (ENSG00000073921)<br>PSEN1 (ENSG00000080815)<br>NPY (ENSG00000122585)<br>APOE (ENSG00000130203)<br>APP (ENSG00000142192)<br>PSEN2 (ENSG00000143801)<br>ACE (ENSG00000159640)<br>INSR (ENSG00000171105)<br>BCL2 (ENSG00000171791)<br>LEP (ENSG00000174697)<br>BDNF (ENSG00000176697)<br>MAPT (ENSG00000186868)<br>CD2AP (ENSG00000198087)<br>INS (ENSG00000254647)<br>Novel protein (ENSG00000288674) |   

____

### Additional file 14 (SPARQL query Example 5-1) 
[Example5-1_Additional_file_14.rq](https://github.com/kushidat/broaderPredicate_uberon/blob/main/Example5-1_Additional_file_14.rq)  
Description: A centralized SPARQL query of Sections 1 through 3 for Alzheimer's disease using DisGeNET and one subquery.  
Search parameters:  
  - Federated (F) or Centralized (C): C
  - Sections: 1, 2, and 3
  - Disease: Alzheimer's disease (umls:C0002395)
  - GDA: DisGeNET (https://www.disgenet.org/)
  - Anatomical parts: Not specified
  - Confidence Level: Not specified
  - Expression Level: Not specified
  - No. of subqueries: 1
  - Property paths: No
  - Limit on the number of rows returned: 100 and No (all rows)
 
The average runtime (10 times) and the query results:  
  - 4 sec / all rows [Execution date: 6 June 2024]
    - [resultOfExample5-1.csv](https://github.com/kushidat/broaderPredicate_uberon/blob/main/resultOfExample5-1.csv)
    - [resultOfExample5-1.xlsx](https://github.com/kushidat/broaderPredicate_uberon/blob/main/resultOfExample5-1.xlsx)  
  - 4 sec / 100 rows [Execution date: 6 June 2024]
  - 2 sec / all rows [Execution date: 4 August 2023]

Statistics of results:  
| Query approach | No. of RIKEN mice | No. of genes | Gene labels (Ensembl Gene IDs) |
|:---|:---:|:---:|:---|
|Example 5-1: Centralized query for AD | 56 | 15 | PICALM (ENSG00000073921)<br>PSEN1 (ENSG00000080815)<br>NPY (ENSG00000122585)<br>APOE (ENSG00000130203)<br>APP (ENSG00000142192)<br>PSEN2 (ENSG00000143801)<br>ACE (ENSG00000159640)<br>INSR (ENSG00000171105)<br>BCL2 (ENSG00000171791)<br>LEP (ENSG00000174697)<br>BDNF (ENSG00000176697)<br>MAPT (ENSG00000186868)<br>CD2AP (ENSG00000198087)<br>INS (ENSG00000254647)<br>Novel protein (ENSG00000288674) |   

____

### Additional file 15 (SPARQL query Example 5-2)  
[Example5-2_Additional_file_15.rq](https://github.com/kushidat/broaderPredicate_uberon/blob/main/Example5-2_Additional_file_15.rq)  
Description: A centralized SPARQL query of Sections 1 through 3 for Alzheimer's disease using DisGeNET and two subqueries.  
Search parameters:  
  - Federated (F) or Centralized (C): C
  - Sections: 1, 2, and 3
  - Disease: Alzheimer's disease (umls:C0002395)
  - GDA: DisGeNET (https://www.disgenet.org/)
  - Anatomical parts: Not specified
  - Confidence Level: Not specified
  - Expression Level: Not specified
  - No. of subqueries: 2
  - Property paths: No
  - Limit on the number of rows returned: 100 and No (all rows)
        
The average runtime (10 times) and the query results:  
  - 4 sec / all rows [Execution date: 6 June 2024]
    - [resultOfExample5-2.csv](https://github.com/kushidat/broaderPredicate_uberon/blob/main/resultOfExample5-2.csv)
    - [resultOfExample5-2.xlsx](https://github.com/kushidat/broaderPredicate_uberon/blob/main/resultOfExample5-2.xlsx) 
  - 4 sec / 100 rows [Execution date: 6 June 2024]
  - 2 sec / all rows [Execution date: 4 August 2023]

Statistics of results:  
| Query approach | No. of RIKEN mice | No. of genes | Gene labels (Ensembl Gene IDs) |
|:---|:---:|:---:|:---|
|Example 5-2: Centralized query for AD | 56 | 15 | PICALM (ENSG00000073921)<br>PSEN1 (ENSG00000080815)<br>NPY (ENSG00000122585)<br>APOE (ENSG00000130203)<br>APP (ENSG00000142192)<br>PSEN2 (ENSG00000143801)<br>ACE (ENSG00000159640)<br>INSR (ENSG00000171105)<br>BCL2 (ENSG00000171791)<br>LEP (ENSG00000174697)<br>BDNF (ENSG00000176697)<br>MAPT (ENSG00000186868)<br>CD2AP (ENSG00000198087)<br>INS (ENSG00000254647)<br>Novel protein (ENSG00000288674) |    

____

### Additional file 16 (SPARQL query Example 6-0)  
[Example6-0_Additional_file_16.rq](https://github.com/kushidat/broaderPredicate_uberon/blob/main/Example6-0_Additional_file_16.rq)  
Description: A centralized SPARQL query of Sections 1 through 3 for melanoma using DisGeNET and without the subquery.  
Search parameters:  
  - Federated (F) or Centralized (C): C
  - Sections: 1, 2, and 3
  - Disease: melanoma (umls:C0025202)
  - GDA: DisGeNET (https://www.disgenet.org/)
  - Anatomical parts: Not specified
  - Confidence Level: Not specified
  - Expression Level: Not specified
  - No. of subqueries: 0
  - Property paths: No
  - Limit on the number of rows returned: 100 and No (all rows)
    
The average runtime (10 times) and the query results:  
  - 465 sec / all rows [Execution date: 6 June 2024]
    - [resultOfExample6-0.csv](https://github.com/kushidat/broaderPredicate_uberon/blob/main/resultOfExample6-0.csv)
    - [resultOfExample6-0.xlsx](https://github.com/kushidat/broaderPredicate_uberon/blob/main/resultOfExample6-0.xlsx)  
  - 439 sec / 100 rows [Execution date: 6 June 2024]
  - 77 sec / all rows [Execution date: 4 August 2023]

Statistics of results:  
| Query approach | No. of RIKEN mice | No. of genes | Gene labels (Ensembl Gene IDs) |
|:---|:---:|:---:|:---|
|Example 6-0: Centralized query for melanoma | 102 | 14 | TYR (ENSG00000077498)<br>PPP6C (ENSG00000119414)<br>PIK3CA (ENSG00000121879)<br>BRCA2 (ENSG00000139618)<br>TP53 (ENSG00000141510)<br>AKT1 (ENSG00000142208)<br>ATM (ENSG00000149311)<br>KIT (ENSG00000157404)<br>TERT (ENSG00000164362)<br>CTNNB1 (ENSG00000168036)<br>PTEN (ENSG00000171862)<br>HRAS (ENSG00000174775)<br>MITF (ENSG00000187098)<br>NRAS (ENSG00000213281) | 

____

### Additional file 17 (SPARQL query Example 6-1)  
[Example6-1_Additional_file_17.rq](https://github.com/kushidat/broaderPredicate_uberon/blob/main/Example6-1_Additional_file_17.rq)  
Description: A centralized SPARQL query of Sections 1 through 3 for melanoma using DisGeNET and one subquery.  
Search parameters:  
  - Federated (F) or Centralized (C): C
  - Sections: 1, 2, and 3
  - Disease: melanoma (umls:C0025202)
  - GDA: DisGeNET (https://www.disgenet.org/)
  - Anatomical parts: Not specified
  - Confidence Level: Not specified
  - Expression Level: Not specified
  - No. of subqueries: 1
  - Property paths: No
  - Limit on the number of rows returned: 100 and No (all rows)

The average runtime (10 times) and the query results:  
  - 7 sec / all rows [Execution date: 6 June 2024]
    - [resultOfExample6-1.csv](https://github.com/kushidat/broaderPredicate_uberon/blob/main/resultOfExample6-1.csv)
    - [resultOfExample6-1.xlsx](https://github.com/kushidat/broaderPredicate_uberon/blob/main/resultOfExample6-1.xlsx)  
  - 7 sec / 100 rows [Execution date: 6 June 2024]
  - 2 sec / all rows [Execution date: 4 August 2023]

Statistics of results:  
| Query approach | No. of RIKEN mice | No. of genes | Gene labels (Ensembl Gene IDs) |
|:---|:---:|:---:|:---|
|Example 6-1: Centralized query for melanoma | 102 | 14 | TYR (ENSG00000077498)<br>PPP6C (ENSG00000119414)<br>PIK3CA (ENSG00000121879)<br>BRCA2 (ENSG00000139618)<br>TP53 (ENSG00000141510)<br>AKT1 (ENSG00000142208)<br>ATM (ENSG00000149311)<br>KIT (ENSG00000157404)<br>TERT (ENSG00000164362)<br>CTNNB1 (ENSG00000168036)<br>PTEN (ENSG00000171862)<br>HRAS (ENSG00000174775)<br>MITF (ENSG00000187098)<br>NRAS (ENSG00000213281) | 

____

### Additional file 18 (SPARQL query Example 6-2)  
[Example6-2_Additional_file_18.rq](https://github.com/kushidat/broaderPredicate_uberon/blob/main/Example6-2_Additional_file_18.rq)  
Description: A centralized SPARQL query of Sections 1 through 3 for melanoma using DisGeNET and two subqueries.  
Search parameters:  
  - Federated (F) or Centralized (C): C
  - Sections: 1, 2, and 3
  - Disease: melanoma (umls:C0025202)
  - GDA: DisGeNET (https://www.disgenet.org/)
  - Anatomical parts: Not specified
  - Confidence Level: Not specified
  - Expression Level: Not specified
  - No. of subqueries: 2
  - Property paths: No
  - Limit on the number of rows returned: 100 and No (all rows)
    
The average runtime (10 times) and the query results:  
  - 7 sec / all rows [Execution date: 6 June 2024]
    - [resultOfExample6-2.csv](https://github.com/kushidat/broaderPredicate_uberon/blob/main/resultOfExample6-2.csv)
    - [resultOfExample6-2.xlsx](https://github.com/kushidat/broaderPredicate_uberon/blob/main/resultOfExample6-2.xlsx)  
  - 7 sec / 100 rows [Execution date: 6 June 2024]
  - 2 sec / all rows [Execution date: 4 August 2023]

Statistics of results:  
| Query approach | No. of RIKEN mice | No. of genes | Gene labels (Ensembl Gene IDs) |
|:---|:---:|:---:|:---|
|Example 6-2: Centralized query for melanoma | 102 | 14 | TYR (ENSG00000077498)<br>PPP6C (ENSG00000119414)<br>PIK3CA (ENSG00000121879)<br>BRCA2 (ENSG00000139618)<br>TP53 (ENSG00000141510)<br>AKT1 (ENSG00000142208)<br>ATM (ENSG00000149311)<br>KIT (ENSG00000157404)<br>TERT (ENSG00000164362)<br>CTNNB1 (ENSG00000168036)<br>PTEN (ENSG00000171862)<br>HRAS (ENSG00000174775)<br>MITF (ENSG00000187098)<br>NRAS (ENSG00000213281) | 

____

### Additional file 19 (SPARQL query Example 7)  
[Example7_Additional_file_19.rq](https://github.com/kushidat/broaderPredicate_uberon/blob/main/Example7_Additional_file_19.rq)  
Description: A federated SPARQL query of Section 4 (Bgee) for the "prefrontal cortex".
Search parameters:  
  - Federated (F) or Centralized (C): F
  - Sections: 4 (Bgee data)
  - Disease: Not used
  - GDA: Not specified
  - Anatomical parts: prefrontal cortex (UBERON:0000451)
  - Confidence Level: high
  - [Expression Score](https://www.bgee.org/support/tutorial-gene-page#expression-and-reported-absence-of-expression): 0 - 100  
  - Sex: any  
  - No. of subqueries: 0
  - Property paths: No
  - Limit on the number of rows returned: 100 and No (all rows) 
    
The average runtime (10 times) and the query results:  
  - 48 sec / all rows (42,448 genes) [Execution date: 6 June 2024]
    - [resultOfExample7_all.csv](https://github.com/kushidat/broaderPredicate_uberon/blob/main/resultOfExample7_all.csv)
    - [resultOfExample7_all.xlsx](https://github.com/kushidat/broaderPredicate_uberon/blob/main/resultOfExample7_all.xlsx)  
  - 3 sec / 100 rows (genes) [Execution date: 6 June 2024]
    - [resultOfExample7_100.csv](https://github.com/kushidat/broaderPredicate_uberon/blob/main/resultOfExample7_100.csv)
    - [resultOfExample7_100.xlsx](https://github.com/kushidat/broaderPredicate_uberon/blob/main/resultOfExample7_100.xlsx)  
  - 10 sec / all rows, Expression Score: > 99 [Execution date: 10 August 2023]
  - 29 sec / all rows, Expression Score: > 99 [Execution date: 4 August 2023]  

Statistics of results:  
| Query approach | No. of genes |
|:---|:---:|
|Example 7: Federated query of Section 4 (Bgee) for the "prefrontal cortex" | 42,448 | 
____

### Additional file 20 (SPARQL query Example 8)  
[Example8_Additional_file_20.rq](https://github.com/kushidat/broaderPredicate_uberon/blob/main/Example8_Additional_file_20.rq)  
Description: A federated SPARQL query of Section 4 (Bgee) for the "skin of body".  
Search parameters:  
  - Federated (F) or Centralized (C): F
  - Sections: 4 (Bgee data)
  - Disease: Not used
  - GDA: Not specified
  - Anatomical parts: skin of body (UBERON:0002097)
  - Confidence Level: high
  - [Expression Score](https://www.bgee.org/support/tutorial-gene-page#expression-and-reported-absence-of-expression): 0 - 100  
  - Sex: any  
  - No. of subqueries: 0
  - Property paths: No
  - Limit on the number of rows returned: 100 and No (all rows) 
    
The average runtime (10 times) and the query results:  
  - 58 sec / all rows [Execution date: 6 June 2024]
    - [resultOfExample8.csv](https://github.com/kushidat/broaderPredicate_uberon/blob/main/resultOfExample8.csv)
    - [resultOfExample8.xlsx](https://github.com/kushidat/broaderPredicate_uberon/blob/main/resultOfExample8.xlsx)  
  - 3 sec / 100 rows [Execution date: 6 June 2024, 100 rows]
  - 29 sec / all rows, Expression Score: > 99  [Execution date: 4 August 2023]

Statistics of results:  
| Query approach | No. of genes |
|:---|:---:|
|Example 8: Federated query of Section 4 (Bgee) for the "skin of body" | 45,724 | 

____

### Additional file 21 (SPARQL query Example 9)  
[Example9_Additional_file_21.rq](https://github.com/kushidat/broaderPredicate_uberon/blob/main/Example9_Additional_file_21.rq)  
Description: A centralized SPARQL query of Section 4 (Bgee) for the "prefrontal cortex".  
Search parameters:  
  - Federated (F) or Centralized (C): C
  - Sections: 4 (Bgee data)
  - Disease: Not used
  - GDA: Not specified
  - Anatomical parts: prefrontal cortex (UBERON:0000451)
  - Confidence Level: high
  - [Expression Score](https://www.bgee.org/support/tutorial-gene-page#expression-and-reported-absence-of-expression): 0 - 100  
  - Sex: any  
  - No. of subqueries: 0
  - Property paths: No
  - Limit on the number of rows returned: 100 and No (all rows) 
    
The average runtime (10 times) and the query results:  
  - 14 sec / all rows (42,448 genes) [Execution date: 6 June 2024]
    - [resultOfExample9_all.csv](https://github.com/kushidat/broaderPredicate_uberon/blob/main/resultOfExample9_all.csv)
    - [resultOfExample9_all.xlsx](https://github.com/kushidat/broaderPredicate_uberon/blob/main/resultOfExample9_all.xlsx)  
  - 4 sec / 100 rows (genes)  [Execution date: 6 June 2024]
    - [resultOfExample9_100.csv](https://github.com/kushidat/broaderPredicate_uberon/blob/main/resultOfExample9_100.csv)
    - [resultOfExample9_100.xlsx](https://github.com/kushidat/broaderPredicate_uberon/blob/main/resultOfExample9_100.xlsx)  
  - 9 sec / all rows, Expression Score: > 99 [Execution date: 4 August 2023] 

Statistics of results:  
| Query approach | No. of genes |
|:---|:---:|
|Example 9: Centralized query of Section 4 (Bgee) for the "prefrontal cortex" | 42,448 |  

____

### Additional file 22 (SPARQL query Example 10)  
[Example10_Additional_file_22.rq](https://github.com/kushidat/broaderPredicate_uberon/blob/main/Example10_Additional_file_22.rq)  
Description: A centralized SPARQL query of Section 4 (Bgee) for the "skin of body".  
Search parameters:  
  - Federated (F) or Centralized (C): C
  - Sections: 4 (Bgee data)
  - Disease: Not used
  - GDA: Not specified
  - Anatomical parts: skin of body (UBERON:0002097)
  - Confidence Level: high
  - [Expression Score](https://www.bgee.org/support/tutorial-gene-page#expression-and-reported-absence-of-expression): 0 - 100  
  - Sex: any  
  - No. of subqueries: 0
  - Property paths: No
  - Limit on the number of rows returned: 100 and No (all rows) 
    
The average runtime (10 times) and the query results:  
  - 16 sec / all rows [Execution date: 6 June 2024]
    - [resultOfExample10.csv](https://github.com/kushidat/broaderPredicate_uberon/blob/main/resultOfExample10.csv)
    - [resultOfExample10.xlsx](https://github.com/kushidat/broaderPredicate_uberon/blob/main/resultOfExample10.xlsx)  
  - 3 sec / 100 rows [Execution date: 6 June 2024]
  - 11 sec / all rows, Expression Score: > 99 [Execution date: 4 August 2023] 

Statistics of results:  
| Query approach | No. of genes |
|:---|:---:|
|Example 10: Centralized query of Section 4 (Bgee) for the "skin of body" | 45,724 | 

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

### Additional file 26 (SPARQL query Example 11-1)  
[Example11-1_Additional_file_26.rq](https://github.com/kushidat/broaderPredicate_uberon/blob/main/Example11-1_Additional_file_26.rq)      
Description: A centralized query for melanoma using DisGeNET and the uberonRDF-KGX (skin of body (UBERON:0002097))  
  
Search parameters:  
  - Federated (F) or Centralized (C): C
  - Sections: All
  - Disease: melanoma (umls:C0025202) 
  - GDA: DisGeNET (https://www.disgenet.org/)
  - Anatomical parts: skin of body (UBERON:0002097)
  - Confidence Level: high
  - [Expression Score](https://www.bgee.org/support/tutorial-gene-page#expression-and-reported-absence-of-expression): 0 - 100  
  - Sex: any 
  - No. of subqueries: 1
  - Property paths: Yes
  - Limit on the number of rows returned: 100 and No (all rows) 
    
The average runtime (10 times) and the query results:  
  - 627 sec / all rows [Execution date: 6 June 2024]
    - [resultOfExample11-1.csv](https://github.com/kushidat/broaderPredicate_uberon/blob/main/resultOfExample11-1.csv)
    - [resultOfExample11-1.xlsx](https://github.com/kushidat/broaderPredicate_uberon/blob/main/resultOfExample11-1.xlsx)  
  - 143 sec / 100 rows [Execution date: 6 June 2024]
  - 499 sec / all rows, Expression Score: > 99 [Execution date: 6 June 2024]
  - 67 sec / all rows, Expression Score: > 99 [Execution date: 4 August 2023]

Statistics of results:  
| Query approach | No. of mice | No. of genes | Gene labels (Ensembl Gene IDs) | No. of anatomical entities | Anatomical entity labels (Uberon IDs) |
|:---|:---:|:---:|:---|:---:|:---|
|Example 11-1: Centralized query for melanoma using the broader predicate| 102 | 14 | TYR (ENSG00000077498)<br>PPP6C (ENSG00000119414)<br>PIK3CA (ENSG00000121879)<br>BRCA2 (ENSG00000139618)<br>TP53 (ENSG00000141510)<br>AKT1 (ENSG00000142208)<br>ATM (ENSG00000149311)<br>KIT (ENSG00000157404)<br>TERT (ENSG00000164362)<br>CTNNB1 (ENSG00000168036)<br>PTEN (ENSG00000171862)<br>HRAS (ENSG00000174775)<br>MITF (ENSG00000187098)<br>NRAS (ENSG00000213281) | 13 | zone of skin (UBERON_0000014)<br>skin epidermis (UBERON_0001003)<br>skin of abdomen (UBERON_0001416)<br>skin of limb (UBERON_0001419)<br>skin of leg (UBERON_0001511)<br>skin of hip (UBERON_0001554)<br>hair follicle (UBERON_0002073)<br>skin of body (UBERON_0002097)<br>forelimb skin (UBERON_0003531)<br>hindlimb skin (UBERON_0003532)<br>upper leg skin (UBERON_0004262)<br>upper arm skin (UBERON_0004263) |  

____


### Additional file 27 (SPARQL query Example 11-2)  
[Example11-2_Additional_file_27.rq](https://github.com/kushidat/broaderPredicate_uberon/blob/main/Example11-2_Additional_file_27.rq)      
Description: A centralized query for melanoma using DisGeNET and the Ubergraph (Endpoint: https://ubergraph.apps.renci.org/sparql), skin of body (UBERON:0002097)     
Search parameters:  
  - Federated (F) or Centralized (C): C
  - Sections: All
  - Disease: melanoma (umls:C0025202) 
  - GDA: DisGeNET (https://www.disgenet.org/)
  - Anatomical parts: skin of body (UBERON:0002097)
  - Confidence Level: high
  - [Expression Score](https://www.bgee.org/support/tutorial-gene-page#expression-and-reported-absence-of-expression): 0 - 100  
  - Sex: any 
  - No. of subqueries: 1
  - Property paths: Yes
  - Limit on the number of rows returned: 100 and No (all rows) 
    
The average runtime (10 times) and the query results:  
  - Transaction timed out (over 3600 sec) [Execution date: 6 June 2024]
    - Results:  ND
  - 3604 sec / 100 rows [Execution date: 6 June 2024]
  - 1875 sec / all rows, Expression Score: > 99 [Execution date: 6 June 2024]
  - Transaction timed out (over 600 sec) [Execution date: 4 August 2023]

____


### SPARQL query Example 12  
[Example12.rq](https://github.com/kushidat/broaderPredicate_uberon/blob/main/Example12.rq)  
Description: A centralized query for Alzheimer's disease 1 using MedGen  
Search parameters:  
  - Federated (F) or Centralized (C): C
  - Sections: All
  - Alzheimer's disease type1 (AD1) (umls:C1863052, medgen:C1863052)
  - GDA: MedGen (https://www.ncbi.nlm.nih.gov/medgen/)
  - Anatomical parts: prefrontal cortex (UBERON:0000451)
  - Confidence Level: high
  - [Expression Score](https://www.bgee.org/support/tutorial-gene-page#expression-and-reported-absence-of-expression): 0 - 100  
  - Sex: any 
  - No. of subqueries: 1
  - Property paths: No
  - Limit on the number of rows returned: 100 and No (all rows) 
    
The average runtime (10 times) and the query results:  
  - 1 sec / all rows [Execution date: 6 June 2024]
    - [resultOfExample12.csv](https://github.com/kushidat/broaderPredicate_uberon/blob/main/resultOfExample12.csv)
    - [resultOfExample12.xlsx](https://github.com/kushidat/broaderPredicate_uberon/blob/main/resultOfExample12.xlsx)  
  - 1 sec / 100 rows [Execution date: 6 June 2024]   
  - 67 sec / all rows, Expression Score: > 99 [Execution date: 4 August 2023]

Statistics of results:  
| Query approach | No. of RIKEN mice | No. of genes | Gene labels (Ensembl Gene IDs) |
|:---|:---:|:---:|:---|
|Example 12: Centralized query for AD1 | 9 | 1 | APP (ENSG00000142192) |  

____

### SPARQL query Example 13  
[Example13.rq](https://github.com/kushidat/broaderPredicate_uberon/blob/main/Example13.rq)  
Description: A centralized query for Alzheimer's disease using MGI  
Search parameters:  
  - Federated (F) or Centralized (C): C
  - Sections: All
  - Alzheimer's disease (umls:C0002395)
  - GDA:MGI (https://www.informatics.jax.org/)  
  - Anatomical parts: prefrontal cortex (UBERON:0000451)
  - Confidence Level: high
  - [Expression Score](https://www.bgee.org/support/tutorial-gene-page#expression-and-reported-absence-of-expression): 0 - 100  
  - Sex: any 
  - No. of subqueries: 1
  - Property paths: No
  - Limit on the number of rows returned: 100 and No (all rows) 
    
The average runtime (10 times) and the query results:  
  - 1 sec / all rows [Execution date: 6 June 2024]
    - [resultOfExample13.csv](https://github.com/kushidat/broaderPredicate_uberon/blob/main/resultOfExample13.csv)
    - [resultOfExample13.xlsx](https://github.com/kushidat/broaderPredicate_uberon/blob/main/resultOfExample13.xlsx)  
  - 1 sec / 100 rows [Execution date: 6 June 2024]
  - 1 sec / all rows, Expression Score: > 99 [Execution date: 4 August 2023]

Statistics of results:  
| Query approach | No. of RIKEN mice | No. of genes | Gene labels (Ensembl Gene IDs) |
|:---|:---:|:---:|:---|
|Example 13: Centralized query for AD | 13 | 4 | PSEN1 (ENSG00000080815)<br>PIN1 (ENSG00000127445)<br>IL33 (ENSG00000137033)<br>APP (ENSG00000142192) |  

____


### SPARQL query Example 14
[Example14.rq](https://github.com/kushidat/broaderPredicate_uberon/blob/main/Example14.rq)      
Description: A centralized query for Alzheimer's disease using DisGeNET and the uberonRDF-KGX (prefrontal cortex (UBERON:0000451))  
  
Search parameters:  
  - Federated (F) or Centralized (C): C
  - Sections: All
  - Disease: Alzheimer's disease (umls:C0002395)
  - GDA: DisGeNET (https://www.disgenet.org/)
  - Anatomical parts: prefrontal cortex (UBERON:0000451)
  - Confidence Level: high
  - [Expression Score](https://www.bgee.org/support/tutorial-gene-page#expression-and-reported-absence-of-expression): 0 - 100  
  - Sex: any 
  - No. of subqueries: 1
  - Property paths: Yes
  - Limit on the number of rows returned: 100 and No (all rows) 
    
The average runtime (10 times) and the query results:  
  - 358 sec / all rows [Execution date: 9 June 2024]
    - [resultOfExample14.csv](https://github.com/kushidat/broaderPredicate_uberon/blob/main/resultOfExample14.csv)
    - [resultOfExample14.xlsx](https://github.com/kushidat/broaderPredicate_uberon/blob/main/resultOfExample14.xlsx)  
  - 357 sec / 100 rows [Execution date: 9 June 2024]
  - 318 sec / all rows, Expression Score: > 99 [Execution date: 9 June 2024] 

Statistics of results:  
| Query approach | No. of mice | No. of genes | Gene labels (Ensembl Gene IDs) | No. of anatomical entities | Anatomical entity labels (Uberon IDs) |
|:---|:---:|:---:|:---|:---:|:---|
|Example 11-1: Centralized query for AD using the broader predicate| 55 | 14 | PICALM (ENSG00000073921)<br>PSEN1 (ENSG00000080815)<br>NPY (ENSG00000122585)<br>APOE (ENSG00000130203)<br>APP (ENSG00000142192)<br>PSEN2 (ENSG00000143801)<br>ACE (ENSG00000159640)<br>INSR (ENSG00000171105)<br>BCL2 (ENSG00000171791)<br>BDNF (ENSG00000176697)<br>MAPT (ENSG00000186868)<br>CD2AP (ENSG00000198087)<br>INS (ENSG00000254647)<br>Novel protein (ENSG00000288674) | 2 | prefrontal cortex (UBERON_0000451)<br>Brodmann (1909) area 10 (UBERON_0013541) |  

____

## Licence

BioResource MetaDatabase by RIKEN BRC is licensed under a [Creative Commons Attribution 4.0 International (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/)  
If you use data from this database, please be sure attribute this database as follows:  
"BioResource Metadatabase (https://knowledge.brc.riken.jp/) © RIKEN BRC licensed under CC Attribution 4.0 International".  

The Bioresource MetaDatabase integrates the BRC's research results using the following external datasets.  
OMA (Orthologs) licensed under [CC Attribution-Share Alike 2.5 (CC BY-SA 2.5)](https://creativecommons.org/licenses/by-sa/2.5/).  
Bgee (Gene expression) licensed under [CC0](https://creativecommons.org/publicdomain/zero/1.0/).  
DisGeNET (Disease-gene interaction) licensed under [Attribution-NonCommercial-ShareAlike 4.0 International](https://creativecommons.org/licenses/by-nc-sa/4.0/).  


