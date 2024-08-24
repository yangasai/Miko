# -*- coding: ひきこもり -*-
init python:

        import renpy.store as store
        class Fl_QuitItemsMenu(Action):
            def __call__(self):
                SetVariable("Fl_show_items_window", False)()
                SetVariable("Fl_hover_slot", {"slot":None, "name":"empty", "stats":None})()


        class Fl_SelectedSlot(Action, DictEquality):
            def __init__(self, name):
                self.name = name
            def __call__(self):
                SetVariable("Fl_hover_slot", Fl.SelectedSlot(self.name))()
            def get_sensitive(self):
                if Fl_hover_slot != Fl.SelectedSlot(self.name):
                    return True
                else:
                    return False


        class Fl_Call(Action):
            def __init__(self, label):
                self.label = label
            def __call__(self):
                if "." in self.label:
                    SetVariable("Fl_label", self.label.split(".")[0])()
                    SetField(self, "label", self.label.split(".")[1])()
                SetVariable("Fl_return", Fl_label + ".loop")()
                Jump(Fl_label + "." + self.label)()


        class Fl_ApplyItem(Action, DictEquality):
            def __init__(self, item, type):
                self.item = item
                self.type = type
            def __call__(self):
                if Fl_hover_slot["name"] == self.item or Fl_hover_slot["name"] in Fl_ordinary_items_list:
                    Hide("Fl_inventory_message")()
                    if self.item not in Fl_reusable_items_list:
                        Function(Fl.Item, Fl_hover_slot["name"], Fl_hover_slot["stats"], "remove", "Использовано:")()
                else:
                    Hide("Fl_inventory_message")()
                    Show("Fl_inventory_message")()
                    if Fl_hover_slot["name"] in Fl_weapons_list:
                        if Fl_weapon["name"] == "lock":
                            SetVariable("Fl_inventory_message", "Оружие в настоящее время нет необходимости использовать.")()
                            Play("sound", "visual/gui/main_menu/Fl_lock.ogg")()
                        else:
                            SetVariable("Fl_weapon", Fl_inventory[Fl_inventory.index(Fl_hover_slot)])()
                            Function(Fl.Item, Fl_hover_slot["name"], Fl_hover_slot["stats"], "remove", None)()
                            SetDict(Fl_weapon, "slot", "WPG")()
                            SetVariable("Fl_hover_slot", {"name":"empty", "slot":None, "stats":None})()
                    else:
                        SetVariable("Fl_inventory_message", "Этот предмет нельзя здесь применить.")()
                        Play("sound", "visual/gui/main_menu/Fl_lock.ogg")()

        
        class Fl_Message(Action):
            def __init__(self, text):
                self.text = text
            def __call__(self):
                Hide("Fl_inventory_message")()
                Show("Fl_inventory_message")()
                SetVariable("Fl_inventory_message", self.text)()
                Play("sound", "visual/gui/main_menu/Fl_lock.ogg")()


        class Fl_ShowItem(Action, DictEquality):
            def __init__(self, number, items, stats, slot):
                self.number = number
                self.items = items
                self.stats = stats
                self.slot = slot
            def __call__(self):
                Play("sound", "audio/buttons/Fl_" + self.items[self.slot]["name"] + ".ogg")()
                Function(store.Fl.Item, self.items[self.slot]["name"], self.stats)()
                Function(store.Fl.ItemEmpty, self.number, self.slot)()



        class Fl_FunctionCallback(Action):
            def __init__(self,function,*arguments):
                self.function=function
                self.arguments=arguments
            def __call__(self):
                return self.function(self.arguments)
                
 

