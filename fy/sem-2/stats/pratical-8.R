x = rnorm(10)
y = rnorm(10)
t.test(x, y)

ttest = t.test(x, y)
names(ttest)
ttest$statistic
ttest[['statistic']]



pts = seq(-4.5, 4.5, length = 100)
plot(pts, dt(pts, df = 18), col = "red", type = 'l')

lines(density(pts))


t.test(x, y)
t.test(x, y, var.equal = TRUE)


tps = replicate(1000, t.test(rnorm(10), rnorm(10))$p.value)
plot(density(tps))

# != <= >= => <- ||

x <- c(17, 19, 22, 25, 27, 28, 41, 45, 51, 55)
y <- c(14, 15, 15, 17, 18, 22, 25, 25, 27, 34)

var.test(x, y)

data <-
  data.frame(
    values = c(
      18,
      19,
      22,
      25,
      27,
      28,
      41,
      45,
      51,
      55,
      14,
      15,
      15,
      17,
      18,
      22,
      25,
      25,
      27,
      34
    ),
    group = rep(c('A', 'B')),
    each = 10
  )


var.test(values ~ group, data = data)
