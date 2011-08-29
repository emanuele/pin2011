import numpy as np
from time import time

def a_b_from_mu_sigma(mu, sigma):
    """Compute the parameters (a, b) of a Beta distribution given
    mu (mean) and sigma (std).
    """
    mu2 = mu*mu
    sigma2 = sigma*sigma
    a = mu*(-mu2 + mu - sigma2)/sigma2
    b = mu * (mu2 - 2*mu + sigma2 + 1) / sigma2 - 1
    return a, b

iterations = 100000
n_subjects = 30
m = 50

t = time()
mu = np.random.uniform(low=0.0, high=1.0, size=iterations)
sigma = np.random.uniform(low=0.0, high=np.sqrt(mu*(1-mu)))
a, b = a_b_from_mu_sigma(mu, sigma)
epsilon = np.random.beta(a=a, b=b, size=(n_subjects, iterations))
e = np.random.binomial(n=m, p=epsilon, size=(n_subjects, iterations))
print "%s subjects, test set of size %s, %s iterations: %s sec." % (n_subjects, m, iterations, time()-t)
