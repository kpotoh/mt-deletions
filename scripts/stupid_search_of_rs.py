from collections import Counter

from Bio.Restriction import Analysis, AllEnzymes
from Bio import SeqIO
import tqdm

PATH_TO_SEQS = "data/raw/sequence.fasta"

fasta = SeqIO.parse(PATH_TO_SEQS, "fasta")

n = 0
pot_rs = []
for rec in tqdm.tqdm(fasta, "Seqs", 56446):
    n += 1
    anal = Analysis(AllEnzymes, rec.seq, linear=False)
    anal.mapping # dict[RS_name, positions]
    
    for restriction_site, positions in anal.mapping.items():
        if len(positions) == 1:
            pot_rs.append(restriction_site)
    
    if n == 10:
        break


print(Counter(pot_rs))  # TODO check and add multiprocessing
