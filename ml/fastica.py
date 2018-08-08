#   http://tetraquark.ru/archives/311
#    Testing of FastICA algorithm from sklearn library.
#    Author: tetraquark | tetraquark.ru
#    Article URL (RUS language): http://tetraquark.ru/archives/311
#
import warnings
warnings.filterwarnings(action='ignore')

import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import FastICA

# Length of the sources signals
n_samples = 1024
time = np.linspace(0, 8, n_samples)

# Signal 1 : sinusoidal signal
signal_1 = np.sin(6 * time)
# add noise to signal 1
signal_1 += 0.2 * np.random.normal(size=signal_1.shape)
# Signal 2 : square signal
signal_2 = np.sign(np.sin(4 * time))
# add noise to signal 2
signal_2 += 0.2 * np.random.normal(size=signal_2.shape)

# Plot the sources signals
plt.figure()
plt.grid()
axes = plt.gca()
axes.set_xlim([0, n_samples])
plt.title("Source signals")
plt.plot(signal_1)
plt.plot(signal_2)

# Create a mixtures from two sources
mix = []
mix.append(signal_1)
mix.append(signal_2)
mix = np.array(mix)
mix = np.dot(mix.T, np.array([[1, 2], [2, 1]]).T)

# Plot the mixtures signals
plt.figure()
plt.grid()
plt.title("Mixtures")
axes = plt.gca()
axes.set_xlim([0, n_samples])
plt.plot(mix)

# Create a FastICA object
ica = FastICA(n_components=2)
# Apply FastICA method and get the independent components matrix S_1
S_1 = ica.fit_transform(mix)
# Copy independent components matrix
S_2 = np.copy(S_1)

# Plot the independent components
plt.figure()
plt.grid()
plt.title("Independent components")
axes = plt.gca()
axes.set_xlim([0, n_samples])
plt.plot(S_1)

# Nullify independent components of signal 1 and signal 2
for i in range(len(S_1)):
    S_1[i][0] = 0
    S_2[i][1] = 0

# Restore the sources signals from the independent components matrix (X = S * A)
# S - matrix of independent components
# A - mixing matrix
restored_signal_1 = np.dot(S_1, ica.mixing_)
restored_signal_2 = np.dot(S_2, ica.mixing_)

# Nullify signal 2 values from signal 1 array and vice versa
for i in range(len(restored_signal_1)):
    restored_signal_1[i][0] = 0
    restored_signal_2[i][1] = 0

# Plot the restored signals
plt.figure()
plt.grid()
plt.title("Restored signals")
axes = plt.gca()
axes.set_xlim([0, n_samples])
plt.plot(restored_signal_1)
plt.plot(restored_signal_2)
plt.show()

