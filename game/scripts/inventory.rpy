# -*- coding: ひきこもり -*-
screen Fl_items(number, name, items, check, stats):
    tag menu
    zorder 100
    modal True
    if check != True:
        $ check = Fl.InventoryIf(check, stats)
    fixed at menu_move:
        frame background "visual/gui/inventory/background2.png"
        imagebutton offset (1423, 184):
            if check:
                hover_sound "visual/gui/main_menu/ClickMenu.mp3"
                auto "visual/gui/inventory/exit2_%s.png"
                action [Fl_QuitItemsMenu(), Return()]
            else:
                idle Fl.Brightness("visual/gui/inventory/exit2_idle.png", -0.2)
        text name style "Fl_text_item_label" offset (793, 172)

        vbox pos (0.309, 0.242) spacing 6:
            use Fl_items_slots(number, items, stats)
        vbox pos (0.526, 0.242) spacing 6:
            use Fl_inventory_slots


screen Fl_inventory(type=None, item=None):
    tag menu
    zorder 100
    modal True
    if type == None:
        for key_i in Fl_key_i_list:
            key key_i action Return()
    fixed offset (27, -4) at menu_move:
        frame background "visual/gui/inventory/icons/" + Fl_hover_slot["name"] + ".png"
        frame background "visual/gui/inventory/background.png"

        imagebutton offset (1378, 279):
            idle "visual/gui/inventory/slots/" + Fl_backpack["name"] + "_idle.png"
            if Fl_backpack["name"] != "empty":
                hover_sound "visual/gui/main_menu/ClickMenu.mp3"
                hover Fl.Brightness("visual/gui/inventory/slots/" + Fl_backpack["name"] + "_hover.png", 0.1)
                insensitive Fl.Brightness("visual/gui/inventory/slots/" + Fl_backpack["name"] + "_idle.png", 0.5)
                action Fl_SelectedSlot("BPK")

        imagebutton offset (1378, 363):
            idle "visual/gui/inventory/slots/" + Fl_weapon["name"] + "_idle.png"
            if Fl_weapon["name"] not in ["empty", "lock"]:
                hover_sound "visual/gui/main_menu/ClickMenu.mp3"
                hover Fl.Brightness(+ "visual/gui/inventory/slots/" + Fl_weapon["name"] + "_idle.png", 0.1)
                insensitive Fl.Brightness(+ "visual/gui/inventory/slots/" + Fl_weapon["name"] + "_idle.png", 0.5)
                action Fl_SelectedSlot("WPG")

        if Fl_hover_slot["slot"] != "BPK" and Fl_hover_slot["name"] != "empty":







            textbutton ["Экипировать" if Fl_hover_slot["name"] in Fl_weapons_list else "Применить"]:
                style "Fl_button_None" offset (1140, 837) text_size 30 xanchor 0.5
                text_style "Fl_text_small_save_load" 
                hover_sound "visual/gui/main_menu/ClickMenu.mp3"
                action [Fl_ApplyItem(item, type), If(Fl_hover_slot["name"] == item, true=Return(), false=Hide("none"))]






        if Fl_hover_slot["name"] != "empty":
            text Fl_items_dict[Fl_hover_slot["name"]] style "Fl_text_label" size 40 pos (0.594, 0.53) xanchor 0.5
            vbox pos (0.439, 0.58):











                text Fl.ItemDescription(Fl_hover_slot["name"]) style "Fl_text_item_description"

        vbox pos (0.187, 0.242) spacing 6:
            use Fl_inventory_slots


    fixed at menu_move:
        imagebutton offset (1573, 174):
            hover_sound "visual/gui/main_menu/ClickMenu.mp3"
            auto "visual/gui/inventory/exit_%s.png"
            action If(type, true=Fl_Message("Вам необходимо использовать нужный предмет."), false=Return())

    fixed align (0.5, 0.5) anchor (0.5, 0.5) at menu_move(0.7):
        text "Инвентарь":
            style "Fl_text_label"
            size 70 text_align 0.5 align (0.5, 0.005) antialias True kerning 2
        if type == None:
            textbutton "<":
                text_style "Fl_text_setting"
                hover_sound "visual/gui/main_menu/ClickMenu.mp3"
                style "Fl_button_None" text_size 60 align (0.34, 0.01)
                action ShowMenu("preferences")
            textbutton ">":
                text_style "Fl_text_setting"
                hover_sound "visual/gui/main_menu/ClickMenu.mp3"
                style "Fl_button_None" text_size 60 align (0.65, 0.01)
                action ShowMenu("load")



screen Fl_inventory_message:
    text Fl_inventory_message style "Fl_text_label" size 40 at message_move
    timer 3.4 action [SetVariable("Fl_inventory_message", ""), Hide("Fl_inventory_message")]


screen Fl_items_slots(number, items, stats):
    grid 4 2 spacing 7:
        for slot in range(0, 8):
            imagebutton:
                idle "visual/gui/inventory/slots/" + items[slot]["name"] + "_idle.png"
                if items[slot]["name"] != "empty":
                    hover_sound "visual/gui/main_menu/ClickMenu.mp3"
                    hover Fl.Brightness("visual/gui/inventory/slots/" + items[slot]["name"] + "_hover.png", 0.1)
                    action Fl_ShowItem(number, items, stats, slot)

screen Fl_inventory_slots:
    grid 4 Fl.InventorySlotsLen()/4 spacing 7:
        for slot in range(0, Fl.InventorySlotsLen()):
            imagebutton:
                idle "visual/gui/inventory/slots/" + Fl_inventory[slot]["name"] + "_idle.png"
                if Fl_inventory[slot]["name"] not in ["empty", "lock"] and not Fl_show_items_window:
                    hover_sound "visual/gui/main_menu/ClickMenu.mp3"
                    hover "visual/gui/inventory/slots/" + Fl_inventory[slot]["name"] + "_hover.png"
                    insensitive Fl.Brightness("visual/gui/inventory/slots/" + Fl_inventory[slot]["name"] + "_idle.png", 0.5)
                    action Fl_SelectedSlot(slot)
                if Fl_inventory[slot]["name"] != "lock" and slot > 3:
                    foreground "visual/gui/inventory/slots/plus_idle.png"
                    hover_foreground "visual/gui/inventory/slots/plus_hover.png"
                    if Fl_inventory[slot]["name"] != "empty":
                        insensitive_foreground Fl.Brightness("visual/gui/inventory/slots/plus_idle.png", 0.5)

