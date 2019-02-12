# https://stackoverflow.com/questions/2890703/how-to-join-two-wav-files-using-python

import wave
infiles=["a.wav",'allo.wav',"allo.wav"]
outfile='aallox.wav'

data=[]
for infile in infiles:
	w=wave.open(infile,'rb')
	data.append([w.getparams(),w.readframes(w.getnframes())])
	w.close()
output=wave.open(outfile,"wb")
output.setparams(data[0][0])
output.writeframes(data[0][1])
output.writeframes(data[1][1])
output.close()