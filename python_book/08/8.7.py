# ma_dict = {}
# def make_album(name, album):
#     ma_dict[name] = album
#     return ma_dict
#
# while True:
#     n_ame = input('Vvedite Imya artista:')
#     if n_ame == "q":
#         break
#     a_lbum = input('Vvedite nazvanie alboma:')
#     if a_lbum == "q":
#         break
#     my_dict = make_album(n_ame.title(), a_lbum.title())
# print(ma_dict)

def make_album(name_artist, album, number_trake='0'):
    my_dict = {'artist': name_artist.title(), 'album': album.title()}
    if number_trake != "0":
        my_dict["n_trake"] = number_trake
    return my_dict


aria = make_album('aria', 'shtill', "12")
agata = make_album('agata', 'opium')

print(aria, agata)
