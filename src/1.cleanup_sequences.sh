#!/bin/bash
# USAGE: bash 1.cleanup_sequences.sh INPUT.fasta OUTPUT.fasta

# INPUT=data/raw/sequence_mtDNA_FASTA_57k_total_seq.fasta
# OUTPUT=data/interim/sequences.clean.fasta
INPUT=$1
OUTPUT=$2

# awk 'BEGIN {RS=">"} /Homo sapiens.*[Mm]ito/ {printf ">"$o}' $INPUT > $OUTPUT


# grep '>' data/interim/s2.fasta | egrep -v "Homo sapiens.*[Mm]ito.*complete*" | less  # check

# isolates must be saved!!!


# fish@fish01-IdeaPad-3-17ALC6:~/mt-deletions$ 
# egrep "(Homo.*[Mm]ito.*complete)|(Homo.*[Mm]ito.*partial)|(Homo.*assembly.*mito)" data/interim/headers.txt > data/interim/clean_headers.txt



# awk 'BEGIN  {RS=">"} ! /RNA|transcr|gene|nuclear|protein|product|UNVERIFIED/ {printf ">"$o}' data/raw/sequence_mtDNA_FASTA_57k_total_seq.fasta | grep '>' > data/interim/clh.txt


awk 'BEGIN  {RS=">"} ! /RNA|transcr|gene|nuclear|protein|product|UNVERIFIED/ {printf ">"$o}' $INPUT | \
    awk 'BEGIN {RS=">"} /Homo.*[Mm]itochondrion/ {printf ">"$o}' $INPUT > $OUTPUT
