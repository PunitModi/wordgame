from tkinter import*


guesses=" "
turns=8
s=" "
    



def can1():
    global canvas
    canvas.create_rectangle(50,20,170,110,outline="blue",fill="white",width=3)
    canvas.grid(row=15,column=1)

def can2():
    global canvas
    canvas.create_rectangle(170,40,250,110,outline="blue",fill="white",width=3)
    canvas.grid(row=15,column=1)

def can3():
    global canvas
    canvas.create_oval(60,95,90,125,outline="blue",fill="blue",width=2)      # 1st circle
    canvas.grid(row=15,column=1)


def can4():
    global canvas
    canvas.create_oval(160,95,190,125,outline="blue",fill="blue",width=2)  # 2nd circle 
    canvas.grid(row=15,column=1)

def can5():
    global canvas
    canvas.create_rectangle(90,20,120,10,outline="blue",fill="Red",width=3)  #upper side part
    canvas.grid(row=15,column=1)

def can6():
    global canvas
    canvas.create_rectangle(180,50,230,65,outline="blue",fill="white",width=3)  # rectangle in the small rectangle
    canvas.grid(row=15,column=1)

def can7():
    global canvas
    canvas.create_rectangle(95,40,130,55,outline="Red",fill="Red",width=3)   #  for + sigh
    canvas.grid(row=15,column=1)

def can8():
    global canvas
    canvas.create_rectangle(120,30,105,65,outline="Red",fill="Red",width=3)  #  for + sigh
    canvas.grid(row=15,column=1)


def setword():
    global word,master
    word=e1.get()
    word=word.lower()
    word.replace(" ","")
    print("\n\n\n----PLAYER 2 ----\nGuess a letter and write in your entry box and press submit letter BUTTON")
    print("Good Luck ! PLAYER 2")

def logic():
    Label(master,bg="yellow").grid(row=3,column=0) # for space
    Label(master,text="Guess the word:",font="Helvetica 17 italic",bg="yellow",fg="blue").grid(row=4,column=0) # For Heading
    global guesses,turns,s,guess
    failed=0          # count the num  of time user fail
    guess=e2.get() # input the wrong alphabet then  enter another alphabet
    guesses+=guess # every input char in stored in guesses
    
    for i,char in enumerate(word): # all char from the input word taking one at a time 
        if char in guesses:        #comparing that char with the char in guesses
            Label(master,text=char,font="Helvetica 17 italic",bg="yellow",fg="blue").grid(row=i+5,column=0)
        else:
            Label(master,text="*",font="Helvetica 17 italic",bg="yellow",fg="blue").grid(row=i+5,column=0)
            failed +=1    # every failure increment in failure 
    if failed==0:
        Label(master,text="YOU WIN!",font="Helvetica 25 bold",bg="yellow").grid(row=13,column=1)
        Label(master,text="The word is: "+word,bg="yellow").grid(row=14,column=1)# this print the correct word
        

    if guess not in word:   # check input with  the char in word 

        turns -= 1
        Label(master,text="Wrong Guesses : ",font="Helvetica 17 italic",bg="yellow",fg="green").grid(row=17,column=0)
        s=s + " "+guess
        Label(master,text=s,font="Helvetica 17 italic",bg="yellow",fg="green").grid(row=18,column=0)
        Label(master,bg="yellow").grid(row=29,column=0)
        Label(master,bg="yellow").grid(row=30,column=0)
        Label(master,text="you have " + str(turns) + ' attempts left',font="Helvetica 10 italic",bg="yellow").grid(row=31,column=1)
        design()
        
def design():
        if turns==7:
            can1()
        if turns==6:
            can1()
            can2()
        if turns==5:
            can1()
            can2()
            can3()
        if turns==4:
            can1()
            can2()
            can3()
            can4()
        if turns==3:
            can1()
            can2()
            can3()
            can4()
            can5()
        if turns==2:
            can1()
            can2()
            can3()
            can4()
            can5()
            can6()
            
        if turns==1:
            can1()
            can2()
            can3()
            can4()
            can5()
            can6()
            can7()
        if turns==0:
            can1()
            can2()
            can3()
            can4()
            can5()
            can6()
            can7()
            can8()
            Label(master,text="YOU LOSE ! ",font="Helvetica 25 bold",bg="yellow",fg="black").grid(row=13,column=1)
            Label(master,text="The word is: "+word,bg="yellow").grid(row=14,column=1)   # this print the correct word
        if turns==-1:
            master.destroy()
            main()



           
def reset():
     master.destroy()
     
     main()
     

def main():
     global master,e1,e2,canvas
     master=Tk()     # create a GUI window
     master.configure(bg="yellow") # set the background  colour of GUI window
     master.title("Punit's Guess The Word Game") #  set the name of tkinter GUI window
     master.geometry("750x850") # size of GUI window
     canvas=Canvas(master,bg="yellow",bd=2,width=300,height=150)
     
     Label(master,text="PLAYER 1 Entry Box",font="15",bg="yellow",fg="black").grid(row=1,column=0)
     e1=Entry(master)
     e1.grid(row=1,column=1,ipadx="20")
     Button(master,text="Submit Word",bg="red",fg="black",command=setword).grid(row=1,column=2)
     
     Label(master,text="PLAYER 2 Entry Box",font="15",bg="yellow",fg="black").grid(row=2,column=0)
     e2=Entry(master)
     e2.grid(row=2,column=1,ipadx="20")
     Button(master,text="Submit letter",bg="red",fg="black",command=logic).grid(row=2,column=2)

     Button(master,text="RESET",bg="white",fg="red",command=reset).grid(row=32,column=1)

     master.mainloop()    

main()     
