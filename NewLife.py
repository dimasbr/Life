import time
import thread

from Tkinter import *

root=Tk()

root.geometry("620x600")
root.resizable(width=False, height=False)



    



size = 20
fps=0.1

class cell:
    def change (self):
        if self.alive == 0: self.butt.configure(bg = 'white')
        if self.alive == 1: self.butt.configure(bg = 'red')
        if self.alive == 2: self.butt.configure(bg = 'green')
        self.butt.update_idletasks()

    def buttonClicked(self, event=None):
        if self.alive != 2 :
            self.alive += 1
        else :
            self.alive = 0
        self.change()
        
    def __init__ (self, location) :
        self.location = location
        self.alive = 0
        self.to_be = None
        self.butt = Button(root, text='', bg='white', command=self.buttonClicked)
        self.butt.grid(row=self.location[0], column=self.location[1])



class board:

    def fill(self):
        for i in xrange(size):
            self.map.append([])
            for j in xrange(size):
                self.map[i].insert(j, cell((i, j)))

#    def printBoard(self):
#        for i in xrange(size):
#            for j in xrange(size):
#                cell = self.map[i][j]
#                if cell.alive == True: print 'W',
#                else: print '_',
#            print('\n')

    def stepForCell(self, cell):
            mapa = self.map
            a = []
            b = []
            g = 0
            r = 0
            w = 0
            cell_loc = cell.location

            if cell_loc[0] > 0: i = cell_loc[0]-1
            else: i = size-1
            if cell_loc[1] >0: j = cell_loc[1]-1
            else: j = size-1
            a.append(mapa[i][j].location)

            i = cell_loc[0]
            if cell_loc[1] >0: j = cell_loc[1]-1
            else: j = size-1
            a.append(mapa[i][j].location)

            if cell_loc[0] < size-1: i=cell_loc[0]+1
            else: i = 0
            if cell_loc[1] >0: j = cell_loc[1]-1
            else: j = size-1
            a.append(mapa[i][j].location)

            if cell_loc[0] > 0: i = cell_loc[0]-1
            else: i = size-1
            j = cell_loc[1]
            a.append(mapa[i][j].location)

            if cell_loc[0] < size-1: i=cell_loc[0]+1
            else: i = 0
            a.append(mapa[i][j].location)

            if cell_loc[0] > 0: i = cell_loc[0]-1
            else: i = size-1
            if cell_loc[1] < size-1: j=cell_loc[1]+1
            else: j = 0
            a.append(mapa[i][j].location)

            i = cell_loc[0]
            if cell_loc[1] < size-1: j=cell_loc[1]+1
            else: j = 0
            a.append(mapa[i][j].location)

            if cell_loc[0] < size-1: i=cell_loc[0]+1
            else: i = 0
            if cell_loc[1] < size-1: j=cell_loc[1]+1
            else: j = 0
            a.append(mapa[i][j].location)

            for i in xrange(len(a)): b.append(mapa[a[i][0]][a[i][1]].alive)
            
            for i in b:
                if i == 0 : w+=1
                if i == 1 : r+=1
                if i == 2 : g+=1
            if cell.alive == 0 :
                if r > 2 : self.map[cell.location[0]][cell.location[1]].to_be = 1
                if g > 2 : self.map[cell.location[0]][cell.location[1]].to_be = 2
            if cell.alive == 1 :
                if w > 6 : self.map[cell.location[0]][cell.location[1]].to_be = 0
                if g > 2 : self.map[cell.location[0]][cell.location[1]].to_be = 2
            if cell.alive == 2 :
                if w > 6 : self.map[cell.location[0]][cell.location[1]].to_be = 0
                if r > 2 : self.map[cell.location[0]][cell.location[1]].to_be = 1


    def update_frame(self):
            for i in xrange(size):
                for j in xrange(size):
                    cell = self.map[i][j]
                    self.stepForCell(self.map[i][j])

    def update(self):
            for i in xrange(size):
                for j in xrange(size):
                    cell = self.map[i][j]
                    loc = cell.location
                    if cell.to_be != None:
                        self.map[i][j].alive = cell.to_be
                        self.map[i][j].to_be = None
                        self.map[i][j].change()

    def circle(self):
        self.done = False
        while self.done == False:
            time.sleep(fps)
            self.update_frame()
            self.update()

    def circl_th(self, event=None):
        thread.start_new_thread(self.circle, ())

    def loop_stop(self, event=None):
        self.done = True

    def __init__(self):
        self.map = []
        self.butt = Button(root, text='GO', bg='green', command=self.circl_th)
        self.butt.grid(row=10, column=20)
        self.buttst = Button(root, text='STOP', bg='red', command=self.loop_stop)
        self.buttst.grid(row=11, column=20)


boardd = board()
boardd.fill()

root.mainloop()
                
