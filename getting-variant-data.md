# Pseudo code for getting splice variants data (example is for donor sites)

1. Obtain splice sites from previous step
```
    donor_sites = input(donor.sites.txt)
```

2. Obtain variants data from ClinVar
    - [Link to download](ftp://ftp.ncbi.nlm.nih.gov/pub/clinvar/tab_delimited/variant_summary.txt.gz)
    - In the file, only following columns are required; Clinical significance, Assembly, Chromosome, Start, Stop, ReferenceAllele, AlternateAllele
    - Only variants from GRch37 (hg19) assembly are needed. Clinical significance is used for labeling the variants i.e. benign and likely benign is ctrl (0), while pathogenic and likely pathogenic is case (1).
```
    variants = input(variant_summary.txt)
    variants = variants[variants$Assembly = “GRch37”
    variants@class = ifelse(variants$Clinical significance == [“benign”, “likely benign”], 0, 1)
```

3. Use GenomicRanges packages to find variants that locate in splice sites and filter out variants not in splice sites
```
    overlap = GenomicRanges.findOverlaps(variants, donor_sites)
    variants = variants[overlap], where overlap is a matrix keeping index of variants and donor_sites for every overlaps found
```

4. Obtain reference and alternative sequences of each variants using package from Bioconductor (as mentioned in [pseudocode for getting splice site data](https://github.com/smiile8888/rna-splice-sites-recognition/blob/master/getting-splice-sites.md))
```
    variants_i@reference = getSeq(variants_i@chromosome, donor_sites@start[overlap_donor_i], donor_sites@end[overlap_donor_i])
    variants_i@alternative = getAlternativeSeq(reference_seq, variant_position_on_splice_site, reference_allele, alternative_allele), where reference_seq is sequence obtained from step above, variant_position_on_splice_site = position on splice site where variant is locate, reference_allele and alternative_allele = two alleles of the variants. The output of this function should be the DNA sequence with only 1 nt difference from the sequence obtained from step above.
```

5. Get reverse complementary sequence if the splice site is on minus strand
```
    variants_i@reference = getReverseComplementary(variants_i@reference)
    variants_i@alternative = getReverseComplementary(variants_i@alternative)
```