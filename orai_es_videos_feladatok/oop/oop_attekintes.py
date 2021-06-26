# eddig procedurális kódokat írtunk. kód-sorok, melynél a funkcionalitáson volt a hangsúly
# egyszerűbb feladatok kényelmesen megoldhatók vele
# OOP esetében áthelyezzük a hangsúlyt az alapszintű működésről az adatokra
# az OOP tágítja a tudatteret és komplexebb feladatok is megoldhatók vele
# az objektumok adatokat és működéseket fognak egybe

students = {
    "Test Elek": {  # a kulcsok a nevek, az értékek pedig az egyéb adatok
        "born": 1985,
        "grades": {
            "literature": [3, 2, 5, 3, 5],
            "english": [4, 4, 2, 3],
        }
    },
    "Test Elekina": {
        "born": 1985,
        "grades": {
            "literature": [3, 2, 5, 3, 5],
            "english": [4, 4, 2, 3],
        }
    }
}
