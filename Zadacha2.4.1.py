def volume(h1, h2, v1):
    volume_mute = (h2 / h1) * v1
    return volume_mute


a = volume(12, 9, 2000)

print(a)
