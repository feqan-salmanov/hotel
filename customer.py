import datetime
import psycopg2
con = psycopg2.connect(
    user="postgres",
    password="feqan3.0",
    database="HOTEL_1",
    host="127.0.0.1",
    port="5432"
)
cursor = con.cursor()
def customerin():
    print("""
    [1] Hesaba giriş et
    [2] Hesab yarat 
    [3] Hesaba pul yukle 
    """)
    secim = input("Prosses seçin :")
    if secim not in ["1", "2", "3"]:
        print("Belə bir seçim yoxdur :")
        raise "Belə bir seçim yoxdur"
    if secim == "1":
        customer_id = int(input("Istifadəçi İD'si girin :"))
        cust_id = "SELECT id FROM customer WHERE id=%s"
        cursor.execute(cust_id, (customer_id,))
        cs_id = cursor.fetchall()
        for i in cs_id:
            if i[0] == customer_id:
                password = int(input("Şifrə girin :"))
                customer_password = "SELECT password FROM customer WHERE id=%s"
                cursor.execute(customer_password, (customer_id,))
                password_1 = cursor.fetchall()
                for g in password_1:
                    if g[0] == password:
                        custoemr_about = "SELECT name,surname,phone,balance,created_at,updated_at " \
                                         "FROM customer WHERE id=%s"
                        cursor.execute(custoemr_about, (customer_id,))
                        data = cursor.fetchone()
                        name = data[0]
                        surname = data[1]
                        phone = data[2]
                        balance = data[3]
                        created_at = data[4]
                        updatd_at = data[5]
                        print(f"""
                        CUTOMER :
                                ID              : ---->>>>> {customer_id}
                                Ad              : ---->>>>> {name}
                                Soyad           : ---->>>>> {surname}
                                Telefon         : ---->>>>> {phone}
                                Balans          : ---->>>>> {balance}
                                Yaradılma vaxtı : ---->>>>> {created_at}
                                Yenilənmə vaxtı : ---->>>>> {updatd_at}
                        """)
                    else:
                        print("Parolanı səf girmisiniz...")
                        raise "Parolanı səf girmisiniz..."
            else:
                print("Belə bir hesab yoxdur.")
                raise "Belə bir hesab yoxdur."
    if secim == "2":
        today = datetime.datetime.now()
        print("Hesab yaratmaya xoş gəlmisiniz....")
        ad = input("Adınızı :")
        soyad = input("Soyadınız :")
        telefon = int(input("Telefon nömrəniz :"))
        pasword1 = int(input("Şifrə seçin :"))
        cur_com = "INSERT INTO customer(name,surname,phone,created_at,updated_at,balance,password)" \
                  " VALUES(%s,%s,%s,%s,%s,%s,%s)"
        cursor.execute(cur_com, (ad, soyad, telefon, today, today, 0, pasword1))
        con.commit()
    if secim == "3":
        date = datetime.datetime.now()
        csv_id = input("Istifadəçi İD'si seçin :")
        passw = int(input("Parola girin :"))
        cs_admin = "SELECT password,name,surname,balance FROM customer WHERE id=%s"
        cursor.execute(cs_admin, (csv_id,))
        data = cursor.fetchall()
        for i in data:
            if passw == i[0]:
                print(f"""
                    Istifadəçi adı     : ---->>>> {i[1]}
                    Istifadəçi soyadı  : ---->>>> {i[2]}
                    Istifadəçi balansı : ---->>>> {i[3]}
                                                  """)
                yuklenecek = int(input("Yüklənəcək məbləğ :"))
                if yuklenecek <= 0:
                    print("səf prosses..")
                    raise "səf prosses.."
                else:
                    with con:
                        with con.cursor() as cursor_1:
                            cari_balans = i[3] + yuklenecek
                            cr_bl = "UPDATE customer SET balance=%s,updated_at=%s WHERE id=%s"
                            time = datetime.datetime.now()
                            cursor_1.execute(cr_bl, (cari_balans, time, csv_id))
                            payment = "INSERT INTO customer_payment(customer_id,amount,created_at,updated_at) " \
                                      "VALUES(%s,%s,%s,%s)"
                            cursor_1.execute(payment, (csv_id, yuklenecek, date, time))
                    con.close()
            else:
                print(i[0])
                print("Parolanı səf girmisiniz...")
                raise "Parolanı səf girmisiniz..."
