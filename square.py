class square:
    width=0
    height=0
    def __init__(self,width,height):
        self.width=width
        self.height=height
    def toString(self):
        print("chieu dai la",self.width,"\n")
        print("chieu rong la",self.height,"\n") 
    def ChuVi(self):
        return (self.width+self.height)*2
    def DienTich(self):
        return self.width*self.height

    

    
    
