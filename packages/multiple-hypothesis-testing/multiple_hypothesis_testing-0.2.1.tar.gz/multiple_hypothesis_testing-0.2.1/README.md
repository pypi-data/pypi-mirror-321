# MultiTest -- Global Tests for Multiple Hypothesis

This package is a Python implementation of the global tests for multiple hypothesis testing proposed in [1] and [2].

## News
- Changed the default normalization of ordered P-values when ealuating HC to use the mean and standard deviation of the beta distribution. To get the old behavior, initialize with `normalization = 'donoho-jin2008'`.
- 2024-01-15: Added the `MultiTest.fdr` method for False-discovery rate with optimized rate parameter.
- 2024-01-15: Added the `MultiTest.minp` method for minimal P-values as in Bonferroni style inference.

## The package includes several techniques for multiple hypothesis testing:
- ``MultiTest.hc`` Higher Criticism
- ``MultiTest.hcstar`` Higher Criticism with limited range proposed in [1]
- ``MultiTest.hc_jin`` Higher Criticism with limited range proposed as proposed in [3]
- ``MultiTest.berk_jones`` Berk-Jones statistic
- ``MultiTest.fdr`` False-discovery rate with optimized rate parameter
- ``MultiTest.minp`` Minimal P-values as in Bonferroni style inference
- ``MultiTest.fisher`` Fisher's method to combine P-values
In all cases, one should reject the null for large values of the test statistic.

## Example:
```
import numpy as np
from scipy.stats import norm
from multitest import MultiTest

p = 100
z = np.random.randn(p)
pvals = 2*norm.cdf(-np.abs(z)/2)

mtest = MultiTest(pvals)

hc, p_hct = mtest.hc(gamma = 0.3)
bj = mtest.berk_jones()

ii = np.arange(len(pvals))
print(f"HC = {hc}, Indices of P-values below HCT: {ii[pvals <= p_hct]}")
print(f"Berk-Jones = {bj}")
```

## Use cases: 
This package was used to obtain evaluations reported in [5] and [6].

## References:
[1] Donoho, David. L. and Jin, Jiashun. "Higher criticism for detecting sparse hetrogenous mixtures." The Annals of Statistics 32, no. 3 (2004): 962-994.
[2] Donoho, David L. and Jin, Jiashun. "Higher critcism thresholding: Optimal feature selection when useful features are rare and weak." proceedings of the national academy of sciences, 2008.
[3] Jin, Jiashun, and Wanjie Wang. "Influential features PCA for high dimensional clustering." The Annals of Statistics 44, no. 6 (2016): 2323-2359.
[4] Amit Moscovich, Boaz Nadler, and Clifford Spiegelman. "On the exact Berk-Jones statistics and their p-value calculation." Electronic Journal of Statistics. 10 (2016): 2329-2354.
[5] Donoho, David L., and Alon Kipnis. "Higher criticism to compare two large frequency tables, with sensitivity to possible rare and weak differences." The Annals of Statistics 50, no. 3 (2022): 1447-1472.
[6] Kipnis, Alon. "Unification of rare/weak detection models using moderate deviations analysis and log-chisquared p-values." Statistica Scinica 2025.