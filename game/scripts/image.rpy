init 1 python:

    #Дисклеймер
    Fl.RegImage("preview", "disclaimer_day", "jpg")
    Fl.RegImage("preview", "disclaimer_sunset", "jpg")
    Fl.RegImage("preview", "disclaimer_night", "jpg")


    #ДОЖДЬ
    Fl.RegImage("rain", "rain_large", "png")
    Fl.RegImage("rain", "rain_large2", "png")
    Fl.RegImage("rain", "rain_normal", "png")
    Fl.RegImage("rain", "rain_normal2", "png")
    Fl.RegImage("rain", "rain_small", "png")
    Fl.RegImage("rain", "rain_small2", "png")

    #СНЕГ
    Fl.RegImage("snow", "snow", "png")


    #СПЕЦАЛЬНЫЕ
    Fl.RegImage("special", "fogging", "png")
    Fl.RegImage("special", "vignette", "png")
    Fl.RegImage("special", "vignette2", "png")
    Fl.RegImage("special", "vignette3", "png")
    Fl.RegImage("special", "entrance_night_vision_layer", "png")
    Fl.RegImage("special", "rage1", "png")
    Fl.RegImage("special", "rage2", "png")
    Fl.RegImage("special", "white_effect", "png")
    Fl.RegImage("special", "blood_effect", "png")


    #МЕНЮ
    Fl.RegImage("gui/main_menu", "main_menu_a1", "png")
    Fl.RegImage("gui/main_menu", "main_menu_a2", "png")
    Fl.RegImage("gui/main_menu", "main_menu_a3", "png")


    #Загрузка
    Fl.RegImage("gui/main_menu", "load_layer", "png")
    Fl.RegImage("gui/main_menu", "load_layer2", "png")


    #Настройки
    Fl.RegImage("gui/main_menu", "peref_layer", "png")


    #ЗАГРУЗОЧНЫЙ ЭКРАН  
    Fl.RegImage("gui/loading", "loading", "png")
    Fl.RegImage("gui/loading", "icon", "png")



############################################################################################################################
    #BG
    Fl.RegImage("bg", "bg black", "png")
    Fl.RegImage("bg", "bg komnata_summer", "png")
    Fl.RegImage("bg", "bg komnata_winter", "png")
    Fl.RegImage("objects", "komnata_winter_layer", "png")












init:
    #ДОЖДЬ 
    image rain:
        truecenter
        xzoom 1.3 yzoom 1.7
        contains:
            SnowBlossom("rain_large", 10, 50, (75, 125), (1600, 1700))
        contains:
            SnowBlossom("rain_normal", 25, 50, (50, 100), (1500, 1600))
        contains:
            SnowBlossom("rain_small", 150, 50, (25, 50), (1400, 1500))
    
    
    image rain_right:
        "rain"
        rotate 16.0

    image rain_left:
        "rain"
        rotate -16.0

    image rain_hard:
        contains:
            "rain"
        contains:
            "rain"

    image rain_hard_right:
        contains:
            "rain_right"
        contains:
            "rain_right"

    image rain_hard_left:
        contains:
            "rain_left"
        contains:
            "rain_left"
 

    #Туман
    image smoke:
        Fl_ease_slowly_repeat



    #Пыль
    image dust5:
        dust_alpha_linear_repeat(5, 10.0, 14.0)
    
    image dust6:
        dust_alpha_linear_repeat(6, 28.0, 32.0)
    
    image dust7:
        dust_alpha_linear_repeat(7, 13.0, 17.0)

    image dust8:
        dust_alpha_linear_repeat(8, 15.0, 19.0)
    
    image dust9:
        dust_alpha_linear_repeat(9, 10.0, 14.0)

    image dust10:
        dust_alpha_linear_repeat(10, 28.0, 32.0)

    image dust11:
        dust_alpha_linear_repeat(11, 13.0, 17.0)

    image dust12:
        dust_alpha_linear_repeat(12, 15.0, 19.0)


    image dust_full:
        "dust5"
        "dust6"
        "dust7"
        "dust8"
        "dust9"
        "dust10"
        "dust11"
        "dust12"


    #Освещение с пылью
    image light_l:
        light_and_dust_contains("l_light")

    image light_r:
        light_and_dust_contains("r_light")

    image light_c:
        "light_l"
        "light_r"


    image light_l_menu:
        light_and_dust_contains("l_light_menu")

    image light_r_menu:
        light_and_dust_contains("r_light_menu")

    image light_c_menu:
        "light_l_menu"
        "light_r_menu"


    #ИЗОБРАЖЕНИЯ С АНИМАЦИЯМИ
    image tv_effect: 
        "visual/special/tv_effect1.jpg"
        0.1
        "visual/special/tv_effect2.jpg"
        0.1
        "visual/special/tv_effect3.jpg"
        0.1
        repeat

    image rage:
        "rage1" with Dissolve1
        pause 2.0
        "rage2" with Dissolve1
        pause 2.0
        repeat



    image blink:
        contains:
            "blink_up"
            pos (0,-1080)
            ease 1.5 xalign 0 yalign 0
        contains:
            "blink_down"
            pos (0,1080)
            ease 1.5 xalign 0 yalign 0


    image blinking:
        subpixel True
        contains:
            "blink_up"
            pos (0,-1080)
            ease 1.5 xalign 0 yalign 0
        contains:
            "blink_down"
            pos (0,1080)
            ease 1.5 xalign 0 yalign 0
        pause 2.0
        contains:
            "blink_up"
            xalign 0 yalign 0
            ease 1.5 pos (0,-1080)
        contains:
            "blink_down"
            xalign 0 yalign 0
            ease 1.5 pos (0,1080)

    image Fl_unblink:
        subpixel True
        contains:
            "blink_up"
            xalign 0 yalign 0
            ease 1.5 pos (0,-1080)
        contains:
            "blink_down"
            xalign 0 yalign 0
            ease 1.5 pos (0,1080)


    image pulsing:
        subpixel True
        "pulsing1"
        pause(0.2) 
        "pulsing2"
        pause(0.2) 
        "pulsing3"
        pause(0.2) 
        "pulsing2"
        repeat


    image prolog_dream:
        subpixel True
        "prologue1"
        pause(0.1) 
        "prologue2"
        pause(0.1) 
        "prologue3"
        pause(0.1) 
        "prologue2"
        repeat


    image Fl_unblink:
        subpixel True
        contains:
            "blink_up"
            xalign 0 yalign 0
            ease 1.5 pos (0,-1080)
        contains:
            "blink_down"
            xalign 0 yalign 0
            ease 1.5 pos (0,1080)

    image blink:
        subpixel True
        contains:
            "blink_up"
            pos (0,-1080)
            ease 1.5 xalign 0 yalign 0
        contains:
            "blink_down"
            pos (0,1080)
            ease 1.5 xalign 0 yalign 0


    image blinking:
        subpixel True
        contains:
            "blink_up"
            pos (0,-1080)
            ease 1.5 xalign 0 yalign 0
        contains:
            "blink_down"
            pos (0,1080)
            ease 1.5 xalign 0 yalign 0
        pause 2.0
        contains:
            "blink_up"
            xalign 0 yalign 0
            ease 1.5 pos (0,-1080)
        contains:
            "blink_down"
            xalign 0 yalign 0
            ease 1.5 pos (0,1080)


    
    #Мико
    image uv normal d2 = Fl.SpritesReg('uv',['uv_2_body', 'uv_2_pioneer', 'uv_2_normal'],size = "normal")
    image uv smile d2 = Fl.SpritesReg('uv',['uv_2_body', 'uv_2_pioneer', 'uv_2_smile'],size = "normal")