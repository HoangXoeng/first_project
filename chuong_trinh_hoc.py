import os
import random


def ngayThang(thang):
    thang_31 = [1,3,5,7,8,10,12]
    thang_30 = [4,6,9,11]
    for i in thang_31:
        if thang == i:
            return "31 days"
    for i in thang_30:
        if thang == i:
            return "30 days"
    if thang == 2:
        nam = int(input("Enter the year"))
        if ((nam % 4 == 0) and (nam % 100 != 0)) or ((nam % 100 == 0) and (nam % 400 == 0)):
            return "29 days"
        else:
            return "28 days"
# Chuc nang 1



def tinh_luong_nhan_vien(gio_lam,luong):
    tien_luong = 0
    if gio_lam <= 40:
        tien_luong = gio_lam * luong
    else:
        tien_luong = (40 * luong) + ((gio_lam-40) * (luong*1.5))
    return tien_luong
# Chuc nang 2


def xap_xep_luong(so_luong_nhan_vien):
    list_luong = []
    list_nhan_vien = []
    for i in range(so_luong_nhan_vien):
        name = input("nhap ten nhan vien: ")
        list_luong.append(name)
        luong = float(input("nhap tien luong cua nhan vien: "))
        list_luong.append(luong)
        list_nhan_vien.append(list_luong)
        list_luong = []
    
    tg = []
    for i in range(len(list_nhan_vien)):
        for j in range(i, len(list_nhan_vien)):
            if list_nhan_vien[i][1] > list_nhan_vien[j][1]:

                tg = list_nhan_vien[i]
                list_nhan_vien[i] = list_nhan_vien[j]
                list_nhan_vien[j] = tg

    return list_nhan_vien
# Chuc nang 3

def namenv(name):
    name = name.split()
    ten_day_du = []
    ho_ten_dem = []
    ten = []    
    lenname = len(name)
    for i in name:
        char = i.capitalize()
        ten_day_du.append(char)    #in ra ho va ten


    for j in range(lenname - 1 ):
        ho_ten_dem.append(name[j].capitalize())   #in ra ho va ten dem
    
    ten = name[lenname-1].capitalize() #in ra ten
    ten_day_du = ' '.join(ten_day_du)
    ho_ten_dem = ' '.join(ho_ten_dem)
    ten  = ''.join(ten)
    return ten_day_du,ho_ten_dem,ten
# Chuc nang 4

def diem_Trung_Binh(so_mon):

    diem_mon = 0
    diem_tong = 0
    tong_he_so = 0
    for i in range(so_mon):
        while True:
            diem = int(input(f"Diem mon hoc {i+1} : "))
            if diem >= 0 and diem <= 10:
                break
        
        while True:
            he_so = float(input("Nhap he so mon hoc: "))
            if he_so >= 0 and he_so <= 3 and he_so % 0.5 == 0:
                break
        tong_he_so = tong_he_so + he_so
        diem_mon = diem * he_so
        diem_tong = diem_tong + diem_mon

    return diem_tong,tong_he_so
# Chuc nang 5
def menu1():
    print("1. Nap Tien")
    print("2. Choi tom cua")
    print("3. Xem tai khoan")
    print("0. Thoat")

def menu_game():
    print("____________________________")
    print("| (1)Tom | (2)Cua | (3)Bau  |")
    print("----------------------------")
    print("| (4)Ca  | (5)Ga  | (6)Nai  | ")
    print("-----------------------------")

def tom_cua(choose):
    list_op = ["Tom","Cua","Bau","Ca","Ga","Nai"]
    xx1 = random.choice(list_op)
    xx2 = random.choice(list_op)
    xx3 = random.choice(list_op)
    list_ket_qua = [xx1,xx2,xx3]
    lua_chon = ""
    dem_ket_qua = 0 
    if choose == 1:
        lua_chon = "Tom"
    elif choose == 2:
        lua_chon = "Cua"
    elif choose == 3:
        lua_chon = "Bau"
    elif choose == 4:
        lua_chon = "Ca"
    elif choose == 5:
        lua_chon = "Ga"
    else:
        lua_chon = "Nai"
    for i in list_ket_qua:
        if i == lua_chon:
            dem_ket_qua = dem_ket_qua + 1
    return dem_ket_qua,list_ket_qua,lua_chon

def menu():
    os.system("cls")
    print("          --------------------------------------------------------------------")
    print("          --------------------------------------------------------------------") 
    print("          --------                                                    --------")
    print("          --------        𝓒𝓱𝓾𝓸𝓰 𝓣𝓻𝓲𝓷𝓱 𝓗𝓸𝓬 𝓣𝓱𝓸𝓷𝓰 𝓜𝓲𝓷𝓱                  --------")
    print("          --------                                                    --------")
    print("          --------------------------●▬▬▬▬๑۩۩๑▬▬▬▬▬●---------------------------")
    print("          --------------------------------------------------------------------") 
    print()
    print()
    print("          ______________________   ꧁•⊹٭ME₦U٭⊹•꧂   ______________________")
    print()
    print()
    print("_________________________________________________________________________________________")
    print("|                                                                                       |")
    print("| Please choose your option:                                                            |")
    print("|                                                                                       |")
    print("|╰┈➤   Option 1: Calender ☂                                               (Press key 1) |")
    print("|╰┈➤   Option 2: Employee salary                                          (Press key 2) |")
    print("|╰┈➤   Option 3: Follow the salary                                        (Press key 3) |")
    print("|╰┈➤   Option 4: Staff information                                        (Press key 4) |")
    print("|╰┈➤   Option 5: Calculate student's scores                               (Press key 5) |")
    print("|╰┈➤   Option 6: Funny game                                               (Press key 6) |")
    print("|╰┈➤   Option 0: ＥＸＩＴ                                                 (Press key 0) |")
    print("|_______________________________▔▔▔▔▔▔▔◥ 🧡 ◤▔▔▔▔▔▔▔____________________________________|")

while True:
    menu()
    option = int(input("Enter your option: "))
    while True:
        if option >= 0 and option <=6:
            break
        else:
            option = int(input("Enter your option again: "))
    
    if option == 1:
        while True:
            thang = int(input("Enter the month you want check: "))
            while True:
                if thang < 1 or thang > 12:
                    thang = int(input(""))
                else:
                    break
            print(ngayThang(thang))
            
            stop = input("𝘿𝙤 𝙮𝙤𝙪 𝙬𝙖𝙣𝙩 𝙘𝙤𝙣𝙩𝙞𝙣𝙪𝙚 𝙮/𝙣")
            if stop != "y":
                break

    elif option == 2:
        while True:
            gioLam = float(input("Enter work time:  "))
            luong = float(input("enter your salary: "))
            print(tinh_luong_nhan_vien(gioLam,luong))

            stop = input("𝘿𝙤 𝙮𝙤𝙪 𝙬𝙖𝙣𝙩 𝙘𝙤𝙣𝙩𝙞𝙣𝙪𝙚 𝙮/𝙣")
            if stop != "y":
                break
    
    elif option == 3:
        while True:
            soLuongNhanVien = int(input("Enter number of staff: "))
            list_luong =xap_xep_luong(soLuongNhanVien)
            print()
            print("Danh sach luong tang dan")
            print("__________________________________________________________________________________")
            for i in range(soLuongNhanVien):
                print('| '+ f"{i+1}" , end = " |")
                a = 40 - len(list_luong[i][0])
                print(list_luong[i][0] , end = " "*a)
                sochuso=len(str(list_luong[i][1]))
                b = 25 - sochuso
                print("|  "f"đ{list_luong[i][1]:,.0f} " + " "*b +"|")
                print("|___|________________________________________|___________________________________|")


            stop = input("𝘿𝙤 𝙮𝙤𝙪 𝙬𝙖𝙣𝙩 𝙘𝙤𝙣𝙩𝙞𝙣𝙪𝙚 𝙮/𝙣")
            if stop != "y":
                break

    elif option == 4:
        while True:
            name = input("Enter name of staff: ")            
            fullname,lessname,namee = namenv(name)
            print('ho va ten lot cua nhan vien la: ',lessname)
            print('ten cua nhan vien la: ',namee)
            print('ho va ten day du la: ',fullname) 

            stop = input("𝘿𝙤 𝙮𝙤𝙪 𝙬𝙖𝙣𝙩 𝙘𝙤𝙣𝙩𝙞𝙣𝙪𝙚 𝙮/𝙣")
            if stop != "y":
                break

    elif option == 5:
        while True:
            soMonHoc = int(input("Enter number of subject: "))
            diem,heso = diem_Trung_Binh(soMonHoc)
            print("Number of subject: ",soMonHoc)
            print("Sum of coefficient: ", heso)
            print("AVG of scores :", float(diem/heso))

            stop = input("𝘿𝙤 𝙮𝙤𝙪 𝙬𝙖𝙣𝙩 𝙘𝙤𝙣𝙩𝙞𝙣𝙪𝙚 𝙮/𝙣")
            if stop != "y":
                break

    elif option == 6:
        tai_khoan = 0
        while True:
            menu1()
            option = int(input("Nhap lua chon"))
            while True:
                if option <0 or option > 3:
                    option = int(input("Ban da nhap sai, vui long nhap lai: "))
                else:
                    break

            if option == 1:
                while True:
                    tiennap = int(input("nhap so tien muon nap vao: "))
                    while True:
                        if tiennap <= 0:
                            tiennap = int(input("ban vua nhap sai, vui long nhap lai: "))
                        else:
                            break
                    tai_khoan = tai_khoan + tiennap

                    stopg = input("Ban co muon nap them tien 𝙮/𝙣")
                    if stopg != "y":
                        break

            elif option == 2:
                while True:
                    if tai_khoan == 0:
                        print("tai khoan ban da het, vui long nap them")
                        break
                    else:
                        menu_game()
                        tien_cuoc = int(input("nhap so tien cuoc: "))
                        while True:
                            if tien_cuoc <= 0:
                                tien_cuoc = int(input("Ban vua nhap sai, vui long nhap lai: "))
                            else:
                                break

                        if tien_cuoc > tai_khoan:
                            print("tien cuoc khong du, vui long nap them vao tai khoan")
                            break

                    choose = int(input("Nhap lua chon cua ban"))
                    dem,ket_qua,lua_chon = tom_cua(choose)
                    ketqua = ' '.join(ket_qua)
                    print("Lua chon cua ban la: ",lua_chon)
                    print("Ket qua ra la: ",ketqua)

                    if dem == 0:
                        print("Co",dem," ",lua_chon,"Ban da thua cuoc")
                        tai_khoan = tai_khoan - tien_cuoc
                    else:
                        print("Co",dem," ",lua_chon,"chuc mung ban da chien thang")
                        tai_khoan = tai_khoan + (tien_cuoc * dem )

                    print("So tien con lai trong tai khoan cua ban la:  "f"đ{tai_khoan:,.0f}")

                    stopg = input("𝘿𝙤 𝙮𝙤𝙪 𝙬𝙖𝙣𝙩 𝙘𝙤𝙣𝙩𝙞𝙣𝙪𝙚 𝙮/𝙣")
                    if stopg != "y":
                        break
            elif option == 3:
                print("So tien trong tai khoan cua ban con "f"đ{tai_khoan:,.0f}")
            else:
                stop = input("Ban co muon thoat khoi tro choi      𝙮/𝙣")
                if stop == "y":
                    break


    elif option == 0:
        stop = input("𝐃𝐎 𝐘𝐎𝐔 𝐖𝐀𝐍𝐓 𝐓𝐎 𝐄𝐗𝐈𝐓 𝐌𝐘 𝐏𝐑𝐎𝐆𝐑𝐀𝐌      𝙮/𝙣")
        if stop == "y":
            break
        

print("𝑻𝑯𝑨𝑵𝑲𝑺 𝑭𝑶𝑹 𝑼𝑺𝑰𝑵𝑮 𝑴𝒀 𝑷𝑹𝑶𝑮𝑹𝑨𝑴")
