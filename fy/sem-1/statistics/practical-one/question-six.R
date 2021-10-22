#i.
exp(5) #Returns the exponential value of 5

#ii.
log(5) #Returns the log(base e) of 5

#iii.
log10(5) #Returns the log(base 10) of 5

#iv.
seq(from = 0, to = 500, by = 5) #Returns a sequence from 0 to 500

#v.
data = read.csv(text = " roll_no,name,grade 
1,Jhon Doe,A
2,Emma Watson,A
3,Peter Parkour,B
4,Salina James,B"
, header =TRUE)
data$grade
split(data,f = data$grade) #Groups the data as per the factor provided
