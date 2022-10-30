d = dict()
while True:
    place = input()
    if place == "off":
        print(d)
        break
    else:
        place = int(place)
        isp = input()
        track = input()
        kort = (place, isp)
        d[kort] = track