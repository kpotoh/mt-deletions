#!/bin/bash
# USAGE: bash 1.cleanup_sequences.sh INPUT.fasta OUTPUT.fasta

# INPUT=data/raw/sequence_mtDNA_FASTA_57k_total_seq.fasta
# OUTPUT=data/interim/sequences.clean.fasta
INPUT=$1
OUTPUT=$2

awk 'BEGIN {RS=">"} /Homo sapiens.*[Mm]ito/ {printf ">"$o}' $INPUT > $OUTPUT


# grep '>' data/interim/s2.fasta | egrep -v "Homo sapiens.*[Mm]ito.*complete" | less  # check

isolates must be saved!!!