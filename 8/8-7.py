def make_album(musican_name, musican_album, numb_songs=None):
    if numb_songs:
        musican_info = {'name' : musican_name, 'album' : musican_album, 'songs' : numb_songs}
    else:
        musican_info = {'name' : musican_name, 'album' : musican_album}
    return musican_info

info = make_album('Elvise', 'Karamba')
print(info)
info = make_album('karl', 'mars')
print(info)
info = make_album('otar', 'Kmba')
print(info)
info = make_album('test', 'count', 20)
print(info)