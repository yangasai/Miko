# -*- coding: ひきこもり -*-
screen say:
    window:
        background None
        id "window"
        add ("visual/gui/dialogue_box/prologue/dialogue_box_st.png"):
            xpos 118
            ypos 866
        if persistent.Fl_podsk_count == True:
            use view_score_screen
        imagebutton:
            auto ("visual/gui/dialogue_box/prologue/backward_%s.png")
            xpos 0
            ypos 912
            action ShowMenu("history")
        imagebutton:
            auto ("visual/gui/dialogue_box/prologue/hide_%s.png")
            xpos 1508
            ypos 903
            action HideInterface()
        imagebutton:
            auto ("visual/gui/dialogue_box/prologue/save_%s.png")
            xpos 1567
            ypos 903
            action ShowMenu('Fl_save')
        imagebutton:
            auto ("visual/gui/dialogue_box/prologue/menu_%s.png")
            xpos 1625
            ypos 903
            action ShowMenu('save')
        imagebutton:
            auto ("visual/gui/dialogue_box/prologue/load_%s.png")
            xpos 1682
            ypos 903
            action ShowMenu('load')
        if not config.skipping:
            imagebutton:
                auto ("visual/gui/dialogue_box/prologue/forward_%s.png")
                xpos 1759
                ypos 912
                action Skip()
        else:
            imagebutton:
                auto ("visual/gui/dialogue_box/prologue/fast_forward_%s.png")
                xpos 1759
                ypos 912
                action Skip()
        text what:
            id "what"
            xpos 194
            ypos 930
            xmaximum 1481
            size 28
            color "#ffffff"
            line_spacing 1
        if who:
            text who:
                id "who"
                xpos 220
                ypos 900
                size 31
                line_spacing 1
            
        if Time == True:
            imagebutton:
                xalign 0.01 yalign 0.01 yoffset 0
                auto "visual/gui/dialogue_box/api_1_%s.png"
                action Jump("time_city")
        if Anime_new == True:
            imagebutton:
                xalign 0.01 yalign 0.08 yoffset 0
                auto "visual/gui/dialogue_box/api_3_%s.png"
                action Function(anime_new)
        if Anime_new == False and Talk == True:
            imagebutton:
                xalign 0.01 yalign 0.08 yoffset 0
                auto "visual/gui/dialogue_box/api_2_%s.png"
                action Jump("talk_Miko")
            
        if Anime_new == True and Talk == True:
            imagebutton:
                xalign 0.01 yalign 0.15 yoffset 0
                auto "visual/gui/dialogue_box/api_2_%s.png"
                action Jump("talk_Miko")
        




#Сейвы
screen Fl_save():
    tag menu
    modal True
    add "visual/gui/quick_menu_zad.png"
    fixed yoffset 0 at menu_move:
        add "visual/gui/main_menu/save/save_background.png"

    fixed align (0.5, 0.5) anchor (0.5, 0.5) at menu_move(0.7, 0.5, 0):
        text ["{font=[Script ]}Сохранить{/font}"]:
            size 70
            text_align 0.5
            xalign 0.5
            yalign 0.005
            antialias True
            kerning 2
        textbutton "<":
            hover_sound "visual/gui/main_menu/ClickMenu.mp3"
            style "Fl_button_None"
            text_style "Fl_text_setting_s"
            text_size 60
            xalign 0.34
            yalign 0.01
            action ShowMenu("load")
        textbutton ">":
            hover_sound "visual/gui/main_menu/ClickMenu.mp3"
            style "Fl_button_None"
            text_style "Fl_text_setting_s"
            text_size 60
            xalign 0.65
            yalign 0.01
            action ShowMenu("preferences")
        textbutton ["Сохранить игру"]:
            hover_sound "visual/gui/main_menu/ClickMenu.mp3"
            text_style "Fl_text_big_save_load"
            style "Fl_button_None"
            text_size 55
            ypos 950
            xalign 0.5
            if persistent._file_page != "Fl_FilePage_auto":
                action (Fl_FunctionCallback(Fl.CallbackOnSave, selected_slot), FileSave(selected_slot))
        textbutton ["Удалить"]:
            hover_sound "visual/gui/main_menu/ClickMenu.mp3"
            text_style "Fl_text_big_save_load"
            style "Fl_button_None"
            text_size 55
            xpos 1470
            ypos 950
            action FileDelete(selected_slot)
        textbutton ["Назад"]:
            hover_sound "visual/gui/main_menu/ClickMenu.mp3"
            text_style "Fl_text_big_save_load"
            style "Fl_button_None"
            text_size 55
            xpos 200
            ypos 950
            action [Hide("Fl_save", Dissolve(1.0)), Return()]
    use Fl_save_load_slots
        

#Загрузка
screen load():
    tag menu
    modal True
    add "visual/gui/quick_menu_zad.png"
    fixed yoffset 0 at menu_move:
        add "visual/gui/main_menu/save/save_background.png"

    fixed align (0.5, 0.5) anchor (0.5, 0.5) at menu_move(0.7, 0.5, 0):
        text ["{font=[Script ]}Загрузить{/font}"]:
            size 70
            text_align 0.5
            xalign 0.5
            yalign 0.005
            antialias True
            kerning 2
        textbutton "<":
            hover_sound "visual/gui/main_menu/ClickMenu.mp3"
            style "Fl_button_None"
            text_style "Fl_text_setting_s"
            text_size 60
            xalign 0.34
            yalign 0.01
            action ShowMenu("preferences")
        textbutton ">":
            hover_sound "visual/gui/main_menu/ClickMenu.mp3"
            style "Fl_button_None"
            text_style "Fl_text_setting_s"
            text_size 60
            xalign 0.65
            yalign 0.01
            action ShowMenu("Fl_save")

        textbutton ["Загрузить игру"]:
            hover_sound "visual/gui/main_menu/ClickMenu.mp3"
            text_style "Fl_text_big_save_load"
            style "Fl_button_None"
            text_size 55
            ypos 950
            xalign 0.5
            action (Fl_FunctionCallback(Fl.CallbackOnLoad, selected_slot), FileLoad(selected_slot))
        textbutton ["Удалить"]:
            hover_sound "visual/gui/main_menu/ClickMenu.mp3"
            text_style "Fl_text_big_save_load"
            style "Fl_button_None"
            text_size 55
            xpos 1470
            ypos 950
            action FileDelete(selected_slot)
        textbutton ["Назад"]:
            hover_sound "visual/gui/main_menu/ClickMenu.mp3"
            text_style "Fl_text_big_save_load"
            style "Fl_button_None"
            text_size 55
            xpos 200
            ypos 950
            action [Hide("load", Dissolve(1.0)), Return()]
    use Fl_save_load_slots
    


#Настройки
screen preferences():
    tag menu
    modal True
    add "visual/gui/quick_menu_zad.png"
    fixed yoffset 0 at menu_move:
        add "visual/gui/main_menu/save/save_background.png"

    add "visual/gui/main_menu/preferences/Fl_preference_osn.png" at menu_move(0.68, 0.165, 0)

    fixed align (0.5, 0.5) anchor (0.5, 0.5) at menu_move(0.7, 0.5, 0):
        textbutton "<":
            hover_sound "visual/gui/main_menu/ClickMenu.mp3"
            style "Fl_button_None"
            text_style "Fl_text_setting_s"
            text_size 60
            xalign 0.34
            yalign 0.01
            action ShowMenu("Fl_save")
        textbutton ">":
            hover_sound "visual/gui/main_menu/ClickMenu.mp3"
            style "Fl_button_None"
            text_style "Fl_text_setting_s"
            text_size 60
            xalign 0.65
            yalign 0.01
            action ShowMenu("load")

    add "visual/gui/main_menu/preferences/Fl_rezim_osn.png":
        zoom 0.65 xpos 485 ypos 280

    if not _preferences.fullscreen:
        imagebutton:
            xalign 0.43 yalign 0.33 yoffset 0
            idle ("visual/gui/main_menu/preferences/Fl_window_hover.png")
            hover ("visual/gui/main_menu/preferences/Fl_window_hover.png")
        imagebutton:
            xalign 0.26 yalign 0.33 yoffset 0
            auto "visual/gui/main_menu/preferences/Fl_fullscreen_%s.png"
            hover_sound "visual/gui/main_menu/ClickMenu.mp3"
            action (Preference("display", "fullscreen"))
    else:
        imagebutton:
            xalign 0.43 yalign 0.33 yoffset 0
            auto "visual/gui/main_menu/preferences/Fl_window_%s.png"
            hover_sound "visual/gui/main_menu/ClickMenu.mp3"
            action (Preference("display", "window"))
        imagebutton:
            xalign 0.26 yalign 0.33 yoffset 0
            idle ("visual/gui/main_menu/preferences/Fl_fullscreen_hover.png")
            hover ("visual/gui/main_menu/preferences/Fl_fullscreen_hover.png")


    add "visual/gui/main_menu/preferences/Fl_filtr_osn.png": 
        zoom 0.65 xpos 480 ypos 405
        
    if persistent.Fl_swear_filter == True:
        imagebutton:
            xpos 367 ypos 476
            idle ("visual/gui/main_menu/preferences/Fl_on_hover.png")
            hover ("visual/gui/main_menu/preferences/Fl_on_hover.png")
            action (SetField(persistent, "Fl_swear_filter", True))
    
        imagebutton:
            xpos 673 ypos 476
            auto "visual/gui/main_menu/preferences/Fl_off_%s.png"
            hover_sound "visual/gui/main_menu/ClickMenu.mp3"
            action (SetField(persistent, "Fl_swear_filter", False))
        
    else:
        imagebutton:
            xpos 367 ypos 476
            auto "visual/gui/main_menu/preferences/Fl_on_%s.png"
            hover_sound "visual/gui/main_menu/ClickMenu.mp3"
            action (SetField(persistent, "Fl_swear_filter", True))
        imagebutton:
            xpos 673 ypos 476
            idle ("visual/gui/main_menu/preferences/Fl_off_hover.png")
            hover ("visual/gui/main_menu/preferences/Fl_off_hover.png")
    

    add "visual/gui/main_menu/preferences/Fl_skip_menu.png":
        zoom 0.65 xpos 485 ypos 545
        
    if not _preferences.skip_unseen:
        imagebutton:
            xalign 0.363 yalign 0.585 yoffset 0
            idle ("visual/gui/main_menu/preferences/Fl_readed_hover.png")
            hover ("visual/gui/main_menu/preferences/Fl_readed_hover.png")
        imagebutton:
            xalign 0.233 yalign 0.585 yoffset 0
            auto "visual/gui/main_menu/preferences/Fl_all_%s.png"
            hover_sound "visual/gui/main_menu/ClickMenu.mp3"
            action (Preference("skip", "all"))
    else:
        imagebutton:
            xalign 0.363 yalign 0.585 yoffset 0
            auto "visual/gui/main_menu/preferences/Fl_readed_%s.png"
            hover_sound "visual/gui/main_menu/ClickMenu.mp3"
            action (Preference("skip", "seen"))
        imagebutton:
            xalign 0.233 yalign 0.585 yoffset 0
            idle ("visual/gui/main_menu/preferences/Fl_all_hover.png")
            hover ("visual/gui/main_menu/preferences/Fl_all_hover.png")


    add "visual/gui/main_menu/preferences/Fl_podsk_osn.png":
        zoom 0.65 xpos 485 ypos 685
        
    if persistent.Fl_podsk_count == True:
        imagebutton:
            xpos 380 ypos 746
            idle ("visual/gui/main_menu/preferences/Fl_on2_hover.png")
            hover ("visual/gui/main_menu/preferences/Fl_on2_hover.png")
        imagebutton:
            xpos 667 ypos 746
            auto "visual/gui/main_menu/preferences/Fl_off2_%s.png"
            hover_sound "visual/gui/main_menu/ClickMenu.mp3"
            action (SetField(persistent, "Fl_podsk_count", False))
    else:
        imagebutton:
            xpos 380 ypos 746
            auto "visual/gui/main_menu/preferences/Fl_on2_%s.png"
            hover_sound "visual/gui/main_menu/ClickMenu.mp3"
            action (SetField(persistent, "Fl_podsk_count", True))
        imagebutton:
            xpos 667 ypos 746
            idle ("visual/gui/main_menu/preferences/Fl_off2_hover.png")
            hover ("visual/gui/main_menu/preferences/Fl_off2_hover.png")


    add "visual/gui/main_menu/preferences/Fl_music_menu.png":
        zoom 0.68 xpos 1150 ypos 278    
    bar:
        value Preference("music volume")
        right_bar "visual/gui/main_menu/preferences/Fl_scale_chist.png"
        left_bar "visual/gui/main_menu/preferences/Fl_scale_poln.png"
        thumb "visual/gui/main_menu/preferences/Fl_begunok.png"
        xpos 1061
        ypos 333
        xmaximum 365
        ymaximum 70


    add "visual/gui/main_menu/preferences/Fl_sound_menu.png":
        zoom 0.72 xpos 1140 ypos 413
    bar:
        value Preference("sound volume")
        right_bar "visual/gui/main_menu/preferences/Fl_scale_chist.png"
        left_bar "visual/gui/main_menu/preferences/Fl_scale_poln.png"
        thumb "visual/gui/main_menu/preferences/Fl_begunok.png"
        xpos 1061
        ypos 477
        xmaximum 365
        ymaximum 70


    add "visual/gui/main_menu/preferences/Fl_ambience_menu.png":
        zoom 0.7 xpos 1151 ypos 562 
    bar:
        value Preference("voice volume")
        right_bar "visual/gui/main_menu/preferences/Fl_scale_chist.png"
        left_bar "visual/gui/main_menu/preferences/Fl_scale_poln.png"
        thumb "visual/gui/main_menu/preferences/Fl_begunok.png"
        xpos 1061
        ypos 621
        xmaximum 365
        ymaximum 70

    
    add "visual/gui/main_menu/preferences/Fl_text_menu.png":
        zoom 0.7 xpos 1151 ypos 711 
    bar:
        value Preference("text speed")
        right_bar "visual/gui/main_menu/preferences/Fl_scale_chist.png"
        left_bar "visual/gui/main_menu/preferences/Fl_scale_poln.png"
        thumb "visual/gui/main_menu/preferences/Fl_begunok.png"
        xpos 1061
        ypos 765
        xmaximum 365
        ymaximum 70
    


    fixed align (0.5, 0.5) anchor (0.5, 0.5) at menu_move(1.0, 0.5, 0):
        textbutton ["Назад"]:
            hover_sound "visual/gui/main_menu/ClickMenu.mp3"
            text_style "Fl_text_setting" style "Fl_button_None"
            pos (423, 830) action [Hide("preferences", Dissolve(1.0)), Return()]


#История
define config.history_length = 100
define gui.history_height = 1100
define gui.history_name_xpos = 0
define gui.history_name_ypos = 0
define gui.history_name_width = 0
define gui.history_name_xalign = 0.0
define gui.history_text_xpos = 250
define gui.history_text_ypos = 0
define gui.history_text_width = 1500
define gui.history_text_xalign = 0.0
define gui.scrollbar_size = 18

screen history():
    tag menu
    predict False
    add "visual/gui/quick_menu_zad.png"
    
    $ xmax = 1600
    $ xposition = 100


    button style "blank_button" xpos 0 ypos 0 action Return():
        xfill True
        yfill True

    window background Frame("visual/gui/main_menu/history/choice_box.png",50,50) top_padding 33 bottom_padding 40 at bg_zoom_th:
        xfill True
        ysize gui.history_height
        viewport id "text_history_screen":
            draggable True
            mousewheel True
            scrollbars None
            yinitial 1.0
            has vbox
            for history in _history_list:
                if history.who:
                    text history.who:
                        font "font/MainMenu.ttf"
                        pos (50, 0)
                        size 29
                        if "color" in history.who_args:
                            color history.who_args["color"]
                textbutton history.what:
                    style "log_button"
                    text_font "font/Fl_font.ttf"
                    text_size 28
                    xmaximum 1550
                    xpos 50
                    
                    
        vbar:
            value YScrollValue("text_history_screen")
            bottom_bar Frame("visual/gui/main_menu/history/vbar_nofull.png",0,0)
            top_bar Frame("visual/gui/main_menu/history/vbar_full.png",0,0)
            thumb "visual/gui/main_menu/history/thumb.png"
            thumb_offset 10
            ymaximum 800
            align (0.97, 0.49)
