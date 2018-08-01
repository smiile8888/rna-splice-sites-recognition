# RNA Splice Sites Recognition

    In Eukaryotes, the initial RNA or precursor-mRNA that is transcribed from a gene’s DNA template must be processed before it becomes a mature messenger RNA (mRNA) that can direct the synthesis of protein. One of the steps in this processing, called “RNA splicing,” involves the removal or splicing out of certain sequences referred to as intervening sequences, or introns. The final mRNA thus consists of the remaining sequences, called exons, which are connected to one another through the splicing process. Some RNA molecules have the capability to splice themselves but some splice alternatively. The splicing research [1](#References) discovered that alternative patterns of splicing within a single precursor-mRNA at different junctions could yield in a variety of mature mRNAs. Most of the alternative splicing is caused by a mutation of a splice site which can reduce spliceosome binding specificity of that splice site or completely make it loss of function. The alternative splicing can produce different functional proteins, which could lead to causing many diseases in human [2](#References). 

    Many studies have proposed models to recognize the splice sites to reveal which splice sites contain a mutation that may cause a splicing error. Position-Weight-Matrix (PWM) is a model commonly used to recognize DNA-binding motif sequences by transforming sequence data into a probability matrix [3](#References). It can be used to recognize simple sequence structures. However, growing evidence indicates that sequence specificities can be more accurately captured by more complex techniques [4-6](#References). Recently, some deep learning methods outperformed other recent approaches in many problems including DNA-binding sites recognition [7-9](#References) but not much work has specifically been done in recognition of RNA Splice sites. Therefore, I plan to apply a Convolutional Neural Network (CNN) model to the task of recognizing the splice sites and classifying the sequence whether is pathogenic or not.

## Goals
- Build a model to recognize splice sites – both of donor and acceptor
- Build a mutation scoring system
    - To determine whether or not a mutation causes mis-recognizing of spliceosome
- Use as a baseline for a competition of a coming conference this year

## References
[1]	Berget, Susan M., Claire Moore, and Phillip A. Sharp. "Spliced segments at the 5′ terminus of adenovirus 2 late mRNA." Proceedings of the National Academy of Sciences 74.8 (1977): 3171-3175.
[2]	Faustino, Nuno André, and Thomas A. Cooper. "Pre-mRNA splicing and human disease." Genes & development 17.4 (2003): 419-437.
[3]	Stormo, Gary D. "DNA binding sites: representation and discovery." Bioinformatics 16.1 (2000): 16-23.   
[4]	Rohs, Remo, et al. "Origins of specificity in protein-DNA recognition." Annual review of biochemistry 79 (2010): 233-269.
[5]	Kazan, Hilal, et al. "RNAcontext: a new method for learning the sequence and structure binding preferences of RNA-binding proteins." PLoS computational biology 6.7 (2010): e1000832.
[6]	Siggers, Trevor, and Raluca Gordaˆn. "Protein–DNA binding: complexities and multi-protein codes." Nucleic acids research 42.4 (2013): 2099-2111.
[7]	Alipanahi, Babak, et al. "Predicting the sequence specificities of DNA-and RNA-binding proteins by deep learning." Nature biotechnology 33.8 (2015): 831-838.
[8]	Zhou, Jian, and Olga G. Troyanskaya. "Predicting effects of noncoding variants with deep learning-based sequence model." Nature methods 12.10 (2015): 931-934.
[9]	Kelley, David R., Jasper Snoek, and John L. Rinn. "Basset: learning the regulatory code of the accessible genome with deep convolutional neural networks." Genome research 26.7 (2016): 990-999.
[10]	Dean, Victoria, et al. “Deep learning for branch point selection in RNA splicing”, MLCB2016, https://vdean.github.io/MLCB2016_paper.pdf
