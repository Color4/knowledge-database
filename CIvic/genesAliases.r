
     t2 <-genesA %>%
    gather(variable,value,-id,-entrez_id,-name,-description) %>%
    mutate(group = extract_numeric(variable)) %>%
    mutate(variable =  gsub("\\d","",x = variable)) %>%
      spread(variable,value)


       t3 <- t2[!is.na(t2$`aliases/`),]

       https://stackoverflow.com/questions/11254524/omit-rows-containing-specific-column-of-na


       drops <-c("group")
> t4 <-t3[,!names(t3)%in% drops]

sortedt4 <- t4[order(t4$id) , ]

write.csv(sortedt4, file = "AliasGenes.csv")
