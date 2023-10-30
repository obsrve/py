def make_album(musican_name, musican_album, numb_songs=None):
    if numb_songs:
        musican_info = {'name' : musican_name, 'album' : musican_album, 'songs' : numb_songs}
    else:
        musican_info = {'name' : musican_name, 'album' : musican_album}
    return musican_info

while True:
    print('\nEnter musican name and album:')
    print('(q is to quit)')

    name = input('Name:')
    if name == 'q':
        break
    album = input('Album:')
    if album == 'q':
        break

    call = make_album(name, album)
    print(call)

