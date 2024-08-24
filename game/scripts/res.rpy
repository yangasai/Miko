# -*- coding: ひきこもり -*-
init python:

    from random import randint


    #ТЕКСТОВЫЕ
    th = Character(u'', what_prefix='«', what_suffix='»', color="#ffa200", what_color="ffffff", font="font/Fl_font.ttf",  drop_shadow = [ (2, 2) ], what_drop_shadow = [ (2, 2) ], what_drop_shadow_color = "#000")
    r = Character(u'', what_prefix='', what_suffix='', color="#ffa200", what_color="ffffff", font="font/Fl_font.ttf",  drop_shadow = [ (2, 2) ], what_drop_shadow = [ (2, 2) ], what_drop_shadow_color = "#000")

    #ПЕРСЫ
    Gg = Character(u'Игрок', color="#7B68EE", what_color="ffffff", font="font/Fl_font.ttf", drop_shadow = [ (2, 2) ], what_drop_shadow = [ (2, 2) ], what_drop_shadow_color = "#000")
    Miko = Character(u'Мико', color="#C0C0C0", what_color="ffffff", font="font/Fl_font.ttf", drop_shadow = [ (2, 2) ], what_drop_shadow = [ (2, 2) ], what_drop_shadow_color = "#000")
    

define player_name = ""
default evil = True

init python:
    gui.init(1920, 1080)


define gui.name_text_font = "font/Fl_font.ttf"
define gui.interface_text_font = "font/Fl_font.ttf"



init -777 python:
    import datetime
    import requests
    import webbrowser
    persistent.game_last_time = datetime.datetime.now()
    if persistent.gametime is None:
        persistent.gametime = 0
    def show_gametime(st, at):
        t = datetime.datetime.now()
        dt = t - persistent.game_last_time
        persistent.game_last_time = t
        persistent.gametime += dt.total_seconds() 
        minutes, seconds = divmod(int(persistent.gametime), 60)
        hours, minutes = divmod(minutes, 60)
        img = Text("%0*d:%0*d:%0*d" % (2, hours, 2, minutes, 2, seconds), 
            style="Fl_text_big_save_load", yalign=0.97, xalign=0.59, font="font/MainMenu.ttf", size=35)
        return img, .1


    def get_current_time():
        return datetime.datetime.now().strftime('%H:%M:%S')

    def time_displayable(st, at):
        return Text(get_current_time(), style="Fl_text_big_save_load", yalign=0.97, xalign=0.38, font="font/MainMenu.ttf", size=35), 1.0




    #API
    import requests
    def api_time(city):
        # API для получения времени
        url = f"http://worldtimeapi.org/api/timezone/Europe/{city}"
        response = requests.get(url)
        data = response.json()
        current_time = data["datetime"]
        formatted_time = format_time(current_time)

        return formatted_time

    def format_time(raw_time):
        # Извлечь компоненты даты и времени из строки времени
        date_components = raw_time[:10].split("-")
        time_components = raw_time[11:19].split(":")
        
        # Форматировать дату и время в нужном формате
        formatted_time = f"{date_components[2]}.{date_components[1]}.{date_components[0]} {time_components[0]}:{time_components[1]}:{time_components[2]}"
        
        return formatted_time


    #Site
    import webbrowser
    def anime_new():
        url = "https://jut.su/anime/2024/"
        webbrowser.open(url)


init:
    #Часы
    image GameTime = DynamicDisplayable(show_gametime)
    image Time = DynamicDisplayable(time_displayable)

    $ time_Moscow = api_time("Moscow")
    $ time_Kaliningrad = api_time("Kaliningrad")
    $ time_Volgograd = api_time("Volgograd")




    #FLASH
    $ FlashFast = Fade(0.5, 0, 0.5, color="#fff")
    $ Flash = Fade(1, 0, 1, color="#fff")
    $ Flash2 = Fade(2, 0, 2, color="#fff")
    $ Flash_red = Fade(1, 0, 1, color="#FF0000")
    $ backdrop = "prologue"


    #ПЕРЕМЕННЫЕ DISSOLVE
    $ dopscene = False
    $ Fast = Dissolve(0.5)
    $ Dissolve1 = Dissolve(1.0)
    $ Dissolve2 = Dissolve(2.0)
    $ Dissolve3 = Dissolve(3.0)
    $ Dissolve4 = Dissolve(4.0)
    $ Dissolve5 = Dissolve(5.0)
    $ Dissolve6 = Dissolve(6.0)


    #User
    $ User = os.environ.get('username')






    #ЭФФЕКТ ПЕРЕХОДА
    $ Fl_effect_time = ImageDissolve("visual/move/Fl_effect1.png", 1.0, ramplen = 25, reverse = False, alpha = True) 
    $ Fl_effect_time_pause = ImageDissolve("visual/move/Fl_effect1.png", 2.5, ramplen = 25, reverse = False, alpha = True)

    $ Fl_effect_1 = ImageDissolve("visual/move/Fl_effect2.png", 1.0, ramplen = 25, reverse = False, alpha = True) 
    $ Fl_effect_1_pause = ImageDissolve("visual/move/Fl_effect2.png", 1.0, ramplen = 25, reverse = False, alpha = True) 

    $ Fl_effect_2 = ImageDissolve("visual/move/Fl_effect3.png", 2.0, ramplen = 25, reverse = False, alpha = True) 
    $ Fl_effect_2_pause = ImageDissolve("visual/move/Fl_effect3.png", 2.0, ramplen = 25, reverse = False, alpha = True) 

    $ Fl_effect_3 = ImageDissolve("visual/move/Fl_effect4.png", 1.5, ramplen = 25, reverse = False, alpha = True) 
    $ Fl_effect_3_pause = ImageDissolve("visual/move/Fl_effect4.png", 2.0, ramplen = 25, reverse = False, alpha = True) 

    $ Fl_effect_4 = ImageDissolve("visual/move/Fl_effect5.png", 1.5, ramplen = 25, reverse = False, alpha = True) 
    $ Fl_effect_4_pause = ImageDissolve("visual/move/Fl_effect5.png", 2.5, ramplen = 25, reverse = False, alpha = True) 

    $ Fl_effect_5 = ImageDissolve("visual/move/Fl_effect6.png", 1.5, ramplen = 25, reverse = False, alpha = True) 
    $ Fl_effect_5_pause = ImageDissolve("visual/move/Fl_effect6.png", 2.5, ramplen = 25, reverse = False, alpha = True) 

    $ Fl_effect_6 = ImageDissolve("visual/move/Fl_effect7.png", 2.5, ramplen = 25, reverse = False, alpha = True) 
    $ Fl_effect_6_pause = ImageDissolve("visual/move/Fl_effect7.png", 2.5, ramplen = 25, reverse = False, alpha = True) 

    $ Fl_effect_left1 = ImageDissolve("visual/move/Fl_effect_left.png", 1.2, ramplen = 25, reverse = False, alpha = True) 
    $ Fl_effect_left1_pause = ImageDissolve("visual/move/Fl_effect_left.png", 2.5, ramplen = 25, reverse = False, alpha = True) 

    $ Fl_effect_left2 = ImageDissolve("visual/move/Fl_effect_left.png", 2.0, ramplen = 25, reverse = False, alpha = True) 
    $ Fl_effect_left2_pause = ImageDissolve("visual/move/Fl_effect_left.png", 2.5, ramplen = 25, reverse = False, alpha = True) 

    $ Fl_effect_right1 = ImageDissolve("visual/move/Fl_effect_right.png", 1.2, ramplen = 25, reverse = False, alpha = True) 
    $ Fl_effect_right1_pause = ImageDissolve("visual/move/Fl_effect_right.png", 2.5, ramplen = 25, reverse = False, alpha = True) 

    $ Fl_effect_right2 = ImageDissolve("visual/move/Fl_effect_right.png", 2.0, ramplen = 25, reverse = False, alpha = True) 
    $ Fl_effect_right2_pause = ImageDissolve("visual/move/Fl_effect_right.png", 2.5, ramplen = 25, reverse = False, alpha = True) 

    $ Fl_effect_down1 = ImageDissolve("visual/move/Fl_effect_down.png", 1.2, ramplen = 25, reverse = False, alpha = True) 
    $ Fl_effect_down1_pause = ImageDissolve("visual/move/Fl_effect_down.png", 2.5, ramplen = 25, reverse = False, alpha = True) 

    $ Fl_effect_down2 = ImageDissolve("visual/move/Fl_effect_down.png", 2.0, ramplen = 25, reverse = False, alpha = True) 
    $ Fl_effect_down2_pause = ImageDissolve("visual/move/Fl_effect_down.png", 2.5, ramplen = 25, reverse = False, alpha = True) 

    $ Fl_effect_mosaic = ImageDissolve("visual/move/Fl_mosaic.png", 2.0, ramplen = 25, reverse = False, alpha = True) 
    $ Fl_effect_mosaic_pause = ImageDissolve("visual/move/Fl_mosaic.png", 2.5, ramplen = 25, reverse = False, alpha = True) 




    #Дисклеймер
    image Fl_preview:
        preview_anim




    image Fl_music_effect:
        subpixel True
        "vignette2" with Dissolve1
        pause 3.0
        "fogging" with Dissolve1
        pause 3.0
        repeat

    image Fl_mute_effect:
        subpixel True
        "vignette2" with Dissolve1
        pause 2.0
        "fogging" with Dissolve1
        pause 2.0
        repeat


    image interference_anim:
        four_contains_xyzoom_effects("interference")




init -15:
    #Переменные
    $ hp = 0
    $ ph = 0
    $ it_0 = 0
    $ it_1 = 0
    $ it_2 = 0
    $ it_3 = 0
    $ it_4 = 0
    $ it_5 = 0
    $ it_6 = 0
    $ time = 0
    $ room = "komnata"
    $ pick = 0
    $ lnt_v = 1
    $ persistent.Fl_autosaves = True
    $ load_value = 0
    $ Fl_proverka = True
    $ persistent.Fl_filter = True
    $ Time = False
    $ Talk = False
    $ Anime_new = False




init -18:
    #Формирование Мико и игрока
    $ coding = 0
    $ gamer = 0
    $ artist = 0
    $ music = 0
    $ no_hobby = 0

    $ Summer = 0
    $ Winter = 0


    #Coding
    $ J_js = 0
    $ py = 0
    $ c_plus = 0
    $ c_sharp = 0
    $ rpy = 0
    $ n = False

    
    #Artist
    $ Anime = 0


    #Мико характер
    $ Bad = 0
    $ Good = 0
    