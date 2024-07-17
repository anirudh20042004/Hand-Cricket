import random
print('.........WELCOME TO ODD OR EVEN MATCH..........')
def bowling():
        score=0
        u=1
        print('-------------------------------------------')
        print('Your Bowling')
        while u==1:
            tu=1
            while tu==1:
              yt=int(input('Enter a number between 0 and 10:'))
              if yt>9:
                      print('>>Please enter a number between 0 and 10 only')
                      tu=1
              else:
                      tu=2
            ty=random.randint(1,9)
            print('Computer choosed:',ty)
            if ty==yt:
                print('Computer Out')
                u=2
                print('Computer scored:',score)
                print('You have to score',score+1,'inorder to win the match')
            else:
                u=1
                score=score+ty
        print('--------------------------------------------')
        print('Your Batting')
        uw=1
        sc=0
        while uw==1:
            qw=3
            while qw==3:
                    ry=int(input('Enter a number between 0 and 10:'))
                    if ry>9:
                            print('>>Please enter a number between 0 and 10 only')
                            qw=3
                    else:
                            qw=1                            
            yr=random.randint(1,9)
            print('Computer choosed:',yr)
            if ry==yr:
                print('OUT')
                print('Your score is:',sc)
                uw=2
                if sc>score:
                    print('...You wins the match!!')
                elif sc==score:
                    print('Draw')
                else:
                    print('...Computer wins the match')
            else:
                uw=1
                sc=sc+ry
                if sc>=score+1:
                        uw=3
                        print('You wins the match')
                else:
                        uw=1
def batting():
         print('--------------------------------------------')
         print('Your Batting')
         sc=0
         uw=1
         while uw==1:
            uy=1
            while uy==1:
              ry=int(input('Enter a number between 0 and 10:'))
              if ry>9:
                      print('>>Please Enter a number between 0 and 10 only')
                      uy=1
              else:
                      uy=2
            yr=random.randint(1,9)
            print('Computer choosed:',yr)
            if ry==yr:
                print('OUT')
                print('Your score is:',sc)
                print('Computer need to score',sc+1,'inorder to win the match')
                uw=2                
            else:
                uw=1
                sc=sc+ry
         print('--------------------------------------------')
         print('Your Bowling')
         score=0
         u=1
         while u==1:
            ip=4
            while ip==4:
                yt=int(input('Enter a number between 0 and 10:'))
                if yt>9:
                        print('>>Please Enter a number between 0 and 10 only')
                        ip=4
                else:
                        ip=5
            ty=random.randint(1,9)
            print('Computer choosed:',ty)
            if ty==yt:
                print('Computer Out')
                print('Computer scored:',score)
                if score>sc:
                        print('Computer wins the match')
                        u=2
                else:
                        print('You wins the match!!....')
                        u=2
                        
            else:
                score=score+ty
                if score>sc:
                        print('...Computer wins the match')
                        u=3
                else:
                        u=1
q=1
while q==1:
 print('Enter 1:ODD')
 print('Enter 2:EVEN')
 x=int(input('Enter your choice(1/2):'))
 if x==1:
    p=int(input('Enter a number between 0 and 10:'))
    io=random.randint(1,9)
    print('Computer choosed:',io)
    p1=p+io
    if p1%2==1:
        print('Since',p,'+',io,'=',p1,'is odd')
        print('You wins the choice')
        print('Enter 1:Batting')
        print('Enter 2:Bowling')
        e=int(input('Enter your choice(1/2):'))
        if e==1:
            batting()
        elif e==2:
            bowling()
        else:
            None
    else:
        print('Since',p,'+',io,'=',p1,'is even')
        print('Computer wins the choice')
        y=random.randint(1,8)
        if y%2==0:
          print('Computer chooses to bat')
          bowling()
        else:
          print('Computer chooses to bowl')
          batting()
 elif x==2:
    p=int(input('Enter a number between 0 and 10:'))
    io=random.randint(1,9)
    print('Computer choosed:',io)
    p1=p+io
    if p1%2==0:
        print('Since',p,'+',io,'=',p1,'is even')
        print('You wins the choice')
        print('Enter 1:Batting')
        print('Enter 2:Bowling')
        e=int(input('Enter your choice(1/2):'))
        if e==1:
            batting()
        elif e==2:
            bowling()
        else:
            None
    else:
        print('Since',p,'+',io,'=',p1,'is odd')
        print('Computer wins the choice')
        y=random.randint(1,8)
        if y%2==0:
          print('Computer chooses to bat')
          bowling()
        else:
          print('Computer chooses to bowl')
          batting()
 print('FINISHED')
 print('If you want to play the match again Enter Y else N')
 i=input('Enter your choice:')
 if i.upper()=='Y':
         q=1
 else:
         q=2
         print('Thank you')

        
        
          
                
         
         
         
         
                    
            
            
        
                
                
        


