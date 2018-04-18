#dayso.py
import msvcrt
n=input("nhap n:")
print("a)")
for i in range(1,int(n)+1):
    print(i);
print("b)")
s=0;
for i in range(1,int(n)+1):
    if (int(i) % 2==0):
        s=s+i
print(s)
g=msvcrt.getch()
