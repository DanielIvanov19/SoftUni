length = int(input())
width = int(input())
height = int(input())
percent = float(input())
aquarium_volume = length*width*height
volume_in_liters = aquarium_volume/1000
needed_liters = volume_in_liters - volume_in_liters*percent/100
print(needed_liters)