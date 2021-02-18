import pyedflib
import numpy
import os

#file_name = os.path.join(pyedflib.util.test_data_path(), 'test_generator.edf')
#filename='physionet.org/files/chbmit/1.0.0/chb01/chb01_03.edf'
filename = 'clean_signals/chb11/chb11_02.edf'
f = pyedflib.EdfReader(filename)
n = f.signals_in_file
signal_labels = f.getSignalLabels()
sigbufs = numpy.zeros((n, f.getNSamples()[0]))

for i in numpy.arange(n):
    sigbufs[i, :] = f.readSignal(i)

csv_filename = filename.replace(".edf", ".csv")
print(csv_filename)
if csv_filename == filename:
    raise Exception('Impossible to replace file extension')

header = ';'.join(signal_labels)
print(header)
numpy.savetxt(csv_filename, sigbufs.T, delimiter=';', header=header)
