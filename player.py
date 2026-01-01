import os
import sys

# 🔧 FIX VLC DLLs EN WINDOWS
if sys.platform.startswith("win"):
    vlc_path = r"C:\Program Files\VideoLAN\VLC"
    if os.path.exists(vlc_path):
        os.add_dll_directory(vlc_path)

import vlc


class MusicPlayer:
    def __init__(self, music_folder="music"):
        self.music_folder = music_folder
        self.songs = self.load_songs()
        self.current_index = 0
        self.instance = vlc.Instance()
        self.player = self.instance.media_player_new()
        self.volume = 70
        self.player.audio_set_volume(self.volume)

    def load_songs(self):
        if not os.path.exists(self.music_folder):
            print("⚠️ Carpeta de música no encontrada")
            return []

        songs = [
            os.path.join(self.music_folder, f)
            for f in os.listdir(self.music_folder)
            if f.lower().endswith(".mp3")
        ]

        if not songs:
            print("⚠️ No hay archivos MP3 en la carpeta music/")
        return songs

    def play(self):
        if not self.songs:
            print("❌ No hay canciones para reproducir")
            return

        media = self.instance.media_new(self.songs[self.current_index])
        self.player.set_media(media)
        self.player.play()

    def pause(self):
        self.player.pause()

    def toggle_play(self):
        if self.player.is_playing():
            self.pause()
        else:
            self.play()

    def next_song(self):
        if not self.songs:
            return
        self.current_index = (self.current_index + 1) % len(self.songs)
        self.play()

    def previous_song(self):
        if not self.songs:
            return
        self.current_index = (self.current_index - 1) % len(self.songs)
        self.play()

    def forward_10s(self):
        self.player.set_time(self.player.get_time() + 10000)

    def backward_10s(self):
        self.player.set_time(max(0, self.player.get_time() - 10000))

    def volume_up(self):
        self.volume = min(100, self.volume + 10)
        self.player.audio_set_volume(self.volume)

    def volume_down(self):
        self.volume = max(0, self.volume - 10)
        self.player.audio_set_volume(self.volume)


# 🧪 TEST DIRECTO
if __name__ == "__main__":
    import time

    mp = MusicPlayer()
    mp.play()
    time.sleep(5)
    mp.next_song()
    time.sleep(5)
    mp.volume_down()
