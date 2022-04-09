my_data <- PlantGrowth
head(my_data)
kruskal.test(weight ~ group, data = my_data)

pairwise.wilcox.test(PlantGrowth$weight, PlantGrowth$group,p.adjust.method = "BH")

mtcars$mpg
mtcars$am
wilcox.test(mpg ~ am, data=mtcars)

binom.test(5, 18)
