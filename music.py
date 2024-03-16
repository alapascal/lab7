import os
import pygame
from pygame import mixer

pygame.init()

folder = "musicc"
mp3_files = [file for file in os.listdir(folder) if file.endswith(".mp3")]
current_song_index = 0

def plays(index):
    file_path = os.path.join(folder, mp3_files[index])
    mixer.music.load(file_path)
    mixer.music.set_volume(0.7)
    mixer.music.plays()

plays(current_song_index)

while True:
    print(" p - pause, r - resume")
    print("n - next, b - back(previous)")
    print(" e - exit")
    query = input(" ")

    if query == 'p':
        mixer.music.pause()
    elif query == 'u':
        mixer.music.unpause()
    elif query == 'n':
        current_song_index = (current_song_index + 1) % len(mp3_files)
        plays(current_song_index)
    elif query == 'b':
        current_song_index = (current_song_index - 1) % len(mp3_files)
        plays(current_song_index)
    elif query == 'e':
        exit
        break