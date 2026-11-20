cijferVak1 = 4
cijferVak2 = 4
cijferVak3 = 10


gemideldeCijfer = (cijferVak1 + cijferVak2 + cijferVak3) / 3

if cijferVak1 < 4 or cijferVak2 < 4 or cijferVak3 < 4:
    print("Gezakt!")
    
elif gemideldeCijfer >= 5.5:
    print("Geslaagd!")
else:
    print("Gezakt!")