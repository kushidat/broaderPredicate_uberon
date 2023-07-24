import re
import urllib.parse
import os
import pandas as pd
import hashlib

def read_file(file_name):
    with open(file_name, 'r') as file:
        return file.read()

def save_file(file_name, text):
    with open(file_name, 'w') as file:
        file.write(text)

lines = read_file('uberon_kgx_tsv_edges.tsv').split('\n')  

# romove blank line
lines = list(filter(lambda line: line != '', lines))

# remove coloum name
lines = [x for x in lines if re.sub('^id.+', r'', x)]

# Extract specified coloum
cal0_id = list(map(lambda line: line.split('\t')[0], lines)) #A
cal1_subject = list(map(lambda line: line.split('\t')[1], lines)) #B
cal2_predicate = list(map(lambda line: line.split('\t')[2], lines)) #C
cal3_object = list(map(lambda line: line.split('\t')[3], lines)) #D
cal4_relation = list(map(lambda line: line.split('\t')[4], lines)) #F
cal5_knowledge_source = list(map(lambda line: line.split('\t')[5], lines)) #G

# Edit cal0_id (e.g., urn:uuid:0cc1e1ad-8e84-4c0c-82eb-c93f67bd7249) #A
cal0_id_urn = [re.sub('(.+)', r'<\1>', x) for x in cal0_id]

# Edit cal1_subject (e.g., UBERON:0011591) #B
cal1_subject_uri = [re.sub('UBERON:(.+)', r'<http://purl.obolibrary.org/obo/UBERON_\1>', x) for x in cal1_subject]
cal1_subject_uri = [re.sub('BFO:(.+)', r'<http://purl.obolibrary.org/obo/BFO_\1>', x) for x in cal1_subject_uri]
cal1_subject_uri = [re.sub('BSPO:(.+)', r'<http://purl.obolibrary.org/obo/BSPO_\1>', x) for x in cal1_subject_uri]
cal1_subject_uri = [re.sub('CARO:(.+)', r'<http://purl.obolibrary.org/obo/CARO_\1>', x) for x in cal1_subject_uri]
cal1_subject_uri = [re.sub('CHEBI:(.+)', r'<http://purl.obolibrary.org/obo/CHEBI_\1>', x) for x in cal1_subject_uri]
cal1_subject_uri = [re.sub('CL:(.+)', r'<http://purl.obolibrary.org/obo/CL_\1>', x) for x in cal1_subject_uri]
cal1_subject_uri = [re.sub('NBO:(.+)', r'<http://purl.obolibrary.org/obo/GO_\1>', x) for x in cal1_subject_uri]
cal1_subject_uri = [re.sub('NCBITaxon:(.+)', r'<http://purl.obolibrary.org/obo/NCBITaxon_\1>', x) for x in cal1_subject_uri]
cal1_subject_uri = [re.sub('GO:(.+)', r'<http://purl.obolibrary.org/obo/GO_\1>', x) for x in cal1_subject_uri]
#cal1_subject_uri = [re.sub('OBO:GOREL_(.+)', r'<http://purl.obolibrary.org/obo/GOREL_\1>', x) for x in cal1_subject_uri]
#cal1_subject_uri = [re.sub('OBO:(uberon/core#/.+)', r'<http://purl.obolibrary.org/obo/\1>', x) for x in cal1_subject_uri]
cal1_subject_uri = [re.sub('OBO:(.+)', r'<http://purl.obolibrary.org/obo/\1>', x) for x in cal1_subject_uri]
cal1_subject_uri = [re.sub('owl:(.+)', r'<http://www.w3.org/2002/07/owl#\1>', x) for x in cal1_subject_uri]
cal1_subject_uri = [re.sub('PATO:(.+)', r'<http://purl.obolibrary.org/obo/PATO_\1>', x) for x in cal1_subject_uri]
cal1_subject_uri = [re.sub('PR:(.+)', r'<http://purl.obolibrary.org/obo/PR_\1>', x) for x in cal1_subject_uri]
cal1_subject_uri = [re.sub('RO:(.+)', r'<http://purl.obolibrary.org/obo/RO_\1>', x) for x in cal1_subject_uri]
cal1_subject_uri = [re.sub('(http://birdgenenames.org/cgnc/GeneReport\?id=.+)', r'<\1>', x) for x in cal1_subject_uri]
cal1_subject_uri = [re.sub('SO:(.+)', r'<http://purl.obolibrary.org/obo/SO_\1>', x) for x in cal1_subject_uri]
cal1_subject_uri = [re.sub('NCBIGene:(.+)', r'<http://identifiers.org/ncbigene/\1>', x) for x in cal1_subject_uri]
cal1_subject_uri = [re.sub('ENVO:(.+)', r'<http://purl.obolibrary.org/obo/ENVO_\1>', x) for x in cal1_subject_uri]

# Edit cal2_predicate (e.g., biolink:subclass_of) #C
cal2_predicate_uri = [re.sub('biolink:(.+)', r'<https://w3id.org/biolink/vocab\1>', x) for x in cal2_predicate]

# Edit cal3_object (e.g., UBERON:0001018) #D
cal3_object_uri = [re.sub('UBERON:(.+)', r'<http://purl.obolibrary.org/obo/UBERON_\1>', x) for x in cal3_object]
cal3_object_uri = [re.sub('BFO:(.+)', r'<http://purl.obolibrary.org/obo/BFO_\1>', x) for x in cal3_object_uri]
cal3_object_uri = [re.sub('BSPO:(.+)', r'<http://purl.obolibrary.org/obo/BSPO_\1>', x) for x in cal3_object_uri]
cal3_object_uri = [re.sub('CARO:(.+)', r'<http://purl.obolibrary.org/obo/CARO_\1>', x) for x in cal3_object_uri]
cal3_object_uri = [re.sub('CHEBI:(.+)', r'<http://purl.obolibrary.org/obo/CHEBI_\1>', x) for x in cal3_object_uri]
cal3_object_uri = [re.sub('CL:(.+)', r'<http://purl.obolibrary.org/obo/CL_\1>', x) for x in cal3_object_uri]
cal3_object_uri = [re.sub('NBO:(.+)', r'<http://purl.obolibrary.org/obo/GO_\1>', x) for x in cal3_object_uri]
cal3_object_uri = [re.sub('NCBITaxon:(.+)', r'<http://purl.obolibrary.org/obo/NCBITaxon_\1>', x) for x in cal3_object_uri]
cal3_object_uri = [re.sub('GO:(.+)', r'<http://purl.obolibrary.org/obo/GO_\1>', x) for x in cal3_object_uri]
#cal3_object_uri = [re.sub('OBO:GOREL_(.+)', r'<http://purl.obolibrary.org/obo/GOREL_\1>', x) for x in cal3_object_uri]
#cal3_object_uri = [re.sub('OBO:(uberon/core#/.+)', r'<http://purl.obolibrary.org/obo/\1>', x) for x in cal3_object_uri]
cal3_object_uri = [re.sub('OBO:(.+)', r'<http://purl.obolibrary.org/obo/\1>', x) for x in cal3_object_uri]
cal3_object_uri = [re.sub('owl:(.+)', r'<http://www.w3.org/2002/07/owl#\1>', x) for x in cal3_object_uri]
cal3_object_uri = [re.sub('PATO:(.+)', r'<http://purl.obolibrary.org/obo/PATO_\1>', x) for x in cal3_object_uri]
cal3_object_uri = [re.sub('PR:(.+)', r'<http://purl.obolibrary.org/obo/PR_\1>', x) for x in cal3_object_uri]
cal3_object_uri = [re.sub('RO:(.+)', r'<http://purl.obolibrary.org/obo/RO_\1>', x) for x in cal3_object_uri]
cal3_object_uri = [re.sub('(http://birdgenenames.org/cgnc/GeneReport\?id=.+)', r'<\1>', x) for x in cal3_object_uri]
cal3_object_uri = [re.sub('SO:(.+)', r'<http://purl.obolibrary.org/obo/SO_\1>', x) for x in cal3_object_uri]
cal3_object_uri = [re.sub('NCBIGene:(.+)', r'<http://identifiers.org/ncbigene/\1>', x) for x in cal3_object_uri]
cal3_object_uri = [re.sub('ENVO:(.+)', r'<http://purl.obolibrary.org/obo/ENVO_\1>', x) for x in cal3_object_uri]

# Edit cal4_relation (e.g., rdfs:subClassOf) #E
cal4_relation_uri = [re.sub('BFO:(.+)', r'<http://purl.obolibrary.org/obo/BFO_\1>', x) for x in cal4_relation]
cal4_relation_uri = [re.sub('BSPO:(.+)', r'<http://purl.obolibrary.org/obo/BSPO_\1>', x) for x in cal4_relation_uri]
cal4_relation_uri = [re.sub('CL:(.+)', r'<http://purl.obolibrary.org/obo/CL_\1>', x) for x in cal4_relation_uri]
cal4_relation_uri = [re.sub('inverseOf', r'<http://www.w3.org/2002/07/owl#inverseOf>', x) for x in cal4_relation_uri]
cal4_relation_uri = [re.sub('CL:(.+)', r'<http://purl.obolibrary.org/obo/CL_\1>', x) for x in cal4_relation_uri]
cal4_relation_uri = [re.sub('rdfs:(.+)', r'<http://www.w3.org/2000/01/rdf-schema#\1>', x) for x in cal4_relation_uri]
cal4_relation_uri = [re.sub('subPropertyOf', r'<http://www.w3.org/2000/01/rdf-schema#subPropertyOf>', x) for x in cal4_relation_uri]
cal4_relation_uri = [re.sub('RO:(.+)', r'<http://purl.obolibrary.org/obo/RO_\1>', x) for x in cal4_relation_uri]
cal4_relation_uri = [re.sub('OBO:(.+)', r'<http://purl.obolibrary.org/obo/\1>', x) for x in cal4_relation_uri]

# Edit cal5_knowledge_source (e.g., UBERON 2023-06-27) #F
cal5_knowledge_source_literal = [re.sub(';', r'"^^<http://www.w3.org/2001/XMLSchema#string>, "', x) for x in cal5_knowledge_source]


### Create triples
# 1/
# <cal1_subject_uri> <cal2_predicate_uri> <cal3_object_uri> . 
# e.g., <CL:0002620> <biolink:related_to> <UBERON:0002097> .
nt_cal1_subject_uri_cal2_predicate_uri_cal3_object_uri = ["{0}	{1}	{2} .".format(line1, line2, line3) for line1, line2, line3 in zip(cal1_subject_uri, cal2_predicate_uri, cal3_object_uri)]
# remove overlap lines
nt_cal1_subject_uri_cal2_predicate_uri_cal3_object_uri = list(set(nt_cal1_subject_uri_cal2_predicate_uri_cal3_object_uri)) 
# sort
nt_cal1_subject_uri_cal2_predicate_uri_cal3_object_uri = sorted(nt_cal1_subject_uri_cal2_predicate_uri_cal3_object_uri) 
save_file('subject_predicateOfBiolink_object.ttl', "\n".join(nt_cal1_subject_uri_cal2_predicate_uri_cal3_object_uri))

# 2/
# <cal1_subject_uri> <cal4_relation> <cal3_object_uri> . 
# e.g., <CL:0002620> <BFO:0000050> <UBERON:0002097> .
nt_cal1_subject_uri_cal4_relation_uri_cal3_object_uri = ["{0}	{1}	{2} .".format(line1, line2, line3) for line1, line2, line3 in zip(cal1_subject_uri, cal4_relation_uri, cal3_object_uri)]
# remove overlap lines
nt_cal1_subject_uri_cal4_relation_uri_cal3_object_uri = list(set(nt_cal1_subject_uri_cal4_relation_uri_cal3_object_uri)) 
# sort
nt_cal1_subject_uri_cal4_relation_uri_cal3_object_uri = sorted(nt_cal1_subject_uri_cal4_relation_uri_cal3_object_uri) 
save_file('subject_relation_object.ttl', "\n".join(nt_cal1_subject_uri_cal4_relation_uri_cal3_object_uri))

# 3/
# <cal1_subject_uri> <cal4_relation> <cal3_object_uri> . from BFO:0000050
# e.g., <CL:0002620> <http://purl.org/rbrc/resource/broader> <UBERON:0002097> .
nt_cal1_subject_broader_cal3_object_uri_from_BFO_0000050 = [re.sub('(^.+)<http://purl.obolibrary.org/obo/BFO_0000050>(.+) .', r'\1 <http://purl.org/rbrc/resource/broader> \2 .', x) for x in nt_cal1_subject_uri_cal4_relation_uri_cal3_object_uri]
nt_cal1_subject_broader_cal3_object_uri_from_BFO_0000050 = [re.sub('^(?!.*<http://purl.org/rbrc/resource/broader>).+$', r'', x) for x in nt_cal1_subject_broader_cal3_object_uri_from_BFO_0000050]
# remove overlap lines
nt_cal1_subject_broader_cal3_object_uri_from_BFO_0000050 = list(set(nt_cal1_subject_broader_cal3_object_uri_from_BFO_0000050)) 
# sort
nt_cal1_subject_broader_cal3_object_uri_from_BFO_0000050 = sorted(nt_cal1_subject_broader_cal3_object_uri_from_BFO_0000050) 
save_file('subject_broader_object_from_BFO_0000050.ttl', "\n".join(nt_cal1_subject_broader_cal3_object_uri_from_BFO_0000050))

# 4/
# <cal1_subject_uri> <cal4_relation> <cal3_object_uri> . from rdfs:subClassOf
# e.g., <CL:0002620> <http://purl.org/rbrc/resource/broader> <UBERON:0002097> .
###nt_cal1_subject_broader_cal3_object_uri_from_subClassOf = [re.sub('^(?!.*subClassOf).*$', r'', x) for x in nt_cal1_subject_uri_cal4_relation_uri_cal3_object_uri]
nt_cal1_subject_broader_cal3_object_uri_from_subClassOf = [re.sub('(^.+)<http://www.w3.org/2000/01/rdf-schema#subClassOf>(.+) .', r'\1 <http://purl.org/rbrc/resource/broader> \2 .', x) for x in nt_cal1_subject_uri_cal4_relation_uri_cal3_object_uri]
nt_cal1_subject_broader_cal3_object_uri_from_subClassOf = [re.sub('^(?!.*<http://purl.org/rbrc/resource/broader>).+$', r'', x) for x in nt_cal1_subject_broader_cal3_object_uri_from_subClassOf]
# remove overlap lines
nt_cal1_subject_broader_cal3_object_uri_from_subClassOf = list(set(nt_cal1_subject_broader_cal3_object_uri_from_subClassOf)) 
# sort
nt_cal1_subject_broader_cal3_object_uri_from_subClassOf = sorted(nt_cal1_subject_broader_cal3_object_uri_from_subClassOf) 
save_file('subject_broader_object_from_subClassOf.ttl', "\n".join(nt_cal1_subject_broader_cal3_object_uri_from_subClassOf))


###
# reference (in Japanese): https://www.suzu6.net/posts/21/
# reference (in Japanese): https://www.suzu6.net/posts/22/
