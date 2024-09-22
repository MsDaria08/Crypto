str = ('Ф ГЛЗИЬ ГИФРЗР-ЗИЕИДШЛ ДРГШНЦЛ КЗИАШУНК ПЛЧУШЪ. ПНФИДЩ НИЗНК И КАРП! ИУРФЯЭЦРУРЗКАК Л, ДШФРЪ, ФИПНЦЛНУКЦР: "ЬЧШ Ъ"')

str = str.lower()
str_len = 0
_map = dict()

prep = ['.', '-', '!', ' ', '"', ':', ',']

for el in str:
    if el not in prep:
        str_len += 1
        if el in _map.keys() and el != ' ':
            _map[el] += 1
        else:
            _map[el] = 1

for el in _map.keys():
    _map[el] = round(_map[el] / str_len, 2)

list_letter = {k: v for k, v in sorted(_map.items(), key=lambda item: item[1])}
for el in list_letter:
    print (el, _map[el])


str = str.replace( 'р', 'А')
str = str.replace( 'л', 'И')
str = str.replace( 'д', 'З')

str = str.replace( 'и', 'О')
str = str.replace( 'з', 'P')
str = str.replace( 'ь', 'Г')
str = str.replace( 'ч', 'Д')

str = str.replace( 'ц', 'Л')
str = str.replace( 'ъ', 'Я')

str = str.replace( 'у', 'Н')
str = str.replace( 'т', 'Ч')
str = str.replace( 'н', 'К')

str = str.replace( 'г', 'П')
str = str.replace( 'ю', 'Ф')
str = str.replace( 'п', 'С')
str = str.replace( 'е', 'Т')

str = str.replace( 'ф', 'В')
str = str.replace( 'ы', 'Х')

str = str.replace( 'ш', 'Е')
str = str.replace( 'с', 'Ц')

str = str.replace( 'ж', 'Й')
str = str.replace( 'о', 'Б')

str = str.replace( 'к', 'У')
str = str.replace( 'а', 'Ж')
str = str.replace( 'щ', 'ь')
str = str.replace( 'я', 'Ы')
str = str.replace( 'э', 'Ш')


print()
print(str)