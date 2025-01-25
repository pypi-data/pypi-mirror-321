from Bio import SeqIO


def filter_by_gap(file_in, max_gap_pct, file_out):
    file_out_handle = open(file_out, 'w')
    for each_seq in SeqIO.parse(file_in, 'fasta'):
        seq_str = str(each_seq.seq)
        gap_num = seq_str.count('-')
        gap_pct = gap_num*100 / len(seq_str)
        if gap_pct <= max_gap_pct:
            file_out_handle.write('>%s\n%s\n' % (each_seq.id, seq_str))
    file_out_handle.close()


msa_in      = '/Users/songweizhi/Desktop/AmoA_genes.bmge.aln'
msa_out     = '/Users/songweizhi/Desktop/AmoA_genes.gap40.bmge.aln'
gap_cutoff  = 40

filter_by_gap(msa_in, gap_cutoff, msa_out)
