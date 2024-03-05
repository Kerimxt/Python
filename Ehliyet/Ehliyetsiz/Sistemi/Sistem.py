def ehliyet_alabilir_mi():
    yas = int(input("Yaşınızı girin: "))
    surucu_belgesi_var_mi = input("Şu anda bir sürücü belgeniz var mı? (Evet/Hayır): ").lower()
    
    if yas >= 18 and surucu_belgesi_var_mi == "hayır":
        print("Ehliyet alabilirsiniz!")
    else:
        print("Ehliyet alamazsınız.")

ehliyet_alabilir_mi()
