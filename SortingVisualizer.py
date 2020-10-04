from tkinter import *
import time 
import tkinter.font as tkFont
from random import random
import random
import winsound

class Node():
    def __init__(self, x, y, height):
        self.x = x
        self.y = y
        self.height = height
        self.box = None

class ResizingCanvas(Canvas):
    def __init__(self,parent,**kwargs):
        Canvas.__init__(self,parent,**kwargs)
        self.bind("<Configure>", self.on_resize)
        self.height = self.winfo_reqheight()
        self.width = self.winfo_reqwidth()

    def on_resize(self,event):
        # determine the ratio of old width/height to new width/height
        wscale = float(event.width)/self.width
        hscale = float(event.height)/self.height
        self.width = event.width
        self.height = event.height
        # resize the canvas 
        self.config(width=self.width, height=self.height)
        # rescale all the objects tagged with the "all" tag
        self.scale("all",0,0,wscale,hscale)

class createCanvas():
    def __init__(self, root):
        self.root = root
        self.myframe = Frame(self.root)
        self.myframe.pack(fill=BOTH, expand=YES)
        self.mycanvas = ResizingCanvas(self.myframe,width=1000, height=1000, bg="white", highlightthickness=0)
        self.mycanvas.pack(fill=BOTH, expand=YES)

        self.time = Label(text="", font = tkFont.Font(size = 15))
        self.time.pack()
        
        self.arr = [None]*100

        w = self.mycanvas.width/1000
        h = self.mycanvas.height/1000

        for i in range(len(self.arr)):
            self.arr[i] = Node(25+9.5*i, 800, ((i+1)/100)*500)
            self.arr[i].box = self.draw_cell(self.arr[i].x*w, self.arr[i].y*h, -9.5*w, -self.arr[i].height*h, "teal")

    def update(self):
        w = self.mycanvas.width/1000
        h = self.mycanvas.height/1000

        self.mycanvas.delete("grid")

        for i in range(len(self.arr)):
            self.arr[i].x = 25+9.5*i
            self.arr[i].box = self.draw_cell(self.arr[i].x*w, self.arr[i].y*h, -9.5*w, -self.arr[i].height*h, "teal")
        
        self.mycanvas.update()

    def draw_cell(self, x,y, size_x, size_y, color):
        box = self.mycanvas.create_rectangle(x, y, (x+size_x), (y+size_y), fill=color, tags = "grid")
        return box

    def showWindow(self):
        self.root.mainloop()

    def getCanvas(self):
        return self.mycanvas

    def randomize(self):
        random.shuffle(self.arr)
        self.update()

    def bubbleSort(self):
        self.time.config(text = "Bubble Sort in progress...")
        start_time  = time.time()

        for i in range(len(self.arr)-1):
            for j in range(0, len(self.arr)-i-1):
                if(self.arr[j].height>self.arr[j+1].height):
                    self.arr[j], self.arr[j+1] = self.arr[j+1], self.arr[j]
                    self.update()

        end_time = time.time()

        self.time.config(text = "Success! Excecution Time: " + str(int(end_time-start_time)) + " seconds")

    def insertionSort(self):
        self.time.config(text = "Insertion Sort in progress...")
        start_time  = time.time()

        for i in range(1, len(self.arr)):
            key = self.arr[i]

            j = i-1 

            while j>=0 and key.height<self.arr[j].height:
                self.arr[j+1] = self.arr[j]
                self.update()
                j-= 1

            self.arr[j+1] = key

        end_time = time.time()

        self.time.config(text = "Success! Excecution Time: " + str(int(end_time-start_time)) + " seconds")

    def merge(self, arr, start, mid, end): 
        start2 = mid + 1; 

        if (arr[mid].height <= arr[start2].height): 
            return; 
            
        while (start <= mid and start2 <= end): 

            if (arr[start].height <= arr[start2].height): 
                start += 1; 
            else: 
                value = arr[start2]; 
                index = start2; 

                while (index != start): 
                    arr[index] = arr[index - 1]; 
                    index -= 1; 
                    self.update()
                    
                arr[start] = value; 

                start += 1; 
                mid += 1; 
                start2 += 1; 
                

    def mergeSort(self, arr, l, r): 
        if (l < r): 
            m = l + (r - l) // 2; 

            self.mergeSort(arr, l, m); 
            self.mergeSort(arr, m + 1, r); 
            self.merge(arr, l, m, r); 
    
    def partition(self,arr,low,high): 
        i = (low-1)         
        pivot = arr[high].height   
    
        for j in range(low , high): 
    
            if arr[j].height < pivot: 
                i = i+1 
                arr[i] , arr[j] = arr[j],arr[i] 

                self.update()
        arr[i+1], arr[high] = arr[high], arr[i+1] 
        self.update()
        return (i+1) 
 
    def quickSort(self,arr,low,high): 
        if low < high: 
            pi = self.partition(arr,low,high) 
    
            self.quickSort(arr, low, pi-1) 
            self.quickSort(arr, pi+1, high) 

    def heapify(self, arr, n, i): 
        largest = i
        l = 2 * i + 1  
        r = 2 * i + 2
    
        if l < n and arr[i].height < arr[l].height: 
            largest = l 
    
        if r < n and arr[largest].height < arr[r].height: 
            largest = r 
  
        if largest != i: 
            arr[i],arr[largest] = arr[largest],arr[i] # swap 
            self.update()
    
            self.heapify(arr, n, largest) 
    
    def heapSort(self, arr): 
        n = len(arr) 
    
        for i in range(n//2 - 1, -1, -1): 
            self.heapify(arr, n, i) 
    
        for i in range(n-1, 0, -1): 
            arr[i], arr[0] = arr[0], arr[i]
            self.update()
            self.heapify(arr, i, 0) 

def main():
    root = Tk()
    canvas = createCanvas(root)
    can = canvas.getCanvas()

    Title = Label(root, text=" "*1000 + "Sorting Visualizer" + " "*1000, fg = "white", bg = "black",  font = tkFont.Font(family="Times New Roman", size=15), wraplength=1000000)
    can.create_window(500,10,window=Title)

    button = Button(text="Shuffle Array", command=canvas.randomize)
    button.pack()
    can.create_window(300, 850, window = button)

    button2 = Button(text="Bubble Sort", command=canvas.bubbleSort)
    button2.pack()
    can.create_window(400, 850, window = button2)

    button3 = Button(text="Insertion Sort", command=canvas.insertionSort)
    button3.pack()
    can.create_window(500, 850, window = button3)

    def mergeSortAlgo():
        canvas.time.config(text = "Merge Sort in progress...")
        start_time = time.time()

        canvas.mergeSort(canvas.arr, 0, len(canvas.arr)-1)
        end_time = time.time()

        canvas.time.config(text = "Success! Excecution Time: " + str(int(end_time-start_time)) + " seconds")

    button4 = Button(text="Merge Sort", command=mergeSortAlgo)
    button4.pack()
    can.create_window(600, 850, window = button4)

    def quickSortAlgo():
        canvas.time.config(text = "Quick Sort in progress...")
        start_time = time.time()

        canvas.quickSort(canvas.arr, 0, len(canvas.arr)-1)
        end_time = time.time()

        canvas.time.config(text = "Success! Excecution Time: " + str(int(end_time-start_time)) + " seconds")
    
    button5 = Button(text="Quick Sort", command=quickSortAlgo)
    button5.pack()
    can.create_window(700, 850, window = button5)

    def heapSortAlgo():
        canvas.time.config(text = "Heap Sort in progress")
        start_time = time.time()
        canvas.heapSort(canvas.arr)

        end_time = time.time()

        canvas.time.config(text = "Success! Excecution Time: " + str(int(end_time-start_time)) + " seconds")


    button6 = Button(text="Heap Sort", command=heapSortAlgo)
    button6.pack()
    can.create_window(800, 850, window = button6)

    canvas.showWindow()



if __name__ == '__main__':
    main()