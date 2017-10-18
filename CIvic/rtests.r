reshape(dat, idvar="ID", direction="long",
             varying=list(Start=c(2,5,8), End=c(3,6,9), Value=c(4,7,10)),
             v.names = c("DateRangeStart", "DateRangeEnd", "Value") )
