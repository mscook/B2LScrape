#Copyright 2013 Mitchell Jon Stanton-Cook Licensed under the
#Educational Community License, Version 2.0 (the "License"); you may
#not use this file except in compliance with the License. You may
#obtain a copy of the License at
#
##http://www.osedu.org/licenses/ECL-2.0
#
##Unless required by applicable law or agreed to in writing,
#software distributed under the License is distributed on an "AS IS"
#BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express
#or implied. See the License for the specific language governing 
#permissions and limitations under the License. 

"""
Fetch a set of sequences from NCBI 
"""

import textwrap
from Bio import Entrez
from Bio import SeqIO

Entrez.email = "Beatson.Lab@gmail.com"
delchars = ''.join(c for c in map(chr, range(256)) if not c.isalnum())

def fetch(csv_file):
    """
    """
    out = csv_file.replace('.csv', '.fa')
    with open(csv_file) as fin, open(out, 'w') as fout:
        for line in fin:
            id, acc = line.split(',')
            acc =  acc.translate(None, delchars)
            if acc != '':
                print id, len(acc)
                try:
                    handle = Entrez.efetch(db="nucleotide",
                                               id=acc.strip(),                                
                                               rettype="gbwithparts")                              
                except:
                    print "Broken accession %s" % (acc)
                    break
                gene = SeqIO.read(handle, "genbank")                                      
                handle.close()                                      
                count = 0
                print "Working with %s: " % (id)
                for idx, feat in enumerate(gene.features):
                    if feat.type == 'CDS':
                        count = count+1
                        try:
                            ft = feat.qualifiers['gene']
                        except:
                            ft = ' '
                        try:
                            product = feat.qualifiers['product']
                        except:
                            product = ' '
                        try:
                            note = feat.qualifiers['note']
                        except:
                            note = ' '
                        info = '('+str(idx)+')*** '+str(ft[0])+'. '+str(product[0])+'. '+str(note[0])
                        print info
                if count == 0:
                    print "Have a problem with %s: " % (id)
                else:
                    selection = int(raw_input("Index of selection: "))
                    sel_feature = gene.features[selection]
                    # >70-tem8674, bla-TEM, Beta-lactams Antibiotic resistance (ampicillin), Unknown sp. [Beta-lactams]
                    fout.write(">%s, %s, %s, %s [%s]\n" % (acc.strip(), id, info.split('*** ')[1].replace(',', ';').strip(), 'Unknown sp.', csv_file.split('/')[-1].split('.')[0]))
                    dna = str(sel_feature.extract(gene.seq))
                    wrapped = textwrap.wrap(dna.upper(), 80)
                    for e in wrapped:
                        fout.write(e+'\n')
