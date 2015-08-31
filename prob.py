import collections
import matplotlib.pyplot as plt

x = [1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 3, 4, 4, 4, 4, 5, 6, 6, 6, 7, 7, 7, 7, 7, 7, 7, 7, 8, 8, 9, 9]

plt.figure()
plt.boxplot(x)
plt.savefig("Thinkful_2.2.1.boxplot.png")

plt.figure()
plt.hist(x, histtype='bar')
plt.savefig("Thinkful_2.2.1.histogram.png")

import numpy as np 
import scipy.stats as stats
import matplotlib.pyplot as plt

plt.figure()
graph1 = stats.probplot(x, dist="norm", plot=plt)
plt.savefig("Thinkful_2.2.1.QQplot.png") 

c = collections.Counter(x)

print c

count_sum = sum(c.values())

for k,v in c.iteritems():
  print "The frequency of number " + str(k) + " is " + str(float(v) / count_sum)

