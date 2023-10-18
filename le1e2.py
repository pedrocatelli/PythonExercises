duration = int(input())

hours = int(duration/3600)
minutes = int((duration % 3600)/60)
seconds = (duration % 3600) % 60

print(f"{hours}:{minutes}:{seconds}")