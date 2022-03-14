# mean
mean(1:10)
mean(1:6)
mean(1:20)



mean(sample(
  1:6,
  1000,
  replace = T
))

mean(sample(
  1:10,
  10,
  replace = T
))

mean(sample(
  1:50,
  100,
  replace = T
))


# Variance

var(1:10)
var(1:6)
var(1:20)

# Functions

f <- function(x) 3 / x^4
g <- function(x) x * f(x)
h <- function(x) x^2 * f(x)

area <- integrate(f, lower = 2, upper = Inf)
area

EX <- integrate(g, lower = 1, upper = Inf)
EX

VarX <- integrate(h, lower = 1, upper = Inf)
VarX



f <- function(x) 8 / x^2
g <- function(x) x^2 * f(x)
h <- function(x) x^5 * f(x)
f

area <- integrate(f, lower = 2, upper = Inf)
area

EX <- integrate(g, lower = 1, upper = Inf)
EX

VarX <- integrate(h, lower = 1, upper = Inf)
VarX

f <- function(x) 100 / x^8 
g <- function(x) x  * f(x)
h <- function(x) 3*x * f(x)

area <- integrate(f, lower = 2, upper = Inf)
area

EX <- integrate(g, lower = 1, upper = Inf)
EX

VarX <- integrate(h, lower = 1, upper = Inf)
VarX



