"""
Készíts egy olyan Python osztályt, ami számolja a fogadott és elküldött üzenetetek és meg tudja állapítani,
hogy ez mennyibe került nekünk. Hogy milyen műveleteket végzett el a felhasználó az legyen egy listában tárolva
(például: operations = [1,1,1,2,2,1,1,1,2,2,2,2,1,1]). Az 1-es jelentse azt, hogy fogadott egy db üzenetet,
a 2-es pedig azt, hogy küldött egyet. Az osztály neve legyen az, hogy MessageBox.
"""

operations = [1, 1, 1, 2, 2, 1, 1, 1,2, 2, 2, 2, 1, 1]


class MessageBox:  # osztály mindig nagybetű és camelCase
    def __init__(self):
        self.received = 0  # kapott üzenet és a küldött nullázása
        self.sent = 0

    def send(self):
        self.sent += 1  # küldésre +1 (függvénnyel adjuk hozzá)

    def receive(self):
        self.received += 1  # fogadásra +1 (függvénnyel adjuk hozzá)

    def count_sent(self):
        return self.sent  # megszámláljuk az összes küldött üzenetet és értéket ad vissza

    def count_received(self):
        return self.received  # megszámláljuk az összes kapott üzenetet és értéket ad vissza

    def price(self, price_per_message):
        return self.count_sent() * price_per_message  # az üzenetek száma x árral és értéket ad vissza


# példányosíjuk
messages = MessageBox()  # initnek nincsen paramétere, így nem kell a zárójelbe semmit írni
for op in operations:  # végig megyünk a listán
    if op == 1:
        messages.send()  # ha 1, akkor a send függvény a sent értékét növeli
    elif op == 2:
        messages.receive()  # ha 2, akkor a receive függvény a received értékét növeli

print(messages.price(1.123))  # végül kiprinteltetjük a price függvény meghívásával, aminek önmagát és az árat kell átadni
print(messages.count_sent())  # az összes küldött üzenetek száma
print(messages.count_received())  # a fogadott üzenetek száma (amiért nyilván nem fizetünk)