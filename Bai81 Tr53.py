import string

#Khong dung Lamda
s=input('Nhap chuoi: ')
s1=set(s.lower())
sAToZ=set(string.ascii_lowercase)
print('Chuoi',s,' co chua du ky tu a den z:', sAToZ.issubset(s1))

#Dung lamda
CoKyTuADenZ= lambda x: set(string.ascii_lowercase).issubset(set(x.lower()))
print(CoKyTuADenZ(input("Nhap chuoi: ")))