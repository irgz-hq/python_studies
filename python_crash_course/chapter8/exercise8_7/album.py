def make_album(artist_name, album_title, n_music = None):
    album = {
        "artist name": artist_name.title(),
        "album title": album_title.title(),
        }
    if n_music:
        album["number of musics"] = n_music

    return album

album1 = make_album("Michael Jackson", "Thriller")
album2 = make_album("Racionais", "Sobrevivendo no Inferno")
album3 = make_album("Racionais", "Nada Como Um Dia Após o Outro Dia ", 21)

albums = [album1, album2, album3]

for album in albums:
    print(album)