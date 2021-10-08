x = c(1,4,7,NA,12,19,15,21,20)
mean(x) # Outputs -> NA
mean(x,na.rm = TRUE)

#Example with values
x = c(1:75)
mean(x)

#Example with NA
x = c(5,6,8,48,NA,62,100)
mean(x, na.rm = TRUE)

