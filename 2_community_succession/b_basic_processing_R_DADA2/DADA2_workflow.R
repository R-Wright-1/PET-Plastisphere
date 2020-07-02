
## Robyn Wright
## MiSeq samples (PhD)

##_______DADA2________##
#______________________#

# following SOP published as: "Bioconductor Workflow for Microbiome Data Analysis: from raw reads to community analyses [version 2; referees: 3 approved]"
# workflow can also be found here: http://web.stanford.edu/class/bios221/MicrobiomeWorkflowII.html

# "DADA2" workflow: http://benjjneb.github.io/dada2/tutorial.html


# May need to install packages using e.g.:
# source("https://bioconductor.org/biocLite.R")
# biocLite('phyloseq')



#______________________#
	 #__PACKAGES__#
#______________________#

library(ggplot2)
library(gridExtra)
library(dada2)
library(phyloseq)
library(DECIPHER)
library(phangorn)
library(knitr)
library(BiocStyle)

set.seed(100)

packageVersion("phyloseq")
packageVersion("DADA2")

#__________________________#
	 #__PREPARE DATA__#
#__________________________#

# you need a folder containing all your fasta files (unzipped)

# indicate path
miseq_path <- file.path("/Users/u1560915/Documents/OneDrive/PhD_Plastic_Oceans/Experiments/MiSeq2/Analysis_PET2/raw_files")

# sort files to ensure R1 and R2 are in same order
fns <- sort(list.files(miseq_path, full.names = T))
fnFs <- fns[grepl("R1", fns)]
fnRs <- fns[grepl("R2", fns)]



#___________________________#
	 #__TRIM & FILTER__#
#___________________________#

# Most Illumina sequencing data shows a trend of decreasing average quality towards the end of sequencing reads. One should always inspect data quality!
# To do this, randomly pick out 3 fasta files
ii <- sample(length(fnFs), 3)

for(i in ii) { print(plotQualityProfile(fnFs[i]) + ggtitle("Fwd")) }
for(i in ii) { print(plotQualityProfile(fnRs[i]) + ggtitle("Rev")) }

plotQualityProfile(fnFs[1:3]) + ggtitle("Fwd")
plotQualityProfile(fnRs[1:3]) + ggtitle("Rev")

# forward reads seem to maintain quality (above Q30), but reverse reads start looking bad at cycle ~225
# trim the first 10 nucleotides due to Illumina errors (see SOP); in forwards trim at 295 and in reverse at 225

# define a new subdirectory to place the filtered files
filt_path <- file.path(miseq_path, "filtered")

if(!file_test("-d", filt_path)) dir.create(filt_path)
filtFs <- file.path(filt_path, basename(fnFs))
filtRs <- file.path(filt_path, basename(fnRs))

# forward primer: 19bp
# reverse primer: 20bp
# trimming away the primers with trimLeft. This is essential, especially with degenerate primers, which later on would mess with the learning algorithm...
out <- filterAndTrim(fnFs, filtFs, fnRs, filtRs, trimLeft = c(21, 20), truncLen = c(290, 250), maxN = 0, maxEE = c(2,2), truncQ = 2, rm.phix = T, compress = T, multithread = T)
head(out)



#________________________#
	 #__INFER ASVs__#
#________________________#

# ASV = amplicon sequence variants (instead of OTUs)
# read about this in "DADA2: High-resolution sample inference from Illumina amplicon data" (Callahan et al 2016)



#__1. LEARN ERROR RATES

# The DADA2 method relies on a parameterized model of substitution errors to distinguish sequencing errors from real biological variation. Because error rates can (and often do) vary substantially between sequencing runs and PCR protocols, the model parameters can be discovered from the data itself using a form of unsupervised learning in which sample inference is alternated with parameter estimation until both are jointly consistent.

# It is necessary to re-define the file names here if any samples did not have any reads that passed the quality filtering steps
######
filt_path <- file.path("/Users/u1560915/Documents/OneDrive/PhD_Plastic_Oceans/Experiments/MiSeq2/Analysis_PET2/raw_files/filtered/")
if(!file_test("-d", filt_path)) dir.create(filt_path)
fns <- sort(list.files(filt_path, full.names = T))
filtFs <- fns[grepl("R1", fns)]
filtRs <- fns[grepl("R2", fns)]
######

errF <- learnErrors(filtFs, multithread = T)
errR <- learnErrors(filtRs, multithread = T)

# In order to verify that the error rates have been reasonably well-estimated, we inspect the fit between the observed error rates (black points) and the fitted error rates (black lines) in Figure 2.
plotErrors(errF)
plotErrors(errR)



#__2. DEREPLICATION

# Dereplication combines all identical sequencing reads into into “unique sequences” with a corresponding “abundance”: the number of reads with that unique sequence. Dereplication substantially reduces computation time by eliminating redundant comparisons.

derepFs <- derepFastq(filtFs, verbose = T)
derepRs <- derepFastq(filtRs, verbose = T)

sam.names <- sapply(strsplit(basename(filtFs), "_"), `[`, 1)
names(derepFs) <- sam.names
names(derepRs) <- sam.names



#__3. SAMPLE INFERENCE

dadaFs <- dada(derepFs, err = errF, multithread = T, pool = T, verbose = T)
dadaFs[[1]]

dadaRs <- dada(derepRs, err = errR, multithread = T, pool = T, verbose = T)
dadaRs[[1]]



#__4. MERGE PAIRED READS

#The DADA2 sequence inference step removed (nearly) all substitution and indel errors from the data. We now merge together the inferred forward and reverse sequences, removing paired sequences that do not perfectly overlap as a final control against residual errors.
mergers <- mergePairs(dadaFs, derepFs, dadaRs, derepRs, verbose = T)

#inspect the merger data.frame from the first sample
head(mergers[[1]])



#__5. CONSTRUCT SEQUENCE TABLE

# We can now construct an amplicon sequence variant (ASV) table, a higher-resolution version of the OTU table produced by traditional methods.
seqtab <- makeSequenceTable(mergers)
dim(seqtab)

# Inspect distribution of sequence lengths
table(nchar(getSequences(seqtab)))

# amplicon length without primers should be ~373 in my case, so cutting what is extreme
seqtab2 <- seqtab[, nchar(colnames(seqtab)) %in% seq(365, 375)]
table(nchar(getSequences(seqtab2)))



#__6. REMOVE CHIMERAS

seqtabNoC <- removeBimeraDenovo(seqtab2, method = "consensus", multithread = T, verbose = F)
dim(seqtabNoC)

sum(seqtabNoC)/sum(seqtab)



#__7. ASSIGN TAXONOMY
# instead of using the naive Bayesian classifier (Wang et al. 2009), I here employ the new IDTAXA method (Murali et al. 2018) which is more accurate and faster
# download the trained classifier at: http://www2.decipher.codes/Downloads.html
# This bit doesn't seem to work!

#dna <- DNAStringSet(getSequences(seqtabNoC))
#dna <- RemoveGaps(dna)
#load("/Users/u1560915/Documents/OneDrive/PhD_Plastic_Oceans/Experiments/MiSeq_Dada/SILVA_SSU_r132_March2018.RData")

#ids <- IdTaxa(dna, trainingSet, strand = "top", processors = NULL, verbose = T)
#ranks <- c("Kingdom", "Phylum", "Class", "Order", "Family", "Genus", "Species")
#taxid <- t(sapply(ids, function(x) { m <- match(ranks, x$rank); taxa <- x$taxon[m]; taxa[startsWith(taxa, "unclassified_")] <- NA; taxa }))

#colnames(taxid) <- ranks; rownames(taxid) <- getSequences(seqtabNoC)
#taxTab <- taxid
#unname(head(taxTab))
#write.csv(taxid, "taxid.csv")
# Few species assignments were made, both because it is often not possible to make unambiguous species assignments from subsegments of the 16S gene, and because sometimes there is surprisingly little coverage of microbiota in reference databases.


# OLD VERSION USING Wang classifier

seqtabNoC <- readRDS("/Users/u1560915/Documents/OneDrive/PhD_Plastic_Oceans/Experiments/MiSeq2/Analysis_PET2/seqtabNoC.rds")

taxa <- assignTaxonomy(seqtabNoC, "/Users/u1560915/Documents/OneDrive/PhD_Plastic_Oceans/Experiments/MiSeq2/Analysis_PET2/silva_nr_v132_train_set.fa", tryRC=TRUE)
saveRDS(taxa, file = "taxa.rds")
taxa <- addSpecies(taxa, "/Users/u1560915/Documents/OneDrive/PhD_Plastic_Oceans/Experiments/MiSeq2/Analysis_PET2/silva_species_assignment_v132.fa")
taxTab <- taxa


####
#taxa <- read.csv("/Users/u1560915/Documents/OneDrive/PhD_Plastic_Oceans/Experiments/MiSeq2/Analysis_PET2/taxa.csv", header=TRUE)
#taxa_Gab <- readRDS("/Users/u1560915/Documents/OneDrive/PhD_Plastic_Oceans/Experiments/MiSeq2/Analysis_PET2/taxa_16S_MiSeq3.rds")
#head(taxa_Gab)
#write.csv(taxa_Gab, "/Users/u1560915/Documents/OneDrive/PhD_Plastic_Oceans/Experiments/MiSeq2/Analysis_PET2/taxa_16S_MiSeq3.csv")
#saveRDS(taxa, file = "taxa.rds")
####

taxa.print <- taxa
rownames(taxa.print) <- NULL
head(taxa.print)
write.csv(taxa, "taxa.csv")
write.csv(taxa.print, "taxa.print.csv")
write.csv(seqtabNoC, "seqtabNoC.csv")
saveRDS(seqtabNoC, file = "seqtabNoC.rds")

getN <- function(x) sum(getUniques(x))
track <- cbind(out, sapply(dadaFs, getN), sapply(dadaRs, getN), sapply(mergers, getN), rowSums(seqtabNoC))

colnames(track) <- c("input", "filtered", "denoisedF", "denoisedR", "merged", "nonchim")
head(track)
write.csv(track, file = "Track_16S_MiSeq3.csv")