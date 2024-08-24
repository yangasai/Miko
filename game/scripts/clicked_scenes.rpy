# -*- coding: ひきこもり -*-
screen Fl_quest_list:
    tag menu
    modal True
    add "objects/Fl_layer.png"
    text ["{font=[Script ]}{color=#808080}Список предметов:{/color}{/font}"]:
        size 50
        ypos 30
        xalign 0.967
    if ph < 1:
        text ["{font=[Script ]}Телефон:{/font}"]:
            size 40
            ypos 85
            xalign 0.967
        add "objects/Fl_check-mark1.png" at zoom_pr(0.07):
            ypos 92
            xalign 0.99
    else:
        text ["{font=[Script ]}Телефон:{/font}"]:
            size 40
            ypos 85
            xalign 0.967
        add "objects/Fl_check-mark2.png" at zoom_pr(0.07):
            ypos 85
            xalign 0.99

    if hp < 1:
        text ["{font=[Script ]}Наушники:{/font}"]:
            size 40
            ypos 125
            xalign 0.967
        add "objects/Fl_check-mark1.png" at zoom_pr(0.07):
            ypos 133
            xalign 0.99
    else:
        text ["{font=[Script ]}Наушники:{/font}"]:
            size 40
            ypos 125
            xalign 0.967
        add "objects/Fl_check-mark2.png" at zoom_pr(0.07):
            ypos 133
            xalign 0.99

    if room == "kitchen":
        imagebutton:
            xalign 0.014 yalign 0.929 yoffset 0
            idle ("objects/room.png")
            hover ("objects/room.png")
            hover_sound "visual/gui/main_menu/ClickMenu.mp3"
            action (SetVariable("room", "komnata"), Jump("Fl_prologue_room_items"))
    elif room == "komnata":
        imagebutton:
            xalign 0.964 yalign 0.929 yoffset 0
            idle ("objects/kitchen.png")
            hover ("objects/kitchen.png")
            hover_sound "visual/gui/main_menu/ClickMenu.mp3"
            action (SetVariable("room", "kitchen"), Jump("Fl_prologue_kitchen_items"))




screen Fl_clicked_scenes:
    if it_0 < 1:
        imagebutton:
            xalign 0.567 yalign 0.635 yoffset 0
            auto "objects/prolog_item/Fl_cupboard1_%s.png"
            hover_sound "visual/gui/main_menu/ClickMenu.mp3"
            action Jump("Fl_prologue_room_items_check1")

    if it_1 < 1:
        imagebutton:
            xalign 0.567 yalign 0.674 yoffset 0
            auto "objects/prolog_item/Fl_cupboard1_%s.png"
            hover_sound "visual/gui/main_menu/ClickMenu.mp3"
            action Jump("Fl_prologue_room_items_check2")

    if it_2 < 1:
        imagebutton:
            xalign 0.749 yalign 0.426 yoffset 0
            auto "objects/prolog_item/Fl_cupboard2_%s.png"
            hover_sound "visual/gui/main_menu/ClickMenu.mp3"
            action Jump("Fl_prologue_room_items_check3")

    if it_3 < 1:
        imagebutton:
            xalign 0.904 yalign 0.706 yoffset 0
            auto "objects/prolog_item/Fl_cupboard3_%s.png"
            hover_sound "visual/gui/main_menu/ClickMenu.mp3"
            action Jump("Fl_prologue_room_items_check4")

    if it_4 < 1:
        imagebutton:
            xalign 0.354 yalign 0.535 yoffset 0
            auto "objects/prolog_item/Fl_cupboard4_%s.png"
            hover_sound "visual/gui/main_menu/ClickMenu.mp3"
            action Jump("Fl_prologue_room_items_check5")
    


    use Fl_quest_list


    
screen Fl_prologue_kitchen_clicked:

    if it_5 < 1:
        imagebutton:
            xalign 0.233 yalign 0.574 yoffset 0
            auto "objects/prolog_item/Fl_cupboard5_%s.png"
            hover_sound "visual/gui/main_menu/ClickMenu.mp3"
            action Jump("Fl_prologue_kitchen_items_check1")

    if it_6 < 1:
        imagebutton:
            xalign 0.202 yalign 0.776 yoffset 0
            auto "objects/prolog_item/Fl_cupboard6_%s.png"
            hover_sound "visual/gui/main_menu/ClickMenu.mp3"
            action Jump("Fl_prologue_kitchen_items_check2")


    use Fl_quest_list
