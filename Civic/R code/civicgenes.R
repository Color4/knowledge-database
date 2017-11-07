library(dplyr)
library(tidyr)
library(readr)

civic_genes <- read_csv("~/Documents/github/knowledge-database/Civic/civic_raw_data/civic_genes.csv", 
                             col_types = cols(`aliases/0` = col_skip(), 
                                                        `aliases/1` = col_skip(), `aliases/2` = col_skip(),`aliases/3` = col_skip(),`aliases/4` = col_skip(),`aliases/5` = col_skip(),`aliases/6` = col_skip(),`aliases/7` = col_skip(),`aliases/8` = col_skip(),`aliases/9` = col_skip(),`aliases/10` = col_skip(),`aliases/11` = col_skip(),`aliases/12` = col_skip(),`aliases/13` = col_skip(),`aliases/14` = col_skip(),`aliases/15` = col_skip(),`aliases/16` = col_skip(),`aliases/17` = col_skip(),`aliases/18` = col_skip()))




t2 <-civic_genes %>%
       gather(variable,value,-id,-entrez_id,-name,-description) %>%
       mutate(group = extract_numeric(variable)) %>%
       mutate(variable =  gsub("\\d","",x = variable)) %>%
       spread(variable,value)

# remove na
t3 <- t2[!is.na(t2$`variants//evidence_items/accepted_count`),]





drops <-c("group","aliases/","type")
t3  <- t3[,!names(t3)%in% drops]

finalsorted <- t3[order(t3$id) , ]

write.csv(finalsorted, file = "VariantGenestestB.csv", fileEncoding = "UTF-8")
##NOTES
#for excel the encoding needs to be fixed,  
# What to do about the boolean True/ false results?  SHould they be changed in database?
# https://stackoverflow.com/questions/11254524/omit-rows-containing-specific-column-of-na
##//https://stackoverflow.com/questions/12466493/reshaping-multiple-sets-of-measurement-columns-wide-format-into-single-columns
