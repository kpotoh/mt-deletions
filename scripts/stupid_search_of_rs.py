import random
from collections import Counter
from multiprocessing import Pool

import pandas as pd
from Bio.Restriction import Analysis, AllEnzymes
from Bio.SeqRecord import SeqRecord
from Bio import SeqIO
import tqdm

PATH_TO_SEQS = "data/raw/sequence.fasta"
THREADS = 24  # and 10GB of RAM
PROB = 0.01

enzymes = AllEnzymes.copy()


def _cleanup_enzyme_collection():
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
    for restr_enz, positions in anal.with_N_sites(1).items():
        pos = positions[0]
        re_name = repr(restr_enz)
        site = restr_enz.site

        one_data = {
            "RE": re_name,
            "Site": site,
            "SeqName": rec.description,
            "CutPos": pos,
        }
        pot_rs.append(one_data)
    return pot_rs


def main():
    """ 1 hour on 23 threads """
    fasta = SeqIO.parse(PATH_TO_SEQS, "fasta")
    with Pool(THREADS) as p:
        collection_of_pot_rs = p.map(extract_restr_enz, fasta)

    pot_rs = []
    for xx in collection_of_pot_rs:
        for x in xx:
            pot_rs.append(x)  
    
    df = pd.DataFrame(pot_rs)
    df.to_csv("../data/processed/re.csv", index=None)

    df_counts = df.RE.value_counts().reset_index()
    df_counts.columns = ["RE", "CuttedSeqs"]
    df_counts.to_csv("../data/share/cuted_seqs_num.csv", index=None)


if __name__ == "__main__":
    main()


