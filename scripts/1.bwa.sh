#!/bin/bash
# CAUTION! sequence names should not used spaces
#USAGE: ./1.bwa.sh pathToBwa pathToSamtools fastaReference multiFastaSequesteredAndRandomized coreNumber
#output samFile

#BWA v.0.7.17-r1188
BWAPATH=$1

#SAMTOOLS v.1.5 (using htslib 1.5)
SAMTOOLSPATH=$2
REF=$3
SAMPLE=$4
THREADS=$5

$BWAPATH index $REF
$BWAPATH bwasw -t $THREADS $REF $SAMPLE | $SAMTOOLSPATH view -h -f 0 -F 256 -@ $THREADS > "$SAMPLE.sam"
