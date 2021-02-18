import os
import pyedflib
import pyedflib.highlevel as hl


#filename = 'clean_signals/chb11/chb11_02_permuted.edf'
filename = 'physionet.org/files/chbmit/1.0.0/chb12/chb12_06.edf'
# Read signal file
signals, signal_headers, header = hl.read_edf(filename, digital=False)
print('Signals in file: ',filename.split('/')[-1], ': ', len(signals))
print('Channel names:')
n = 1
for h in signal_headers:
    print('Channel ', n, ': ', h.get('label'), sep='')
    n = n + 1

