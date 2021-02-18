import os

f = open('physionet.org/files/chbmit/1.0.0/chb01/chb01-summary.txt','r')
channels = []
for line in f:
    line = line.split()
    if len(line) > 0 and line[0]=='Channel':
        channels.append(line[2])

for i in range (2,24):
    number = ('0' + str(i))[-2:]
    filename = 'physionet.org/files/chbmit/1.0.0/chb{n}/chb{n}-summary.txt'.format(n=number)
    f = open(filename,'r')
    index = 0 
    for line in f:
        line = line.split()
        if len(line) > 0 and line[0]=='Channel':
            channel = int(line[1][:-1])
            #print(channel)
            if channel < 24:
                if line[2] != channels[channel-1]:
                    print('Error on file:', filename)
                    print(line[2],"!=", channels[channel-1])