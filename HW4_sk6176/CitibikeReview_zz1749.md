## Hi Kim, this is Zhiao commenting on your citi-bike multi-week assignment

### 1. Verify your Null and alternative hypotheses are formulated correctly:
- The null hypothesis is not formulated correctedly as you compared the frequency of women's biking duration with the ratio of men's duration without clearly indicate what the ratio is over. 
- The H0 and H1 are not clearly formulated as well as below: W and M are representing women and men here
# _$H_0$_ : $\frac{W_{\mathrm{man}}}{W_{\mathrm{women}}} <= \frac{M_{\mathrm{}}}{M_{\mathrm{week}}}$
# _$H_1$_ : $\frac{W_{\mathrm{weekend}}}{W_{\mathrm{week}}} > \frac{M_{\mathrm{weekend}}}{M_{\mathrm{week}}}$
- However, I assume that you null hypothesis is: women's ratio of the frequency of a specific segment of duration like (0,300] over the total frequency is the same or higher than that ratio of women.

### 2. Verify that the data supports the project:
- if your null hypothesis is what I assumed above, your data wrangling process: clean the outliner(>0.95) seems to be inapprehensible since the 95% here is the significance level you should use in your hypothesis test later

### 3. Choose an appropriate test to test H0 given the type of data, and the question asked.
- For me, I would choose z-test since you are comparing differences between two sample proportions
- The formula would be:
# $z = \frac{(p_0 - p_1)}{SE} $
# $p =\frac{p_0  n_0 + p_1  n_1}{n_0+n_1}$
# $SE = \sqrt{ p  ( 1 - p )  (\frac{1}{n_0} + \frac{1}{n_1}) }$

# Thank you, wish this could help you! Zhiao