import tkinter as tk
from PIL import ImageTk,Image  

class View():

    _instance = None
    
    def __init__(self):
        
        self.gameManager = None
        self.listCardsBoard = []
        self.currentPlayer = None
        self.cardleft=None
        self.cardRight=None
        
        
        self.root=tk.Tk()
        maxWidth=1280
        maxHeight=720
        self.root.geometry(str(maxWidth)+"x"+str(maxHeight))
        self.mainFrame = tk.Frame(self.root,width=maxWidth,height=maxHeight)
        self.mainFrame.pack(fill="both", expand=True)
        
        
        
        #leftFrame
        self.leftFrame = tk.Frame(self.mainFrame,width=int(maxWidth*0.75),height=int(maxHeight))
        self.leftFrame.pack(side=tk.LEFT)        
        
        #Canvas inside leftFrame
        self.drawCanvas = tk.Canvas(self.leftFrame,width=int(maxWidth*0.75),height=int(maxHeight),bg="pink")
        self.drawCanvas.pack()
        
        #rightFrame
        self.rightFrame = tk.Frame(self.mainFrame,width=int(maxWidth*0.25),height=int(maxHeight))
        self.rightFrame.pack(side=tk.RIGHT)

        #Canvas inside rightFrame
        self.infoCanvas = tk.Canvas(self.rightFrame,width=int(maxWidth*0.25),height=int(maxHeight) , bg="#873200")
        self.infoCanvas.pack(side=tk.TOP)
        
        #Frame inside rightFrame
#        self.infoFrame = tk.Frame(self.rightFrame,width=int(maxWidth*0.25),height=int(maxHeight/2))
#        self.infoFrame.pack(side=tk.BOTTOM)
#        self.infoFrame.pack_propagate(False)
        20,20,
        #Element inside right Canvas
        padx = int((maxWidth*0.25-(maxWidth*0.25*(1-0.2)))/2)
        pady = int((maxHeight*0.05))
        self.playerNumberText = self.infoCanvas.create_text(int((maxWidth*0.25)/2),pady,anchor=tk.N,text="PLAYER")
        
        
        self.playerSaneText = self.infoCanvas.create_text(padx,int(((maxHeight-(2*pady))/5)*1)+pady,anchor=tk.NW,text="SANE : ")
        self.playerInsaneText = self.infoCanvas.create_text(padx,int(((maxHeight-(2*pady))/5)*2)+pady,anchor=tk.NW,text="INSANE : ")


        self.viewHandCanvasText = self.infoCanvas.create_text(int((maxWidth*0.25)/2),int(((maxHeight-(2*pady))/5)*3)+pady,anchor=tk.N,text="VOIR MA MAIN")
        self.infoCanvas.tag_bind(self.viewHandCanvasText, '<1>', self._viewHand)
        
        self.viewOtherCardsCanvasText = self.infoCanvas.create_text(int((maxWidth*0.25)/2),int(((maxHeight-(2*pady))/5)*4)+pady,anchor=tk.N,text="VOIR LES AUTRES CARTES EN JEU")
        self.infoCanvas.tag_bind(self.viewOtherCardsCanvasText, '<1>', self._viewOtherCards)

        
        
        
        
        
        
        
        
        
        
        self.cardDrawLeft = None
        self.cardDrawRight = None

        #Bind image to function, doesn't work cause cardDrawX are None
#        self.drawCanvas.tag_bind(self.cardDrawLeft, '<1>', self._leftCardClicked)
#        self.drawCanvas.tag_bind(self.cardDrawRight, '<1>', self._rightCardClicked)

#        #Temp
#        imgFile = Image.open("../media/test.jpg")
#
#        imgFile = imgFile.resize((int(drawCanvas.winfo_width()/2),int(drawCanvas.winfo_height())),Image.ANTIALIAS)
#        self.imgLeft = ImageTk.PhotoImage(imgFile,master=self.root)
#        self.imgRight = self.imgLeft
        #TempdrawCanvas
#        
#        self.cardDrawLeft = drawCanvas.create_image(0,0, anchor=tk.NW, image=self.imgLeft)  
#        self.cardDrawRight = self.leftFrame.drawCanvas.create_image(int(self.leftFrame.drawCanvas.winfo_width()/2),0,anchor=tk.NW,image=self.imgRight)
#        
#        
#        self.viewHandButton = tk.Button(self.infoFrame, text ="Voir ma main", command = self._viewHand)
#        self.viewHandButton.pack(side=tk.TOP)

        self.root.mainloop()

#    def buttonPushed(self):
#       self.root.destroy()

    def setGameManager(self,gameManager):
        self.gameManager = gameManager
        
    def getGameManager(self):
        return self.gameManager

    def _leftCardClicked(self,event):
        self.leftFrame.drawCanvas.itemconfigure(self.cardDrawLeft,state="hidden")
        
    def _rightCardClicked(self,event):
        self.dleftFrame.rawCanvas.itemconfigure(self.cardDrawLeft,state="normal")

    def chooseTargetPlayer(nbPlayer, players):
        pass

    def _viewHand(self,event):
        print("view")

    def _viewOtherCards(self,event):
        print("other")
    

LP=View()