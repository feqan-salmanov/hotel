import hoteladminpanel
import customer
import sifaris
import psycopg2
con = psycopg2.connect(
    user="postgres",
    password="feqan3.0",
    database="HOTEL_1",
    host="127.0.0.1",
    port="5432"
)
cursor = con.cursor()
print("""
[1] Istifadəçi seçimləri
[2] Sifariş
[3] Sayt ADMIN
""")
secim = input("Prosses seçin :")
if secim not in ["1", "2", "3"]:
    print("Belə bir seçim yoxdur :")
    raise "Belə bir seçim yoxdur"
if secim == "1":
    print(customer.customerin())
if secim == "2":
    print(sifaris.sifaris())
if secim == "3":
    print(hoteladminpanel.hotel())


## hee duz yazmisan bele deyirdim

# baxir oz kefine istesen  database qosulmani da bir ayri fayla yazib
# cagira bilersen  birde her defe eyni seyleri tekara tekrar yazmaga ehtiyac qalmasin