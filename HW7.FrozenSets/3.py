newspaper = range(1, 76)
magazine = range(77, 104)
both = range(21, 34)
def task(newspaper, magazine, both):
    only_newspaper = (set(newspaper)).difference(set(both))
    only_magazine = (set(magazine)).difference(set(both))
    print(len(only_magazine) + len(only_newspaper) + len(both))
task(newspaper, magazine, both)
