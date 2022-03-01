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
def sifaris():
    print("""
    [1] Sifariş et 
    [2] Qiymətləndir
    """)
    secim = input("Prosses seçin :")
    if secim not in ["1", "2"]:
        print("Belə bir seçim yoxdur...")
        raise "Belə bir seçim yoxdur..."
    if secim == "1":
        zaman10 = datetime.datetime.now()
        cus_id = input("Istifadəçi İD'si :")
        names = "SELECT id,name FROM hotel"
        cursor.execute(names)
        data = cursor.fetchall()
        for i in data:
            print(f"""
                    Hotel ID'si :--->>>> {i[0]}     Hotel adı :--->>>>{i[1]}
                    """)
        hotel = input("Hansı hotel (İD'si) :")
        room_about = "SELECT hr.id,room_number,floor,rt.name,hr.description,price FROM  " \
                     "hotel_room AS hr,hotel AS h, room_type AS rt WHERE h.id=hr.hotel_id and hr.room_type_id=rt.id " \
                     " and h.id=%s"
        cursor.execute(room_about, (hotel,))
        data2 = cursor.fetchall()
        for a in data2:
            print(f""""
>Otax ID'si:->{a[0]}  Otax NO'su:->{a[1]}  Mərtəbə:->{a[2]}   Otax tipi:->{a[3]}   Açıxlama:->{a[4]}    Qiymət:->{a[5]}<    
            """)
        rom_no = input("Otax ID'si seçin :")
        from_date = input("Otelı giriş tarixi :")
        to_datte = input("Oteldən çıxış tarixi :")
        dest = input("Açıxlama :")
        with con:
            with con.cursor() as cursor_1:
                booking = """INSERT INTO 
                booking(customer_id,room_id,from_date,to_date,description,created_at,updated_at)
                         VALUES(%s,%s,%s,%s,%s,%s,%s) RETURNING id"""
                zaman20 = datetime.datetime.now()
                cursor_1.execute(booking, (cus_id, rom_no, from_date, to_datte, dest, zaman10, zaman20))
                id_5 = cursor_1.fetchone()[0]
                servis = "SELECT id,name,price FROM service"
                cursor_1.execute(servis)
                data3 = cursor_1.fetchall()
                for b in data3:
                    print(f"""
                            Servis ID'si:---->>> {b[0]}    Servis ADI:---->>> {b[1]}   Servis dəyəri:---->>> {b[2]}
                            """)
                ser = input("Servis ID'si seçin :")
                booking_servis = "INSERT INTO booking_service(booking_id,service_id,created_at,updated_at)" \
                                 " VALUES(%s,%s,%s,%s)"
                zaman30 = datetime.datetime.now()
                cursor_1.execute(booking_servis, (id_5, ser, zaman10, zaman30))
                deyer = "SELECT price FROM hotel_room WHERE id=%s"
                cursor_1.execute(deyer, (rom_no, ))
                d1 = cursor_1.fetchone()[0]
                deyer2 = "SELECT price FROM service WHERE id=%s"
                cursor_1.execute(deyer2, (ser,))
                d2 = cursor_1.fetchone()[0]
                toplam = d1 + d2
                cs_bl = "SELECT balance FROM customer WHERE id=%s"
                cursor_1.execute(cs_bl, (cus_id,))
                bal = cursor_1.fetchone()[0]
                if bal < toplam:
                    print("Balansınızda kifayət qədər vəsat yoxdur.")
                    raise "Balansınızda kifayət qədər vəsat yoxdur."
                else:
                    hot_bln = "SELECT balance FROM hotel WHERE id=%s"
                    cursor_1.execute(hot_bln, (hotel, ))
                    d3 = cursor_1.fetchone()[0]
                    yekun = d3 + toplam
                    hotel_baln = "UPDATE hotel SET balance=%s WHERE hotel.id=%s"
                    cursor_1.execute(hotel_baln, (yekun, hotel))
                    new_bl = bal - toplam
                    cust = "UPDATE customer SET balance=%s WHERE customer.id=%s"
                    cursor_1.execute(cust, (new_bl, cus_id))
        print(f"""""
        TOPLAM DƏYƏR:
                        Qeydiyyat ID'niz :---->>> {id_5}
                        {toplam} AZN

        """)
    if secim == "2":
        zaman40 = datetime.datetime.now()
        print("QEYDIYYAT ID'nizi GIRIN...")
        rum = input("Qeyydiyyat ID'si :")
        print("Xidmətimizi 1 və 10 arası dəyərləndirin!!")
        rat = input("Xidmətə verdiyiniz dəyər :")
        comment = input("Bizə tövsiyələrinizi yazın :")
        rating = "INSERT INTO rating(booking_id,star,comment,created_at,updated_at) VALUES(%s,%s,%s,%s,%s)"
        zaman60 = datetime.datetime.now()
        cursor.execute(rating, (rum, rat, comment, zaman40, zaman60))
        con.commit()
# hec ne yekunlasdir hazir olarda git-den gonderersen