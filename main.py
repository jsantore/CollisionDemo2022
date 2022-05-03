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
    game_window.display_text = "Eat Mushrooms!"
    add_mushrooms(game_window)
    game_window.on_draw = types.MethodType(comp151_draw, game_window)  # magic line to make comp151 draw work for arcade
    game_window.on_key_press = types.MethodType(handle_key_press, game_window)
    arcade.run()



def comp151_draw(window):
    arcade.start_render()
    window.spider.draw()
    window.player.draw()
    #here is the first check for collisions
    if does_collide(window.player, window.spider):
        window.display_text = "Yikes! its a big SPIDER!!"
    if does_collide_with_any_in_list(window.player, window.mushroom_list):
        window.display_text = "That's a tasty Mushroom"
    arcade.draw_text(window.display_text, 50, 750, arcade.color.ANTI_FLASH_WHITE, font_size=20)
    for mushroom in window.mushroom_list:
        mushroom.draw()
    arcade.finish_render()

def does_collide(sprite1, sprite2):
    return sprite1.collides_with_sprite(sprite2)

def does_collide_with_any_in_list(player, sprite_list):
    #first I'll create an arcade thing to do most of the work for me
    easy_list = arcade.SpriteList()
    easy_list.extend(sprite_list)
    return player.collides_with_list(easy_list)


def handle_key_press(window, key, mod):
    if key == arcade.key.LEFT:
        window.player.center_x -= 20
    elif key == arcade.key.RIGHT:
        window.player.center_x += 20
    if key == arcade.key.UP:
        window.player.center_y += 20
    elif key == arcade.key.DOWN:
        window.player.center_y -= 20

def add_mushrooms(game_window):
    #randomly place 6 Mushrooms on the screen
    for mushroom_number in range(6):
        current_sprite = arcade.Sprite("mushroom.png")
        current_sprite.center_x = random.randint(0,800)
        current_sprite.center_y = random.randint(100,760)
        game_window.mushroom_list.append(current_sprite)


if __name__ == '__main__':
    main()