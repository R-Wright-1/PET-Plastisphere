library(vegan)

#read in data and get treatments, times and replicate numbers
#note: data is log transformed
data <- read.csv("/Users/robynwright/Documents/OneDrive/Github/PET-Plastisphere/2_community_succession/e_nmds_PRC_heatmap/PRC_calculation/all_samples_log.csv", header=TRUE)

#change row names to those of samples
row.names(data) <- data[,1]
#delete the now unneeded columns
data <- data[,-c(1)]

#tell it how many days and treatments
day <- gl(8, 18, labels=c(0, 1, 3, 7, 14, 21, 30, 42))
treatment <- factor(rep(c(0, 0, 0, 'LCW', 'LCW', 'LCW', 'LC', 'LC', 'LC', 'PET', 'PET', 'PET', 'WPET', 'WPET', 'WPET', 'BHET', 'BHET', 'BHET'), 8))
replicate <- gl(3, 1, length=144)

mod <- prc(data, treatment, day)
mod
summ <- summary(mod)
logabu <- colSums(data)
logabu
#plot(mod, select = logabu > 100, axis=2)
plot(mod, select = logabu > 100)
ctrl <- how(plots = Plots(strata=replicate, type="free"), within=Within(type="series"), nperm=99)
anova(mod, permutations=ctrl, first=TRUE)

#and then write to files