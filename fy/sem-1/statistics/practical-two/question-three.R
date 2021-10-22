#Load the data from the .csv file
data <- read.csv("question-three-dataset.csv", header = TRUE )
data

#Mean
mean(data$Occurance)

#Median
median(data$Occurance)