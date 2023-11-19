def make_album(artist_name, album_title, n_music = None):
    album = {
        "artist name": artist_name.title(),
        "album title": album_title.title(),
        }
    if n_music:
        album["number of musics"] = n_music

    return album

print("Digit q any time for exit the program")
while True:
    artist_name = input("\nDigit the artist name: ")
    if artist_name == "q":
        break
    album_title = input("Digit the album title: ")
    if album_title == "q":
        break
    n_music = input("Digit the number of musics or no: ")
    if n_music == "q":
        break
    print(make_album(artist_name, album_title, n_music))
