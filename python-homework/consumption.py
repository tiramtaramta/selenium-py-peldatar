"""
Az autód 7 litert fogyaszt országúton és 9-et városban.
A hévízi üdülésedre 170 kilómétert utazol országúton és 35-öt városban.
Mennyit fogyaszt az autód csak oda? És oda-vissza? Mennyibe kerül a teljes út, ha 350 Ft a benzin?
Oldd meg ezt feladatot úgy, hogy nem előre megadott értékekkel (országúti fogyasztás, városi fogyasztás,
országúton megtett út, városban megtett út, benzin ára) dolgozol, hanem a felhasználótól kéred ezeket be.
Ahol szükséges, ne feledd konvertálni az értékeket!
"""
per_km_city = int(input("Mennyit fogyaszt városban az autód? "))
per_km_hw = int(input("Mennyit fogyaszt országúton az autód? "))
gas_price = int(input("Mennyibe kerül a benzin? "))
km_city = int(input("Mennyit mész városban? "))
km_hw = int(input("Mennyit mész országúton? "))

cons_one_way = (km_city * (per_km_city / 100)) + (km_hw * (per_km_hw / 100))
cons_return = int(cons_one_way * 2)
total_price = int(cons_return * gas_price)

print(f"Az autód teljes fogyasztása csak oda: {cons_one_way} liter")
print(f"Az autód teljes fogyasztása oda-vissza: {cons_return} liter")
print(f"Az út teljes költsége: {total_price} Ft")
