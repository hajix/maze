from turtle import *
from multiprocessing import *

def readInt(f):
        return int(f.readline().strip())

def drawAjor(turtle,x,y):
        global wallWidth
        turtle.up()
        turtle.goto(x*wallWidth, y*wallWidth)
        turtle.down()
        turtle.goto(x*wallWidth,(y+1)*wallWidth)
        turtle.goto((x-1)*wallWidth,(y+1)*wallWidth)
        turtle.goto((x-1)*wallWidth,y*wallWidth)
        turtle.goto(x*wallWidth,y*wallWidth)
        turtle.up()

def drawYourSelf(turtle,x,y):
        y=y+2
        global wallWidth
        turtle.color("green")
        turtle.up()
        turtle.goto((x-0.5)*wallWidth ,(y-.75)*wallWidth)
        turtle.down()
        turtle.circle(wallWidth/3)

def cleanYourSelf(turtle,x,y):
        y=y+2
        global wallWidth
        turtle.color("white")
        turtle.up()
        turtle.goto((x-0.5)*wallWidth ,(y-.75)*wallWidth)
        turtle.down()
        turtle.circle(wallWidth/3)


banna = Turtle()
banna.color("red")
banna.width(3)
banna.speed(400)

ninja = Turtle()
ninja.width(2)
ninja.speed(400)

myFile = open('1.txt')

mazeWidth = readInt(myFile)
mazeHeight = readInt(myFile)
wallWidth = 200/mazeWidth

startX = readInt(myFile)
x=startX
startY = readInt(myFile)
y=startY

lst=[]
for i in range (mazeHeight):
        lst.append([])
        for j in range (mazeWidth):
                lst[i].append(0)

row = 0
for line in myFile:
        row = row + 1
        wall = 0
        while True:
                wall = line.find('#',wall)
                if(wall==-1):
                        break
                drawAjor(banna,wall,row)
                lst[mazeHeight-row][wall]=1
                wall+=1

drawYourSelf(ninja,startX,startY)
lst[mazeHeight-1-startY][startX]=(.4,.4)

###################################################################

bfs = [(x,y),]

while (len(bfs) > 0):
    #print bfs,
    cur=bfs[0]
    #print cur
    bfs = bfs[1:]
    x,y=cur
    #up
    if y+1<mazeHeight and lst[(mazeHeight-1-y)-1][x]==0:
        bfs.append((x,y+1))
        lst[(mazeHeight-1-y)-1][x]=cur
    #down
    if y-1>-1 and lst[(mazeHeight-1-y)+1][x]==0:
        bfs.append((x,y-1))
        lst[(mazeHeight-1-y)+1][x]=cur
    #right
    if x+1<mazeWidth and lst[(mazeHeight-1-y)][x+1]==0:
        bfs.append((x+1,y))
        lst[(mazeHeight-1-y)][x+1]=cur
    #left
    if x-1>-1 and lst[(mazeHeight-1-y)][x-1]==0:
        bfs.append((x-1,y))
        lst[(mazeHeight-1-y)][x-1]=cur

######################################################################

bazgasht=[]
outCount=0
for i in range (mazeWidth):
        for j in range (mazeHeight):
                if ( (lst[mazeHeight-1-j][i]!=1) and ( (i==0) or (i==mazeWidth-1) or (j==0) or (j==mazeHeight-1) ) ):
                        bazgasht.append([(i,j)])
                        outCount=outCount+1

for i in range (outCount):
        m,n=bazgasht[i][-1]
        while True:
                bazgasht[i].append(lst[(mazeHeight-1-n)][m])
                (m,n)=lst[(mazeHeight-1-n)][m]
                if (m,n) ==(.4,.4):
                        break


#########################################################################

masirLength=[]
for i in range (outCount):
        masirLength.append(len(bazgasht[i]))
masirLength.sort()

for i in range(outCount):
        if len(bazgasht[i])==masirLength[0]:
                bazgasht=bazgasht[i]
                break
bazgasht.reverse()
bazgasht=bazgasht[1:]

print bazgasht
print "the length of way is : " + str(len(bazgasht))

for i in range (len(bazgasht)):
        (x,y)=bazgasht[i]
        drawYourSelf(ninja,x,y)


exitonclick()
