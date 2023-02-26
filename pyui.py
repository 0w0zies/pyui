import pygame

global frameTime,t,owo,selectedtextbox,textposition,shiftheld,running,hoveredbutton
shiftheld = False
selectedtextbox = -1
textposition = 0
hoveredbutton = -1
buttons = []
textboxes = []
text = []
owo = 0
running = True
frameTime = 0
t = 0
uisize = 1 #default: 1

#keybindings
keys = [
    [pygame.K_AMPERSAND,"`","~"],
    [pygame.K_0,"0",")"],
    [pygame.K_1,"1","!"],
    [pygame.K_2,"2","@"],
    [pygame.K_3,"3","#"],
    [pygame.K_4,"4","$"],
    [pygame.K_5,"5","%"],
    [pygame.K_6,"6","^"],
    [pygame.K_7,"7","&"],
    [pygame.K_8,"8","*"],
    [pygame.K_9,"9","("],
    [pygame.K_MINUS,"-","_"],
    [pygame.K_PLUS,"+","="],

    [pygame.K_q,"q","Q"],
    [pygame.K_w,"w","W"],
    [pygame.K_e,"e","E"],
    [pygame.K_r,"r","R"],
    [pygame.K_t,"t","T"],
    [pygame.K_y,"y","Y"],
    [pygame.K_u,"u","U"],
    [pygame.K_i,"i","I"],
    [pygame.K_o,"o","O"],
    [pygame.K_p,"p","P"],
    [pygame.K_LEFTBRACKET,"[","{"],
    [pygame.K_RIGHTBRACKET,"]","}"],
    [pygame.K_BACKSLASH,"\\","|"],
    
    [pygame.K_a,"a","A"],
    [pygame.K_s,"s","S"],
    [pygame.K_d,"d","D"],
    [pygame.K_f,"f","F"],
    [pygame.K_g,"g","G"],
    [pygame.K_h,"h","H"],
    [pygame.K_j,"j","J"],
    [pygame.K_k,"k","K"],
    [pygame.K_l,"l","L"],
    [pygame.K_SEMICOLON,";",":"],
    [pygame.K_QUOTE,"'",'"'],
    
    [pygame.K_z,"z","Z"],
    [pygame.K_x,"x","X"],
    [pygame.K_c,"c","C"],
    [pygame.K_v,"v","V"],
    [pygame.K_b,"b","B"],
    [pygame.K_n,"n","N"],
    [pygame.K_m,"m","M"],
    [pygame.K_COMMA,",","<"],
    [pygame.K_PERIOD,".",">"],
    [pygame.K_SLASH,"/","?"],
    
    [pygame.K_SPACE," "," "],
]

def makewindow(size,txtbxes,btns,txt,title="Pyui window"):
    global uisize
    text = txt
    textboxes = txtbxes
    buttons = btns
    pygame.init()
    surface = pygame.display.set_mode((size[0] * uisize,size[1] * uisize),0,0,0,1)
    pygame.display.set_caption(title)
    return surface

def getcollision(x,y,width,height):
    if x <= pygame.mouse.get_pos()[0] and x + width >= pygame.mouse.get_pos()[0]:
        if y <= pygame.mouse.get_pos()[1] and (y + height) >= pygame.mouse.get_pos()[1]:
            return True
    return False

def getframetime():
    return t

def render(surface):
    global frameTime,t,owo,selectedtextbox,textposition,shiftheld,running,hoveredbutton
    t = (pygame.time.get_ticks() - frameTime) / 1000
    frameTime = pygame.time.get_ticks()
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LSHIFT or event.key == pygame.K_RSHIFT:
                shiftheld = True
            if selectedtextbox != -1:
                awoo = False
                cantypechar = True
                for v in keys:
                    if event.key == v[0]:
                            cantypechar = True
                            char = v[1]
                            if shiftheld == True and textboxes[selectedtextbox][6] == True:
                                char = v[2]
                            elif shiftheld == True:
                                break
                            if char.isnumeric() == False:
                                if textboxes[selectedtextbox][5] == True:
                                    cantypechar = False
                                    if textboxes[selectedtextbox][7] == "any":
                                        if char == ".":
                                            if "." not in textboxes[selectedtextbox][3]:
                                                cantypechar = True
                                        if char == "-":
                                            if "-" not in textboxes[selectedtextbox][3]:
                                                cantypechar = True
                            print(cantypechar)
                            if cantypechar == True:
                                textboxes[selectedtextbox][3] = textboxes[selectedtextbox][3][0:textposition]+char+textboxes[selectedtextbox][3][textposition:len(textboxes[selectedtextbox][3])]
                                textposition += 1
                                owo = 0
                                awoo = True
                                break
                if awoo == False:
                    if event.key == pygame.K_DELETE:
                        textboxes[selectedtextbox][3] = textboxes[selectedtextbox][3][0:textposition]+textboxes[selectedtextbox][3][textposition + 1:len(textboxes[selectedtextbox][3])]
                    if event.key == pygame.K_BACKSPACE:
                        textboxes[selectedtextbox][3] = textboxes[selectedtextbox][3][0:textposition - 1]+textboxes[selectedtextbox][3][textposition:len(textboxes[selectedtextbox][3])]
                        textposition -= 1
                        owo = 0
                    if event.key == pygame.K_LEFT and textposition > 0:
                        textposition -= 1
                        owo = 0
                    if event.key == pygame.K_RIGHT and textposition < len(textboxes[selectedtextbox][3]):
                        textposition += 1
                        owo = 0
                    if event.key == pygame.K_ESCAPE or event.key == pygame.K_RETURN:
                        selectedtextbox = -1
                    if textposition < 0:
                        textposition = 0
                    elif textposition >= len(textboxes[selectedtextbox][3])+1:
                        textposition = len(textboxes[selectedtextbox][3])+1
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LSHIFT or event.key == pygame.K_RSHIFT:
                shiftheld = False
            
            
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                buttonpressed = False
                for v in buttons:
                    if getcollision(v[0][0],v[0][1],v[1][0],v[1][1]):
                        v[4] = 25
                        if v[3] != None:
                            v[3]()
                        selectedtextbox = -1
                        buttonpressed = True
                        break
                aa = 0
                if buttonpressed == False:
                  for v in textboxes:
                    if getcollision(v[0][0],v[0][1],v[1][0],v[1][1]):
                        textposition = len(v[3])
                        selectedtextbox = aa
                    aa += 1
    surface.fill((50,50,50))
    owo += t * 900

    for v in text:
        newtextbox(surface,v[0],v[1],v[2],v[3],v[4],textsize=v[5],alignment=v[6],font=v[7])
    btns = 0
    hoveredbutton = -1
    for v in buttons:
        if getcollision(v[0][0],v[0][1],v[1][0],v[1][1]):
            v[4] += t * 300
            if v[4] >= 75:
                v[4] = 75
            hoveredbutton = btns
        else:
            v[4] -= t * 150
            if v[4] <= 50:
                v[4] = 50
        if v[6] == None:
            pygame.draw.rect(surface, (25,25,25), pygame.Rect(v[0][0], v[0][1], v[1][0] + 4, v[1][1] + 4), 0,3)
            pygame.draw.rect(surface, (0,0,0), pygame.Rect(v[0][0] - 1, v[0][1] - 1, v[1][0] + 2, v[1][1] + 2), 0,3)
            pygame.draw.rect(surface, (v[4],v[4],v[4]), pygame.Rect(v[0][0], v[0][1], v[1][0], v[1][1]), 0,3)
            newtextbox(surface,v[0][0] + (v[1][0] / 2),v[0][1] + (v[1][1] / 2),v[2],(int(25 + ((v[4] - 50) * 0.1)),int(25 + ((v[4] - 50) * 0.1)),int(25 + ((v[4] - 50) * 0.1))),None,textsize=int(v[5] + ((v[4] - 50) * (v[5] * 0.005))),alignment="center")
        else:
            pygame.draw.rect(surface, (0,0,0), pygame.Rect(v[0][0] - 1, v[0][1] - 1, v[1][0] + 2, v[1][1] + 2), 0,3)
            pygame.draw.rect(surface, (v[4],v[4],v[4]), pygame.Rect(v[0][0], v[0][1], v[1][0], v[1][1]), 0,3)
            size = v[6].get_width()/v[6].get_height()
            xpos = (v[0][0] - (((v[1][1] * size) / 2))) + (v[1][0] / 2)
            rect = (int((v[0][0] - xpos)),0,v[1][0],v[1][1])
            surface.blit(pygame.transform.scale(v[6],(v[1][1] * size,v[1][1])),(xpos + rect[0],v[0][1]),rect)
        btns += 1

    aa = 0
    for v in textboxes:
            aaa = v[2]
            if aa == selectedtextbox:
                aaa = v[3]
                if owo % 1000 >= 500:
                    aaa = textboxes[selectedtextbox][3][0:textposition]+"|"+textboxes[selectedtextbox][3][textposition:len(textboxes[selectedtextbox][3])]
                else:
                    aaa = textboxes[selectedtextbox][3][0:textposition]+" "+textboxes[selectedtextbox][3][textposition:len(textboxes[selectedtextbox][3])]
            else:
                if v[3] != "":
                    aaa = v[3]
            if getcollision(v[0][0],v[0][1],v[1][0],v[1][1]):
                v[4] += t * 300
                if v[4] >= 75:
                    v[4] = 75
            else:
                v[4] -= t * 150
                if v[4] <= 50:
                    v[4] = 50
            if v[8] == True:
                aaa = blanktext(v[3])
            pygame.draw.rect(surface, (0,0,0), pygame.Rect(v[0][0] - 1, v[0][1] - 1, v[1][0] + 2, v[1][1] + 2), 0,3)
            pygame.draw.rect(surface, (v[4] + 5,v[4] + 5,v[4] + 5), pygame.Rect(v[0][0], v[0][1], v[1][0], v[1][1]), 0,3)
            newtextbox(surface,v[0][0] + 15,v[0][1] + (v[1][1] / 2),aaa,(int(25 + ((v[4] - 50) * 0.1)),int(25 + ((v[4] - 50) * 0.1)),int(25 + ((v[4] - 50) * 0.1))),None,textsize=25,alignment="left")
            aa += 1
    return running

def changetext(txt,string):
    text[txt][2] = string
def blanktext(text):
    result = ""
    for v in text:
        result = result+"*"
    return result

def addbutton(position,size,text,function,fontsize=20,image=None,customvalues=[]):
    global uisize
    if image != None:
        image = pygame.image.load(image).convert_alpha()
    buttons.append([(position[0] * uisize,position[1] * uisize),(size[0] * uisize,size[1] * uisize),text,function,75,fontsize,image,customvalues])

def addtextbox(position,size,starttext,numonly,capsallowed,numtype="any",blanktext=False,customvalues=[]):
    global uisize
    textboxes.append([(position[0] * uisize,position[1] * uisize),(size[0] * uisize,size[1] * uisize),starttext,"",75,numonly,capsallowed,numtype,blanktext,customvalues])

def gettextboxtext(textbox):
    return textboxes[textbox][3]

def clearelements():
    global text,textboxes,buttons
    text = []
    textboxes = []
    buttons = []

def addtext(x,y,txt,textcolor,background,textsize=15,alignment = "left",font="C:\\Windows\\Fonts\\ARIAL.TTF"):
    global uisize
    text.append([x * uisize,y * uisize,txt,textcolor,background,textsize,alignment,font])

def newtextbox(screen,x,y,text,textcolor,background,textsize=15,alignment = "left",font="C:\\Windows\\Fonts\\ARIAL.TTF",blit=True):
    font = pygame.font.Font(font,textsize)
    txt = font.render(text, True, textcolor, background)
    posx = x
    if alignment == "center":
        posx = x - (txt.get_size()[0] / 2)
    if alignment == "left":
        posx = x
    if alignment == "right":
        posx = x - txt.get_size()[0]
    pos = (int(posx),int(y - (txt.get_size()[1] / 2)))
    if blit == True:
        screen.blit(txt, pos)
    return txt