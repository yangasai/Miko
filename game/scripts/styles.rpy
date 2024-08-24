# -*- coding: ひきこもり -*-
init python:
    Script                                          = "font/MainMenu.ttf"
    Fl_dls                                         = "font/Fl_dls.ttf"

    style.Fl_imagemap                                            = Style(style.default)
    style.Fl_imagemap.hover_sound                                = "visual/gui/main_menu/ClickMenu.mp3"

    style.blank_button = Style(style.button)
    style.blank_button.background = "gui/main_menu/none.png"
    style.blank_button.hover_background = "gui/main_menu/none.png"
    style.blank_button.selected_background = "gui/main_menu/none.png"
    style.blank_button.selected_hover_background = "gui/main_menu/none.png"
    style.blank_button.selected_idle_background = "gui/main_menu/none.png"


    style.timebar = Style(style.default)
    style.timebar.left_bar = Frame("images/QTE/Fl_timer1.png", 0, 0)
    style.timebar.right_bar = Frame("images/QTE/Fl_timer2.png", 0, 0)
    style.timebar.xmaximum = 695 
    style.timebar.ymaximum = 27

    style.Fl_text_big_save_load                          = Style(style.default)
    style.Fl_text_big_save_load.font                     = "font/MainMenu.ttf"
    style.Fl_text_big_save_load.size                     = 55
    style.Fl_text_big_save_load.color                    = "#FFFFFF"
    style.Fl_text_big_save_load.hover_color              = "#808080"
    style.Fl_text_big_save_load.selected_color           = "#FFFFFF"
    style.Fl_text_big_save_load.selected_idle_color      = "#FFFFFF"
    style.Fl_text_big_save_load.selected_hover_color     = "#808080"
    style.Fl_text_big_save_load.insensitive_color        = "#FFFFFF"

    style.Fl_text_small_setting                             = Style(style.default)
    style.Fl_text_small_setting.font                         = "font/MainMenu.ttf"
    style.Fl_text_small_setting.size                         = 50
    style.Fl_text_small_setting.hover_color                  = "#FFFFFF"
    style.Fl_text_small_setting.selected_color               = "#808080"
    style.Fl_text_small_setting.outlines                     = [(1, "#000000", 0, 0)]

    style.Fl_text_setting                                = Style(style.default)
    style.Fl_text_setting.font                           = "font/MainMenu.ttf"
    style.Fl_text_setting.size                           = 35
    style.Fl_text_setting.color                          = "#808080"
    style.Fl_text_setting.hover_color                    = "#FFFFFF"
    style.Fl_text_setting.selected_color                 = "#FFFFFF"
    style.Fl_text_setting.outlines                       = [(1, "#000000", 0, 0)]

    style.Fl_text_setting_s                                = Style(style.default)
    style.Fl_text_setting_s.font                           = "font/Fl_font.ttf"
    style.Fl_text_setting_s.size                           = 35
    style.Fl_text_setting_s.color                          = "#808080"
    style.Fl_text_setting_s.hover_color                    = "#FFFFFF"
    style.Fl_text_setting_s.selected_color                 = "#FFFFFF"
    style.Fl_text_setting_s.outlines                       = [(1, "#000000", 0, 0)]

    style.Fl_text_setting_dls_s                                = Style(style.default)
    style.Fl_text_setting_dls_s.font                           = "font/Fl_dls.ttf"
    style.Fl_text_setting_dls_s.size                           = 35
    style.Fl_text_setting_dls_s.color                          = "#808080"
    style.Fl_text_setting_dls_s.hover_color                    = "#FFFFFF"
    style.Fl_text_setting_dls_s.selected_color                 = "#FFFFFF"
    style.Fl_text_setting_dls_s.outlines                       = [(1, "#000000", 0, 0)]

    style.Fl_text_setting_sl                                = Style(style.default)
    style.Fl_text_setting_sl.font                           = "font/Fl_font.ttf"
    style.Fl_text_setting_sl.size                           = 13
    style.Fl_text_setting_sl.color                          = "#808080"
    style.Fl_text_setting_sl.hover_color                    = "#FFFFFF"
    style.Fl_text_setting_sl.selected_color                 = "#FFFFFF"
    style.Fl_text_setting_sl.outlines                       = [(1, "#000000", 0, 0)]
    
    style.Fl_button_None                                 = Style(style.button)
    style.Fl_button_None.background                      = None
    style.Fl_button_None.hover_background                = None
    style.Fl_button_None.selected_background             = None
    style.Fl_button_None.selected_hover_background       = None
    style.Fl_button_None.selected_idle_background        = None
    
    style.Fl_save_load_button                            = Style(style.button)
    style.Fl_save_load_button.font                       = "font/MainMenu.ttf"
    style.Fl_save_load_button.size                       = 22
    style.Fl_save_load_button.color                      = "#FFFFFF"
    style.Fl_save_load_button.background                 = "visual/gui/main_menu/save/save_load_button_idle.png"
    style.Fl_save_load_button.hover_background           = "visual/gui/main_menu/save/save_load_button_hover.png"
    style.Fl_save_load_button.selected_background        = "visual/gui/main_menu/save/save_load_button_selected.png"
    style.Fl_save_load_button.selected_hover_background  = "visual/gui/main_menu/save/save_load_button_selected.png"
    style.Fl_save_load_button.selected_idle_background   = "visual/gui//main_menu/save/save_load_button_selected.png"
    
    style.Fl_text_small_save_load                        = Style(style.default)
    style.Fl_text_small_save_load.font                   = "font/MainMenu.ttf"
    style.Fl_text_small_save_load.size                   = 40
    style.Fl_text_small_save_load.color                  = "#FFFFFF"
    style.Fl_text_small_save_load.hover_color            = "#808080"
    style.Fl_text_small_save_load.selected_color         = "#FFFFFF"
    style.Fl_text_small_save_load.selected_idle_color    = "#FFFFFF"
    style.Fl_text_small_save_load.selected_hover_color   = "#808080"
    style.Fl_text_small_save_load.insensitive_color      = "#FFFFFF"
    
    style.Fl_text_normal                          = Style(style.default)
    style.Fl_text_normal.font                     = "font/Fl_font.ttf"
    style.Fl_text_normal.size                     = 75
    style.Fl_text_normal.color                    = "#FFFFFF"
    style.Fl_text_normal.hover_color              = "#808080"
    style.Fl_text_normal.selected_color           = "#FFFFFF"
    style.Fl_text_normal.selected_idle_color      = "#FFFFFF"
    style.Fl_text_normal.selected_hover_color     = "#808080"
    style.Fl_text_normal.insensitive_color        = "#FFFFFF"
    
    style.Fl_text_label                                      = Style(style.default)
    style.Fl_text_label.font                                 = "font/MainMenu.ttf"
    style.Fl_text_label.size                                 = 50
    style.Fl_text_label.insensitive_color                    = "#FFFFFF"
    style.Fl_text_label.outlines                             = [(1, "#000000", 0, 0)]

    style.log_button = Style(style.button)
    style.log_button.child = None
    style.log_button.focus_mask = None
    style.log_button.background  = None
    
    style.loading_bar                                         = Style(style.default)
    style.loading_bar.left_bar                                = Frame("visual/gui/loading/bar_full.png")
    style.loading_bar.right_bar                               = Frame("visual/gui/loading/bar_null.png")
    style.loading_bar.thumb                                   = None
    style.loading_bar.thumb_offset                            = 0
    style.loading_bar.maximum                                 = (650, 54)

    style.Fl_text_item_label                                 = Style(style.default)
    style.Fl_text_item_label.font                            = "font/MainMenu.ttf"
    style.Fl_text_item_label.size                            = 42
    style.Fl_text_item_label.xanchor                         = 0.5
    style.Fl_text_item_label.insensitive_color               = "#690000"
    style.Fl_text_item_label.outlines                        = [(1, "#000000", 0, 0)]

    style.Fl_text_item_description                          = Style(style.default)
    style.Fl_text_item_description.font                      = 50
    style.Fl_text_item_description.size                      = 23
    style.Fl_text_item_description.xsize                     = 42
    style.Fl_text_item_description.text_align                = 0.5
    style.Fl_text_item_description.insensitive_color         = "#DB0000"
    style.Fl_text_item_description.outlines                  = [(1, "#000000", 0, 0)]
