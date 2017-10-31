library(dplyr)
library(tidyr)

//https://stackoverflow.com/questions/12466493/reshaping-multiple-sets-of-measurement-columns-wide-format-into-single-columns

     t2 <-CivicVarGroups2 %>%
    gather(variable,value,-id,-name,-description) %>%
    mutate(group = parse_number(variable)) %>%
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
