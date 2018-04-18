class SinhVien:
    ten = ""
    namsinh = ""
    khoa = ""
    def __init__(self,ten,namsinh,khoa):
        self.ten = ten
        self.namsinh = namsinh
        self.khoa = khoa
    def getten(self):
        return self.ten
    def getnamsinh(self):
        return self.namsinh
    def getkhoa(self):
        return self.khoa
    def toString(self):
        print("Ho ten:",self.ten,"\nnam sinh:",self.namsinh,"\nkhoa:",self.khoa)
        
