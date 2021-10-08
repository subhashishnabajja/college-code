#Read the data from the csv file
data <- read.csv("question-two-dataset.csv",header = TRUE)
data

#Meadian
median(data$Occurance)

#Mean
mean(data$Occurance)