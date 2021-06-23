per_km_city = input("Mennyit fogyaszt városban az autód? ")
per_km_hw = int(input("Mennyit fogyaszt városban az autód? "))
gas_price = int(input("Mennyibe kerül a benzin? "))
km_city = int(input("Mennyit mész városban? "))
km_hw = int(input("Mennyit mész országúton? "))

cons_one_way = ((km_city * per_km_city) / 100 + (km_hw * per_km_hw) / 100)
cons_return = cons_one_way * 2
total_price = cons_return * gas_price