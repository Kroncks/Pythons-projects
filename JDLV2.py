from casioplot import *
from random import *

fichier=""

#--------------------
#  ecrant + marges
#97-49
f=[97,49]
co=97
li=49

items=[[(0,2),(1,2),(2,2),(2,1),(1,0)],
[(1,5),(1,6),(2,5),(11,5),(11,6),(11,7),(12,4),(12,8),(13,3),(13,9),(14,3),(14,9),(15,6),(16,4),(16,8),(17,5),(17,6),(17,7),(18,6),(21,3),(21,4),(21,5),(22,3),(22,4),(22,5),(23,2),(23,6),(25,1),(25,2),(25,6),(25,7),(35,3),(35,4),(36,3)],
[(0,0),(0,2),(1,3),(2,3),(3,3),(3,0),(4,1),(4,2),(4,3)],
[(0,2),(0,6),(0,7),(0,19),(0,20),(0,24),(1,3),(1,6),(1,7),(1,19),(1,20),(1,23),(2,3),(2,6),(2,20),(2,23),(3,3),(3,23),(4,3),(4,8),(4,9),(4,11),(4,15),(4,17),(4,18),(4,23),(5,0),(5,3),(5,9),(5,10),(5,11),(5,15),(5,16),(5,17),(5,23),(5,26),(6,1),(6,2),(6,3)
,(6,10),(6,16),(6,23),(6,24),(6,25)]]

#--------------------


def point(x,y,c=(0,0,0)):
  x=4*x-2
  y=(47-y)*4+2
  for i in range(4):
    for i in range(4):
      set_pixel(x,y,c)
      x+=1
    y+=1
    x-=4



j=[]
for i in range(li):
  j.append([])
  for y in range(co):
    j[i].append(False)
#--------------------

def affich():
  clear_screen()
  for i in range(1,li-1):
    for y in range(1,co-1):
      if j[i][y] != False:
        point(y,i)
        
  point(co-1,li-1,(255,0,0))
  for i in range(h,47*4+2):
    set_pixel(l,i,(255,0,0))
  for i in range(1,l):
    set_pixel(i,h,(255,0,0))  
  show_screen()

def calcul():
  c=[]
  for i in range(1,li-1):
    c.append([])
    for y in range(1,co-1):
      c[i-1].append(j[i-1][y+1]+j[i][y+1]+j[i+1][y+1]+j[i-1][y]+j[i+1][y]+j[i-1][y-1]+j[i][y-1]+j[i+1][y-1])
      #print(c[i-1][y-1],end="")
    #print()
  
  for i in range(1,li-1):
    for y in range(1,co-1):  
      if c[i-1][y-1]>=4:
        j[i][y]=False
        
        #point(y,i,(255,255,255))
        
      elif c[i-1][y-1]==3:
        j[i][y]=True
        #point(y,i)
      
      elif c[i-1][y-1]==2:
        None
      else:
        j[i][y]=False
        #point(y,i,(255,255,255))
  #show_screen()

      

#--------------------
def menu():
  x=""
  m=["1 fenetre     ("+str(f[0])+"-"+str(f[1])+")","2 import","3 aleat","4 module","5 modif",""]
  while not(x in ["1","2","3","4","5"]):
    for i in m:
      print(i)
    x=input("")
  if x=="1":
    fenetre()
  elif x=="2":
    importer(fichier)
  elif x=="3":
    aleat()
  elif x=="4":
    preset()
  else :
    modif()

def importer(liste):
  print("===== IMPORTER ======")
  print("\n"*3)
  if liste=="":
    print("Pas de donnees")
    input()
    menu()
  else:
    j=liste
  

def aleat():
  # li->f[]
  #remplacer 
  #li -1
  print("------ALEATOIRE------")
  print("\n"*3)
  print("frequence (0-100)% :")
  f=input()
  if f=="":
    for y in range(1,li-1):
      for x in range(1,co-1):
        j[y][x]=bool(randint(0,1))
  else :
    f=int(f)/100
    for y in range(1,li-1):
      for x in range(1,co-1):
        j[y][x]=bool(random()<=f)

def fenetre():
  x=""
  while not(x.isdigit())or int(x)>97 or int(x)<10:
    print("==fenetre graphique==")
    print()
    print("min = 10")
    print("max = 97")
    print()
    print("largeur    hauteur   ")
    x=input("> ")
  co=x
  x=""
  while not(x.isdigit())or int(x)>49 or int(x)<10:  
    print("==fenetre graphique==")
    print()
    print("min = 10")
    print("max = 49")
    print()
    print("largeur    hauteur   ")
    x=input("> "+co+" "*(9-len(co))+"> ")
  li=x
  f[0]=int(co)
  f[1]=int(li)
  menu()
  


#--------------------
def modif():
  print("\n"*6)
  while 1==1:
    x=input("x")
    y=input("y")
    print()  
    if x=="" or y=="":
      break
    j[int(y)][int(x)]=bool(1)

def preset():
  while 1==1:
    print()
    print("1 planeur")  
    print("2 canon")
    print("\n")
    print("int ( 1 -",len(items),")")
    m=input("module : ")
    if m=="":
      break
    x=int(input("x"))
    y=int(input("y"))
    for points in items[int(m)-1]:
      j[y+points[1]][x+points[0]]=True
  print("\n"*5)
  if input("modif ?")!="":
    modif()
    
#  
menu()
co,li=f[0],f[1]
#

l=co*4-6
h=(49-li)*4+1

def jeu():
  while 1==1:
    affich()
    calcul()

jeu()
