def make_album(artist_name, album_title, songs=None):
    album = {'artist': artist_name, 'album': album_title}
    if songs:
        album['songs'] = songs
    return album
music = make_album('jimi hendrix', 'are you experienced')
music1 = make_album('the cure', 'crying', 500)
music2 = make_album('cream', 'john barleycorn')
print(music)
print(music1)
print(music2)
