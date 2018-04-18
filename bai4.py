from sinhvien import SinhVien
from sinhvien import Khoa
import msvcrt
l = []
l.append(SinhVien("001","mai a ","57"))
l.append(SinhVien("002","tran b","58"))
l.append(SinhVien("003","le c  ","57"))
l.append(SinhVien("004","pham q","58"))
l.append(SinhVien("005","ngo m ","59"))

for i in l:
    i.xuat()
    
print()

g = []
g.append(Khoa("56","khoa 56 cntt"))
g.append(Khoa("57","khoa 57 cntt"))
g.append(Khoa("58","khoa 58 cntt"))              
g.append(Khoa("59","khoa 59 cntt"))

for i in g:
    i.xuat()
            
print()
for i in l:
    if (str(i.getKhoa())=="57"):
        i.xuat()
msvcrt.getch()
