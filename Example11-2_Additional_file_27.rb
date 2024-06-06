# Example 11-2: Centralized query for Melanoma using the ubergraph [> 5 min/100 rows]
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

SELECT DISTINCT ?mouse ?ensembl2 ?lower_anatomicalEntity
WHERE {
SERVICE <https://ubergraph.apps.renci.org/sparql> {
  {?lower_anatomicalEntity rdfs:subClassOf obo:UBERON_0002097 .}
  UNION
  {?lower_anatomicalEntity <http://purl.obolibrary.org/obo/BFO_0000050> obo:UBERON_0002097.}
	}
  {
    SELECT DISTINCT ?mouse ?ensembl2 ?lower_anatomicalEntity
    WHERE {
   GRAPH <http://metadb.riken.jp/db/bgee> {
    ?oma_gene2 a orth:Gene .
    ?oma_gene2 lscr:xrefEnsemblGene ?ensembl2 .
    ?oma_gene2 orth:organism/obo:RO_0002162 taxon:9606 . # human
    ?oma_gene2 genex:isExpressedIn ?cond .
    ?cond genex:hasAnatomicalEntity ?lower_anatomicalEntity . # skin of body
    ?cond genex:hasSex "any" .   
    ?expr genex:hasExpressionCondition ?cond .
    ?expr genex:hasSequenceUnit ?oma_gene2 .
    ?expr a genex:Expression .
    ?expr genex:hasConfidenceLevel obo:CIO_0000029 . # high confidence level
    ?expr genex:hasExpressionLevel ?exprLevel .
    FILTER (?exprLevel > 99)
  }
  {
    SELECT DISTINCT ?mouse ?ensembl2
    WHERE {
      GRAPH <http://metadb.riken.jp/db/xsearch_animal_brso> {
        ?mouse brso:genomic_feature/brso:has_genomic_segment/rdfs:seeAlso ?mgi1 .
        ?mouse foaf:homepage ?homepage_mouse .
      }
      GRAPH <http://metadb.riken.jp/db/mgi_ncbi_ensembl> {
        ?mgi1 rdfs:seeAlso ?ensembl1 .
      }
      GRAPH <http://metadb.riken.jp/db/omaRDF> {
        ?cluster a orth:OrthologsCluster .
        ?cluster orth:hasHomologousMember ?node1 .
        ?cluster orth:hasHomologousMember ?node2 .
        FILTER (?node1 != ?node2)
        ?node1 orth:hasHomologousMember* ?protein1 .
        ?node2 orth:hasHomologousMember* ?protein2 .
        ?protein1 sio:SIO_010079 ?oma_gene1 . # sio:SIO_010079 (is encoded by)
        ?oma_gene1 lscr:xrefEnsemblGene ?ensembl1 .
        ?oma_gene1 lscr:xrefNCBIGene ?ncbi1 .
        ?protein2 lscr:xrefUniprot ?uniprot2.
        ?protein2 sio:SIO_010079 ?oma_gene2 .
        ?protein2 orth:organism ?oma_organism2 .
        ?oma_organism2 obo:RO_0002162 taxon:9606 .
        ?oma_gene2 lscr:xrefNCBIGene ?ncbi2 .
        ?oma_gene2 lscr:xrefEnsemblGene ?ensembl2 .
      }
      GRAPH <http://metadb.riken.jp/db/uniprot_ncbigene> {
        ?uniprot2 rdfs:seeAlso ?ncbi2 .
        ?uniprot2 rdfs:seeAlso ?identifiers_ncbi2 .
        FILTER (?ncbi2 != ?identifiers_ncbi2)
      }
      GRAPH <http://metadb.riken.jp/db/gda_score_05> {
        ?gda sio:SIO_000628 ?identifiers_ncbi2 .
        ?gda sio:SIO_000628 ?umls .
        VALUES (?umls) { (umls:C0025202) } # Melanoma
        FILTER (?identifiers_ncbi2 != ?umls)
      }
     }
    }
   }
  }
}
LIMIT 100 OFFSET 0

