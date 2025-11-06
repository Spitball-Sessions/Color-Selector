import arcade, logging, random
from arcade.types import Color
from collections import namedtuple as nt

LOG_LEVEL = "INFO"

def start_logging():
    log = logging.getLogger(__name__)
    log.setLevel(LOG_LEVEL)

    handler = logging.StreamHandler()
    formatter = logging.Formatter("%(name)s:%(levelname)s: %(message)s")
    handler.setFormatter(formatter)
    log.addHandler(handler)

    return log


Game_Info = nt("Game_Info",["screen_width","screen_height","window_name"])
game_info = Game_Info(screen_width=1280, screen_height=720, window_name= "TITLE")


class Square():
    def __init__(self, bottom, height, left, width, color, c_value) -> None:
        self.top = bottom + height
        self.bottom = bottom
        self.left = left
        self.right = left + width
        self.width = width
        self.height = height 
        self.color = color
        self.c_value = c_value

    def __repr__(self):
        return f"Square(top = {self.top}, bottom = {self.bottom}, left = {self.left}, right = {self.right}, width = {self.width}, height = {self.height}, color = {self.color}, color_value = {self.c_value})"




class GameView(arcade.Window):
    def __init__(self):
        super().__init__(*game_info)
        self.background_color = arcade.csscolor.BLACK

        self.box_counter = 0
        self.css_color_boxes = []

        #gets the names of all the Colors:
        self.get_colors()
        self.create_boxes()
        
    def __repr__(self) -> str:
        self.csscolors_list = self.csscolors_list

    def get_colors(self):
        self.csscolors_list = arcade.csscolor.__dict__.items()
        self.css_item_list = [(name, value)
            for name, value in arcade.csscolor.__dict__.items()
            if not name.startswith("__") and isinstance(value, tuple)]
        log.info(self.css_item_list)

        self.colors_list = arcade.color.__dict__.items()
        self.color_item_list = [item for item in self.colors_list]
            
        
    def setup(self):
        #temporary
        list_names = [
            key for key,value in self.csscolors_list
        ]

        background = random.choice(list_names)
        if not background == "BLACK":
            self.background_color = getattr(arcade.csscolor, background)

    def create_boxes(self):

        for i in self.css_item_list:
            left = 10 + ((self.box_counter%15) * 85)
            bottom = 10 + ((self.box_counter//15-1) * 70)
            height = 60
            width = 75
            log.info(f"color = {i[0]}, color value = {i[1]}")
            box = Square(left=left, bottom=bottom, height=height, width=width, color=i[0], c_value=i[1])
            log.info(f"box = {box}")
            self.box_counter+=1
            self.css_color_boxes.append(box)


        log.debug(repr(self.css_color_boxes))
        


    def on_update(self,delta_time):
        pass

    def on_draw(self):
        self.clear()
        for box in self.css_color_boxes:
            log.debug(f"Box is {box}")
            arcade.draw_lbwh_rectangle_filled(box.left, box.bottom, box.width, box.height, box.c_value)
        

    def on_key_press(self, key, modifiers):
        if key == arcade.key.ESCAPE:
            self.setup()


if __name__ == "__main__":
    log = start_logging()
    window = GameView()
    window.setup()
    arcade.run()



