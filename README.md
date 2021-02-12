# A multi-OMIC characterisation of biodegradation and microbial community succession within the PET Plastisphere
### Robyn J. Wright, Rafael Bosch, Morgan G.I. Langille, Matthew I. Gibson and Joseph A. Christie-Oleza

This is the Github repository for all code used to produce the analyses in [A Multi-OMIC Characterisation of Biodegradation and Microbial Community Succession Within the PET Plastisphere](https://https://www.researchsquare.com/article/rs-104576/v1)</br>
<i>Note that this link will be updated with a link to the full paper once published.</i></br>

I have not provided comprehensive instructions on reproducing these analyses, but with some basic knowledge of Python usage, the scripts should be able to just be run (in the directories that they are in, as these already have the data needed). In some cases, larger files may need unzipping etc. Please feel free to [email me](mailto:robyn.wright@dal.ca) with any questions.

## This repository has the following sections:</br>

### 1. FTIR with raw plastics</br>
A .csv file with the FTIR data, an .Rmd document used to perform baseline correction, a .txt file with the baseline-corrected spectra, a .py script to plot these spectra and a .png file that this creates.</br>
Note that the same script was used for normalising the FTIR spectra after incubation also, but file names and output locations were manually changed.</br></br>

### 2. Community succession</br>
**a) DNA yields:** DNA concentrations in each sample as measured by Qubit as well as bioanalyser and qPCR results of the library used for MiSeq (note that this also contained samples run for other projects in the same run) and the metadata files used for the SRA submission</br>
**b) Basic processing DADA2 in R:** this has the script used for analysis and several of the plots output by this. Raw sequencing data can be downloaded from the NCBI SRA [PRJNA544783](https://www.ncbi.nlm.nih.gov/Traces/study/?query_key=3&WebEnv=NCID_1_11700513_130.14.22.76_5555_1593658013_3135564330_0MetA0_S_HStore&o=acc_s%3Aa)</br>
**c) Stacked bar:** All samples and taxonomy arranged by time point, a script for plotting the stacked bar plots and the bar plots .png with taxa below 1% abundance grouped to 'other'</br>
**d) Diversity:** A script for plotting the mean diversity of treatments on different days, and outputting this information to .csv files</br>
**e) NMDS, principal response curve and heatmap:** scripts for carrying out the PRC analysis in R, extracting the data in Python and plotting this alongside a regular NMDS plot and a heat map of the important ASVs</br>
**f) ANOSIM and PERMANOVA:** A script for carrying out the ANOSIM and PERMANOVA tests listed in one of the supplementary tables</br>
**g) Colonisation dynamics:** Two versions of the analysis that examines the day on which each ASV is highest in abundance. The first version (colonisation_plot.py producing Overall fig order abundance.png) was from the first submission and this was later edited to the current versions (colonisation_new_R1.py and New figure.png) based on reviewer suggestions. These both produce heatmaps with taxa normalised to the day on which they are most abundant</br>
**h) PICRUSt2:** almost all PICRUSt2 results (some were removed due to large file sizes, but these haven't been used for plotting). This includes:
	- figure: final versions of the figures shown in the main and supplementary results</br>
	- older_plots: older versions of figures representing the data that weren't included in the final manuscript version</br>
	- picrust_out: the key output from running PICRUSt2 with the inclusion of additional genes related to PET degradation</br>
	- R-notebook: R notebook used to investigate the output of PICRUSt2 and the abundance of PETases within the predicted metagenome</br>
	- stratified_plots: data and scripts used to plot figures showing abundance of key genes stratified by the taxa that contributed to them</br>
**i) Community metabolomics:** Data and scripts used to plot the NMDS plot showing the distance between the metabolomics results obtained from the different community incubations on day 42</br>
**j) Other figures previous:** Some previous figures that didn't make it into the final manuscript version</br>
**z) Add genes to picrust:** Details on adding genes of interest to the default PICRUSt2 database using Hidden Markov Models of these genes. Includes an R markdown document and .html output with step-by-step instructions for recreating this</br></br>

### 3. Isolates</br>
**a) Genomic analysis:** Genome annotations for each isolate as well as results of the HMM search. Note that details on making the HMM can be found in z) Add genes to picrust, above</br>
**b) Growth of isolates:** data and scripts for plotting the growth of the two isolates on a range of common growth substrates, as measured by a plate reader across 72 hours of incubation</br>
**c) Proteomic analysis of isolates:** scripts and data used for calculating fold change, making the plots and making the Thioclava gene cluster plot</br>
**d) Metabolomic analysis of isolates:** scripts for calculating fold change, carrying out T-tests and plotting each metabolite. Note that the values shown here are taken directly from the appropriate raw metabolomics data, as presented in Supplementary Table 8</br>
**e) Global distribution:** details and scripts used to perform the searches for the isolates in [the plastisphere meta-analysis data](https://www.nature.com/articles/s41396-020-00814-9), the [TARA oceans data](http://ocean-microbiome.embl.de/companion.html) ([mitag 16S rRNA gene](http://ocean-microbiome.embl.de/data/16SrRNA.miTAGs.tgz) and [assembled metagenomes](https://doi.org/10.6084/m9.figshare.4902920)):</br>
	- figures created during analyses</br>
	- blast_database: BLAST databases created for each sample to be searched</br>
	- blast_out: output files from BLAST searches of all samples using the 16S rRNA gene sequences (both obtained from whole genome sequencing and sanger sequencing) of both isolates</br>
	 - metagenome: output files from all MetaQUAST runs with the two isolates against the [assembled TARA oceans metagenomes](https://doi.org/10.6084/m9.figshare.4902920) (note only summary files have been kept due to the large size of other output files)</br>
	 - plastisphere_16S: data used and figures produced by searches for the 16S sequences of both isolates in the data obtained from our recent [plastisphere meta-analysis](https://www.nature.com/articles/s41396-020-00814-9)</br>
	 - TARA_16S: data used and figures produced by searches for the 16S sequences of both isolates in the [TARA oceans mitag sequences](http://ocean-microbiome.embl.de/data/16SrRNA.miTAGs.tgz)</br></br>

### 4. Community and isolates (5 month growth experiment)</br>
**a) Growth at three months and FTIR analysis at five months:** scripts and raw FTIR data for plotting the growth of isolates and communities on different types of PET</br>

### 5. All code used for this chapter of my PhD thesis</br>
I think that all of this is repeated in the above sections, but I am leaving it in for compatibility with what I have listed in my PhD thesis (which will be linked once it is available - after the embargo period)
