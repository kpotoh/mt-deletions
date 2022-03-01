# mt-deletions


## Workflow

### 1 Download human mt genomes from [NCBI](https://www.ncbi.nlm.nih.gov/nuccore/?term=ddbj_embl_genbank%5Bfilter%5D+AND+txid9606%5Borgn%3Anoexp%5D+AND+complete-genome%5Btitle%5D+AND+mitochondrion%5Bfilter%5D) with query to **Nucleotide database**:
```
ddbj_embl_genbank[filter] AND txid9606[orgn:noexp] AND complete-genome[title] AND mitochondrion[filter] 
```

### 2 Clean up sequences from non human mt genomes
```
bash scripts/0.cleanup_sequences.sh SEQS OUT_SEQS
```

### 3 Align to reference and form the multiple alignment
```
bash scripts/1.bwa.sh bwa samtools data/share/NC_012920.1.fasta data/raw/sequence.fasta 24

mv data/raw/sequence.fasta.sam data/interim/

perl scripts/2.longest-alignments.pl data/interim/sequence.fasta.sam > data/interim/sequence.fasta.purified.sam

python3 scripts/3.sam2fasta.py data/share/NC_012920.1.fasta data/interim/sequence.fasta.purified.sam data/interim/mulal.fasta
```

### 4 Analize alignment to search ubiquitous restriction sites
Deletions distribution
```
egrep -o "\-*" data | sort | uniq -c | awk '{print $1 "\t" length($2) "\t" $2 "\t" length($2)%3}' | tee logs/gaps_birds.log
```

**[Analysis](./nb/EDA_mulal.ipynb) in jupyter notebook**
