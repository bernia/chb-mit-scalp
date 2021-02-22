# chb-mit-scalp

This repo contains some scripts in order to prepare the data from chb-mit-scalp EEG to use it in classification systems.
The main script is [homogenize_signals.py](homogenize_signals.py) , which converts the signal files (.edf) into compressed picke.
It process the pacients one by one and creates numpy arrays with the same number of channels for each pacient.
In some pacients, there are files without some of the channels that other files have for the same pacient. The script
adds zero arrays for these channels in order to have the same size of data for every pacient.

First, you need to download the data. (Create a directory first. In this case we create 'UC13' dir)
```
mkdir UC13 && cd UC13
wget -r -N -c -np https://physionet.org/files/chbmit/1.0.0/
```

After downloading the data, in order to clean the data you need to run the Python script homogenize_signals.py
The script can run with these depencencies:
- Python >3.8  (It can probably work for older versions, but has not been tested)
- Numpy 1.19.5
- pyEdflib 0.1.20 (You can install it from pip)

Now you can run the script. It will create a directory called "clean_signals" with all the processed signals.
```
python homogenize_signals.py
```
It will last 2-3 hours, depending of the CPU capacity.

If you want to change something, you can edit the script. 
There are some parameters by the end of the file that you can change in order to process the pacients' data manually.
