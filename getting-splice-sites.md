# Pseudo code for getting splice sites data

1. Obtain human gene definition from UCSC (hg19), header of the table is **[gene_symbol, isoform_id, chromosome, strand, start, end, coding_start, coding_end, number_of_exons, starts_exons, ends_exons]**
[Link to download](http://hgdownload.cse.ucsc.edu/goldenpath/hg19/database/refFlat.txt.gz)
```
    gene_def = input(refFlat.txt)
    size_of_splice_site = 20
```
2. From the gene definition table, extract protein coding genes by filtering out any genes with coding_start == coding_end
```
    gene_def = gene_def [gene_def@coding_start != gene_def@coding_end]
```

3. Using starts_exons and ends_exons columns, intron start and end positions of each gene are obtained. 
```
    gene_i = gene_def[i], where i is index of gene in the gene definition table
    gene_i@intron_starts = gene_i_ends_exons[1:(n-1)]
    gene_i@intron_ends = gene_i_starts_exons[2:n], where n is number of exons, intron_starts is a vector of intron start positions and intron_ends is a vector of intron end positions.
```

4. Splice junction is the position that separates the intron and the exon, where the 5' end of the intron is the donor site and the 3'end of the intron is the acceptor site.
```
    gene_i@donor_starts = gene_i@intron_starts - size_of_splice_site
    gene_i@donor_ends = gene_i@intron_starts + size_of_splice_site
    gene_i@acceptor_starts = gene_i@intron_ends - size_of_splice_site
    gene_i@acceptor_ends = gene_i@intron_ends + size_of_splice_site
```
If gene is on the minus strand, then swap donor and acceptor
```
    if(gene_i@strand == “-”) then
        gene_i@donor_starts = gene_i@acceptor_starts
        gene_i@donor_ends = gene_i@acceptor_ends
        gene_i@acceptor_starts = gene_i@donor_starts
        gene_i@acceptor_ends = gene_i@donor_ends
```
5. Using Bioconductor in R package to obtain sequences using chromosome, start and end position of donor and acceptor.Link to the [Bioconductor library](https://bioconductor.org/packages/release/data/annotation/html/BSgenome.Hsapiens.UCSC.hg19.html)
```
Plus strand -> gene_i@sequences = getSeq(chromosome, start_position, end_position)
Minus strand - >gene_i@sequences = getReverseComplementary(getSeq(chromosome, start_position, end_position)), where getSeq is a function to get sequence from coordinate (chromosome, start, end) and getReverseComplementary is a function to get a complementary sequence of the specified DNA sequence.
```