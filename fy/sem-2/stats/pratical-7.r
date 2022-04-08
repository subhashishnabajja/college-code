Mydata = read.csv("data.csv", header = TRUE)
Mydata

attach(Mydata)

xbar = mean(X1)
s = sd(X1)
n = length(X1)


Mu = 134

tstat = (xbar - Mu)/(s / (n^0.5))
tstat

res <- prop.test(x = 95, n = 160, p = .5, correct = FALSE)
res

prop.test(x = 95, n = 160, p = 0.5, correct = FALSE, alternative = "less")

prop.test(x = 95, n = 160, p = 0.5, correct = FALSE, alternative = "greater")


res <- prop.test(x = c(490, 400), n = c(500,500))
res
