This repo will explore the correlation between the number of languages spoken in a country and gdp in that country. 

## Research Questions

**Questions:**
- Does languages per country correlate with GDP negatively?
- Does it correlate with population?

**Solution:** 
- Use correlation.
- Dataset from kaggle and ethnologue. 

**Why:** Pearson correlation is used to solve this problem.

## Mathematical Foundations

### Variance

Variance measures the spread or dispersion of a dataset around its mean. It quantifies how far individual data points deviate from the average value.

**Population Variance:**
$$\sigma^2 = \frac{1}{N} \sum_{i=1}^{N} (x_i - \mu)^2$$

**Sample Variance:**
$$s^2 = \frac{1}{n-1} \sum_{i=1}^{n} (x_i - \bar{x})^2$$

Where:
- $\sigma^2$ = population variance
- $s^2$ = sample variance  
- $N$ = population size
- $n$ = sample size
- $\mu$ = population mean
- $\bar{x}$ = sample mean
- $x_i$ = individual data point

### Covariance

Covariance measures the degree to which two variables change together. It indicates the direction of the linear relationship between variables.

**Population Covariance:**
$$\sigma_{xy} = \frac{1}{N} \sum_{i=1}^{N} (x_i - \mu_x)(y_i - \mu_y)$$

**Sample Covariance:**
$$s_{xy} = \frac{1}{n-1} \sum_{i=1}^{n} (x_i - \bar{x})(y_i - \bar{y})$$

Where:
- $\sigma_{xy}$ = population covariance
- $s_{xy}$ = sample covariance
- $\mu_x, \mu_y$ = population means of X and Y
- $\bar{x}, \bar{y}$ = sample means of X and Y
- $x_i, y_i$ = individual data points

**Interpretation:**
- Positive covariance: Variables tend to increase together
- Negative covariance: One variable increases as the other decreases
- Zero covariance: No linear relationship

### Correlation

Correlation is a standardized measure of the linear relationship between two variables, ranging from -1 to +1.

**Pearson Correlation Coefficient:**
$$r = \frac{\sum_{i=1}^{n} (x_i - \bar{x})(y_i - \bar{y})}{\sqrt{\sum_{i=1}^{n} (x_i - \bar{x})^2 \sum_{i=1}^{n} (y_i - \bar{y})^2}}$$

**Alternative Formula using Covariance:**
$$r = \frac{s_{xy}}{s_x s_y}$$

Where:
- $r$ = correlation coefficient
- $s_{xy}$ = sample covariance
- $s_x, s_y$ = sample standard deviations of X and Y

**Interpretation:**
- $r = 1$: Perfect positive linear relationship
- $r = -1$: Perfect negative linear relationship  
- $r = 0$: No linear relationship
- $|r| > 0.7$: Strong correlation
- $0.3 < |r| < 0.7$: Moderate correlation
- $|r| < 0.3$: Weak correlation

