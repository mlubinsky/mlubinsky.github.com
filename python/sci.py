from scipy import stats
import matplotlib
print "config dir=", matplotlib.get_configdir()
matplotlib.use('TkAgg')

import matplotlib.pyplot as plt
generated = stats.norm.rvs(size=5000)
print 'Mean', 'Std', stats.norm.fit(generated)
print 'Skewtest', 'pvalue', stats.skewtest(generated)
print 'Kurtosistest', 'pvalue', stats.kurtosistest(generated)
print 'Normaltest', 'pvalue', stats.normaltest(generated)
print '95 percentile', stats.scoreatpercentile(generated, 95)
print 'Percentile at 1', stats.percentileofscore(generated, 1)

#matplotlib.rcParams['backend'] = 'TkAgg'
#matplotlib.use('agg')
#plt.ion()
plt.hist(generated)
print "BACKEND ", matplotlib.get_backend()
#plt.savefig('foo.png')
plt.show()

