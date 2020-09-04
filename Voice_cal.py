from tkinter import *
import speech_recognition as sr
from gtts import gTTS
import time
import random
from pygame import mixer




class Main:
    def __init__(self,mat):
        self.mat = mat
        self.textcalc = ""
        self.sat = StringVar()
        self.em = StringVar()
        self.text1 = StringVar()
        self.text2 = StringVar()
        self.text3 = StringVar()
        self.texti=''
        self.num1=''
        self.num2=''
        self.a='Click Mic icon and Speak'
        self.b=''
        self.text1.set(self.a)
        self.text2.set(self.b)
        self.fetch = {('add','addition','plus', '+','sum','summation'): '+',
                 ('subtraction','minus','subduction', '-','diminution','reduce'): '-',
                 ('multiply','into','multiplication', '*','cross'): '*',
                 ('division','divide','/', 'upon'): '/',
                 ('modulus','mod'): '%'}
        c=''
        for x in range(6):
            c=c+str(random.choice('0123456789abcdef'))
        self.colr='#'+str(c)
            
            

        self.dell=  PhotoImage(file='dell.png', height=38, width=42)
        self.mic =  PhotoImage(file='mic.png',height=30, width=30)
        self.micb=  PhotoImage(file='micb.png',height=150, width=200)
        self.right= PhotoImage(file='right.png',height=50, width=50)
        self.reset= PhotoImage(file='reset.png',height=50, width=50)
        self.close= PhotoImage(file='close.png',height=18, width=18)
               
        
        self.manualcal()
 # ==================== Images ===========================================================
      
        
        
 


# ========================== fun Manual Calcu ============================================       
    def manualcal(self):
        self.mainframe = Frame(self.mat, bg='#000')
        self.mainframe.pack(fill=BOTH)
        
        self.anw = Frame(self.mainframe,bg='black')
        self.anw.pack()
        self.ans = Frame(self.anw,bg='black')
        self.ans.pack()
        self.voicecalc = Label(self.ans, justify='right', font=('Poppins',20,'bold'), bg='black', fg='white', bd=0)
        self.voicecalc.pack(anchor=NE, ipady=12)
        self.speakbutton = Button(self.voicecalc, image=self.mic,bg='black', bd=0, command= lambda: self.voicecal(),justify='right')
        self.speakbutton.pack(anchor=NE)
        
        
        self.hist= Entry(self.ans, textvariable=self.em, justify='right',font=('Poppins',23,'bold'), bg='black', fg='#b7b8b8', bd=0)
        self.hist.pack(ipady=5) 
        self.display = Entry(self.ans, textvariable=self.sat, justify='right',font=('Poppins' ,35,'bold'), bg='black', fg='white', bd=0)
        self.display.pack(ipady=5)


        self.normalcal=Frame(self.anw,bg='black')
        self.normalcal.pack()
        
        
        self.onelab = Button(self.normalcal, text='1', font=('Poppins',24,'bold'), bg='black', bd=0, fg=self.colr, command=lambda : self.dis(1))
        self.onelab.grid(row=2,column=0, ipadx=6, ipady=7)
        self.twolab = Button(self.normalcal, text='2', font=('Poppins',24,'bold'), bg='black', bd=0, fg=self.colr, command=lambda : self.dis(2))
        self.twolab.grid(row=2,column=1, ipadx=6, ipady=7)
        self.threelab = Button(self.normalcal,  text='3', font=('Poppins',24,'bold'), bg='black', bd=0, fg=self.colr, command=lambda : self.dis(3))
        self.threelab.grid(row=2,column=2, ipadx=6, ipady=7)
        self.fourlab = Button(self.normalcal,  text='4', font=('Poppins',24,'bold'), bg='black', bd=0, fg=self.colr, command=lambda : self.dis(4))
        self.fourlab.grid(row=1,column=0, ipadx=6, ipady=7)
        self.fivelab = Button(self.normalcal,  text='5', font=('Poppins',24,'bold'), bg='black', bd=0, fg=self.colr, command=lambda : self.dis(5))
        self.fivelab.grid(row=1,column=1, ipadx=6, ipady=7)
        self.sixlab = Button(self.normalcal,  text='6', font=('Poppins',24,'bold'), bg='black', bd=0, fg=self.colr, command=lambda : self.dis(6))
        self.sixlab.grid(row=1,column=2, ipadx=6, ipady=7)
        self.sevenlab = Button(self.normalcal, text='7', font=('Poppins',24,'bold'), bg='black', bd=0, fg=self.colr, command=lambda : self.dis(7))
        self.sevenlab.grid(row=0,column=0, ipadx=6, ipady=7)
        self.eightlab = Button(self.normalcal,  text='8', font=('Poppins',24,'bold'), bg='black', bd=0, fg=self.colr, command=lambda : self.dis(8))
        self.eightlab.grid(row=0,column=1, ipadx=6, ipady=7)
        self.ninelab = Button(self.normalcal,  text='9', font=('Poppins',24,'bold'), bg='black', bd=0, fg=self.colr, command=lambda : self.dis(9))
        self.ninelab.grid(row=0,column=2, ipadx=6, ipady=7)
        self.dotlab = Button(self.normalcal,  text='.', font=('Poppins',24,'bold'), bg='black', bd=0, fg=self.colr, command=lambda : self.dis("."))
        self.dotlab.grid(row=3,column=0, ipadx=6, ipady=7)
        self.zerolab = Button(self.normalcal,  text='0', font=('Poppins',24,'bold'), bg='black', bd=0, fg=self.colr, command=lambda : self.dis(0))
        self.zerolab.grid(row=3,column=1, ipadx=6, ipady=7)
        self.clearlab = Button(self.normalcal,  text='c', font=('Poppins',24,'bold'), bg='black', bd=0, fg=self.colr, command=lambda : self.clear())
        self.clearlab.grid(row=3,column=2, ipadx=6, ipady=7)
        
        
        #====================================================================================================================================
        self.mullab = Button(self.normalcal, text='x', font=('Poppins',24,'bold'), bg='black', bd=0, fg=self.colr, command=lambda : self.dis('x'))
        self.mullab.grid(row=2,column=3, ipadx=6, ipady=7)
        self.divlab = Button(self.normalcal, text='/', font=('Poppins',24,'bold'), bg='black', bd=0, fg=self.colr, command=lambda : self.dis('/'))
        self.divlab.grid(row=2,column=4, ipadx=6, ipady=7)
        self.sublab = Button(self.normalcal, text='-', font=('Poppins',24,'bold'), bg='black', bd=0, fg=self.colr, command=lambda : self.dis('-'))
        self.sublab.grid(row=1,column=4, ipadx=6, ipady=7)
        self.addlab = Button(self.normalcal, text='+', font=('Poppins',24,'bold'), bg='black', bd=0, fg=self.colr, command=lambda : self.dis('+'))
        self.addlab.grid(row=1,column=3, ipadx=6, ipady=7)
        self.perlab = Button(self.normalcal, text='%', font=('Poppins',24,'bold'), bg='black', bd=0, fg=self.colr, command=lambda : self.dis('%'))
        self.perlab.grid(row=0,column=3, ipadx=6, ipady=7)
        self.dellab = Button(self.normalcal, image=self.dell,font=('Poppins',24,'bold'), bg='black', bd=0, command=lambda : self.delfun())
        self.dellab.grid(row=0,column=4, ipadx=6, ipady=7, sticky=E)
        self.equallab = Button(self.normalcal, text='=', font=('Poppins',24,'bold'), bg='black', bd=0, fg=self.colr, command=lambda : self.calcu())
        self.equallab.grid(row=3,column=3, ipadx=28,ipady=10,columnspan=2)




    def dis(self,n):
        self.textcalc
        if str(n) in '+-x/%':
            if len(self.textcalc)==0:
                self.textcalc = self.textcalc + str(n)
            elif str(n)=='-':
                if self.textcalc[-2] in '+-x/%' and self.textcalc[-1] in '+-x/%':
                    self.textcalc = self.textcalc[:-1]+str(n)
                else:
                    self.textcalc = self.textcalc + str(n)
            else:
                if (self.textcalc[-1] in '+-x/%' and self.textcalc[-2] in '+-x/%'):
                    self.textcalc = self.textcalc[:-2]+str(n)
                elif self.textcalc[-1] in '+-x/%':
                    self.textcalc = self.textcalc[:-1]+str(n)
                else:
                    self.textcalc = self.textcalc + str(n)                   
        else:
            self.textcalc = self.textcalc + str(n)
        self.sat.set(self.textcalc)
    
    def clear(self):
        self.textcalc
        self.textcalc = ''
        self.em.set(self.textcalc)
        self.sat.set(self.textcalc)
    
    def delfun(self):
        self.textcalc
        self.textcalc = self.textcalc[:-1]
        self.sat.set(self.textcalc)
        
    def calcu(self):
        self.textcalc
        self.em.set(self.textcalc)
        self.textcalc = self.textcalc.replace('x','*')
        self.calculation = str(eval(self.textcalc))
        self.sat.set(self.calculation)
        self.textcalc = self.calculation
    






#====================================== Speaking Calc ===============================================================================

    def voicecal(self):
        self.anw.destroy()
        self.voi = Frame(self.mainframe, bg='#000')
        self.voi.pack(fill=BOTH)

        self.speakc = Frame(self.voi,bg='black')
        self.speakc.pack()
        
        self.closebut = Button(self.speakc, text='x', bg='black', bd=0,fg=self.colr,font=('Poppins',15,'bold'), command=lambda : self.closefun())
        self.closebut.grid(row=0,column=0, ipadx=0,ipady=0,columnspan=2, sticky= NE)
        self.micbbut = Button(self.speakc, image=self.micb, bg='black', bd=0,command = lambda: self.speaker())
        self.micbbut.grid(row=1,column=0, ipadx=40,ipady=58,columnspan=2)
  
      
        self.dislab = Entry(self.speakc, textvariable=self.text1, insertwidth=50,font=('Poppins',10,'bold'), bg='black', fg='white', bd=0, width=40,  justify='center')
        self.dislab.grid(row=2,column=0, ipadx=3,ipady=5,columnspan=2)
        self.dislab1 = Entry(self.speakc, textvariable=self.text2, insertwidth=50,font=('Poppins',8,'bold'), bg='black', fg='white', bd=0, width=40, justify='center')
        self.dislab1.grid(row=3,column=0, ipadx=3,ipady=1,columnspan=2)
        self.dislab2 = Entry(self.speakc, textvariable=self.text3, insertwidth=50,font=('Poppins',8,'bold'), bg='black', fg='white', bd=0, width=40, justify='center')
        self.dislab2.grid(row=4,column=0, ipadx=3,ipady=1,columnspan=2) 

        
        self.resetbut = Button(self.speakc, image=self.reset,bg='black', bd=0,command= lambda: self.speaker())
        self.resetbut.grid(row=5,column=0, ipadx=0,ipady=30)
        self.rightbut = Button(self.speakc, image=self.right,bg='black', bd=0, command= lambda: self.rightclick())
        self.rightbut.grid(row=5,column=1, ipadx=0,ipady=30)
        
        
        
    def speaker(self):
        r= sr.Recognizer()
        with sr.Microphone(device_index=1) as source:
            print("Speak: ")
            audio = r.listen(source)
            try:
                self.texta = r.recognize_google(audio)
                self.text1.set(self.texta)
                self.text2.set('If this is what you spoke,')
                self.text3.set('click Right else click Reset')
            except:
                self.texta = "Sorry, click reset button to speak again"
                self.text2.set('')
                self.text3.set('')
                self.text1.set(self.texta)
    
    def rightclick(self):
        self.key = self.texta.split(' ')
        for x in self.key:
            for j in self.fetch.keys():
                if x in j:
                    self.oper=self.fetch[j]
                elif x[0] in '0123456789' and len(self.num1)==0:
                    self.num1=x
                    break
                elif x[0] in '0123456789' and len(self.num1)!=0 and len(self.num2)==0:
                    self.num2=x
                    break 
        self.caltodo= self.num1 + self.oper + self.num2
        self.ans=eval(self.caltodo)
        self.tex= "Your answer for {1} is {0}".format(self.ans,self.caltodo)
        self.speakans = gTTS(str(self.tex))
        self.speakans.save('Aans.mp3')      
        self.text1.set(self.ans)
        self.text2.set('')
        self.text3.set('')
        mixer.init()
        mixer.music.load('Aans.mp3')
        mixer.music.play(0)

    def closefun(self):
        self.mainframe.destroy()       
        self.textcalc = ""
        self.sat = StringVar()
        self.em = StringVar()
        self.text1 = StringVar()
        self.text2 = StringVar()
        self.text3 = StringVar()
        self.texti=''
        self.num1=''
        self.num2=''
        self.a='Click Mic icon and Speak'
        self.b=''
        self.text1.set(self.a)
        self.text2.set(self.b)
        self.manualcal()






if __name__=='__main__':
    window = Tk()
    window.title('Calculator')
    window.geometry('288x475') 
    Main(window)
    window.mainloop()






'''    self.one=   PhotoImage(file='1.png', height=50, width=50)
        self.two=   PhotoImage(file='2.png', height=50, width=50)
        self.three= PhotoImage(file='3.png', height=50, width=50)
        self.four=  PhotoImage(file='4.png', height=50, width=50)
        self.five=  PhotoImage(file='5.png', height=50, width=50)
        self.six=   PhotoImage(file='6.png', height=50, width=50)
        self.seven= PhotoImage(file='7.png', height=50, width=50)
        self.eight= PhotoImage(file='8.png', height=50, width=50)
        self.nine=  PhotoImage(file='9.png', height=50, width=50)
        self.zero=  PhotoImage(file='0.png', height=50, width=50)
        self.dot=   PhotoImage(file='dot.png', height=50, width=50)
        
        self.add=   PhotoImage(file='+.png', height=50, width=50)
        self.sub=   PhotoImage(file='-.png', height=50, width=50)
        self.mul=   PhotoImage(file='x.png', height=50, width=50)
        self.div=   PhotoImage(file='div.png', height=50, width=50)
        self.per=   PhotoImage(file='%.png', height=50, width=50)
        
        self.equal= PhotoImage(file='=.png', height=50, width=50)
        self.c=     PhotoImage(file='c.png', height=50, width=50)
'''  




