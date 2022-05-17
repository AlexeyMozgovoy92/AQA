def converter(byn, currency):
    euro=3.2
    usd=2.65
    rur=3030
    if currency=='евро':
        return byn / euro
    elif currency=='доллар':
        return byn / usd
    elif currency=='росруб':
        return byn / rur 
    else:
        return 'неправильная валюта'