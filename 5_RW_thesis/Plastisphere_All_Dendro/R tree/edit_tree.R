#install.packages("ape")
library("ape")
library("gplots")
library("ggplot2")
library("ggtree")
#library("phangorn")
#library("gridExtra")
#library("dada2")
#library("msa")
#library("phyloseq")
#source("https://bioconductor.org/biocLite.R")
#biocLite('msa')
#library("seqinr")
#biocLite('DECIPHER')
#library("DECIPHER")

#Before this can be run, the sequences from the file made by the 'get_abundant_sequences.py' script should be aligned to the SILVA database using the ARB aligner:
#https://www.arb-silva.de/aligner/
#The results of this alignment then need to be turned into a tree using QIIME with the command:
#make_phylogeny.py -i aligned_fasta_from_ARB.fasta -o ARB_aligned_mid_rooted.dnd' -r midpoint
#By default QIIME uses fasttree to construct the tree

tree <- read.tree("/Users/u1560915/Documents/OneDrive/PhD_Plastic_Oceans/Experiments/MiSeq2/Analysis_PET2/tree/0.5% aligned no control.dnd")
#pdf(filename="/Users/u1560915/Documents/OneDrive/PhD_Plastic_Oceans/Experiments/MiSeq2/PET_analysis/tree/silva_0.5%.pdf")
pdf(file="/Users/u1560915/Documents/OneDrive/PhD_Plastic_Oceans/Experiments/MiSeq2/Analysis_PET2/tree/tree2.pdf", height=20, width=15)
plt <- ggtree(tree, aes(size=1))
plt <- flip(plt, 128, 120)
plt <- flip(plt, 115, 119)
plt + geom_tiplab2(size=0, align=TRUE, linesize=1, angle=0)
plt + geom_tiplab(size=3, color="purple")+ geom_text2(aes(label=node))
#plt <- flip(plt, 113, 136)
#plt <- flip(plt, 112, 50)
open_tree(plt, angle=45)
open_tree(plt, angle=45) + geom_tiplab2(size=3, align=TRUE, linesize=.5)
#+geom_treescale(0,-1)
dev.off()
tree$tip.label

"ASV000028", "ASV000007", "ASV000153", "ASV004528", "ASV000145", "ASV000203", "ASV000052", "ASV000041", 
"ASV000061", "ASV000057", "ASV000005", "ASV000079", "ASV004313", "ASV000068", "ASV000038",
"ASV000066", "ASV000032", "ASV000042", "ASV000010", "ASV000014", "ASV000016", "ASV000022",
"ASV000074", "ASV000064", "ASV000085", "ASV000035", "ASV000056", "ASV000030", "ASV000051",
"ASV000046", "ASV006228", "ASV000009", "ASV000045", "ASV000034", "ASV000054", "ASV000027",
"ASV000058", "ASV000024", "ASV000050", "ASV000047", "ASV000067", "ASV000036", "ASV000060",
"ASV000025", "ASV000772", "ASV000044", "ASV000059", "ASV000037", "ASV000033", "ASV000082",
"ASV017996", "ASV000015", "ASV000008", "ASV000020", "ASV000043", "ASV000049", "ASV000018",
"ASV000062", "ASV000011", "ASV000040", "ASV000026", "ASV000003", "ASV000076", "ASV000002",
"ASV000031", "ASV001733", "ASV000012", "ASV000021", "ASV000006", "ASV000063", "ASV000075", "ASV000053",
"ASV000023", "ASV000004", "ASV000013", "ASV000001", "ASV000017", "ASV000039", "ASV000019",
"ASV000073", "ASV000065", "ASV000055", "ASV000078", "ASV000111", "ASV000048", "ASV000070",


[1]     
 [8]      
[15] 
[22]    
[29]  
[36]      
[43]     
[50]   
[57]   
[64] 
[71] 
[78] 
[85] 


dev.off()