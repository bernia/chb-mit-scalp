import bz2
import pickle
import _pickle as cPickle

# Load any compressed pickle file
def decompress_pickle(file):
    data = bz2.BZ2File(file, 'rb')
    data = cPickle.load(data)
    return data

signal_dict = decompress_pickle('clean_signals/chb04/chb04_28.edf.pkl.pbz2')
print(signal_dict.keys())
print(signal_dict.get('metadata'))
for key in signal_dict.keys():
    print(len(signal_dict.get(key)))
