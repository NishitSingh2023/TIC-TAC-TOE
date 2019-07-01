from turtle import *
class game:
    check={'7':[False,None],'8':[False,None],'9':[False,None],'4':[False,None],'5':[False,None],'6':[False,None],'1':[False,None],'2':[False,None],'3':[False,None]}
    def check_plots(self):
        g=True
        p=u=0
        for q in self.check:
            if self.check[q]==[g,'user']:
                u=u+1
            elif self.check[q]==[g,'pc']:
                p=p+1
        return (u,p)
    def lock(self,x,person):
        for i in self.check:
            if i==x:
                self.check[i][0]=True
                self.check[i][1]=person
                break
    def check_avail(self,x):
        if self.check[x][0]==False:
            return True
        else:
            return False
    def putin(self,x):
        if x=='7':
            penup()
            goto(50,30)
            pendown()
            circle(25)
            return True
        elif x=='8':
            penup()
            goto(115,30)
            pendown()
            circle(25)
            return True
        elif x=='9':
            penup()
            goto(175,30)
            pendown()
            circle(25)
            return True
        elif x=='4':
            penup()
            goto(50,-30)
            pendown()
            circle(25)
            return True
        elif x=='5':
            penup()
            goto(115,-30)
            pendown()
            circle(25)
            return True
        elif x=='6':
            penup()
            goto(175,-30)
            pendown()
            circle(25)
            return True
        elif x=='1':
            penup()
            goto(50,-90)
            pendown()
            circle(25)
            return True
        elif x=='2':
            penup()
            goto(115,-90)
            pendown()
            circle(25)
            return True
        elif x=='3':
            penup()
            goto(175,-90)
            pendown()
            circle(25)
            return True
    def draw(self,x,person):
        if self.check_avail(x):
            self.lock(x,person)
            return self.putin(x)
    def cons(self,a,b,c,v):
        if self.check[a]==v and self.check[b]==v:
            return self.draw(c,'pc')
    def res(self,per):
        c=[True,per]
        if self.check['7']==c and self.check['4']==c and self.check['1']==c:
            penup()
            goto(30,60)
            pendown()
            goto(30,-120)
            return False
        elif self.check['7']==c and self.check['8']==c and self.check['9']==c:
            penup()
            goto(0,30)
            pendown()
            goto(180,30)
            return False
        elif self.check['7']==c and self.check['5']==c and self.check['3']==c:
            penup()
            goto(0,60)
            pendown()
            goto(180,-120)
            return False
        elif self.check['9']==c and self.check['5']==c and self.check['1']==c:
            penup()
            goto(180,60)
            pendown()
            goto(0,-120)
            return False
        elif self.check['9']==c and self.check['6']==c and self.check['3']==c:
            penup()
            goto(120,60)
            pendown()
            goto(120,-120)
            return False
        elif self.check['1']==c and self.check['2']==c and self.check['3']==c:
            penup()
            goto(0,-90)
            pendown()
            goto(180,-90)
            return False
        elif self.check['4']==c and self.check['5']==c and self.check['6']==c:
            penup()
            goto(0,-30)
            pendown()
            goto(180,-30)
            return False
        elif self.check['8']==c and self.check['5']==c and self.check['2']==c:
            penup()
            goto(90,60)
            pendown()
            goto(90,-120)
            return False
        else:
            return True
    def win(self):
        v=[True,'pc']
        begin_fill()
        fillcolor('black')
        if self.cons('7','9','8',v):
            end_fill()
            return True
        elif self.cons('7','1','4',v):
            end_fill()
            return True
        elif self.cons('7','3','5',v):
            end_fill()
            return True
        elif self.cons('1','3','2',v):
            end_fill()
            return True
        elif self.cons('9','3','6',v):
            end_fill()
            return True
        elif self.cons('9','1','5',v):
            end_fill()
            return True
        elif self.cons('4','6','5',v):
            end_fill()
            return True
        elif self.cons('8','2','5',v):
            end_fill()
            return True
        elif self.cons('7','8','9',v):
            end_fill()
            return True
        elif self.cons('8','9','7',v):
            end_fill()
            return True
        elif self.cons('9','6','3',v):
            end_fill()
            return True
        elif self.cons('6','3','9',v):
            end_fill()
            return True
        elif self.cons('2','3','1',v):
            end_fill()
            return True
        elif self.cons('1','2','3',v):
            end_fill()
            return True
        elif self.cons('1','4','7',v):
            end_fill()
            return True
        elif self.cons('7','4','1',v):
            end_fill()
            return True
        elif self.cons('7','5','3',v):
            end_fill()
            return True
        elif self.cons('5','3','7',v):
            end_fill()
            return True
        elif self.cons('9','5','1',v):
            end_fill()
            return True
        elif self.cons('5','1','9',v):
            end_fill()
            return True
        elif self.cons('4','5','6',v):
            end_fill()
            return True
        elif self.cons('5','6','4',v):
            end_fill()
            return True
        elif self.cons('8','5','2',v):
            end_fill()
            return True
        elif self.cons('5','2','8',v):
            end_fill()
            return True
        else:
            end_fill()
            return False
    def defend(self):
        v=[True,'user']
        begin_fill()
        fillcolor('black')
        if self.cons('7','9','8',v):
            end_fill()
            return True
        elif self.cons('7','1','4',v):
            end_fill()
            return True
        elif self.cons('7','3','5',v):
            end_fill()
            return True
        elif self.cons('1','3','2',v):
            end_fill()
            return True
        elif self.cons('9','3','6',v):
            end_fill()
            return True
        elif self.cons('9','1','5',v):
            end_fill()
            return True
        elif self.cons('4','6','5',v):
            end_fill()
            return True
        elif self.cons('8','2','5',v):
            end_fill()
            return True
        elif self.cons('4','2','1',v):
            end_fill()
            return True
        elif self.cons('2','6','3',v):
            end_fill()
            return True
        elif self.cons('8','6','9',v):
            end_fill()
            return True
        elif self.cons('4','8','7',v):
            end_fill()
            return True
        elif self.cons('7','8','9',v):
            end_fill()
            return True
        elif self.cons('8','9','7',v):
            end_fill()
            return True
        elif self.cons('9','6','3',v):
            end_fill()
            return True
        elif self.cons('6','3','9',v):
            end_fill()
            return True
        elif self.cons('2','3','1',v):
            end_fill()
            return True
        elif self.cons('1','2','3',v):
            end_fill()
            return True
        elif self.cons('1','5','7',v):
            end_fill()
            return True
        elif self.cons('7','4','1',v):
            end_fill()
            return True
        elif self.cons('7','5','3',v):
            end_fill()
            return True
        elif self.cons('5','3','7',v):
            end_fill()
            return True
        elif self.cons('9','5','1',v):
            end_fill()
            return True
        elif self.cons('5','1','9',v):
            end_fill()
            return True
        elif self.cons('4','5','6',v):
            end_fill()
            return True
        elif self.cons('5','6','4',v):
            end_fill()
            return True
        elif self.cons('8','5','2',v):
            end_fill()
            return True
        elif self.cons('5','2','8',v):
            end_fill()
            return True
        else:
            end_fill()
            return False
    def sys(self):
        begin_fill()
        fillcolor('black')
        if self.check['5']==[False,None]:
            if self.draw('5','pc')==True:
                end_fill()
                return True
        elif True:
            a,b=self.check_plots()
            if self.check['1']==[False,None] and a+b==1:
                if self.draw('1','pc')==True:
                    end_fill()
                    return True
            elif True:
                if a+b>=3 and a+b<=7:
                    if self.draw('9','pc')==True:
                        end_fill()
                        return True
                    elif self.draw('3','pc')==True:
                        end_fill()
                        return True
                    elif self.draw('1','pc')==True:
                        end_fill()
                        return True
                    elif self.draw('7','pc')==True:
                        end_fill()
                        return True
def play():
    hey=True
    w=False
    p=game()
    while hey:
        try:
            ins=input("Your Turn: ")
        except:
            pass
        else:
            if (ins=='7' or ins=='8' or ins=='9' or ins=='4' or ins=='5' or ins=='6' or ins=='1' or ins=='2' or ins=='3') and p.check_avail(ins):
                p.draw(ins,'user')
                if p.win()==True:
                    pass
                elif p.defend()==True:
                    pass
                elif p.sys()==True:
                    pass
                p1=p.res('user')
                p2=p.res('pc')
                hey= p1 and p2
                x,y=p.check_plots()
                if x+y==9 and (p1 and p2):
                    w=True
                    break
                else:
                    pass
            else:
                pass
    state="Player" if p1==False else "It's a Draw" if w==True else "Computer"
    print('Winner is',state) if p1==True and w==False else print('Its a Draw')
    penup()
    goto(-290,130)
    write('Winner',font=('Lao UI',14,'normal'))
    goto(-290,105)
    write(state,font=('Times New Roman',20,'normal'))
    goto(-320,-160)
    write('Created by,',font=('Arial',14,'normal'))
    #anything to add in future
    goto(-320,-195)
    write('      Nishit Singh                                                   ',font=('FrankRuehl',20,'normal'))
    goto(-320,-245)
    write('      Enter to close...   ',font=('FrankRuehl',11,'normal'))
    ch=input("Enter to close...")
def plate():
    penup()
    goto(-335,-265)
    pendown()
    goto(-335,275)
    goto(320,275)
    goto(320,-265)
    goto(-335,-265)
    penup()
    bgcolor('Lightcyan')
    goto(0,0)
    pendown()
    forward(180)
    backward(60)
    left(90)
    forward(60)
    backward(180)
    forward(120)
    backward(60)
    right(90)
    forward(60)
    backward(180)
    forward(60)
    left(90)
    forward(120)
    backward(180)
    penup()
    goto(-150,220)
    write('Tic Tac Toe',font=('Arial',30,'normal'))
    goto(-180,200)
    write('Place your choice in the manner  7    8    9')
    goto(-180,185)
    write('                                                      4    5    6')
    goto(-180,170)
    write('                                                      1    2    3')
    play()
print("TIC TAC TOE Input Panel")
print("\nYou got inputs as \n \t\t\t\t7     8     9\n\t\t\t\t4     5     6\n\t\t\t\t1     2     3")
print("\nPress the key to draw when your turn comes")
print("\nDon't forget!! You are WHITE and are going to play against the computer.")
print("\n I hope U liked it v1.9.4\n")
plate()
