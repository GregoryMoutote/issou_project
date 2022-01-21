import mutagen

audioReader = mutagen.File("Musics/megalovania.mp3")
print("Nom de la musique" + str(audioReader["TIT2"]))

print("Auteurs " + str(audioReader["TPE2"]))

print("Desc " + str(audioReader["TXXX:"]))