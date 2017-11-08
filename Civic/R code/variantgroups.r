library(dplyr)
library(tidyr)
library(readr)


civic_vargroups <- read_csv("~/Documents/github/knowledge-database/Civic/civic_raw_data/civic_vargroups.csv")


     t2 <-civic_vargroups %>%
    gather(variable,value,-id,-name,-description, -type) %>%
    mutate(group = readr::parse_number(variable)) %>%
    mutate(variable =  gsub("\\d","",x = variable)) %>%
      spread(variable,value)


       t3 <- t2[!is.na(t2$`aliases/`),]

       https://stackoverflow.com/questions/11254524/omit-rows-containing-specific-column-of-na


       drops <-c("group")
> t4 <-t3[,!names(t3)%in% drops]

sortedt4 <- t4[order(t4$id) , ]

write.csv(sortedt4, file = "AliasGenes.csv")

Myeloid And Lymphoid Neoplasms With Eosinophilia And Abnormalities Of PDGFRA, PDGFRB, And FGFR1
FGF/VEGF Receptor Tyrosine Kinase Inhibitor, PD173074
