# Example 7 [3 sec/100 rows, 48 sec/all rows]
# Federated (prefrontal cortex)
PREFIX brso: <http://purl.jp/bio/10/brso/>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX sio: <http://semanticscience.org/resource/>
PREFIX lscr: <http://purl.org/lscr#>
PREFIX obo: <http://purl.obolibrary.org/obo/>
PREFIX taxon: <http://purl.uniprot.org/taxonomy/>
PREFIX foaf: <http://xmlns.com/foaf/0.1/>
PREFIX orth: <http://purl.org/net/orth#>
PREFIX genex: <http://purl.org/genex#>
PREFIX umls: <http://linkedlifedata.com/resource/umls/id/>

SELECT *
WHERE {
  SERVICE <https://bgee.org/sparql/> {
    SELECT DISTINCT ?ensembl2
    WHERE {
#   GRAPH <http://metadb.riken.jp/db/bgee> {
    ?oma_gene2 a orth:Gene .
    ?oma_gene2 lscr:xrefEnsemblGene ?ensembl2 .
    ?oma_gene2 orth:organism/obo:RO_0002162 taxon:9606 . # human
    ?oma_gene2 genex:isExpressedIn ?cond .
    ?cond genex:hasAnatomicalEntity obo:UBERON_0000451 . # prefrontal cortex
#     ?cond genex:hasAnatomicalEntity obo:UBERON_0002097 . # skin of body
    ?cond genex:hasSex "any" .
    ?expr genex:hasExpressionCondition ?cond .
    ?expr genex:hasSequenceUnit ?oma_gene2 .
    ?expr a genex:Expression .
    ?expr genex:hasConfidenceLevel obo:CIO_0000029 . # high confidence level
    ?expr genex:hasExpressionLevel ?exprLevel .
    FILTER (?exprLevel > 99)
  } LIMIT 100 OFFSET 0
 }
}
