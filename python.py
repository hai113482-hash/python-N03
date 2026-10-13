 --Bai 1
n=int(input("nhap vao mot so nguyen: "))
if(n>0):
    print("So duong")
elif(n<0):
    print("So am")
else:
    print("So 0")
 --Bai 2
 a=float(input("Nhap a:"))
 b=float(input("Nhap b:"))
 if a>b
 print(f"{a} lon hon {b}")
 elif a<b
 print(f"{b} lon hon {a}")
 else:
 print(" Hai so bang nhau")
 --Bai 3
 n=int(input())
 print("So chan" if n%2==0 else"So le")
 --Bai 4
 d=float(input())
 if d>=9: print("Xuat sac")
 elif d>=8: print("Gioi")
 elif d>=7: print("Kha")
 elif d>=5: print("Trung binh")
 else: print("Yeu")
 --Bai 5
 a=float(input())
 b=float(input())
 c=float(input())
 if a>0 and b>0 and c>0:
     if a+b>c and a+c>b and b+c>a:
         print("duoc")
     else:
         print("khong")
 else:
     print("khong")
  --Bai 6
  x1=int(input())
  y1=int(input())
  x2=int(input())
  y2=int(input())
  if x1==x2 or y1==y2
  print("Yes")
  else:
      print("No")
 --Bai 7
 a = float(input())
b = float(input())

if a != 0:
    print(f"Phương trình có nghiệm duy nhất x = {-b / a}")
elif b == 0:
    print("Phương trình có vô số nghiệm")
else:
    print("Phương trình vô nghiệm")
 --Bai 8
 a = float(input("Cạnh a: "))
b = float(input("Cạnh b: "))
c = float(input("Cạnh c: "))

if a <= 0 or b <= 0 or c <= 0 or a + b <= c or a + c <= b or b + c <= a:
    print("Ba cạnh không hợp lệ")
elif a == b == c:
    print("Tam giác đều")
elif a == b or b == c or a == c:
    print("Tam giác cân")
else:
    x, y, z = sorted([a, b, c])
    if abs(x**2 + y**2 - z**2) < 1e-9:
        print("Tam giác vuông")
    else:
        print("Tam giác thường")
  --Bai 9
  a = float(input("Cạnh a: "))
b = float(input("Cạnh b: "))
c = float(input("Cạnh c: "))

if a <= 0 or b <= 0 or c <= 0 or a + b <= c or a + c <= b or b + c <= a:
    print("Ba cạnh không hợp lệ")
elif a == b == c:
    print("Tam giác đều")
elif a == b or b == c or a == c:
    print("Tam giác cân")
else:
    x, y, z = sorted([a, b, c])
    if abs(x**2 + y**2 - z**2) < 1e-9:
        print("Tam giác vuông")
    else:
        print("Tam giác thường")
    --Bai 10
    a=int(input())
    b=int(input())
    n=int(input())
    if a+b==n:
        print("+")
    elif a-b==n:
        print("*")
    elif b!=0 and a/b==n:
        print("/")
    else:
        print("NO")