# # This file is about pygame module
#
# from pygame import mixer
#
# mixer.init()
# mixer.music.load("Aksar-Is-Duniya-Mein_(webmusic.in).mp3")
# mixer.music.set_volume(1.0)
# mixer.music.play()

from pygame import mixer

# Starting the mixer
mixer.init()

# Loading the song
mixer.music.load("Aksar-Is-Duniya-Mein_(webmusic.in).mp3")

# Setting the volume
mixer.music.set_volume(0.7)

# Start playing the song
mixer.music.play()

# infinite loop
while True:

    print("Press 'p' to pause, 'r' to resume")
    print("Press 'e' to exit the program")
    query = input(" ")

    if query == 'p':

        # Pausing the music
        mixer.music.pause()
    elif query == 'r':

        # Resuming the music
        mixer.music.unpause()
    elif query == 'e':

        # Stop the mixer
        mixer.music.stop()
        break
