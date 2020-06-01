from collections import Counter

def my_mp3_playlist(file_path):
    music_file = open(file_path, 'r').read().split(';\n')
    songs = []
    for element in music_file:
        songs.append(element.split(';'))
    mp3_dict = {}

    song_names = []
    max_len = 0
    for name in songs:
        name[2] = float(name[2].replace(':', '.'))

    longest_song_length = max(map(lambda x: x[2], songs))
    longest_song_name = [ listt[0] for listt in songs if longest_song_length in listt]
    num_of_songs = len(songs)

    artists = []
    max_artist_appears = ''
    for artist in songs:
        artists.append(artist[1])
        if artists.count(artist[1]) > max_len:
            max_len = artists.count(artist[1])
            max_artist_appears = artist[1]
    return (''.join(longest_song_name), num_of_songs, max_artist_appears)

print(my_mp3_playlist(r"C:\Users\owner\Documents\GitHub\python\book\campus\songs.txt"))