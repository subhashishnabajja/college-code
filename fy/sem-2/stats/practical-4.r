dbinom(
x = 5,
size = 10,
prob = 0.5
)
# P (4 <= k <= 7)
sum(dbinom( x = 4:7, size = 10, prob = 0.5))


k <- 0:10
probability <- dbinom(x = k , size = 10, prob = 0.5)
plot(x = k, y = probability, main = "Probability Distribution Function")
prob <- pbinom (q = k, size = 10, prob = 0.5)
prob
plot(x = k, y = prob, main = "Cumulative Distribution Function")
mean(1:6)
var(1:6)
# Normal Distribution
curve(dnorm(x), xlim = c(-3.5,3.5), ylab = "Density", main = "Standard Normal Density Function")
dnorm(x = c(-1.96, 0, 1.996))
curve(pnomr(x), xlim = c-3.5,3.5)

# PDF
k <- 0:10
probability <- dbinom(x = k, size = 10, prob = 0.5)
plot(x = k, y = probability, main = "Prob")
dbinom(x = 5, size = 10, prob = 0.5)
# P(4 <= k <= 7)
sum(dbinom( x = 4:7, size = 10, prob = 0.5))
k <- 0:10
probability <- dbinom( x = k, size = 10, prob = 0.5)
plot(x = k, y = probability, main = "Probability Distribution Function")
prob <- pbinom (q = k, size = 10, prob = 0.5)
plot( x = k, y = prob, main = "Cumulative Distribution Function")
mean(1:6)
var(1:6)
curve(dnorm(x), xlim = c(-3.5, 3.5), ylab = "Density", xlab = "Standard Normal Distribution")
dnorm(x = c(-1.96, 0, 1.96))
curve(pnorm(x), xlib = c(-3.5, 3.5), ylab = "Probability", main = "Standard Normal Cumulative Distribution Function")
pnorm(1.337)
pnorm(4, mean = 5, sd = 5) - pnorm(3, mean = 5, sd = 5)
curve(dchisq(x, df = 3), xlim = c(0,10), ylim = c(0,1), col = "blue", ylab = "", main = "PDF and CDF of chi square distribution M = 3")
curve(pchisq(x, df = 3), xlim = c(0, 10), add = TRUE, col = "red")
