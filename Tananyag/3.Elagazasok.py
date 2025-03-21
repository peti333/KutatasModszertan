#if, azaz elágazás

szam = 5
nagySzam = 200

if nagySzam > szam:
    print("ide futottunk")

if False:
    print("ide sose futottunk")

if 3 == 3:
    print("ide is")

if szam < 3:
    print("kicsi")
elif szam > 3 and szam < 10:
    print("közepes")
else:
    print("nagy")