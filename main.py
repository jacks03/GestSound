from player import MusicPlayer
import time

player = MusicPlayer()

print("Reproduciendo música...")
player.play()

time.sleep(5)
print("Pausa")
player.pause()

time.sleep(2)
print("Play otra vez")
player.play()

time.sleep(5)
print("Adelantar 10s")
player.forward_10s()
