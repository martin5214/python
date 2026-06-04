
uzivatelske_jmeno = "stavebnik"
heslo = "stavba"
zadane_uzivatelske_jmeno= input("Zadej uživatelské jméno: ")
zadane_heslo = input("Zadej heslo: ")
if zadane_uzivatelske_jmeno == uzivatelske_jmeno and zadane_heslo == heslo:
    print("úspěšně jste se přihlásily")
else:
        print("zadali jste špatné uživatelské jméno nebo heslo ") 

plocha_tvarnice = 0.1
delka_steny = int(input("Zadej délku stěny (metry): "))
vyska_steny = int(input("Zadej výšku stěny (metry): "))
vyska_okna = int(input("Zadej výšku okna (metry): "))
delka_okna = int(input("Zadej délku okna (metry): "))
plocha_steny_s_oknem = delka_steny * (vyska_steny) + delka_okna * (vyska_okna)
plocha_okna = delka_okna * (vyska_okna)
plocha_steny_bez_okna = plocha_steny_s_oknem - plocha_okna
print(f"Plocha stěny včetně okna : {plocha_steny_s_oknem}.m^2")
print(f"Plocha okna : {plocha_okna}.m^2")
print(f"Plocha stěny bez okna : {plocha_steny_bez_okna}.m^2")
potrebnych_tvarnic = plocha_steny_bez_okna / (plocha_tvarnice)
print(f"počet tvárnic potřebných k vyzdění plochy stěny : {potrebnych_tvarnic} ks")

print("Dostupnost materiálu na pobočkách v ČR")
print("*" * 38)


print("| Město    | Druh materiálu | Počet kusů na pobočce |")
print("*" * 53)


print("| Praha    | tvárnice       | 500                   |")
print("| Brno     | tvárnice       | 300                   |")
print("| Ostrava  | tvárnice       | 700                   |")