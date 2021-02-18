import pyedflib
import numpy as np
import os

#file_name = os.path.join(pyedflib.util.test_data_path(), 'test_generator.edf')
#filename='physionet.org/files/chbmit/1.0.0/chb01/chb01_03.edf'
filename='clean_signals/chb11/chb11_02.edf'
f = pyedflib.EdfReader(filename)
n = f.signals_in_file
signal_labels = f.getSignalLabels()
sigbufs = np.zeros((n, f.getNSamples()[0]))

print('n signals', n)
#print('signal_labels', signal_labels)
for label in signal_labels: print(label)
#print('sigbufs', sigbufs)

#for i in np.arange(n):
#    sigbufs[i, :] = f.readSignal(i)

#print(sigbufs.shape)
#print([x for x in sigbufs.mean(axis=1)])
