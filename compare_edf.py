import pyedflib
import pyedflib.highlevel as hl

file1 = 'physionet.org/files/chbmit/1.0.0/chb11/chb11_02.edf'

file2 = 'clean_signals/chb11/chb11_02.edf'

#print(hl.compare_edf(file1, file2, True))

signals_1, signal_headers_1, header_1 = hl.read_edf(file1, digital=True)
signals_2, signal_headers_2, header_2 = hl.read_edf(file2, digital=True)

for sig1, shead1, sig2, shead2 in zip(signals_1,signal_headers_1,signals_2, signal_headers_2):
    dmin1, dmax1 = shead1['digital_min'], shead1['digital_max']
    pmin1, pmax1 = shead1['physical_min'], shead1['physical_max']

    dmin2, dmax2 = shead2['digital_min'], shead2['digital_max']
    pmin2, pmax2 = shead2['physical_min'], shead2['physical_max']
    
    label1 = shead1['label']
    label2 = shead2['label']

    #print("Digital min:", dmin1, dmin2)
    #print("Digital max:", dmax1, dmax2)
    #print("Physical min:", pmin1, pmin2)
    #print("Physical max:", pmax1, pmax2)
    #print("Signal min:", sig1.min(), sig2.min())
    #print("Signal max:", sig1.max(), sig2.max())
    if dmin1 != dmin2: print("Digital min:", dmin1, dmin2) ;print(label1, label2)
    if dmax1 != dmax2: print("Digital max:", dmax1, dmax2) ;print(label1, label2)
    if pmin1 != pmin2: print("Physical min:", pmin1, pmin2) ;print(label1, label2)
    if pmax1 != pmax2: print("Physical max:", pmax1, pmax2) ;print(label1, label2)
    if sig1.min() != sig2.min(): print("Signal min:", sig1.min(), sig2.min() , end='  ') ;print(label1, label2)
    if sig1.max() != sig2.max(): print("Signal max:", sig1.max(), sig2.max() , end='  ') ;print(label1, label2)