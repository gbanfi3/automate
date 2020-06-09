# assert False, "hello üzenet"
lampa = {"NS": "green", "EW": "red"}

def switchLamp(intersection):
    for key in intersection.keys():
        if intersection[key] == "green":
            intersection[key] = "yellow"
        elif intersection[key] == "yellow":
            intersection[key] = "red"
        else:
            intersection[key] = "green"
#    assert "red" in intersection.values(), "nincs benne red!"

print(lampa)
switchLamp(lampa)
print(lampa)
switchLamp(lampa)
print(lampa)
switchLamp(lampa)
print(lampa)
switchLamp(lampa)
