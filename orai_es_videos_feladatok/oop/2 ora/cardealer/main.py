from dealership import Dealership
from game import Game

audi_dealership = Dealership()  # Letrehozunk egy Dealershipet

new_game = Game(audi_dealership)  # A fenti Dealershipet adjuk be a jatekunkban.

new_game.start_application()  # amikor A jatek ltrejott, akkor tudjuk meghivni rajta a start_applicationt.