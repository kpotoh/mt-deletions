# mt-deletions


## Workflow

### 1 Download human mt genomes from [NCBI](https://www.ncbi.nlm.nih.gov/nuccore/?term=ddbj_embl_genbank%5Bfilter%5D+AND+txid9606%5Borgn%3Anoexp%5D+AND+complete-genome%5Btitle%5D+AND+mitochondrion%5Bfilter%5D) with query to Nucleotide database:
```
ddbj_embl_genbank[filter] AND txid9606[orgn:noexp] AND complete-genome[title] AND mitochondrion[filter] 
```

### 2 Clean up sequences from non human mt genomes
```
python scripts/0.cleanup_sequences.sh SEQS OUT_SEQS
```

### 3 Align to reference and form the multiple alignment
```
bash scripts/1.bwa.sh pathToBwa pathToSamtools fastaReference multiFastaSequesteredAndRandomized coreNumber
perl scripts/2.longest-alignments.pl samFile > purifiedSamFile
python scripts/3.sam2fasta.py fastaReference purifiedSamFile fastaMultipleAlignment
```

### 4 Analize alignment to search ubiquitous restriction sites
```
TODO
```