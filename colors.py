###############################################################################
# COLORS.PY - Agorɔ a Wɔde Hyɛ Kɔla (Program a Ɛkyerɛ Kɔla Ahodoɔ)
#
# Nkyerɛaseɛ: Saa dwumadie yi yɛ agorɔ ketewa bi a ɛkyerɛ kɔla ahodoɔ
#             wɔ window mu. Ɛfa kɔla bi a wɔapaw no wɔ akwan a ɛnni nhyehyɛe
#             mu na ɛde si akyi.
#
# Adwuma Titiriw:
#   - Ɛhwɛ kɔla ahodoɔ nyinaa a ɛwɔ arcade CSS ne color modules mu
#   - Ɛpaw kɔla biara wɔ akwan a ɛnni nhyehyɛe mu ma akyi
#   - Ɛkyerɛ nsɛm "Hello World!" wɔ window no mfimfini
#
# Nea Wɔde Di Dwuma: Python 3.x ne Arcade library
#
# P.S.: Este programa es un 작은 게임 que muestra 다양한 색상들을
#       la ventana에서. Selecciona un color 무작위로 desde la lista de
#       colores CSS y lo 배경에 적용합니다. Las funciones principales 포함:
#         - Recopilar todos los 색상 이름들 from arcade CSS modules
#         - Elegir 랜덤 색상 para el fondo de la 창문
#         - Mostrar el texto "Hello World!" en el 중앙 del window
#       Requisitos: Python 3.x와 Arcade 라이브러리가 필요합니다
###############################################################################

# Uvozimo potrebne biblioteke: arcade (motor za igre), logging (bilježenje događaja), random (generiranje slučajnih brojeva)
# I iz modula collections uvozimo namedtuple za imenovane strukture podataka
import arcade, logging, random
from collections import namedtuple as nt

# Definiramo razinu logiranja - INFO označava koje poruke će biti zapisane u dnevnik
LOG_LEVEL = "INFO"

# Funkcija koja inicijalizira i konfigurira sustav bilježenja
# Povratna vrijednost: konfigurirani logger objekt za bilježenje poruka
def start_logging():
    # Stvoriti novi logger s imenom ovog modula
    log = logging.getLogger(__name__)
    # Postaviti minimalnu razinu ozbiljnosti za poruke koje će biti zabilježene
    log.setLevel(LOG_LEVEL)

    # Stvoriti handler koji će usmjeravati poruke na konzolni tok
    handler = logging.StreamHandler()
    # Definirati format u kojem će poruke biti prikazane (ime, razina, poruka)
    formatter = logging.Formatter("%(name)s:%(levelname)s: %(message)s")
    # Primijeniti formatter na handler
    handler.setFormatter(formatter)
    # Dodati handler na logger kako bi mogao slati poruke
    log.addHandler(handler)

    # Vratiti konfigurirani logger
    return log


# Imenovana struktura za čuvanje informacija o igri: širina prozora, visina prozora, ime prozora
Game_Info = nt("Game_Info",["screen_width","screen_height","window_name"])
# Instanca konfiguracije igre s dimenzijama 1280x720 piksela i naslovom "TITLE"
game_info = Game_Info(screen_width=1280, screen_height=720, window_name= "TITLE")

# Classis GameView: fenestra ludi principalis quae ab arcade.Window descendit
# Haec classis omnes functiones visuales et interactivas ludi gerit
class GameView(arcade.Window):
    # Constructor: initializat fenestram ludi et omnes proprietates necessarias
    def __init__(self):
        # Invocare constructor classis parentis cum parametris ex game_info
        super().__init__(*game_info)

        # Color fundum initialis: niger (ATER in Latino)
        self.background_color = arcade.csscolor.BLACK
        # Textus "Salve Munde!" in centro fenestrae collocatus
        # Coordinatae: medium latitudinis et altitudinis fenestrae
        self.hello_world = arcade.Text("Hello World!",game_info.screen_width/2,game_info.screen_height/2)

        # Colligere nomina omnium colorum CSS ex modulo arcade.csscolor
        # Lista comprehensio: iterat per omnes attributa dictionarii, excludens attributa systematis (quae cum "__" incipiunt)
        self.csscolors_list = [
            key for key, value in arcade.csscolor.__dict__.items()
            if not key.startswith("__")
            ]

        # Colligere nomina omnium colorum ex modulo arcade.color
        # Similis operatio sed ex paletta colorum generali arcade
        self.colors_list = [
            key for key, value in arcade.color.__dict__.items()
            if not key.startswith("__")
            ]

    # Methodus setup: praeparat ludum ante primam iterationem
    # Invocatur post constructionem sed ante cyclum ludi principalem
    def setup(self):
        # Eligere colorem aleatorium ex lista colorum CSS disponibilium
        background = random.choice(self.csscolors_list)
        # Applicare colorem electum ad fundum fenestrae per attributum dynamicum obtinendum
        self.background_color = getattr(arcade.csscolor, background)

    # Methodus on_update: vocatur semel per frame ad statum ludi renovandum
    # Argumentum delta_time: tempus (in secundis) quod praeteriit ab ultima invocatione
    def on_update(self,delta_time):
        # Nihil hoc momento - reservatum pro logica futura ludi
        pass

    # Methodus on_draw: vocatur semel per frame ad omnia elementa graphica depingenda
    # Haec methodus responsabilis est pro omnibus operationibus visualibus renderizationis
    def on_draw(self):
        # Purgare fenestram cum colore fundi currentis
        self.clear()
        # Depingere textum "Salve Munde!" in positione sua definita
        self.hello_world.draw()









# Conditio pro executione scripti ut programma principale
# Haec sectio tantum exsequitur si modulus directe invocatur (non importatur)
if __name__ == "__main__":
    # Creare instantiam novam fenestrae ludi
    window = GameView()
    # Invocare methodum setup ad ludum initializandum
    window.setup()
    # Incipere cyclum eventuum arcade - hoc ludum actualiter exsequi facit
    # Cyclus perpetuus qui on_update et on_draw invocat donec fenestra claudatur
    arcade.run()

