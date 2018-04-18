class SinhVien:
    mssv=""
    hoten=""
    khoa=""
    def __init__(self,mssv,hoten,khoa):
        self.mssv=mssv
        self.hoten=hoten
        self.khoa=khoa
    def getKhoa(self):
        return self.khoa
    def xuat(self):
        print(self.mssv," ",self.hoten," ",self.khoa)
class Khoa:
    makhoa=""
    tenkhoa=""
    def __init__(self,makhoa,tenkhoa):
        self.makhoa=makhoa
        self.tenkhoa=tenkhoa
    def getMaKhoa(self):
        return self.makhoa
    def getTenKhoa(self):
        return self.tenkhoa
    def xuat(self):
        print(self.makhoa," ",self.tenkhoa)
