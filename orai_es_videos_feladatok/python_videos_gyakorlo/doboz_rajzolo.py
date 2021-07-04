"""
###########
#         #
#  Hello  #
#         #
###########
"""

# statikus megoldással
# width = 11
# height = 5
# text = "Hello"

# dinamikus megoldással
width = int(input("width: "))
height = int(input("height: "))
text = input("text: ")
center_y = height // 2 # egész szám osztással a magasság fele
text_start = (width - len(text)) // 2  # a szélesség - a szöveg hossza osztva kettővel
text_current = 0  # melyik karaktert írtam ki (alapból nulla)

# egymásba ágyazott for ciklusokkal y = a magasság, x = szélesség
for y in range(height):  # y a hanyadik sor
    for x in range(width): # x a sorban levő szélesség
        # y magasság vagy nulla, vagy a szélesség -1
        # x szélesség vagy nulla, vagy a magasság -1
        if y == 0 or y == height - 1 or x == 0 or x == width - 1:
            print("#", end="")  # end="" // ezzel a megoldással érem el, hogy egy sorba írja ki az összes #-et
        elif y == center_y and text_start <= x < text_start + len(text):
            print(text[text_current], end="")
            text_current += 1
        else:
            print(" ", end="")
    print("")  # a sor végénél ki kell tenni egy üres jelet, hogy átugorjon a következő sorra

