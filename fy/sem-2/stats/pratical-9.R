library(dplyr)

PATH <- "https://raw.githubusercontent.com/guru99-edu/R-Programming/master/poisons.csv"
df <- read.csv(PATH) %>%
select(-X) %>% 
mutate(poison = factor(poison, ordered = TRUE))  
glimpse(df)

levels(df$poison)

df % > %
  group_by(poison) % > %
  summarise(
    count_poison = n(),
    mean_time = mean(time, na.rm = TRUE),
    sd_time = sd(time, na.rm = TRUE)
  )


library(ggplot2)

ggplot(df, aes(x = poison, y = time, fill = poison)) + geom_boxplot() + geom_jitter(shape = 15, color = "steelblue",position = position_jitter(0.21)) + theme_classic()

anova_one_way <- aov(time~poison, data = df)

summary(anova_one_way)

TukeyHSD(anova_one_way)



anova_two_way <- aov(time~poison + treat, data = df)

summary(anova_two_way)
