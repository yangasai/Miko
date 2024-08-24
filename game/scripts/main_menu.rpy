# -*- coding: ひきこもり -*-

label splashscreen:
    $ Fl.DefaultVariables()

    $ Fl.PlayMusic("Fl_detroit", 1, 3)
    scene bg black
    $ Fl.Pause(1.5)
    call screen loading(0.25) with Dissolve1
    $ Fl.StopMusic(2)
    $ Fl.Pause (2.5)

    return




#Само меню
label before_main_menu:
    $ renpy.block_rollback()
    scene main_menu_a3
    show rain_hard_left
    show main_menu_a2
    show light_c_menu
    show vignette3
    with Dissolve2
    show main_menu_a1 at rightside
    $ Fl.StopSound(1)
    $ Fl.StopAmbience(1)

    call screen main_menu with Dissolve1

screen main_menu():
        tag menu
        modal True


        text "{font=[Script]}{size=137}{color=#000000}Мико{/color}{/size}{/font}" at leftside:
            yalign 0.155
            xalign 0.175
            antialias True

        text "{font=[Script]}{size=137}Мико{/size}{/font}" at leftside:
            yalign 0.15
            xalign 0.17
            antialias True
        


        style_prefix "navigation"

        imagebutton:
            xalign 0.445 yalign 0.485 yoffset 0
            auto "visual/gui/main_menu/monitor_play_%s.png"
            action (Hide ("main_menu"), Start("Fl_start"))
        
        imagebutton:
            xalign 0.395 yalign 0.535 yoffset 0
            auto "visual/gui/main_menu/loading_%s.png" 
            action (ShowMenu("Fl_load_bg"))

        imagebutton:
            xalign 0.338 yalign 0.544 yoffset 0
            auto "visual/gui/main_menu/comp_peref_%s.png" 
            action (ShowMenu("Fl_preference_bg"))

        if renpy.variant("pc"):
            textbutton "X":
                style "Fl_button_None"
                text_style "Fl_text_setting_dls_s"
                text_size 40
                xpos 1880 
                ypos 0
                action (Quit(confirm=not main_menu))

        if gui.show_name:
            vbox:
                style "main_menu_vbox"

                text "[config.name!t]":
                    style "main_menu_title"

                text "[config.version]":
                    style "main_menu_version"



#Пауза
screen save():
    tag menu
    modal True
    add "visual/gui/quick_menu_zad.png"
    text ["{font=[Script]}Мико на паузе:{/font}"]:
        size 55
        yalign 0.05 
        xalign 0.5
    text ["{font=[Script]}Настоящее время:{/font}"]:
        yalign 0.94
        xalign 0.38
    add "Time"
    text ["{font=[Script]}Проведённое время с Мико:{/font}"]:
        yalign 0.94
        xalign 0.62
    add "GameTime"
    use navigation





#Экран префер 
label Fl_preference_bg:
    $ Fl.StopAmbience(1)
    scene peref_layer
    show light_c_menu
    show vignette3
    with Fl_effect_right1

    call screen Fl_preference_menu  with Fl_effect_right1
    screen Fl_preference_menu:
        tag menu
        modal True
        add "visual/gui/main_menu/Fl_ground.png"

        add "visual/gui/main_menu/preferences/Fl_preference_osn.png":
            zoom 0.7 xpos 90 ypos 41
        text ["{font=[Script]}:{/font}"]:
            size 60
            xalign 0.202
            yalign 0.0425


        add "visual/gui/main_menu/preferences/Fl_rezim_osn.png":
            zoom 0.8 xpos 172 ypos 104

        if not _preferences.fullscreen:
            imagebutton:
                xalign 0.044 yalign 0.149 yoffset 0
                idle ("visual/gui/main_menu/preferences/Fl_window_hover.png")
                hover ("visual/gui/main_menu/preferences/Fl_window_hover.png")
            imagebutton:
                xalign 0.219 yalign 0.151 yoffset 0
                auto "visual/gui/main_menu/preferences/Fl_fullscreen_%s.png"
                hover_sound "visual/gui/main_menu/ClickMenu.mp3"
                action (Preference("display", "fullscreen"))
        else:
            imagebutton:
                xalign 0.044 yalign 0.149 yoffset 0
                auto "visual/gui/main_menu/preferences/Fl_window_%s.png"
                hover_sound "visual/gui/main_menu/ClickMenu.mp3"
                action (Preference("display", "window"))
            imagebutton:
                xalign 0.219 yalign 0.151 yoffset 0
                idle ("visual/gui/main_menu/preferences/Fl_fullscreen_hover.png")
                hover ("visual/gui/main_menu/preferences/Fl_fullscreen_hover.png")

            

        add "visual/gui/main_menu/preferences/Fl_skip_menu.png":
            zoom 0.8 xpos 171 ypos 341
                
        if not _preferences.skip_unseen:
            imagebutton:
                xalign 0.163 yalign 0.385 yoffset 0
                idle ("visual/gui/main_menu/preferences/Fl_readed_hover.png")
                hover ("visual/gui/main_menu/preferences/Fl_readed_hover.png")
            imagebutton:
                xalign 0.068 yalign 0.385 yoffset 0
                auto "visual/gui/main_menu/preferences/Fl_all_%s.png"
                hover_sound "visual/gui/main_menu/ClickMenu.mp3"
                action (Preference("skip", "all"))
        else:
            imagebutton:
                xalign 0.163 yalign 0.385 yoffset 0
                auto "visual/gui/main_menu/preferences/Fl_readed_%s.png"
                hover_sound "visual/gui/main_menu/ClickMenu.mp3"
                action (Preference("skip", "seen"))
            imagebutton:
                xalign 0.068 yalign 0.385 yoffset 0
                idle ("visual/gui/main_menu/preferences/Fl_all_hover.png")
                hover ("visual/gui/main_menu/preferences/Fl_all_hover.png")


        add "visual/gui/main_menu/preferences/Fl_music_menu.png":
            zoom 0.8 xpos 271 ypos 565    
        bar:
            value Preference("music volume")
            right_bar "visual/gui/main_menu/preferences/Fl_scale_chist.png"
            left_bar "visual/gui/main_menu/preferences/Fl_scale_poln.png"
            thumb "visual/gui/main_menu/preferences/Fl_begunok.png"
            xpos 188
            ypos 626
            xmaximum 365
            ymaximum 70


        add "visual/gui/main_menu/preferences/Fl_sound_menu.png":
            zoom 0.8 xpos 261 ypos 694 
        bar:
            value Preference("sound volume")
            right_bar "visual/gui/main_menu/preferences/Fl_scale_chist.png"
            left_bar "visual/gui/main_menu/preferences/Fl_scale_poln.png"
            thumb "visual/gui/main_menu/preferences/Fl_begunok.png"
            xpos 188
            ypos 761
            xmaximum 365
            ymaximum 70


        add "visual/gui/main_menu/preferences/Fl_ambience_menu.png":
            zoom 0.8 xpos 261 ypos 825
        bar:
            value Preference("voice volume")
            right_bar "visual/gui/main_menu/preferences/Fl_scale_chist.png"
            left_bar "visual/gui/main_menu/preferences/Fl_scale_poln.png"
            thumb "visual/gui/main_menu/preferences/Fl_begunok.png"
            xpos 188
            ypos 887
            xmaximum 365
            ymaximum 70
            


        textbutton ["Назад"]:
            hover_sound "visual/gui/main_menu/ClickMenu.mp3"
            text_style "Fl_text_setting" style "Fl_button_None"
            pos (90, 985) action [Hide("Fl_preference_menu", Dissolve(1.0)), Jump("before_main_menu")]






#Экран загрузки Fl
label Fl_load_bg:
    $ Fl.StopAmbience(1)
    scene load_layer2
    show Fl_snow at linear_effects_repeat(0.4, 0.75, 0.7, 0.75, 0.25, 0.3, 0.25)
    show load_layer
    show vignette3
    with Fl_effect_left1

    #Вызов самой загрузки
    call screen Fl_load_menu
    screen Fl_load_menu():
        tag menu
        modal True
        fixed yoffset 120 xoffset 400 at menu_move(0.75, 0.5, 0):
            add "visual/gui/main_menu/save/save_background.png"

        fixed align (0.5, 0.5) anchor (0.5, 0.5) at menu_move(0.7, 0.5, 0):
            text ["{font=[Script]}Загрузить{/font}"]:
                size 60
                text_align 0.5
                xalign 0.873
                yalign 0.305
                antialias True
                kerning 2

            textbutton ["{font=[Script]}Загрузить игру{/font}"]:
                hover_sound "visual/gui/main_menu/ClickMenu.mp3"
                text_style "Fl_text_big_save_load"
                style "Fl_button_None"
                text_size 50
                ypos 1010
                xalign 0.887
                action (Fl_FunctionCallback(Fl.CallbackOnLoad, selected_slot), FileLoad(selected_slot))
            textbutton ["Удалить"]:
                hover_sound "visual/gui/main_menu/ClickMenu.mp3"
                text_style "Fl_text_big_save_load"
                style "Fl_button_None"
                text_size 50
                xpos 1900
                ypos 1010
                action FileDelete(selected_slot)
            textbutton ["Назад"]:
                hover_sound "visual/gui/main_menu/ClickMenu.mp3"
                text_style "Fl_text_big_save_load"
                style "Fl_button_None"
                text_size 50
                xpos 930
                ypos 1010
                action [Hide("Fl_load_menu", Dissolve(1.0)), Jump("before_main_menu")]
        use Fl_save_load_slots_menu






#Экран слотов(меню)
screen Fl_save_load_slots_menu:
    fixed align (0.5, 0.5) anchor (0.5, 0.5) at menu_move(0.7, 0.5, 0, 0.45):
        vbox:
            xalign 0.52
            yalign 0.805 #(0.805 if persistent.Fl_autosaves else 0.4)
            grid 1 10:
                for slot in range(0, 10):
                    if slot == 0:
                        textbutton ["А"]:
                            text_size 38 
                            style "Fl_button_None"
                            text_style "Fl_text_big_save_load"
                            action [FilePage("Fl_FilePage_auto"), SetVariable("selected_slot", False), SelectedIf(persistent._file_page == "Fl_FilePage_auto")]
                    else:
                        textbutton str(slot):
                            text_size 38 right_padding 50 
                            style "Fl_button_None"
                            text_style "Fl_text_big_save_load"
                            action [FilePage("FilePage_" + str(slot)), SetVariable("selected_slot", False), SelectedIf(persistent._file_page == "FilePage_" + str(slot))]
        #Ячейки
        grid 4 3 at menu_move(0.77, 0.5, 0):
            yoffset 170 xoffset 650
            xmaximum 0.81 #Ширина полей
            ymaximum 0.65 #Ширина полей
            transpose False
            xfill True
            yfill True
            for slot in range(1, 13):
                fixed:
                    add FileScreenshot(slot):
                        zoom 0.815
                        xpos 10
                        ypos 10
                    button:
                        action SetVariable("selected_slot", slot)
                        xfill False
                        yfill False
                        style "Fl_save_load_button"
                        has fixed
                        text ("%s." % slot + FileTime(slot, format=" %d.%m.%y, %H:%M", empty=" "+"Пусто") + "\n" + FileSaveName(slot)):
                            style "Fl_save_load_button"
                            xpos 15
                            ypos 15
                            xmaximum 0.8



#Экран слотов(стандарт)
screen Fl_save_load_slots:
    fixed align (0.5, 0.5) anchor (0.5, 0.5) at menu_move(0.7, 0.5, 0):
        vbox:
            xalign 0.08
            yalign 0.53
            grid 1 10:
                for slot in range(0, 10):
                    if slot == 0:
                        textbutton ["А"]:
                            text_size 50 style "Fl_button_None"
                            text_style "Fl_text_big_save_load"
                            action [FilePage("Fl_FilePage_auto"), SetVariable("selected_slot", False), SelectedIf(persistent._file_page == "Fl_FilePage_auto")]
                    else:
                        textbutton str(slot):
                            text_size 50 right_padding 50 style "Fl_button_None"
                            text_style "Fl_text_big_save_load"
                            action [FilePage("FilePage_" + str(slot)), SetVariable("selected_slot", False), SelectedIf(persistent._file_page == "FilePage_" + str(slot))]
        grid 4 3:
            xpos 0.125
            ypos 0.2
            xmaximum 0.81
            ymaximum 0.65
            transpose False
            xfill True
            yfill True
            for slot in range(1, 13):
                fixed:
                    add FileScreenshot(slot):
                        zoom 0.815
                        xpos 10
                        ypos 10
                    button:
                        action SetVariable("selected_slot", slot)
                        xfill False
                        yfill False
                        style "Fl_save_load_button"
                        has fixed
                        text ("%s." % slot + FileTime(slot, format=" %d.%m.%y, %H:%M", empty=" "+"Пусто") + "\n" + FileSaveName(slot)):
                            style "Fl_save_load_button"
                            xpos 15
                            ypos 15
                            xmaximum 0.8





#Подтверждение
screen Fl_quit_menu:
    tag menu3
    modal True
    fixed at menu_move:
    
    
        $ timeofday = persistent.timeofday
        $ time_of_day = persistent.timeofday
        button:
            style "blank_button"
            xalign 0
            yalign 0
            xfill True
            yfill True
            action Return()

        add "visual/gui/choice.png"
        text "{font=[Script]}{size=50}Вы действительно хотите выйти в главное меню?{/size}{/font}":
            text_align 0.5
            yalign 0.40
            xalign 0.5
            antialias True
            kerning 2
            
        textbutton ["Да"]:
            hover_sound "visual/gui/main_menu/ClickMenu.mp3"
            text_style "Fl_text_big_save_load"
            style "Fl_button_None"
            yalign 0.5
            xalign 0.42
            action [Start('Fl_exit')] #MainMenu(confirm = False)]
            at menu_hover
        
        textbutton ["Нет"]:
            hover_sound "visual/gui/main_menu/ClickMenu.mp3"
            text_style "Fl_text_big_save_load"
            style "Fl_button_None"
            yalign 0.5
            xalign 0.58
            action Return()
            at menu_hover


screen loading(time):
    tag menu
    modal True
    for key_dismiss in Fl_key_dismiss_list:
        key key_dismiss action NullAction()
    add "visual/gui/loading/loading.png" at loading_bg_move
    add "interference_anim" at alpha(0.5)
    timer 0.01 repeat True action If(load_value < 100, 
        true=SetVariable("load_value", load_value + time), 
        false=[Stop("music", fadeout=3), Hide("loading", transition=Dissolve(2.0, alpha=True)), Return()])
    vbox xalign 0.5 ypos 0.8:
        text "Загрузка..." xalign 0.5 xanchor 0.5 style "Fl_text_setting"
        bar range 100 value load_value style "loading_bar"
        text str(int(load_value)) + "%" xalign 0.5 xanchor 0.5 style "Fl_text_setting_s"
        text "В игре присуствует автосохранение." xalign 0.5 xanchor 0.5 style "Fl_text_setting_sl"
    add "icon" yoffset 160 at full_rotate_repeat(1.0, 0.5, 1.0, 0.8)








label Fl_exit:#ВЫХОД ИЗ МОДА
    $ _window_hide(dissolve)
    $ Fl.Pause (1, hard=True)
    $ Fl.StopMusic(2)
    scene bg black with Dissolve1
    $ Fl.Pause (3, hard=True)
    return     

