import pygame as pyg             #importing pygame library
from sys import exit             #importing exit function from system to aoid error
pyg.init()                       #initializing library    

width=600
height=600

win=pyg.display.set_mode((width,height))                                        #sets window w and h

board_img= pyg.image.load("assets\\board.png").convert_alpha()                  #loading board image ; USE convert_alpha for png

font=pyg.font.Font("assets\\arial.ttf",26)                                      #font

label_info=font.render("Player 1 Chance", True,(0,0,0),(0,200,128))                      #antialias : TRUE : smooth edges/boundaries of text
label_rect=label_info.get_rect(center=(300,30))                                          #rectangle of label

cross_img= pyg.image.load("assets\\cross.png").convert_alpha() 
circle_img= pyg.image.load("assets\\circle.png").convert_alpha() 

button_img= pyg.image.load("assets\\button.png").convert_alpha()
button_rect=button_img.get_rect(center=(300,550))

block_size=120
is_player1_chance=True
someone_won=False
position=(0,0)
chance_count=0
result=None
pieces=[]
matrix=[
    ['-','-','-'],
    ['-','-','-'],
    ['-','-','-']
]

#matrix[i][j]
      # y  x

clock=pyg.time.Clock()                                                      #creating clock object(var) of Clock() class

def check_clicked_position(position):
    if (position[0]>120 and position[0]<240) and (position[1]>120 and position[1]<240):                       #cross inside the box
        return(1,1)
    elif (position[0]>240 and position[0]<360) and (position[1]>120 and position[1]<240):
        return(1,2)
    elif (position[0]>360 and position[0]<480) and (position[1]>120 and position[1]<240):
        return(1,3)
    elif (position[0]>120 and position[0]<240) and (position[1]>240 and position[1]<360):
        return(2,1)
    elif (position[0]>240 and position[0]<360) and (position[1]>240 and position[1]<360):
        return(2,2)
    elif (position[0]>360 and position[0]<480) and (position[1]>240 and position[1]<360):
        return(2,3)
    elif (position[0]>120 and position[0]<240) and (position[1]>360 and position[1]<480):
        return(3,1)
    elif (position[0]>240 and position[0]<360) and (position[1]>360 and position[1]<480):
        return(3,2)
    elif (position[0]>360 and position[0]<480) and (position[1]>360 and position[1]<480):
        return(3,3)
    return None
    
def check_complition(matrix):
  
    # winner=""                                                           #declaring winner var

    for i in range(0,3):                                                    #completion in row
        if matrix[i][0]==matrix[i][1]==matrix[i][2]:
            if matrix[i][0]=="x":
                winner="Player 1 is Winner"
            elif matrix[i][0]=="o":
                winner="Player 2 is Winner"
            if matrix[i][0] !="-":                                               #only return when its not "-"
                return winner,(120,120*(i+1)+60),(480,120*(i+1)+60)              #draw line horizantally
        
    for i in range(0,3):
        if matrix[0][i]==matrix[1][i]==matrix[2][i]:                        #completion in column
            if matrix[0][i]=="x":
                winner="Player 1 is Winner"
            elif matrix[0][i]=="o":
                winner="Player 2 is Winner"
            if matrix[0][i] !="-":
                return winner,(120*(i+1)+60,120),(120*(i+1)+60,480)             #draw line verically

    if matrix[0][0]==matrix[1][1]==matrix[2][2]:
        if matrix[0][0]=="x":
            winner="Player 1 is Winner"
        elif matrix[0][0]=="o":
            winner="Player 2 is Winner"
        if matrix[0][0] !="-":
            return winner,(120,120),(480,480)                               #draw left to right diagonal
    
    if matrix[0][2]==matrix[1][1]==matrix[2][0]:
        if matrix[1][2]=="x":
            winner="Player 1 is Winner"
        elif matrix[1][2]=="o":
            winner="Player 2 is Winner"
        if matrix[0][2] !="-":
            return winner,(480,120),(120,480)                               #draw right to left diagonal
    
    return "NO one is Winner",(0,0)

def restart():
        global is_player1_chance,position,someone_won,chance_count,result,pieces,matrix,label_info
        is_player1_chance=True
        someone_won=False
        position=(0,0)
        chance_count=0
        result=None
        pieces=[]
        matrix=[
            ['-','-','-'],
            ['-','-','-'],
            ['-','-','-']
        ]

        label_info=font.render("Player 1 Chance", True,(0,0,0),(0,200,128))


while True:                                                #check event
    for event in pyg.event.get():                          #method to quit 
        if event.type==pyg.QUIT:
            pyg.quit()                                     #ends pygame
            exit()                                         #ends loop
        if event.type==pyg.MOUSEBUTTONUP:                  
            position=pyg.mouse.get_pos()                   #position when mouse is clicked
        if event.type==pyg.MOUSEBUTTONDOWN:
            if button_rect.collidepoint(pyg.mouse.get_pos()):
                restart()

    result=check_clicked_position(position)


    if result!=None:
       
        if matrix[result[0]-1][result[1]-1]=="-":
       
            if is_player1_chance:
                pieces.append([cross_img,block_size*result[1]+20,block_size*result[0]+20])                          #list consisting of img , x and y coordinates of piece
                is_player1_chance=False                                                                             #stop after appending once
                matrix[result[0]-1][result[1]-1]="x"                                                               #fills position with x
                label_info=font.render("Player 2 Chance", True,(0,0,0),(0,200,128))                                 #changes label
            else:
                pieces.append([circle_img,block_size*result[1]+20,block_size*result[0]+20])
                is_player1_chance=True  
                matrix[result[0]-1][result[1]-1]="o"
                label_info=font.render("Player 1 Chance", True,(0,0,0),(0,200,128))
  
            chance_count+=1                                                                                             #game is completed at chance_count=9
   
            temp=check_complition(matrix)                                                      #when there is a winner : temp[0] temp[1] temp[2]

            if temp[1]!=(0,0):                                                                  #temp[0]:string ,temp[1]:(0,0)                                               
                label_info=font.render(temp[0], True,(0,200,128))
                someone_won=True


    position=(0,0)

    win.fill((18,18,18))
    win.blit(board_img,(120,120))                          #display element 
    win.blit(label_info,label_rect)

    for piece in pieces:
        win.blit(piece[0],(piece[1],piece[2]))             #index of img ,  x and y coordinate

    if someone_won==True or chance_count==9:
        if someone_won:
            pyg.draw.line(win,(0,200,128),temp[1],temp[2])                  #drawing line (on win)
        else:
            label_info=font.render(temp[0], True,(0,0,0),(0,200,128))


        win.blit(button_img,button_rect)
    pyg.display.update()                                   #displays updates made

    clock.tick(60)                                         #locking loop at 60fps 