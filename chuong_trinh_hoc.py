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
       while True:
           try:
               nam = int(input("Enter the year: "))
               if nam > 0:
                   break
           except ValueError:
               print("Enter the year again")
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
       name = input("Enter name of staff: ")
       list_luong.append(name)
       while True:
           try:
               luong = float(input("Enter the salary of staff: "))
               if luong > 0:
                   break
           except ValueError:
               print("If you entered the wrong input, please try again")      
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
   list_name = []
   namee = ""
   for i in name:
       if i != " ":
           namee += i
       else:
           list_name.append(namee)
           namee = ""
   list_name.append(namee)
   list_nameee = []
   for i in list_name:
       if i != "":
           list_nameee.append(i)
   namee = ""
   list_nameeee = []
   for i in range(len(list_nameee)):
       for j in range(len(list_nameee[i])):
           if j == 0:
               namee = namee + list_nameee[i][j].upper()
           else:
               namee = namee + list_nameee[i][j].lower()
       list_nameeee.append(namee)
       namee = ""
   return list_nameeee
def diem_Trung_Binh(so_mon):
   diem_mon = 0
   diem_tong = 0
   tong_he_so = 0
   for i in range(so_mon):
       while True:
           try:
               diem = float(input(f"subject scores {i+1} : "))
               while True:
                   if diem >= 0 and diem <= 10:
                       break
                   else:
                       diem=float(input("Subject scores range from 0 to 10, please try again: "))
               break
           except ValueError:
               print("If you entered the wrong input, please try again")
             
       while True:
           try:              
               he_so = float(input("Enter subject coefficient: "))
               while True:
                   if he_so >= 1 and he_so <= 3 and he_so % 0.5 == 0:
                       break
                   else:
                       he_so = float(input("The coefficient is between 1 and 3 (Divisible by 0.5), Please trtyh again: "))
               break
           except ValueError:
               print("If you entered the wrong input, please try again")
     
       tong_he_so = tong_he_so + he_so
       diem_mon = diem * he_so
       diem_tong = diem_tong + diem_mon
   return diem_tong,tong_he_so
# Chuc nang 5
def menu1():
   print("option 1. Deposit money into your account")
   print("option 2. Play funny game")
   print("option 3. Check your account")
   print("option 0. Exit game")
def menu_game():
   print("____________________________")
   print("| (1)Tom | (2)Cua | (3)Bau  |")
   print("----------------------------")
   print("| (4)Ca  | (5)Ga  | (6)Huou | ")
   print("-----------------------------")
def tom_cua(choose):
   list_op = ["Tom","Cua","Bau","Ca","Ga","Huou"]
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
       lua_chon = "Huou"
   for i in list_ket_qua:
       if i == lua_chon:
           dem_ket_qua = dem_ket_qua + 1
   return dem_ket_qua,list_ket_qua,lua_chon
def bmi(can_nang,chieu_cao):
   BMI = can_nang/(chieu_cao*chieu_cao)
   tinh_trang = 0
   if BMI <= 18.5:
       tinh_trang = 1
   elif BMI <= 24.9:
       tinh_trang = 2
   elif BMI <= 29.9:
       tinh_trang = 3
   else:
       tinh_trang = 4
   return tinh_trang,BMI
def information():
   print("Full name of author: Tran Hoang Xuan Nguyen")
   print("Nick Name: Xoeng")
   print("Date of birth: 21/06/2005")
   print("Sex: Nam")
   print("interest: Listen to múikc, read book, enjoy the food")
   print("If you have any questions, Contact me: 0373989884")
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
   print("|╰┈➤   Option 3: Salary Management                                        (Press key 3) |")
   print("|╰┈➤   Option 4: Staff information                                        (Press key 4) |")
   print("|╰┈➤   Option 5: Student's scores                                         (Press key 5) |")
   print("|╰┈➤   Option 6: Funny game                                               (Press key 6) |")
   print("|╰┈➤   Option 7: Health Monitoring                                        (Press key 7) |")  
   print("|╰┈➤   Option 8: Author information                                       (Press key 8) |")
   print("|╰┈➤   Option 0: ＥＸＩＴ                                                 (Press key 0) |")
   print("|_______________________________▔▔▔▔▔▔▔◥ 🧡 ◤▔▔▔▔▔▔▔____________________________________|")
while True:
   menu()
   while True:
       try:  
           option = int(input("Enter your option: "))
           while True:              
               if option >= 0 and option <=8:
                   break
               else:
                   option = int(input("Enter your option again: "))
           break
       except ValueError:
           print("Please Try again")
   if option == 1:
       while True:
           while True:
               try:
                   thang = int(input("Enter the month you want check: "))
                   while True:
                       if thang < 1 or thang > 12:
                           thang = int(input("The month from 1 to 12, please try again: "))
                       else:
                           break
                   break
               except ValueError:
                   print("If you entered the wrong input, please try again")
           print(ngayThang(thang))
         
           stop = input("𝘿𝙤 𝙮𝙤𝙪 𝙬𝙖𝙣𝙩 𝙘𝙤𝙣𝙩𝙞𝙣𝙪𝙚 𝙮/𝙣")
           if stop != "y":
               break
   elif option == 2:
       while True:
           while True:
               try:
                   gioLam = float(input("Enter work time:  "))
                   while True:
                       if gioLam > 0:
                           break
                       else:
                           gioLam = float(input("Work time must be greater than 0, please try again: "))
                   break
               except ValueError:
                   print("If you entered the wrong input, please try again: ")
           while True:
               try:
                   luong = float(input("enter your salary: "))
                   while True:
                       if luong > 0:
                           break
                       else:
                           luong = float(input("The salary must be greater than 0, please try again: "))
                   break
               except ValueError:
                   print("If you entered the wrong input, please try again: ")
           print("Your Salary is: ",f"đ{tinh_luong_nhan_vien(gioLam,luong):,.2f}")
           stop = input("𝘿𝙤 𝙮𝙤𝙪 𝙬𝙖𝙣𝙩 𝙘𝙤𝙣𝙩𝙞𝙣𝙪𝙚 𝙮/𝙣")
           if stop != "y":
               break
   elif option == 3:
       while True:
           while True:
               try:
                   soLuongNhanVien = int(input("Enter number of staff: "))
                   if soLuongNhanVien > 0:
                       break
               except ValueError:
                   print("If you entered the wrong input, please try again: ")
           list_luong =xap_xep_luong(soLuongNhanVien)
           print()
           print("LIST OF SALARY")
           print()
           print('| {:^50}|{:^3}|'.format('Name','Salary'))
           print("_______________________________________________________________________________________")
           for i in range(soLuongNhanVien):
               print('| {:<50}|đ{:>30.2f} |'.format(list_luong[i][0],list_luong[i][1]))
           print('|','_'*51,'|','_'*32,'|',sep='')
           stop = input("𝘿𝙤 𝙮𝙤𝙪 𝙬𝙖𝙣𝙩 𝙘𝙤𝙣𝙩𝙞𝙣𝙪𝙚 𝙮/𝙣")
           if stop != "y":
               break
   elif option == 4:
       while True:
           name = input("Enter name of staff: ")        
           list_ten = namenv(name)
           leng = len(list_ten)
           print('Surname and middle name is: ',end = " ")
           for i in range(leng-1):
               print(list_ten[i],end = " ")  
           print()                    
           print('Name of salary is: ',list_ten[leng-1])
           print('Full name is: ', end = " ")
           for i in range(leng):
               print(list_ten[i],end = " ")
           print()
           stop = input("𝘿𝙤 𝙮𝙤𝙪 𝙬𝙖𝙣𝙩 𝙘𝙤𝙣𝙩𝙞𝙣𝙪𝙚 𝙮/𝙣")
           if stop != "y":
               break
   elif option == 5:
       while True:
           while True:
               try:
                   soMonHoc = int(input("Enter number of subject: "))
                   if soMonHoc > 0:
                       break
               except ValueError:
                   print("Please try again")
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
           while True:
               try:
                   option = int(input("Enter your option: "))
                   while True:
                       if option >= 0 and option <= 3:
                           break
                       else:
                           option = int(input("My program have 4 option (0,1,2,3), please try again: "))
                   break
               except ValueError:
                   print("If you entered the wrong input, please try again")
           if option == 1:
               while True:
                   while True:
                       try:
                           tiennap = float(input("Enter the denomination of money you want to deposit into your account: "))
                           while True:
                               if tiennap <= 0:
                                   tiennap =  float(input("The denomination must be greater than 0: "))
                               else:
                                   break
                           break
                       except ValueError:
                           print("If you entered the wrong input, please try again")
                   tai_khoan = tai_khoan + tiennap
                   stopg = input("Do you want to continue 𝙮/𝙣")
                   if stopg != "y":
                       break
           elif option == 2:
               while True:
                   if tai_khoan == 0:
                       print("The account is out of money, please deposit into your account")
                       break
                   else:
                       menu_game()
                       while True:
                           try:
                               tien_cuoc = int(input("Enter the bet amount: "))
                               while True:
                                   if tien_cuoc <= 0:
                                       tien_cuoc = int(input("Please type in again: "))
                                   else:
                                       break
                               break
                           except ValueError:
                               print("If you entered the wrong input, please try again")                  
                       if tien_cuoc > tai_khoan:
                           print("The bet is not enough, please deposit into your account")
                           break
                   while True:
                       try:
                           choose = int(input("Enter your choose"))
                           while True:
                               if choose >= 1 and choose <= 6:
                                   break
                               else:
                                   choose = int(input("Your choice from 1 to 6 , please try again"))
                           break
                       except ValueError:
                           print("If you entered the wrong input, please try again")
                   dem,ket_qua,lua_chon = tom_cua(choose)
                   ketqua = ' '.join(ket_qua)
                   print("Your choose is: ",lua_chon)
                   print("Result is: ",ketqua)
                   if dem == 0:
                       print("Have",dem," ",lua_chon,"You are loser")
                       tai_khoan = tai_khoan - tien_cuoc
                   else:
                       print("Ha",dem," ",lua_chon,"You are winner")
                       tai_khoan = tai_khoan + (tien_cuoc * dem )
                   print("The remaining amount in your account is:  "f"đ{tai_khoan:,.0f}")
                   stopg = input("𝘿𝙤 𝙮𝙤𝙪 𝙬𝙖𝙣𝙩 𝙘𝙤𝙣𝙩𝙞𝙣𝙪𝙚 𝙮/𝙣")
                   if stopg != "y":
                       break
           elif option == 3:
               print("The remaining amount in your account is "f"đ{tai_khoan:,.0f}")
           else:
               stop = input("Do you want to continue      𝙮/𝙣")
               if stop == "y":
                   break
   elif option == 7:
       while True:
           list_chon_an = []
           list_chon_tap = []
           dem_tap = 0
           dem_an = 0
           list_bai_tap = [["running",652],["pedaling",480],
                           ["Body weight",480],["skipping rope",453]
                           ,["indoor cycling",420],["rowing machine exercise",420]
                           ,["aerobic",396],["swimming",396],["jogging slowly",396],["extended walking",340]]
           list_do_an_nhieu = [["beef",250],["chicken thigh meat",177],["chicken breast meat",164],
                       ["pork belly",517],["pork loin",242]
                       ,["salmon",208],["Tuna",129],["shrimp",100],["squid",181],["cheese",353],["avocado",240]
                       ,["Black Chocolate",600]]
           list_do_an_it = [["Wrist",14],["Potato",77],["asparagus",20],["Tomato",20],["cauliflower",34],
                           ["chili",6],["daikon radish",27],["eggplant",27],["carrot"],["chicken egg",45]]
           while True:
               try:
                   can_nang = float(input(' Enter your weight (kg): '))
                   chieu_cao = float(input(" Enter your height (m): "))
                   if chieu_cao > 0 and can_nang > 0:
                       break
               except ValueError:
                   print("Please try again")
           tinh_trang,BMI = bmi(can_nang,chieu_cao)
           print()
           print("Your BMI is: ",round(BMI,2))
           if tinh_trang == 1:
               print("You are underweight, so you should apply eating and exercise methods to increase your body weight. ")
               for i in range(5):
                   mon_an = random.choice(list_do_an_nhieu)
                   list_do_an_nhieu.remove(mon_an)
                   list_chon_an.append(mon_an)
               print("I have a list of hight calories food ")
               print()
               print("_____________________________________________________________________________________")
               for i in range(len(list_chon_an)):
                   print('| {:<50}|{:>30.2f} |'.format(list_chon_an[i][0],list_chon_an[i][1]))
                   dem_an = dem_an + list_chon_an[i][1]
               print('|','_'*51,'|','_'*31,'|',sep='')
               print("By consuming the foods above, you have introduced into your body", dem_an,"calories")
           elif tinh_trang == 2:
               print("You possess a healthy weight and should maintain your regular diet and activities..")
           elif tinh_trang == 3:
               print("You are overweight and should follow a sensible diet plan along with scientific exercise routines to achieve your ideal body shape")
               for i in range(3):
                   bai_tap = random.choice(list_bai_tap)
                   list_bai_tap.remove(bai_tap)
                   list_chon_tap.append(bai_tap)                  
               for i in range(3):
                   mon_an = random.choice(list_do_an_it)
                   list_do_an_it.remove(mon_an)
                   list_chon_an.append(mon_an)
               print("I have a list of exercises ")
               print("_____________________________________________________________________________________")
               for i in range(len(list_chon_tap)):
                   print('| {:<50}|{:>30.2f} |'.format(list_chon_tap[i][0],list_chon_tap[i][1]))
                   dem_tap = dem_tap + list_chon_tap[i][1]
               print('|','_'*51,'|','_'*31,'|',sep='')
               print("By exercising with the above workouts, you have burned", dem_tap,"calories")              
               print()
               print("I have a list of low calories food ")
               print("_____________________________________________________________________________________")
               for i in range(len(list_chon_an)):
                   print('| {:<50}|{:>30.2f} |'.format(list_chon_an[i][0],list_chon_an[i][1]))
                   dem_an = dem_an + list_chon_an[i][1]
               print('|','_'*51,'|','_'*31,'|',sep='')
               print("By consuming the foods above, you have introduced into your body", dem_an,"calories")
           elif tinh_trang == 4:
               print("You are extremely overweight, and this condition can lead to various health issues as well as affect your daily activities")
               for i in range(4):
                   bai_tap = random.choice(list_bai_tap)
                   list_bai_tap.remove(bai_tap)
                   list_chon_tap.append(bai_tap)
               for i in range(3):
                   mon_an = random.choice(list_do_an_it)
                   list_do_an_it.remove(mon_an)
                   list_chon_an.append(mon_an)
               print("I have a list of exercises: ")
               print("_____________________________________________________________________________________")
               for i in range(len(list_chon_tap)):
                   print('| {:<50}|{:>30.2f} |'.format(list_chon_tap[i][0],list_chon_tap[i][1]))
                   dem_tap = dem_tap + list_chon_tap[i][1]
               print('|','_'*51,'|','_'*31,'|',sep='')
               print("By exercising with the above workouts, you have burned", dem_tap,"calories")              
               print()
               print("I have a list of low calories food: ")
               print("_____________________________________________________________________________________")
               for i in range(len(list_chon_an)):
                   print('| {:<50}|{:>30.2f} |'.format(list_chon_an[i][0],list_chon_an[i][1]))
                   dem_an = dem_an + list_chon_an[i][1]
               print('|','_'*51,'|','_'*31,'|',sep='')
               print("By consuming the foods above, you have introduced into your body", dem_an,"calories")
           stop = input("𝘿𝙤 𝙮𝙤𝙪 𝙬𝙖𝙣𝙩 𝙘𝙤𝙣𝙩𝙞𝙣𝙪𝙚 𝙮/𝙣")
           if stop != "y":
                   break
   elif option == 8:
       information()
   elif option == 0:
       stop = input("𝐃𝐎 𝐘𝐎𝐔 𝐖𝐀𝐍𝐓 𝐓𝐎 𝐄𝐗𝐈𝐓 𝐌𝐘 𝐏𝐑𝐎𝐆𝐑𝐀𝐌      𝙮/𝙣")
       if stop == "y":
           break          
os.system("cls")
print("  _______  _                    _             __                            _                                                                                        ")
print(" |__   __|| |                  | |           / _|                          (_)                                                                                      ")
print("    | |   | |__    __ _  _ __  | | __ ___   | |_  ___   _ __    _   _  ___  _  _ __    __ _    _ __ ___   _   _    _ __   _ __  ___    __ _  _ __  __ _  _ __ ___    ")
print("    | |   | '_ \  / _` || '_ \ | |/ // __|  |  _|/ _ \ | '__|  | | | |/ __|| || '_ \  / _` |  | '_ ` _ \ | | | |  | '_ \ | '__|/ _ \  / _` || '__|/ _` || '_ ` _ \   ")
print("    | |   | | | || (_| || | | ||   < \__ \  | | | (_) || |     | |_| |\__ \| || | | || (_| |  | | | | | || |_| |  | |_) || |  | (_) || (_| || |  | (_| || | | | | |  ")
print("    |_|   |_| |_| \__,_||_| |_||_|\_\|___/  |_|  \___/ |_|      \__,_||___/|_||_| |_| \__, |  |_| |_| |_| \__, |  | .__/ |_|   \___/  \__, ||_|   \__,_||_| |_| |_|  ")
print("                                                                                       __/ |               __/ |  | |                  __/ |                          ")
print("                                                                                      |___/               |___/   |_|                 |___/                          ")
