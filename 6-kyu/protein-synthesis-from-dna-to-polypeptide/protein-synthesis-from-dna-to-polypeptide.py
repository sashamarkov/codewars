def protein_synthesis(dna):
    trans = {'T':'A', 'A':'U', 'G':'C', 'C':'G'}
    mrna = ''.join(trans[b] for b in dna)    
    codons = [mrna[i:i+3] for i in range(0, len(mrna), 3)]
    rna_output = ' '.join(codons)
    protein_output = ' '.join(CODON_DICT[c] for c in codons if len(c) == 3)
    return (rna_output, protein_output)