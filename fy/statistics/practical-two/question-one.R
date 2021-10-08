#Import the data from the .csv file
data <- read.csv("question-one-dataset.csv",header = TRUE)
data
#Get the median
median(data$marks)
#Get the mean
mean(data$marks)