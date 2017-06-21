"""Convert DNA sequences to RNA."""

def rna(seq):
    """Convert a DNA sequence to RNA."""

    seq_upper = seq.isupper()

    seq = seq.lower()

    seq = seq.replace('t', 'u')

    if seq_upper:
        return seq.upper()
# will return the sequence as upper case even if original is lower case
    else:
        return seq

def reverse_rna_complement(seq):
    seq_upper = seq.isupper()

    seq = seq[::-1]

    seq = seq.upper()

    seq = seq.replace('A', 'u')
    seq = seq.replace('T', 'a')
    seq = seq.replace('G', 'c')
    seq = seq.replace('C', 'g')

    if seq_upper:
        return seq.upper()
# will return the sequence as upper case even if original is lower case
    else:
        return seq
