from pygame import mixer

caltodo= '4+5'
ans=eval(caltodo)
tex= "{} is answer . ,".format(ans,caltodo)
speakans = gTTS(str(tex))
speakans.save('Aans.mp3')      
print('A')
print("B")
mixer.init()
mixer.music.load('Aans.mp3')
mixer.music.play(0)
