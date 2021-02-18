f = open('physionet.org/files/chbmit/1.0.0/chb16/chb16-summary.txt','r')


changes = 0
channels = {}
for line in f:
    line = line.split()
    if len(line) == 0 : continue
    if line[0] == 'Channels': changes += 1 
    if len(line) > 0 and line[0]=='Channel':
        if channels.get(line[2]) is None: channels[line[2]] = 1
        else: channels[line[2]]= channels.get(line[2]) + 1

print("CHANGES:", changes)
for item in channels.items(): print(item)