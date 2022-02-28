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
def hotel():
    print("""
    [1] Hotel əlavə edin
    [2] Otax əlavə edin
    [3] Servis əlavə et
    """)
    secim = input("Prosses seçin :")
    if secim not in ["1", "2", "3"]:
        print("Belə bir prosses yoxdur...")
        raise "Belə bir prosses yoxdur..."
    else:
        if secim == "1":
            zaman = datetime.datetime.now()
            hotel_name = input("Hotelin adı :")
            address = input("Hotelin addressi :")
            description = input("Açıxlama :")
            contack = input("Əlaqə məlumatları :")
            hotl = "INSERT INTO hotel(name,address,description,contact_details,created_at,updated_at,balance)" \
                   "VALUES(%s,%s,%s,%s,%s,%s,%s)"
            cursor.execute(hotl, (hotel_name, address, description, contack, zaman, zaman, 0))
            con.commit()
        if secim == "2":
            zamn = datetime.datetime.now()
            names = "SELECT id,name FROM hotel"
            cursor.execute(names)
            data = cursor.fetchall()
            for i in data:
                print(f"""
                Hotel ID'si :--->>>> {i[0]}     Hotel adı :--->>>>{i[1]}
                """)
            # üstdəki otel id siralarina gorə istədiyin otelin idsi
            hotel_id = input("Hansı Hotel (İD'si) :")
            number = input("Otax nömrəsi :")
            mert = input("Otağın mərtəbə NO-su :")
            print("""
            Otaq növün seçin.
            [1] ECENOM
            [2] VIP
            """)
            rom_type = input("Otaq növün seçin :")
            if rom_type not in ["1", "2"]:
                print("SƏf seçim etmisiniz...")
                raise "SƏf seçim etmisiniz..."
            desc = input("Açıxlama :")
            price = input("Otax qiyməti :")
            room = "INSERT INTO hotel_room" \
                   "(hotel_id,room_number,floor,room_type_id,description,price,created_at,updated_at)" \
                   " VALUES(%s,%s,%s,%s,%s,%s,%s,%s)"
            zaman4 = datetime.datetime.now()
            cursor.execute(room, (hotel_id, number, mert, rom_type, desc, price, zamn, zaman4))
            con.commit()
    if secim == "3":
        zaman5 = datetime.datetime.now()
        service_name = input("Servisin adı :")
        serviice_prise = input("Serviin qiyməti :")
        servis = "INSERT INTO service(name,price,created_at,updated_at) VALUES(%s,%s,%s,%s)"
        zaman6 = datetime.datetime.now()
        cursor.execute(servis, (service_name, serviice_prise, zaman5, zaman6))
        con.commit()
