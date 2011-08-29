import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as ss

if __name__ == '__main__':

    error = np.array([43, 59, 51, 38, 39,  53, 47, 50, 50, 59, 59,
                       45, 36, 46, 53], dtype=np.float)
    print "errors:", error

    m = 108

    epsilon = error/m
    print "error rates:", epsilon

    print "t-test:"
    t, p = ss.ttest_1samp(epsilon, 0.5)
    print "t =", t
    print "p-value =", p

    mean = epsilon.mean()
    std = epsilon.std()

    xmin = 0.2
    xmax = 0.7

    x = np.linspace(xmin, xmax, 100)
    pdf = ss.norm.pdf(x, mean, std)
    plt.figure()
    plt.plot(epsilon, np.zeros(epsilon.size), 'kx', markersize=14, markeredgewidth=4)
    plt.plot(x, pdf, 'r-', linewidth=4)
    plt.plot([0.5, 0.5], [-0.4, pdf.max()], 'b--', linewidth=4)
    plt.text(xmax*0.75, pdf.max()*0.9, "$t=2.18$", fontsize=36, color='k')
    plt.text(xmax*0.75, pdf.max()*0.75, "$p=0.014$", fontsize=36, color='r')
    plt.xlim([xmin, xmax])
    plt.ylim([-0.5, 6.5])
    plt.yticks([])
    plt.xticks(size=20)
