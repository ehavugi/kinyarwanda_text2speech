import sys
import re
import os
from playsound import playsound
import time
def decompose(word):
	amajwi=r'(o|u|i|e|a|ba|bu|be|bi|bo|ca|cu|ce|ci|co|da|du|de|di|do|fa|fu|fe|fi|fo|ga|gu|ge|gi|go|ha|hu|he|hi|ho|ja|ju|je|ji|jo|ka|ku|ke|ki|ko|la|lu|le|li|lo|ma|mu|me|mi|mo|na|nu|ne|ni|no|pa|pu|pe|pi|po|ra|ru|re|ri|ro|sa|su|se|si|so|ta|tu|te|ti|to|qa|qu|qe|qi|qo|wa|wu|we|wi|wo|va|vu|ve|vi|vo|ya|yu|ye|yi|yo|za|zu|ze|zi|zo|nya|nyu|nye|nyi|nyo|sha|shu|she|shi|sho|pfa|pfu|pfe|pfi|pfo|tsa|tsu|tse|tsi|tso|mba|mbu|mbe|mbi|mbo|mfa|mfu|mfe|mfi|mfo|mpa|mpu|mpe|mpi|mpo|nda|ndu|nde|ndi|ndo|nga|ngu|nge|ngi|ngo|nka|nku|nke|nki|nko|nsa|nsu|nse|nsi|nso|nsha|nshu|nshe|nshi|nsho|nshya|nshyu|nshye|nshyi|nshyo|nta|ntu|nte|nti|nto|nta|ntu|nte|nti|nto|nza|nzu|nze|nzi|nzo|bwa|bwu|bwe|bwi|bwo|bga|bgu|bge|bgi|bgo|cwa|cwu|cwe|cwi|cwo|dwa|dwu|dwe|dwi|dwo|fwa|fwu|fwe|fwi|fwo|gwa|gwu|gwe|gwi|gwo|hwa|hwu|hwe|hwi|hwo|jwa|jwu|jwe|jwi|jwo|kwa|kwu|kwe|kwi|kwo|mwa|mwu|mwe|mwi|mwo|nwa|nwu|nwe|nwi|nwo|nywa|nywu|nywe|nywi|nywo|pfwa|pfwu|pfwe|pfwi|pfwo|pwa|pwu|pwe|pwi|pwo|rwa|rwu|rwe|rwi|rwo|shwa|shwu|shwe|shwi|shwo|shywa|shywu|shywe|shywi|shywo|swa|swu|swe|swi|swo|tswa|tswu|tswe|tswi|tswo|twa|twu|twe|twi|two|vwa|vwu|vwe|vwi|vwo|zwa|zwu|zwe|zwi|zwo|bya|byu|bye|byi|byo|cya|cyu|cye|cyi|cyo|jya|jyu|jye|jyi|jyo|mya|myu|mye|myi|myo|nnya|nnyu|nnye|nnyi|nnyo|pfya|pfyu|pfye|pfyi|pfyo|pya|pyu|pye|pyi|pyo|rya|ryu|rye|ryi|ryo|sya|syu|sye|syi|syo|tya|tyu|tye|tyi|tyo|vya|vyu|vye|vyi|vyo|bywa|bywu|bywe|bywi|bywo|mywa|mywu|mywe|mywi|mywo|pfywa|pfywu|pfywe|pfywi|pfywo|rywa|rywu|rywe|rywi|rywo|vywa|vywu|vywe|vywi|vywo|mbwa|mbwu|mbwe|mbwi|mbwo|mfwa|mfwu|mfwe|mfwi|mfwo|mpwa|mpwu|mpwe|mpwi|mpwo|mvwa|mvwu|mvwe|mvwi|mvwo|ndwa|ndwu|ndwe|ndwi|ndwo|ngwa|ngwu|ngwe|ngwi|ngwo|njwa|njwu|njwe|njwi|njwo|nkwa|nkwu|nkwe|nkwi|nkwo|nkwa|nkwu|nkwe|nkwi|nkwo|nshwa|nshwu|nshwe|nshwi|nshwo|nshywa|nshywu|nshywe|nshywi|nshywo|nswa|nswu|nswe|nswi|nswo|ntwa|ntwu|ntwe|ntwi|ntwo|nzwa|nzwu|nzwe|nzwi|nzwo|ntwa|ntwu|ntwe|ntwi|ntwo|nzwa|nzwu|nzwe|nzwi|nzwo|mbya|mbyu|mbye|mbyi|mbyo|mpya|mpyu|mpye|mpyi|mpyo|mvya|mvyu|mvye|mvyi|mvyo|ncya|ncyu|ncye|ncyi|ncyo|ndya|ndyu|ndye|ndyi|ndyo|njya|njyu|njye|njyi|njyo|nsya|nsyu|nsye|nsyi|nsyo|ntya|ntyu|ntye|ntyi|ntyo|mbywa|mbywu|mbywe|mbywi|mbywo|mvywa|mvywu|mvywe|mvywi|mvywo|njywa|njywu|njywe|njywi|njywo)'
	m=re.findall(r'(o|u|i|e|a|ba|bu|be|bi|bo|ca|cu|ce|ci|co|da|du|de|di|do|fa|fu|fe|fi|fo|ga|gu|ge|gi|go|ha|hu|he|hi|ho|ja|ju|je|ji|jo|ka|ku|ke|ki|ko|la|lu|le|li|lo|ma|mu|me|mi|mo|na|nu|ne|ni|no|pa|pu|pe|pi|po|ra|ru|re|ri|ro|sa|su|se|si|so|ta|tu|te|ti|to|qa|qu|qe|qi|qo|wa|wu|we|wi|wo|va|vu|ve|vi|vo|ya|yu|ye|yi|yo|za|zu|ze|zi|zo|nya|nyu|nye|nyi|nyo|sha|shu|she|shi|sho|pfa|pfu|pfe|pfi|pfo|tsa|tsu|tse|tsi|tso|mba|mbu|mbe|mbi|mbo|mfa|mfu|mfe|mfi|mfo|mpa|mpu|mpe|mpi|mpo|nda|ndu|nde|ndi|ndo|nga|ngu|nge|ngi|ngo|nka|nku|nke|nki|nko|nsa|nsu|nse|nsi|nso|nsha|nshu|nshe|nshi|nsho|nshya|nshyu|nshye|nshyi|nshyo|nta|ntu|nte|nti|nto|nta|ntu|nte|nti|nto|nza|nzu|nze|nzi|nzo|bwa|bwu|bwe|bwi|bwo|bga|bgu|bge|bgi|bgo|cwa|cwu|cwe|cwi|cwo|dwa|dwu|dwe|dwi|dwo|fwa|fwu|fwe|fwi|fwo|gwa|gwu|gwe|gwi|gwo|hwa|hwu|hwe|hwi|hwo|jwa|jwu|jwe|jwi|jwo|kwa|kwu|kwe|kwi|kwo|mwa|mwu|mwe|mwi|mwo|nwa|nwu|nwe|nwi|nwo|nywa|nywu|nywe|nywi|nywo|pfwa|pfwu|pfwe|pfwi|pfwo|pwa|pwu|pwe|pwi|pwo|rwa|rwu|rwe|rwi|rwo|shwa|shwu|shwe|shwi|shwo|shywa|shywu|shywe|shywi|shywo|swa|swu|swe|swi|swo|tswa|tswu|tswe|tswi|tswo|twa|twu|twe|twi|two|vwa|vwu|vwe|vwi|vwo|zwa|zwu|zwe|zwi|zwo|bya|byu|bye|byi|byo|cya|cyu|cye|cyi|cyo|jya|jyu|jye|jyi|jyo|mya|myu|mye|myi|myo|nnya|nnyu|nnye|nnyi|nnyo|pfya|pfyu|pfye|pfyi|pfyo|pya|pyu|pye|pyi|pyo|rya|ryu|rye|ryi|ryo|sya|syu|sye|syi|syo|tya|tyu|tye|tyi|tyo|vya|vyu|vye|vyi|vyo|bywa|bywu|bywe|bywi|bywo|mywa|mywu|mywe|mywi|mywo|pfywa|pfywu|pfywe|pfywi|pfywo|rywa|rywu|rywe|rywi|rywo|vywa|vywu|vywe|vywi|vywo|mbwa|mbwu|mbwe|mbwi|mbwo|mfwa|mfwu|mfwe|mfwi|mfwo|mpwa|mpwu|mpwe|mpwi|mpwo|mvwa|mvwu|mvwe|mvwi|mvwo|ndwa|ndwu|ndwe|ndwi|ndwo|ngwa|ngwu|ngwe|ngwi|ngwo|njwa|njwu|njwe|njwi|njwo|nkwa|nkwu|nkwe|nkwi|nkwo|nkwa|nkwu|nkwe|nkwi|nkwo|nshwa|nshwu|nshwe|nshwi|nshwo|nshywa|nshywu|nshywe|nshywi|nshywo|nswa|nswu|nswe|nswi|nswo|ntwa|ntwu|ntwe|ntwi|ntwo|nzwa|nzwu|nzwe|nzwi|nzwo|ntwa|ntwu|ntwe|ntwi|ntwo|nzwa|nzwu|nzwe|nzwi|nzwo|mbya|mbyu|mbye|mbyi|mbyo|mpya|mpyu|mpye|mpyi|mpyo|mvya|mvyu|mvye|mvyi|mvyo|ncya|ncyu|ncye|ncyi|ncyo|ndya|ndyu|ndye|ndyi|ndyo|njya|njyu|njye|njyi|njyo|nsya|nsyu|nsye|nsyi|nsyo|ntya|ntyu|ntye|ntyi|ntyo|mbywa|mbywu|mbywe|mbywi|mbywo|mvywa|mvywu|mvywe|mvywi|mvywo|njywa|njywu|njywe|njywi|njywo)',word)
	return m

dir_path = os.path.dirname(os.path.realpath(__file__))

if __name__=="__main__":
	if len(sys.argv)>1:
		text=" ".join(sys.argv[1:])
		available=[]
		unavailable=[]
		components=decompose(text.lower())
		for x in components:
			filename=dir_path+"/voices1/"+x+".mp3"

			try:
				handle=open(filename,"rb")
				available.append(handle)
			except:
				print("unavailable word/combination")
				unavailable.append(filename)
		print("components",components)
		# print("available",available)
		print("unavailable",unavailable)
		for i in available:
			try:
				audiojoin+=i.read()
			except:
				audiojoin=i.read()
		print("hello starting")
		audioFinal=open("lastvoice.mp3",'wb').write(audiojoin)
		print("made audio")
		Played=False
		try:
			print("try playing")
			# p = vlc.MediaPlayer("lastvoice.mp3")
			# p.play()
			# time.sleep(10)
			playsound('lastvoice.mp3')
			# p.stop()
		except:
			print("couldn't play")
			pass
		
		
