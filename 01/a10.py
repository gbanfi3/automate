def div42by(num):
    try:
        return 42 / num
    except ZeroDivisionError:
        print("valami baj történt")

# print(div42by(1))
# print(div42by(1.0))

print(div42by(0))

# print(div42by(None))

