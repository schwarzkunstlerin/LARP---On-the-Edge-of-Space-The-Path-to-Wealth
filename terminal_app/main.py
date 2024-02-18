#!/usr/bin/env python3

import time
import os
import getpass
import random

from simple_term_menu import TerminalMenu
from ascii import title, root
from datetime import datetime

usernames = {
    "burgenshfert": "hanshanshans",
    "gustafson": "gusti",
    "kathri": "ahri2137",
    "sawuszkin": "slavic_pow3r",
    "silvestri": "blackrose",
    "smith": "hackerman69",
    "smithson": "t_smithson",
    "stefański": "slava_star",
    "wellingmoor": "well_well",
    "wirgonsin": "wirgi_virgin"
}

passwords = {
    "burgenshfert": "hamburger99",
    "gustafson": "gusti1234",
    "kathri": "mk-hunti-58",
    "sawuszkin": "wielkaLechia555",
    "silvestri": "s3v3rus",
    "smith": "94061508557",
    "smithson": "syrenka",
    "stefański": "1234567890",
    "wellingmoor": "wellingmoor$U",
    "wirgonsin": "ZXSPE21IHtmDZcw"
}

hackerman = []

places = {"pas asteroid X-12": "niebezpieczne, obecność sporej ilości metali ciężkich",
          "pas asteroid BBG-453": "umiarkowanie niebezpieczne, obecność sporej ilości metali ciężkich",
          "pas asteroid BN-1": "silne zakłócenia, skan niemożliwy",
          "pas asteroid Nuah-Men": "niebezpieczne, obecność sporej ilości metali ciężkich i ropy",
          "mgławica magnetyczna XRS-2313": "lekkie zakłócenia, skan niemożliwy",
          "mgławica magnetyczna XER-454": "ciężkie zakłócenia, skan niemożliwy",
          "mgławica magnetyczna XSR-31": "brak anomalii, obecność ropy i pierwiastków kosmicznych",
          "planetoida skalna P-342": "piorytet, wykryto duże ilości ropy i pierwiastków kosmicznych",
          "planetoida skalna P-989": "piorytet, wykryto duże ilości pierwiastków kosmicznych",
          "planetoida skalna P-767": "bezpieczne, umiarkowana ilość ropy i pierwiastków kosmicznych",
          "wrak CSS Manjaro": "brak oznak życia, wykryto zasoby w magazynie",
          "wrak CSS Xentoss": "brak oznak życia, wykryto zasoby w magazynie",
          "wrak USS Enterprise": "brak oznak życia, wykryto zasoby w magazynie",
          "wrak USS Discovery": "silne zakłócenia, skan niemożliwy"}

lottery = False

from pygments import formatters, highlight, lexers
from pygments.util import ClassNotFound
from simple_term_menu import TerminalMenu


def return_menu(username):
    options = [
        "[0] powrót"
    ]
    default_private_terminal_menu = TerminalMenu(options)
    menu_entry_index = default_private_terminal_menu.show()
    if menu_entry_index == 0:
        default_private_system_menu(username)


def return_menu_without_user():
    options = [
        "[0] powrót"
    ]
    default_private_terminal_menu = TerminalMenu(options)
    menu_entry_index = default_private_terminal_menu.show()
    if menu_entry_index == 0:
        main()


def return_menu_without_user_to_main():
    options = [
        "[0] powrót"
    ]
    default_private_terminal_menu = TerminalMenu(options)
    menu_entry_index = default_private_terminal_menu.show()
    if menu_entry_index == 0:
        main()


def read_well_mail(file_name):
    filepath = f"mail/wellingmoor/{file_name}"
    with open(filepath, "r") as f:
        file_content = f.read()
    try:
        lexer = lexers.get_lexer_for_filename(filepath, stripnl=False, stripall=False)
    except ClassNotFound:
        lexer = lexers.get_lexer_by_name("text", stripnl=False, stripall=False)
    formatter = formatters.TerminalFormatter(bg="dark")  # dark or light
    highlighted_file_content = highlight(file_content, lexer, formatter)
    return highlighted_file_content


def read_stef_mail(file_name):
    filepath = f"mail/stefański/{file_name}"
    with open(filepath, "r") as f:
        file_content = f.read()
    try:
        lexer = lexers.get_lexer_for_filename(filepath, stripnl=False, stripall=False)
    except ClassNotFound:
        lexer = lexers.get_lexer_by_name("text", stripnl=False, stripall=False)
    formatter = formatters.TerminalFormatter(bg="dark")  # dark or light
    highlighted_file_content = highlight(file_content, lexer, formatter)
    return highlighted_file_content


def read_smithson_mail(file_name):
    filepath = f"mail/smithson/{file_name}"
    with open(filepath, "r") as f:
        file_content = f.read()
    try:
        lexer = lexers.get_lexer_for_filename(filepath, stripnl=False, stripall=False)
    except ClassNotFound:
        lexer = lexers.get_lexer_by_name("text", stripnl=False, stripall=False)
    formatter = formatters.TerminalFormatter(bg="dark")  # dark or light
    highlighted_file_content = highlight(file_content, lexer, formatter)
    return highlighted_file_content


def read_smi_mail(file_name):
    filepath = f"mail/smith/{file_name}"
    with open(filepath, "r") as f:
        file_content = f.read()
    try:
        lexer = lexers.get_lexer_for_filename(filepath, stripnl=False, stripall=False)
    except ClassNotFound:
        lexer = lexers.get_lexer_by_name("text", stripnl=False, stripall=False)
    formatter = formatters.TerminalFormatter(bg="dark")  # dark or light
    highlighted_file_content = highlight(file_content, lexer, formatter)
    return highlighted_file_content


def read_sil_mail(file_name):
    filepath = f"mail/silvestri/{file_name}"
    with open(filepath, "r") as f:
        file_content = f.read()
    try:
        lexer = lexers.get_lexer_for_filename(filepath, stripnl=False, stripall=False)
    except ClassNotFound:
        lexer = lexers.get_lexer_by_name("text", stripnl=False, stripall=False)
    formatter = formatters.TerminalFormatter(bg="dark")  # dark or light
    highlighted_file_content = highlight(file_content, lexer, formatter)
    return highlighted_file_content


def read_saw_mail(file_name):
    filepath = f"mail/sawuszkin/{file_name}"
    with open(filepath, "r") as f:
        file_content = f.read()
    try:
        lexer = lexers.get_lexer_for_filename(filepath, stripnl=False, stripall=False)
    except ClassNotFound:
        lexer = lexers.get_lexer_by_name("text", stripnl=False, stripall=False)
    formatter = formatters.TerminalFormatter(bg="dark")  # dark or light
    highlighted_file_content = highlight(file_content, lexer, formatter)
    return highlighted_file_content


def read_kath_mail(file_name):
    filepath = f"mail/kathri/{file_name}"
    with open(filepath, "r") as f:
        file_content = f.read()
    try:
        lexer = lexers.get_lexer_for_filename(filepath, stripnl=False, stripall=False)
    except ClassNotFound:
        lexer = lexers.get_lexer_by_name("text", stripnl=False, stripall=False)
    formatter = formatters.TerminalFormatter(bg="dark")  # dark or light
    highlighted_file_content = highlight(file_content, lexer, formatter)
    return highlighted_file_content


def read_gust_mail(file_name):
    filepath = f"mail/gustafson/{file_name}"
    with open(filepath, "r") as f:
        file_content = f.read()
    try:
        lexer = lexers.get_lexer_for_filename(filepath, stripnl=False, stripall=False)
    except ClassNotFound:
        lexer = lexers.get_lexer_by_name("text", stripnl=False, stripall=False)
    formatter = formatters.TerminalFormatter(bg="dark")  # dark or light
    highlighted_file_content = highlight(file_content, lexer, formatter)
    return highlighted_file_content


def read_bur_mail(file_name):
    filepath = f"mail/burgenshfert/{file_name}"
    with open(filepath, "r") as f:
        file_content = f.read()
    try:
        lexer = lexers.get_lexer_for_filename(filepath, stripnl=False, stripall=False)
    except ClassNotFound:
        lexer = lexers.get_lexer_by_name("text", stripnl=False, stripall=False)
    formatter = formatters.TerminalFormatter(bg="dark")  # dark or light
    highlighted_file_content = highlight(file_content, lexer, formatter)
    return highlighted_file_content


def list_files(username):
    directory = f"/home/wiktoria/Desktop/last-stand/mail/{username}" + "/"
    return (file for file in os.listdir(directory) if os.path.isfile(os.path.join(directory, file)))


def read_mail(username):
    clear_terminal()
    print_title()
    print_username(username)
    current_datetime()
    print(f"Masz {len(list(list_files(username)))} wiadomości.\nBy powrócić do menu, kliknij [Enter].\n")

    if username == "wellingmoor":
        terminal_menu = TerminalMenu(list_files(username), preview_command=read_well_mail, preview_size=0.75, title="Skrzynka odbiorcza")
        menu_entry_index = terminal_menu.show()
    elif username == "stefański":
        terminal_menu = TerminalMenu(list_files(username), preview_command=read_stef_mail, preview_size=0.75, title="Skrzynka odbiorcza")
        menu_entry_index = terminal_menu.show()
    elif username == "smithson":
        terminal_menu = TerminalMenu(list_files(username), preview_command=read_smithson_mail, preview_size=0.75, title="Skrzynka odbiorcza")
        menu_entry_index = terminal_menu.show()
    elif username == "smith":
        terminal_menu = TerminalMenu(list_files(username), preview_command=read_smi_mail, preview_size=0.75, title="Skrzynka odbiorcza")
        menu_entry_index = terminal_menu.show()
    elif username == "silvestri":
        terminal_menu = TerminalMenu(list_files(username), preview_command=read_sil_mail, preview_size=0.75, title="Skrzynka odbiorcza")
        menu_entry_index = terminal_menu.show()
    elif username == "sawuszkin":
        terminal_menu = TerminalMenu(list_files(username), preview_command=read_saw_mail, preview_size=0.75, title="Skrzynka odbiorcza")
        menu_entry_index = terminal_menu.show()
    elif username == "kathri":
        terminal_menu = TerminalMenu(list_files(username), preview_command=read_kath_mail, preview_size=0.75, title="Skrzynka odbiorcza")
        menu_entry_index = terminal_menu.show()
    elif username == "gustafson":
        terminal_menu = TerminalMenu(list_files(username), preview_command=read_gust_mail, preview_size=0.75, title="Skrzynka odbiorcza")
        menu_entry_index = terminal_menu.show()
    else:
        terminal_menu = TerminalMenu(list_files(username), preview_command=read_bur_mail, preview_size=0.75, title="Skrzynka odbiorcza")
        menu_entry_index = terminal_menu.show()
    return_menu(username)


def current_datetime():
    now = datetime.now()
    year = int(now.year) + 1000
    now_string = now.strftime("%H:%M:%S %d/%m/" + str(year) + ".0143")
    print(f"\nAKTUALNY CZAS GWIEZDNY: {now_string}\n")


def print_title():
    print(title + "\n")


def print_username(username):
    print(f"PRYWATNY SYSTEM: {username}")


def clear_terminal():
    os.system("clear")


def get_calc_info(username, type1):
    path = str(type1) + "/" + username + ".txt"
    with open(path) as file:
        money = file.readlines()
        return "".join(money)


def write_calc_info(username, type1, value):
    path = str(type1) + "/" + username + ".txt"
    open(path, "w").close()
    file = open(path, "w")
    file.write(str(value))
    file.close()

def get_money_info_statekmatka():
    path = "statek-matka/money.txt"
    with open(path) as file:
        money = file.readlines()
        return "".join(money)


def write_money_info_statekmatka(value):
    path = "statek-matka/money.txt"
    open(path, "w").close()
    file = open(path, "w")
    file.write(str(value))
    file.close()


def write_ubezpieczenie_info(username, value, cel):
    path = "ubezpieczenie/" + username + ".txt"
    file = open(path, "a")
    file.write(f"Kwota: {str(value)} - Cel: {cel}\n")
    file.close()


def print_money_info(username, money):
    clear_terminal()
    print_title()
    print_username(username)
    current_datetime()
    print("\nTwój aktualny stan konta debetowego: " + money + "\n")
    return_menu(username)


def print_money_info_without_menu(username, money):
    clear_terminal()
    print_title()
    print_username(username)
    current_datetime()
    print("\nTwój aktualny stan konta debetowego: " + money + "\n")


def print_rent_info(username, money):
    clear_terminal()
    print_title()
    print_username(username)
    current_datetime()
    print("\nTwój aktualny stan konta emerytalnego: " + money + "\n")
    return_menu(username)


def print_available_places(lista_miejsc):
    print("\nWykryto poniższe miejsca:\n")
    for place in lista_miejsc:
        print(f"MIEJSCE: {place} --- WYNIK SKANU: {places[place]}")


def wpisz_transakcje(kto, ile, typ, cena, korpo):
    file = open("statek-matka/lista-transakcji.txt", 'a')
    file.write(f"{kto} - {korpo} - {typ} - {cena} - {ile}\n")
    file.close()


def wpisz_transakcje_hajsu(kto, ile, komu):
    file = open("statek-matka/kredyty-transakcje.txt", 'a')
    file.write(f"OD: {kto} - DO {komu} - {ile}\n")
    file.close()


def scan():
    places_available = []
    places_names = list(places.keys())
    print("Skanowanie w toku...")
    time.sleep(1)
    print(".")
    time.sleep(1)
    print("..")
    time.sleep(1)
    print("...")
    time.sleep(1)
    print("....")
    time.sleep(1)
    print(".....")
    for x in range(3):
        i = random.randint(0, len(places))
        places_available.append(places_names[i])
    print_available_places(places_available)
    return_menu_without_user_to_main()


def wydobycie():
    clear_terminal()
    print_title()
    current_datetime()
    print("\nROZPOCZĘTO PROCEDURĘ WYDOBYCIA...")
    miejsce = input("Podaj DOKŁADNE miejsce, gdzie będzie przeprowadzany odwiert: ")
    while miejsce not in places.keys():
        print("Nieprawidłowo podane współrzędne!\n")
        miejsce = input("Podaj DOKŁADNE miejsce: ")
    print("Wydobycie w toku...")
    time.sleep(1)
    print(".")
    time.sleep(1)
    print("..")
    time.sleep(1)
    print("...")
    time.sleep(1)
    print("....")
    time.sleep(1)
    print(".....")
    print("Nawiązywanie połączenia z robotnikami...")
    print("Otwórz Discord i podłącz się do kanału głosowego...")
    time.sleep(1)
    print(".")
    time.sleep(1)
    print("..")
    time.sleep(1)
    print("...")
    time.sleep(1)
    print("....")
    time.sleep(1)
    print(".....")
    print("Procedury zakończone. Poczekaj na powrót robotników z miejsca wydobycia.\nZalecany kontakt w eterze.")
    del places[miejsce]
    return_menu_without_user_to_main()


def ubezpieczenie(username):
    clear_terminal()
    print_title()
    print_username(username)
    current_datetime()
    print_money_info_without_menu(username, get_calc_info(username, "money"))
    curr_money = get_calc_info(username, "money")
    print("Ubezpieczenie pozwala Ci przenieść część Twoich środków\nna specjalny cel. Kredyty zostaną wypłacone zgodnie z celem\nw przypadku spełnienia konkretnych warunków.")
    decision = input("Czy chcesz wykupić ubezpieczenie? [tak]/[nie]\n")
    if decision == "tak":
        amount = input("Ile pieniędzy chcesz przeznaczyć na ubezpieczenie? Podaj kwotę: ")
        while int(amount) > int(curr_money):
            print("Nie masz tyle pieniędzy!\n")
            amount = input("Podaj inną kwotę: ")
        point = input("Na jaki cel chcesz przeznaczyć kwotę? Podaj cel i warunek, kiedy ma wyst: ")
        write_calc_info(username, "money", int(curr_money) - int(amount))
        write_ubezpieczenie_info(username, amount, point)
        print("Poprawnie przeprowadzono procedurę.")
        return_menu(username)
    else:
        return_menu(username)


def komora(username):
    clear_terminal()
    print_title()
    print_username(username)
    current_datetime()
    print_money_info_without_menu(username, get_calc_info(username, "money"))
    curr_money = get_calc_info(username, "money")
    print("Komora medyczna pozwala Ci wyleczyć jeden Stan.\nKoszt: 2000")
    decision = input("Czy chcesz wykupić jedną sesję w komorze? [tak]/[nie]\n")
    if decision == "tak":
        while 2000 > int(curr_money):
            print("Nie masz tyle pieniędzy!\n")
            return_menu(username)
            break
        write_calc_info(username, "money", int(curr_money) - 2000)
        print("Poprawnie przeprowadzono procedurę.\nPoczekaj, aż Wirtualna Inteligencja CSS Illiria wezwie Cię na sesję w komorze medycznej.")
        return_menu(username)
    else:
        return_menu(username)


def login():
    clear_terminal()
    print_title()
    current_datetime()
    login1 = input("Podaj login: ")
    password = getpass.getpass("Podaj hasło: ")
    if login1 not in usernames.values() or password not in passwords.values():
        print("BŁĄD! Login lub hasło jest nieprawidłowe!")
        print("Resetowanie...")
        time.sleep(1)
        print(".")
        time.sleep(1)
        print("..")
        time.sleep(1)
        print("...")
        main()

    for n, l in usernames.items():
        if l == login1:
            return n


def transakcja_surowców():
    print("START PROCEDURY TRANSAKCJI SUROWCÓW")
    print("Łączenie z siecią międzygalaktyczną...")
    time.sleep(1)
    print(".")
    time.sleep(1)
    print("..")
    time.sleep(1)
    print("...")
    nazwisko = input("Podaj nazwisko osoby, przeprowadzającej transakcję: ")
    firma = input("Podaj korporację, której chcesz przekazać surowce: ")
    rodzaj = input("Podaj rodzaj wysyłanych surowców: ")
    cena = input("Podaj aktualną cenę, zgodnie z Cennikiem: ")
    ilosc = input("Podaj ilość wysyłanych surowców: ")
    print("PROCESOWANIE...")
    time.sleep(1)
    print(".")
    time.sleep(1)
    print("..")
    time.sleep(1)
    print("...")
    time.sleep(1)
    print("....")
    time.sleep(1)
    print(".....")
    nagroda = int(cena) * int(ilosc)
    aktualna_nagroda = get_money_info_statekmatka()
    value_do_wpisania = int(aktualna_nagroda) + (nagroda)
    write_money_info_statekmatka(str(value_do_wpisania))
    wpisz_transakcje(nazwisko, ilosc, rodzaj, cena, firma)
    print("TRANSAKCJA ZAINICJOWANA\nWybrane surowce należy umieścić w terminalu.")
    print("Kredyty zostaną przelane na konto statku-matki, pracownicy są zobowiązany do rozdzielenia ich\nwe własnym zakresie.")
    return_menu_without_user_to_main()


def loteria(username):
    if not lottery:
        clear_terminal()
        print_title()
        print_username(username)
        current_datetime()
        print_money_info_without_menu(username, get_calc_info(username, "money"))
        curr_money = get_calc_info(username, "money")
        print("Witaj w międzygalaktycznej loterii!\nKoszt losu to 10 Kredytów.\nKUMULACJA! Tylko teraz możesz wygrać 99 999 Kredytów!")
        decision = input("Czy chcesz wykupić jeden los? [tak]/[nie]\n")
        if decision == "tak":
            while 10 > int(curr_money):
                print("Nie masz tyle pieniędzy!\n")
                return_menu(username)
                break
            write_calc_info(username, "money", int(curr_money) - 10)
            print("Losowanie...")
            time.sleep(1)
            print(".")
            time.sleep(1)
            print("..")
            time.sleep(1)
            print("...")
            time.sleep(1)
            print("....")
            time.sleep(1)
            print(".....")
            los = random.randint(1, 100000000)
            if los == 1:
                print("WYGRAŁEŚ!")
                print("GRATULACJE!!!")
                print("W ciągu kilku minut na Twoim koncie pojawią się środki.\nBaw się dobrze!")
            else:
                print("BRAK WYGRANEJ - ch000j Ci w dupę! :)")
            return_menu(username)
        else:
            return_menu(username)
    else:
        print("Aktualnie loteria nie jest przeprowadzana.\nSpróbuj kiedy indziej.")
        return_menu(username)


def żabka(username):
    clear_terminal()
    print_title()
    print_username(username)
    current_datetime()
    print_money_info_without_menu(username, get_calc_info(username, "money"))
    curr_money = get_calc_info(username, "money")
    print("COSMIC ŻABKA NANOSHOP\n")
    print("Aby złożyć zamówienie, wybrany produkt należy zgłosić do Wirtualnej Inteligencji statku-matki.\n")
    print("Aby wyjść, naciśnij [Enter].")
    options = ["[1] kawa - 300",
               "[2] herbata - 500",
               "[3] czekolada - 500",
               "[4] makaron w sosie pomidorowym - 350",
               "[5] jabłka - 400",
               "[6] owoce z drukarki 5D - 400",
               "[7] narkotyki - 100",
               "[8] lekarstwo - 1000"]
    terminal_menu = TerminalMenu(options, title="Dostępny asortyment")
    menu_entry_index = terminal_menu.show()
    return_menu(username)


def default_private_system_menu(username):
    clear_terminal()
    print_title()
    print_username(username)
    current_datetime()
    options = [
        "[1] sprawdź stan konta debetowego",
        "[2] sprawdź stan konta emerytalnego",
        "[3] wykonaj transakcję pomiędzy kontami",
        "[4] wykup ubezpieczenie",
        "[e] poczta e-mail",
        "[c] otwórz korporacyjny sklepik 'COSMIC ŻABKA NANOSHOP'",
        "[d] otwórz korporacyjny sklepik 'EARTH CONGLOMERATE SHOP",
        "[m] wykup dostęp do komory medycznej",
        "[l] puść los na loterii międzygalaktycznej",
        "[x] wyloguj"
    ]
    default_private_terminal_menu = TerminalMenu(options, title="Menu terminala:")
    menu_entry_index = default_private_terminal_menu.show()

    if menu_entry_index == 0:
        print_money_info(username, get_calc_info(username, "money"))
    elif menu_entry_index == 1:
        print_rent_info(username, get_calc_info(username, "rent"))
    elif menu_entry_index == 2:
        print("Transakcje bankowe są chwilowo niedostępne.\nSpróbuj kiedy indziej.")
        time.sleep(1)
        print(".")
        time.sleep(1)
        print(".")
        time.sleep(1)
        print(".")
        return_menu(username)

    elif menu_entry_index == 3:
        ubezpieczenie(username)
    elif menu_entry_index == 4:
        read_mail(username)
    elif menu_entry_index == 5:
        żabka(username)
    elif menu_entry_index == 6:
        print("Korporacyjny sklepik 'EARTH CONGLOMERATE SHOP jest chwilowo niedostępny.\nSpróbuj kiedy indziej.")
        time.sleep(1)
        print(".")
        time.sleep(1)
        print(".")
        time.sleep(1)
        print(".")
        return_menu(username)
    elif menu_entry_index == 7:
        komora(username)
    elif menu_entry_index == 8:
        loteria(username)
    else:
        main()


def hackerman_system_menu(username):
    clear_terminal()
    print_title()
    print(root + "\n")
    print(f"PRYWATNY SYSTEM: {username}")
    current_datetime()
    options = [
        "[1] sprawdź stan konta debetowego",
        "[2] sprawdź stan konta emerytalnego",
        "[3] wykonaj transakcję pomiędzy kontami",
        "[4] wykup ubezpieczenie",
        "[e] poczta e-mail",
        "[c] otwórz korporacyjny sklepik 'COSMIC ŻABKA NANOSHOP'",
        "[d] otwórz korporacyjny sklepik 'EARTH CONGLOMERATE SHOP",
        "[m] wykup dostęp do komory medycznej",
        "[l] puść los na loterii międzygalaktycznej",
        "hackuj innych użytkowników SpaceLink",
        "[x] wyloguj"
    ]
    default_private_terminal_menu = TerminalMenu(options, title="Menu terminala:")
    menu_entry_index = default_private_terminal_menu.show()

    if menu_entry_index == 0:
        ...
    elif menu_entry_index == 1:
        ...
    elif menu_entry_index == 2:
        ...
    elif menu_entry_index == 3:
        ...
    elif menu_entry_index == 4:
        ...
    elif menu_entry_index == 5:
        ...
    elif menu_entry_index == 6:
        ...
    elif menu_entry_index == 7:
        ...
    elif menu_entry_index == 8:
        ...
    elif menu_entry_index == 9:
        ...
    else:
        main()


def kredyty_pomiedzy():
    print("START PROCEDURY ROZDYSPONOWANIA KREDYTÓW")
    print("Łączenie z siecią międzygalaktyczną...")
    time.sleep(1)
    print(".")
    time.sleep(1)
    print("..")
    time.sleep(1)
    print("...")
    aktualne = get_money_info_statekmatka()
    print(f"AKTUALNE KREDYTY CSS ILLIRIA: {aktualne}")
    nazwisko = input("Podaj nazwisko osoby, przeprowadzającej transakcję: ")
    docelowy = input("Podaj nazwisko osoby, której chcesz przekazać kredyty: ")
    ilosc = input("Podaj ilość wysyłanych kredytów: ")
    print("PROCESOWANIE...")
    time.sleep(1)
    print(".")
    time.sleep(1)
    print("..")
    time.sleep(1)
    print("...")
    time.sleep(1)
    print("....")
    time.sleep(1)
    print(".....")
    aktualna_nagroda = get_calc_info(docelowy.lower(), "money")
    value_do_wpisania = int(aktualna_nagroda) + int(ilosc)
    write_calc_info(docelowy.lower(), "money", value_do_wpisania)
    wpisz_transakcje_hajsu(nazwisko, docelowy, ilosc)
    print("TRANSAKCJA ZAKOŃCZONA")
    return_menu_without_user_to_main()


def main():
    clear_terminal()
    print_title()
    print("STATEK-MATKA: CSS Illiria")
    print("SYSTEMY PODTRZYMYWANIA ŻYCIA: online")
    print("SYSTEMY WIRTUALNEJ INTELIGENCJI: online")
    print("POŁĄCZENIE Z SIECIĄ MIĘDZYPLANETARNĄ: tak")
    current_datetime()
    options = ["[z] zaloguj się do prywatnego systemu",
               "[s] skanuj okolicę",
               "[p] przeprowadź transakcję surowców",
               "[r] rozdysponuj Kredyty pomiędzy załogą",
               "[w] zainicjuj procedurę wydobycia"]
    terminal_menu = TerminalMenu(options, title="Menu operacyjne:")
    menu_entry_index = terminal_menu.show()

    if menu_entry_index == 0:
        username = login()
        if username in hackerman:
            hackerman_system_menu(username)
        else:
            default_private_system_menu(username)
        #default_private_system_menu("wellingmoor")
    elif menu_entry_index == 1:
        scan()
    elif menu_entry_index == 2:
        transakcja_surowców()
    elif menu_entry_index == 3:
        kredyty_pomiedzy()
    else:
        wydobycie()


if __name__ == "__main__":
    main()
