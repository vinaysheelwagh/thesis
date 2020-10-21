df <- read.table("C:/Users/Vinaysheel Wagh/Downloads/outputIouFile.csv", 
                 header = TRUE,
                 sep = ",")
df


wilcox.test(df[['Proposed_Model']], df[['Previous_Research']], paired = FALSE,alternative = "greater", mu =0.022, correct = FALSE)


