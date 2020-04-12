def make_album(artist, title, tracks=0):
    """Build a dictionary containing information about an album."""
    album_dict = {
        'artist': artist.title(),
        'title': title.title(),
        }
    if tracks:
        album_dict['tracks'] = tracks
    return album_dict

print("Enter 'q'  to quit")
while True:
    artist = input("Name an artist: ")
    if artist == 'q':
        break
    title = input("What album for that artist: ")
    if title == 'q':
        break

album = make_album(artist, title)
print(album)

# album = make_album('beethoven', 'ninth symphony')
# print(album)

# album = make_album('willie nelson', 'red-headed stranger')
# print(album)