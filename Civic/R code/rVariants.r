




     t2 <-genes %>%
 +     gather(variable,value,-id,-entrez_id,-name,-description) %>%
 +     mutate(group = extract_numeric(variable)) %>%
 +     mutate(variable =  gsub("\\d","",x = variable)) %>%
 +     spread(variable,value)

# remove na
       t2[!is.na(t2$`variants//evidence_items/accepted_count`),]

       https://stackoverflow.com/questions/11254524/omit-rows-containing-specific-column-of-na


       drops <-c("group","aliases/","type")
> dropcols <-t2[,!names(t2)%in% drops]

sortedt2 <- dropcols[order(dropcols$id) , ]

write.csv(sortedt2, file = "VariantGenes.csv")
