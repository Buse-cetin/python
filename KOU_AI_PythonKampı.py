

def uygulama():
     girdi=input("bir sayı giriniz: ")
     if int(girdi)%2==0:
        print( "{} sayısı bir çift sayıdır".format(girdi))
     else:
        print("{} sayısı bir tek sayıdır".format(girdi))
        uygulama()



        sayaç=0
        sayi=int(input("bir sayı giriniz: "))
        for k in range(2,sayi):
            if sayi%k==0:
                sayaç=sayaç+1
                break
            if sayaç==0:
                print("asal sayı değildir")
            else:
                print("asal sayıdır")



             

def TemizVeri():
    ilk_string="ah5me4t"
    ilk_string="".join([i for i in i in ilk_string if not i.isdigit()])
    ikinci_string="M9eHm4et"
    ikinci_string="".join([i for i in ikinci_string if not i.isdigit()])
    üçüncü_string="".join([i for i in üçüncü_string if not i.isdigit()])
    Birleşmiş_Hali=ilk_string+"-"+ikinci_string+"-"+üçüncü_string
    print(Birleşmis_Hali)
    return(Birleşmiş_Hali)
TemizVeri()

   
    
    

    