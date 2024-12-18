import datetime
def get_birthday_from_pesel(pesel: int) -> datetime.datetime:
    pesel = pesel2str(pesel)
    rok = pesel[0:2]
    miesiac = pesel[2:4]
    dzien = pesel[4:6]
    plec = pesel[6:10]
    kontrola = pesel[10]
    if miesiac >= 21 and miesiac <= 32:
        miesiac = miesiac - 20
        rok = rok + 2000
    else:
        rok = rok + 1900 
    return datetime.datetime(rok, miesiac, dzien)

def pesel2str(pesel: int) -> str:
    ret = str(pesel)
    while len(ret) != 11:
        ret = "0" + ret 
    return ret 


def get_gender_form_pesel(pesel: int, plec):
    if (pesel[9]) % 2 == 0:
        plec = str("F")
    else: 
        plec = str("M")
    return plec

# def validate_pesel(pesel: int) -> bool:
#     check = (([0][4][8])*1)+(([1][5][9])*3)+(([2][6])*7)+(([3][7])*9)
#     if len(check) == 2:
print(get_birthday_from_pesel(4253645431))
