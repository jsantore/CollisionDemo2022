import random

import arcade
import Comp151Window
import types




def main():
    game_window = Comp151Window.Comp151Window(900,800, "Collision Demo")
    game_window.background_color = arcade.color.GRAY_ASPARAGUS
    game_window.spider=arcade.Sprite("spider.png")
    game_window.spider.center_x = 700
    game_window.spider.center_y = 100
    game_window.player = arcade.Sprite("Walking Turtle 1.png")
    game_window.player.center_x = 450
    game_window.player.center_y = 400
    game_window.mushroom_list = []
    add_mushroom(game_window)
    game_window.on_draw = types.MethodType(comp151_draw, game_window)  # magic line to make comp151 draw work for arcade
    game_window.on_key_press = types.MethodType(handle_key_press, game_window)
    arcade.run()

def comp151_draw(window):
    arcade.start_render()
    window.spider.draw()
    window.player.draw()
    for mushroom in window.mushroom_list:
        mushroom.draw()
    arcade.finish_render()

def handle_key_press(window, key, mod):
    if key == arcade.key.LEFT:
        window.player.center_x -= 20
    elif key == arcade.key.RIGHT:
        window.player.center_x += 20
    if key == arcade.key.UP:
        window.player.center_y += 20
    elif key == arcade.key.DOWN:
        window.player.center_x -= 20

def add_mushroom(game_window):
    #randomly place 6 Mushrooms on the screen
    for mushroom_number in range(6):
        current_sprite = arcade.Sprite("mushroom.png")
        current_sprite.center_x = random.randint(0,800)
        current_sprite.center_y = random.randint(100,760)
        game_window.mushroom_list.append(current_sprite)


if __name__ == '__main__':
    main()