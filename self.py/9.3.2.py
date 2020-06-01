def my_mp4_playlist(file_path, new_song):
    music_file = open(file_path, 'r')
    music = music_file.read().split(';\n')
    songs = []
    for element in music:
        songs.append(element.split(';'))
    music_file.close()
    songs[2][0] = new_song
    all_songs = []
    for song in songs:
        all_songs.append(";".join(song))
    all_songs = '\n'.join(all_songs)
    music_file = open(file_path, 'w').writelines(all_songs)
    
    print()
    
my_mp4_playlist(r"C:\Users\owner\Documents\GitHub\python\book\campus\songs.txt", "Python Love Story")