import random
from collections import Counter
from multiprocessing import Pool

from Bio.Restriction import Analysis, AllEnzymes
from Bio.SeqRecord import SeqRecord
from Bio import SeqIO
import tqdm

PATH_TO_SEQS = "data/raw/sequence.fasta"
THREADS = 24  # and 10GB of RAM
PROB = 0.01

enzymes = AllEnzymes.copy()


def cleanup_enzyme_collection():
    fasta = SeqIO.parse(PATH_TO_SEQS, "fasta")
    n = 0
    pot_rs = []
    for rec in tqdm.tqdm(fasta, "Seqs", 56446):
        if random.random() > PROB:
            continue
        n += 1
        anal = Analysis(enzymes, rec.seq, linear=False)
        anal.mapping # dict[RS_name, positions]
        
        for rest_enz, positions in anal.mapping.items():
            if len(positions) == 1:
                pot_rs.append(rest_enz)

    ctr = Counter(pot_rs)
    m = 0
    for enz, amount in ctr.items():
        if amount != n:
            if enz in enzymes:
                enzymes.remove(enz)
                m += 1
    print(f"Removed {m} enzymes")
    

def extract_restr_enz(rec: SeqRecord) -> list:
    anal = Analysis(enzymes, rec.seq, linear=False)
    pot_rs = []
    for restr_enz, positions in anal.mapping.items():
        if len(positions) == 1:
            pot_rs.append(restr_enz)
    return pot_rs


def main():
    cleanup_enzyme_collection()

    fasta = SeqIO.parse(PATH_TO_SEQS, "fasta")
    with Pool(THREADS) as p:
        collection_of_pot_rs = p.map(extract_restr_enz, fasta)

    pot_rs = []
    for xx in collection_of_pot_rs:
        for x in xx:
            pot_rs.append(x)  
    
    ctr = Counter(pot_rs)
    most_frequent_rs = {r: v for r, v in ctr.items() if v > 56446 - 1000}

    for rs, num in most_frequent_rs.items():
        print(rs, rs.site, num)




if __name__ == "__main__":
    main()


