audio1=open("allo.mp3","rb").read()
audio2=open("allo.mp3","rb").read()
audio3=open("byu.mp3","rb").read()
audiojoin=audio2+audio1+audio3
audioFinal=open("audiofinal.mp3",'wb').write(audiojoin)
