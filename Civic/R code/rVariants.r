library(dplyr)
library(tidyr)
library(readr)
#too many na's to properly melt

civic_variants <- read_csv("~/Documents/github/knowledge-database/Civic/civic_raw_data/civic_variants.csv")




t2 <-civic_variants %>%
       gather(variable,value,-id,-entrez_id,-name,-description, -gene_id) %>%
       mutate(group = extract_numeric(variable)) %>%
       mutate(variable =  gsub("\\d","",x = variable)) %>%
       spread(variable,value)

# remove na
t2 <-t2[!is.na(t2$`variants//evidence_items/accepted_count`),]



drops <-c("group","aliases/","type")
> dropcols <-t2[,!names(t2)%in% drops]

sortedt2 <- dropcols[order(dropcols$id) , ]

write.csv(sortedt2, file = "VariantGenes.csv")
