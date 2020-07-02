# A multi-OMIC characterisation of biodegradation and microbial community succession within the PET Plastisphere
### Robyn J. Wright, Rafael Bosch, Matthew I. Gibson and Joseph A. Christie-Oleza

This is the Github repository for all code used to produce the analyses in [A multi-OMIC characterisation of biodegradation and microbial community succession within the PET Plastisphere](https://www.microbiologyresearch.org/content/journal/acmi/10.1099/acmi.ac2019.po0168)</br>
<i>Note that this link will be updated with a link to the full paper once published.</i></br>

I have not provided comprehensive instructions on reproducing these analyses, but with some basic knowledge of Python usage, the scripts should be able to just be run (in the directories that they are in, as these already have the data needed). In some cases, larger files may need unzipping etc. Please feel free to [email me](mailto:robyn.wright@dal.ca) with any questions.

## This repository has the following sections:</br>

### 1. FTIR with raw plastics</br>
A .csv file with the FTIR data, a .py script and a .png file that this creates</br></br>

### 2. Community succession</br>
**a) DNA yields:** DNA concentrations in each sample as measured by Qubit as well as bioanalyser and qPCR results of the library used for MiSeq (note that this also contained samples run for other projects in the same run) and the metadata files used for the SRA submission.</br>
**b) Basic processing DADA2 in R:** this has the script used for analysis and several of the plots output by this. Raw sequencing data can be downloaded from the NCBI SRA [PRJNA544783](https://www.ncbi.nlm.nih.gov/Traces/study/?query_key=3&WebEnv=NCID_1_11700513_130.14.22.76_5555_1593658013_3135564330_0MetA0_S_HStore&o=acc_s%3Aa)</br>
**c) Stacked bar:** All samples and taxonomy arranged by time point, a script for plotting the stacked bar plots and the bar plots .png</br>
**d) Diversity:** A script for plotting the mean diversity of treatments on different days, and outputting this information to .csv files</br>
**e) NMDS, principal response curve and heatmap:** scripts for carrying out the PRC analysis in R, extracting the data in Python and plotting this alongside a regular NMDS plot and a heat map of the important ASVs</br>
**f) ANOSIM and PERMANOVA:** A script for carrying out the ANOSIM and PERMANOVA tests listed in one of the supplementary tables</br>
**g) Colonisation dynamics:** A script that sorts ASVs in each sample type by the day on which they are highest in abundance, normalises abundance within each ASV and plots this abundance as a heatmap</br>
**h) PICRUSt2:** almost all PICRUSt2 results (some were removed due to large file sizes, but these haven't been used for plotting), plotting scripts for circular plots and an R notebook that explores the abundance of genes related to PET degradation (abundance, taxa that contribute to each function, etc.). Note that details on adding genes to the PICRUSt2 reference database can be found at my [Plastisphere metaanalysis repository](https://github.com/R-Wright-1/Plastisphere-MetaAnalysis)</br>
**i) Community metabolomics:** data and scripts for plotting the NMDS plot of community metabolome</br></br>

### 3. Isolates</br>
**a) Genomic analysis:** Genome annotations for each isolate as well as results of the HMM search. Note that details on making the HMM can be found at my [Plastisphere metaanalysis repository](https://github.com/R-Wright-1/Plastisphere-MetaAnalysis)</br>
**b) Growth of isolates:** data and scripts for plotting the growth of the two isolates on a range of common growth substrates, as measured by a plate reader across 72 hours of incubation</br>
**c) Proteomic analysis of isolates:** scripts and data used for calculating fold change, making the plots and making the Thioclava gene cluster plot</br>
**d) Metabolomic analysis of isolates:** scripts for calculating fold change, carrying out T-tests and plotting each metabolite. Note that the values shown here are taken directly from the appropriate raw metabolomics data, as presented in Supplementary Table 8</br></br>

### 4. Community and isolates (5 month growth experiment)</br>
**a) Growth at three months and FTIR analysis at five months:** scripts and raw FTIR data for plotting the growth of isolates and communities on different types of PET</br>

### 5. All code used for this chapter of my PhD thesis</br>
I think that all of this is repeated in the above sections, but I am leaving it in for compatibility with what I have listed in my PhD thesis (which will be linked once it is available - after the embargo period)
