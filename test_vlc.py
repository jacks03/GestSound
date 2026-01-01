import vlc
try:
    instance = vlc.Instance()
    print("VLC Instance created successfully")
except Exception as e:
    print(f"Error creating VLC instance: {e}")
