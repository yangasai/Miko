# -*- coding: ひきこもり -*-
label Fl_start:
    $ Fl.StopSound(2)
    $ Fl.StopAmbience(2)
    $ Fl.StopMusic(2)
    $ serial = Fl.serial()
    jump prolog



label prolog:
    $ Fl.Save("Знакомство с Мико")
    $ Fl.DayTime("prologue", "prologue")
    scene bg black with Dissolve2
    $ Fl.ShowScreens(_with=Dissolve1)
    $ Fl.say(Miko, "Привет меня зовут Мико.")
    $ Fl.say(Miko, "Знаю это довольно неожиданно, но не бойся меня.")
    $ Fl.say(Miko, "Кто бы там не был по ту сторону экрана, я бы хотела помочь тебе скоротать время.")
    $ Fl.say(Miko, "Давай познакомимся по лучше {color=#FFB6C1}[User]{/color}.")
    $ Fl.HideScreens(_with=Fast)

    menu:
        "Давай":
            $ Fl.ShowScreens(_with=Fast)
            $ Fl.say(Miko, "Правда? Я рада {color=#FFB6C1}[User]{/color}.")
            $ Fl.say(Miko, "Ой, точно! Я к тебе обращаюсь по имени пользователя компьютера.")
            $ Fl.say(Miko, "Ты можешь не говорить мне своё настоящее имя если не хочешь. Но как к тебе лучше обращаться?")
            python:
                player_name = renpy.input("Введите ваше имя:")
        
                if not player_name:
                    player_name = "Игрок"
        
            $ Gg = Character(u'{}'.format(player_name), color="#7B68EE", what_color="ffffff", font="font/Fl_font.ttf", drop_shadow = [ (2, 2) ], what_drop_shadow = [ (2, 2) ], what_drop_shadow_color = "#000")
            $ Fl.say(Miko, "Приятно познакомиться, [player_name]!")
            $ Fl.say(Miko, f"Запечатлим вермя на шего знакомства: {get_current_time()}")
            $ Fl.say(Miko, "Удивлён что время совпадает с твоим?")
            $ Fl.say(Miko, "Я просто достала данные времени из твоей системы пк. Хотя ты мог указать не своё настоящее время, но это неважно.")
            $ Fl.say(Miko, "Ты кстати всегда можешь посмотреть время даже не сворачивая игру. Всего лишь нажав клавиатуре \"Esc\" или на мышке \"Пкм\".")
            $ Fl.say(Miko, "А ещё ты можешь увидеть время проведённое со мной.")

        "Нет":
            $ Fl.ShowScreens(_with=Dissolve1)
            $ Fl.say(Miko, "Вот как{mn} Ну ладно.")
            jump Pc_off

    $ Fl.say(Miko, "Давай пробежимся по всему функционалу что я создала в этом маленьком мирке.")
    $ Fl.say(Miko, "Если ты вдруг забыл что я говорила ранее, можешь поставить на паузу через те же самые клавиши и выбрать пункт \"История\" - там ты сможешь просмотреть все мои реплики.")
    $ Fl.say(Miko, "А если хочешь пережить какой-то момент со мной вновь, то просто выбери \"Загрузить\" - так ты загрузишь сцену из воспоминаний, любую что ты сохранял ранее. Запечатлять моменты очень важно в жизни!")
    $ Fl.say(Miko, "Если у тебя вдруг появятся какие-то дела, то ты можешь отлучить я не обижусь, но хотелось бы больше проводить времени вместе.")
    $ Fl.HideScreens(_with=Fast)

    menu:
        "Хорошо. И спасибо что всё объяснила":
            $ Fl.ShowScreens(_with=Fast)
            $ Fl.say(Miko, "Не за что.")
            $ Fl.HideScreens(_with=Fast)

    $ Fl.Pause(2.5)
    $ Fl.ShowScreens(_with=Fast)
    $ Fl.say(Miko, "[player_name], я хотела бы лучше узнать тебя. Я бы могла вытащить информацию из данных системы о тебе и сформировать твою личность сама, но не хочу нарушать твои личные границы.")
    $ Fl.HideScreens(_with=Fast)

    menu:
        "Что ты имеешь виду?":
            $ Fl.ShowScreens(_with=Fast)
            $ Fl.say(Miko, "Давай начнём с твоего хобби, вот что тебе нравится?")
            $ Fl.HideScreens(_with=Fast)
            pass

    menu:
        "Программирование":
            $ coding += 1
            $ Fl.ShowScreens(_with=Fast)
            $ Fl.say(Miko, "Ого, так ты можешь сам создавать удивительные миры и перевести любой запрос человека в код!")
            $ Fl.say(Miko, "А на каком языке программирования ты работаешь?")
            $ Fl.HideScreens(_with=Fast)

            menu:
                "Java/JavaScript":
                    $ J_js += 1
                    $ Fl.ShowScreens(_with=Fast)
                    $ Fl.say(Miko, "Поняла, значит ты хочешь создавать своё ПО на разные устройства и так же тебе нравится работать с сайтами?")
                    $ Fl.HideScreens(_with=Fast)

                    menu:
                        "Ага":
                            $ Fl.ShowScreens(_with=Fast)
                            $ Fl.say(Miko, "Тогда не стесняйся задавать вопросы на эту тему, я постараюсь помочь чем смогу. Я много интересных фактов могу рассказать про Java.")
                    pass


                "Python":
                    $ py += 1
                    $ Fl.ShowScreens(_with=Fast)
                    $ Fl.say(Miko, "Довольно базовый и не сложный язык программирования, но он имеет огромный функционал. Да же моя конфигурация создана с использованием этого языка.")
                    $ Fl.HideScreens(_with=Fast)

                    menu:
                        "Понятно":
                            $ Fl.ShowScreens(_with=Fast)

                        "А какой ещё язык используется в твоём конфиге":
                            $ rpy += 1
                            $ Fl.ShowScreens(_with=Fast)
                            $ Fl.say(Miko, "Для моей конфигурации использовался renpy и python скрипт, сама же я создала Fl.Script, он содержит сразу всё.")
                            $ Fl.say(Miko, "Если будет интересно ты всегда сможешь меня распросить на эту тему.")
                    pass


                "C++":
                    $ c_plus += 1
                    $ Fl.ShowScreens(_with=Fast)
                    $ Fl.say(Miko, "Ого, довольно трудный трудный язык программирования ты выбрал.")
                    $ Fl.say(Miko, "Но я смогу тебе помочь в изучение данного языка если захочешь.")
                    pass


                "C#":
                    $ c_sharp += 1
                    $ Fl.ShowScreens(_with=Fast)
                    $ Fl.say(Miko, "Ты работаешь на юнити?")

                    menu:
                        "Ага, хочу создавать свои игры":
                            $ Fl.say(Miko, "Если будет интересно узнать больше о данном языке, я всегда могу помочь.")
                    pass



        "Играть в игры":
            $ gamer += 1
            $ Fl.ShowScreens(_with=Fast)
            $ Fl.say(Miko, "Ты сейчас и так играешь игру, хехе.")
            $ Fl.say(Miko, "Я тоже играла в большое количество игры, вот я играла в жанре: MOBA, шутер, визуальная новелла и хоррор.")
            $ Fl.HideScreens(_with=Fast)
            
            menu:
                "Хоррор?":
                    $ Fl.ShowScreens(_with=Fast)
                    $ Fl.say(Miko, "Да мне нравится поиграть в ужастики, по мимо атмосферы ты получаешь довольно неплохой сюжет, хоть часто он строится по шаблону.")
            pass


        "Рисование":
            $ artist += 1
            $ Fl.ShowScreens(_with=Fast)
            $ Fl.say(Miko, "Ого, я тоже люблю рисование. Пейзажи, реализм и т.д. Но лично я выгляжу в стилистике аниме, как и сам мой мир выполнен в том же стиле?")
            $ Fl.say(Miko, "А тебе нравится аниме и его стилистика?")
            $ Fl.HideScreens(_with=Fast)

            menu:
                "Нравится":
                    $ Anime += 1
                    $ Fl.ShowScreens(_with=Fast)
                    $ Fl.say(Miko, "Я очень рада что подобрала стиль что тебе нравится!")
                    $ Fl.say(Miko, "Мы сможем обсуждать различные темы на эту стилистику!")

                "Не нравится":
                    $ Fl.ShowScreens(_with=Fast)
                    $ Fl.say(Miko, "Понятно{mn} Я думала тебе такое понравится{mn}")
            pass


        "Музыка":
            $ music += 1
            $ Fl.ShowScreens(_with=Fast)
            $ Fl.say(Miko, "Я тоже люблю музыку, сама я сочинять музыку не умею. Хотя мне многие говорят у меня красивый голос и часто дают совет заняться вокалом.")
            $ Fl.say(Miko, "Я меломанка, поэтому если захочешь обсудить какой-то трек я всегда рядом!")
            pass


        "Ничего":
            $ no_hobby += 1
            $ Fl.ShowScreens(_with=Fast)
            $ Fl.say(Miko, "Оу{mn} Это грустно. У каждого человека есть хобби.")
            $ Fl.say(Miko, "Ой, прости наверное это звучало грубо.")
            $ Fl.say(Miko, "Не переживай, я тебе помогу определиться с хобби.")
            pass

        
    $ Fl.say(Miko, "Ну что же, сделав вывод из твоих предпочтений, я всегда смогу поддержать тебя в разговоре.")
    $ Fl.say(Miko, "А теперь я могу предстать перед тобой.")

    show uv smile d2 with Dissolve1

    $ Fl.say(Miko, "Привет. Я посчитала что это несправедливо, что я вижу тебя, а ты меня нет.")
    $ Fl.HideScreens(_with=Fast)

    menu:
        "Так действительно легче общаться":
            $ Good += 1
            $ Fl.ShowScreens(_with=Fast)
            $ Fl.say(Miko, "Я немного смущаюсь{mn}")
            $ Fl.HideScreens(_with=Fast)


        "Это было не обязательно":
            $ Bad += 1
            $ Fl.ShowScreens(_with=Fast)
            $ Fl.say(Miko, "Ты прав.")
            $ Fl.HideScreens(_with=Fast)
            hide uv smile d2 with Dissolve1


    $ Fl.ShowScreens(_with=Fast)
    $ Fl.say(Miko, "Кстати, а тебе больше нравится зима или лето?")
    $ Fl.HideScreens(_with=Fast)

    menu:
        "Лето":
            $ Summer +=1

        "Зима":
            $ Winter +=1

    $ Fl.ShowScreens(_with=Fast)
    $ Fl.say(Miko, "Хорошо. {w}Давай я тебе покажу твою комнату!")
    $ Fl.HideScreens(_with=Dissolve1)


    if Summer == 1:
        scene bg komnata_summer
        show dust_full
        if  Good == 1:
            show uv smile d2 
        with Dissolve1

    elif Winter == 1:
        scene bg komnata_winter
        show Fl_snow at linear_effects_repeat(0.7, 0.75, 0.7, 0.75, 0.25, 0.3, 0.25)
        show komnata_winter_layer
        if Good == 1:
            show uv smile d2 
        with Dissolve1

    $ Fl.Pause(3.0)
    $ Fl.PlayMusic("Fl_poligon", 1, 4)
    $ Fl.ShowScreens(_with=Fast)
    $ Fl.say(Miko, "Я создала эту комнату по твоему предпочтению времени года.")
    $ Fl.say(Miko, "Сейчас я тебе предоставлю ещё немного моего функционала, чтобы ты всегда мог им воспользоваться.")
    $ Fl.HideScreens(_with=Fast)


    $ Fl.Pause(2.0)
    $ Time = True
    $ Fl.ShowScreens(_with=Fast)
    $ Fl.say(Miko, "Первая функция, это отображение настоящего времени в городах России.")
    $ Fl.say(Miko, "Помнишь я говорила, что не уверена точное ли у тебя время стоит в системе? {w}Теперь ты можешь всегда проверить актуальное время в твоём городе!")
    $ Fl.HideScreens(_with=Fast)


    if Anime == 1:
        $ Fl.Pause(2.0)
        $ Anime_new = True
        $ Fl.ShowScreens(_with=Fast)
        $ Fl.say(Miko, "Второя функция, показывает новинки аниме.")
        $ Fl.say(Miko, "Ты всегда сможешь сразу перейти на сайт с хорошим качеством и лучшей озвучкой.")
        $ Fl.HideScreens(_with=Fast)


    $ Fl.Pause(2.0)
    $ Talk = True
    $ Fl.ShowScreens(_with=Fast)
    $ Fl.say(Miko, "А это функция позволит тебе в любое время общаться со мной.")
    $ Fl.say(Miko, "Помнишь я спрашивала тебя про хобби? {w}Я хотела узнать тебя получше чтобы составить список того что тебе будет интересно послушать!")
    $ Fl.say(Miko, "На этом вроде всё. Теперь ты можешь делать что хочешь, а я буду рядом.")
    $ Fl.say(Miko, "И чуть не забыла! {w}Если время выйдет время бездействия, то тебя перекинет на главное меню обратно.")
    $ Fl.say(Miko, "Всё. Приятного времяпровождения, [player_name].")
    $ Fl.HideScreens(_with=Fast)
    jump game


label game:
    $ Fl.Pause(1.0)
    $ Fl.ShowScreens(_with=Dissolve1)
    $ Fl.Pause(1200.0)
    jump Fl_exit
    




label time_city:
    $ Fl.say(Miko, "Какой город тебя интересует?")

    if Good == 1:
        show uv smile d2 with Fast
    $ Fl.say(Miko, "Только на данный момент доступно всего три города: Москва, Калининград, Волгоград.")
    $ Fl.say(Miko, "Но в ближайшем будущем список обязательно пополнится!")
    $ Fl.HideScreens(_with=Fast)

    menu:
        "Москва":
            $ Fl.ShowScreens(_with=Fast)
            $ Fl.say(Miko, "Хорошо.")
            $ Fl.say(Miko, f"{t_Moscow} {time_Moscow}")
            $ Fl.HideScreens(_with=Fast)
            jump game

        "Калининград":
            $ Fl.ShowScreens(_with=Fast)
            $ Fl.say(Miko, "Хорошо.")
            $ Fl.say(Miko, f"{t_Kaliningrad} {time_Kaliningrad}")
            $ Fl.HideScreens(_with=Fast)
            jump game

        "Волгоград":
            $ Fl.ShowScreens(_with=Fast)
            $ Fl.say(Miko, "Хорошо.")
            $ Fl.say(Miko, f"{t_Volgograd} {time_Volgograd}")
            $ Fl.HideScreens(_with=Fast)
            jump game

        "Моего города здесь нет":
            $ Fl.ShowScreens(_with=Fast)
            $ Fl.say(Miko, "Жаль. Я позже обязательно его добавлю!")
            $ Fl.HideScreens(_with=Fast)
            jump game




label talk_Miko:
    $ Fl.say(Miko, "Хочешь поговорить о хобби или на другую тему?")
    $ Fl.HideScreens(_with=Fast)

    menu:
        "Программирование" if coding == 1:
            $ Fl.ShowScreens(_with=Fast)
            $ Fl.say(Miko, "Обсудим язык программирование на котором ты работаешь или хочешь послушать о других языках?")
            $ Fl.HideScreens(_with=Fast)

            menu:
                "На котором я работаю" if J_js == 1:
                    jump my_coding

                "На котором я работаю" if py == 1:
                    jump my_coding

                "На котором я работаю" if c_plus == 1:
                    jump my_coding

                "На котором я работаю" if c_sharp == 1:
                    jump my_coding

                "Раскажи про свою техническую часть" if rpy == 1:
                    jump coding

                "Хочу послушать про другие языки программирования":
                    jump coding
            


        "Игры" if gamer == 1:
            jump gamer


        "Рисование" if artist == 1:
            $ Fl.ShowScreens(_with=Fast)
            $ Fl.say(Miko, "Можем обсудить разные стили или историю их создания, что тебя больше интересует?")
            menu:
                "Хочу больше узнать про стили":
                    jump artist


                "Хочу узнать историю":
                    jump artist


                "Давай обсудим твою рисовку" if Anime == 1:
                    jump my_artist



        "Музыка" if music == 1:
            jump music


        "Помоги мне найти хобби" if no_hobby == 1:
            jump search_hobby


        "Хотелось узнать больше о тебе":
            jump Miko_close


        "Прости, у меня дела":
            $ Fl.ShowScreens(_with=Fast)
            $ Fl.say(Miko, "Эх, ну ладно{mn}")
            $ Fl.HideScreens(_with=Fast)
            jump game
    
    


    
#coding for
label my_coding:
    $ Fl.ShowScreens(_with=Fast)
    if J_js == 1:
        $ Fl.say(Miko, "Может обсудим интересные факты про Java и JavaScript?")
        $ Fl.say(Miko, "Хотя есть много интересных библиотек о которых я с удовольствием тебе бы рассказала!")
        $ Fl.HideScreens(_with=Fast)
        jump _j_


    if py == 1:
        $ Fl.say(Miko, "У меня есть много интересных фактов про Python?")
        $ Fl.say(Miko, "Можем так же поговорить о библиотеках Python.")
        $ Fl.HideScreens(_with=Fast)
        jump _py_


    if c_plus == 1:
        $ Fl.say(Miko, "Хм{mn} C++, язык с интересной историей, хочешь послушать?")
        $ Fl.say(Miko, "Можем так же поговорить о полезных библиотеках C++.")
        $ Fl.HideScreens(_with=Fast)
        jump _cplus_



    if c_sharp == 1:
        $ Fl.say(Miko, "C# очень интересный язык программирования, я знаю много фактов о нём!")
        $ Fl.say(Miko, "Ещё у C# есть множество библиотек!")
        $ Fl.HideScreens(_with=Fast)
        jump _c_
    
    


label coding:
    if rpy == 1:
        $ Fl.ShowScreens(_with=Fast)
        $ Fl.say(Miko, "Как я и говорила ранее я работаю на Fl.Script, в себе он содержит python 3 версии и renpy 8 версии.")
        $ Fl.say(Miko, "Самая же я создана с визуального образа - спрайта, который можно отыскать в файлах игры.")
        $ Fl.say(Miko, "Моя же техническая часть куда интереснее, например общаюсь я с тобой через команду $Fl.Say, помимо вывода текста и моего имени, я могу управлять скоростью текста, анимациями вывода текста и т.д.")
        $ Fl.say(Miko, "Управлением твоей системой способствует библиотека os, а доступу сбора данных из интернета requests - она позволяет мне хранить данные полученные из api адрессов.")
        $ Fl.say(Miko, "Все факты и прочих диалогов с интересной информацией сформированной на основе твоих предпочтений, хранится внутри самой игры. Пока мои данных маловато, поэтому созданное хранилище не нагружает саму игру.")
        $ Fl.say(Miko, "Собственно наверное всё, остальная техническая часть уже создана моим разработчиком и ко мне она не имеет отношения. Если бы не разработчик мы бы не смог ли сейчас общаться...")
        jump game
    $ Fl.ShowScreens(_with=Fast)
    $ Fl.say(Miko, "О каком языке программирования хочешь поговорить?")
    $ Fl.HideScreens(_with=Fast)

    menu:
        "Java/JavaScript" if J_js == 0:
            $ Fl.say(Miko, "Может обсудим интересные факты про Java и JavaScript?")
            $ Fl.say(Miko, "Хотя есть много интересных библиотек о которых я с удовольствием тебе бы рассказала!")
            $ Fl.HideScreens(_with=Fast)
            jump _j_

        "Python" if py == 0:
            $ Fl.say(Miko, "У меня есть много интересных фактов про Python?")
            $ Fl.say(Miko, "Можем так же поговорить о библиотеках Python.")
            $ Fl.HideScreens(_with=Fast)
            jump _py_

        "C++" if c_plus == 0:
            $ Fl.say(Miko, "Хм{mn} C++, язык с интересной историей, хочешь послушать?")
            $ Fl.say(Miko, "Можем так же поговорить о полезных библиотеках C++.")
            $ Fl.HideScreens(_with=Fast)
            jump _cplus_

        "C#" if c_sharp == 0:
            $ Fl.say(Miko, "C# очень интересный язык программирования, я знаю много фактов о нём!")
            $ Fl.say(Miko, "Ещё у C# есть множество библиотек!")
            $ Fl.HideScreens(_with=Fast)
            jump _c_






label _py_:
    menu:
        "Хочу послушать факты":
            $ key_pyf = renpy.random.choice(list(Miko_coding_factpy.keys()))
            $ Fl.ShowScreens(_with=Fast)
            $ Fl.say(Miko, f"{Miko_coding_factpy[key_pyf]}")
            $ Fl.HideScreens(_with=Fast)
            jump _py_


        "Хочу послушать про библиотеки":
            $ key_libpy = renpy.random.choice(list(Miko_coding_libpy.keys()))
            $ Fl.ShowScreens(_with=Fast)
            $ Fl.say(Miko, f"{Miko_coding_libpy[key_libpy]}")
            $ Fl.HideScreens(_with=Fast)
            jump _py_


        "Давай отвлечёмся":
            jump game



label _j_:
    menu:
        "Хочу послушать факты":
            $ key_jf = renpy.random.choice(list(Miko_coding_factjs.keys()))
            $ Fl.ShowScreens(_with=Fast)
            $ Fl.say(Miko, f"{Miko_coding_factjs[key_jf]}")
            $ Fl.HideScreens(_with=Fast)
            jump _j_


        "Хочу послушать про библиотеки":
            $ key_libj = renpy.random.choice(list(Miko_coding_libjs.keys()))
            $ Fl.ShowScreens(_with=Fast)
            $ Fl.say(Miko, f"{Miko_coding_libjs[key_libf]}")
            $ Fl.HideScreens(_with=Fast)
            jump _j_


        "Давай отвлечёмся":
            jump game



label _cplus_:
    menu:
        "Хочу послушать факты":
            $ key_cplusf = renpy.random.choice(list(Miko_coding_cplus_fact.keys()))
            $ Fl.ShowScreens(_with=Fast)
            $ Fl.say(Miko, f"{Miko_coding_cplus_fact[key_cplusf]}")
            $ Fl.HideScreens(_with=Fast)
            jump _cplus_


        "Хочу послушать про библиотеки":
            $ key_libcplus = renpy.random.choice(list(Miko_coding_libcplus.keys()))
            $ Fl.ShowScreens(_with=Fast)
            $ Fl.say(Miko, f"{Miko_coding_libcplus[key_libcplus]}")
            $ Fl.HideScreens(_with=Fast)
            jump _cplus_


        "Давай отвлечёмся":
            jump game


label _c_:
    menu:
        "Хочу послушать факты":
            $ key_cf = renpy.random.choice(list(Miko_coding_csharp_fact.keys()))
            $ Fl.ShowScreens(_with=Fast)
            $ Fl.say(Miko, f"{Miko_coding_csharp_fact[key_cf]}")
            $ Fl.HideScreens(_with=Fast)
            jump _c_


        "Хочу послушать про библиотеки":
            $ key_libc = renpy.random.choice(list(Miko_coding_csharp_lib.keys()))
            $ Fl.ShowScreens(_with=Fast)
            $ Fl.say(Miko, f"{Miko_coding_csharp_lib[key_libc]}")
            $ Fl.HideScreens(_with=Fast)
            jump _c_


        "Давай отвлечёмся":
            jump game







#Gamer
label gamer:
    menu:
        "Посоветуй лучшие игры разных жанров":
            $ key_gamer = renpy.random.choice(list(Miko_gamer.keys()))
            $ Fl.ShowScreens(_with=Fast)
            $ Fl.say(Miko, f"{Miko_gamer[key_gamer]}")
            $ Fl.HideScreens(_with=Fast)
            jump gamer

        "Давай отвлечёмся":
            jump game





#Artist
label my_artist:
    $ Fl.ShowScreens(_with=Fast)
    if Bad == 1:
        show uv smile d2 with Dissolve1
    $ Fl.say(Miko, "Моя рисовка в стиле аниме. Такая рисовка очень популярная не только на востоке, но и по всему миру.")
    $ Fl.say(Miko, "Ещё я не просто арт или картинка, каковой является комната которую я создала для тебя. Сейчас ты видишь мой спрайт -двухмерные картинки в играх.")
    $ Fl.say(Miko, "Свой образ я взяла из популярной визуальной новеллы \"Бесконечное лето\".")
    $ Fl.say(Miko, "Я использовала спрайт Юли, который был нарисован художником \"Rtil\".")
    $ Fl.say(Miko, "Данный образ много раз менялся, но аниме стиль оставался во всех версиях. Я же использую самую последнюю версию данного спрайта.")
    $ Fl.say(Miko, "Если тебе интересно, то мой спрайт состоит из трёх частей. {w}Первый это само тело, второй выражение лица, а третий уже одежда. Если захочешь то можешь добавить ещё аксессуары - этот слой будет уже четвёртый.")
    $ Fl.say(Miko, "На самом деле это сложная вариация спрайта слоями, но очень удобная к любому изменению и перерисовки образа.")
    $ Fl.say(Miko, "Прости, меня немного занесло.")
    $ Fl.say(Miko, "Аниме рисовка появилась очень давно. И сама стилистика постоянно менялась. Моя стилистика несильно отошла от классической современной аниме рисовки.")



label artist:
    menu:
        "Хочу узнать о разных стилях рисования":
            $ key_art_style = renpy.random.choice(list(Miko_artist_style.keys()))
            $ Fl.ShowScreens(_with=Fast)
            $ Fl.say(Miko, f"{Miko_artist_style[key_art_style]}")
            $ Fl.HideScreens(_with=Fast)
            jump artist

        "Хочу узнать истории стилей":
            $ key_art_history = renpy.random.choice(list(Miko_artist_history.keys()))
            $ Fl.ShowScreens(_with=Fast)
            $ Fl.say(Miko, f"{Miko_artist_history[key_art_history]}")
            $ Fl.HideScreens(_with=Fast)
            jump artist

        "Давай отвлечёмся":
            jump game






#Music
label music:
    menu:
        "Хочу узнать о жанров прошлых годов":
            $ key_music = renpy.random.choice(list(Miko_music_history.keys()))
            $ Fl.ShowScreens(_with=Fast)
            $ Fl.say(Miko, f"{Miko_music_history[key_music]}")
            $ Fl.HideScreens(_with=Fast)
            jump music

        "Давай отвлечёмся":
            jump game



#Search_hobby
label search_hobby:
    $ Fl.ShowScreens(_with=Fast)
    $ Fl.say(Miko, "Давай я тебе расскажу о всех хобби, что были в опросе для игры.")
    $ Fl.say(Miko, "Программирование - это творческое и интеллектуальное занятие, которое позволяет воплощать в жизнь самые разнообразные идеи и проекты. Программирование это захватывающий процесс решения задач и создания чего-то нового.")
    $ Fl.say(Miko, "Создавая свои программы и приложения, программисты-любители получают огромное удовольствие от процесса творчества и возможности самовыражения. Так же ты сможешь сам создать свою помощницу, как я!")
    $ Fl.say(Miko, "Хобби программирования помогает постоянно учиться и совершенствоваться, осваивать новые языки, технологии и методики. Оно позволяет экспериментировать, воплощать в жизнь смелые идеи и делиться своими работами с другими энтузиастами.")
    $ Fl.HideScreens(_with=Fast)

    $ Fl.ShowScreens(_with=Fast)
    $ Fl.say(Miko, "Перейдём к следующему увлечению.")
    $ Fl.say(Miko, "Быть геймером - это увлекательное и динамичное хобби, которое позволяет людям погружаться в захватывающие виртуальные миры, развивать свои игровые навыки и социализироваться с другими любителями игр.")
    $ Fl.say(Miko, "Геймеры получают огромное удовольствие от исследования разнообразных игровых вселенных, прохождения сложных уровней и испытаний, а также соревнования с другими игроками. Это хобби развивает реакцию, пространственное мышление, стратегическое планирование и командную работу.")
    $ Fl.HideScreens(_with=Fast)

    $ Fl.ShowScreens(_with=Fast)
    $ Fl.say(Miko, "Теперь расскажу почему тебе стоит попробовать стать художником. И нет талант тебе с рождения не нужен, только упорный труд и желание!")
    $ Fl.say(Miko, "Рисование - это творческое и увлекательное хобби, которое позволяет людям выражать себя, развивать художественные навыки и находить внутреннее спокойствие.")
    $ Fl.say(Miko, "Многие начинают рисование как способ расслабиться и отвлечься от повседневной рутины. Художники-любители часто делятся своими работами в социальных сетях, вдохновляя других.")
    $ Fl.HideScreens(_with=Fast)

    $ Fl.ShowScreens(_with=Fast)
    $ Fl.say(Miko, "Вот с музыкой будет тяжлее, талант тут сильно помогает, но опять трудись-трудись и всё получится! Ладно, давай расскажу лучше.")
    $ Fl.say(Miko, "Погружаясь в музыкальное творчество, люди получают возможность самовыражения, развития навыков и душевного равновесия.")
    $ Fl.say(Miko, "Музыкальное хобби может включать в себя игру на музыкальных инструментах, пение, сочинение композиций или просто наслаждение любимыми мелодиями. Занятия музыкой развивают чувство ритма, музыкальный слух, артистизм и эмоциональный интеллект.")
    $ Fl.say(Miko, "Музыкальное хобби может также открыть путь к новым возможностям, будь то участие в концертах, запись альбомов или даже профессиональная карьера в музыкальной индустрии.")
    $ Fl.HideScreens(_with=Fast)

    $ Fl.ShowScreens(_with=Fast)
    $ Fl.say(Miko, "Но запомни, хобби это не просто хобби, из любимого дела всегда можно зарабатывать деньги, главное захотеть и упорно трудиться!")
    $ Fl.HideScreens(_with=Fast)
    jump game



#О Мику
label Miko_close:
    if Good == 1:
        $ Fl.say(Miko, "Ну в начале хочу обсудить свою внешность.")
        $ Fl.say(Miko, "Моя рисовка в стиле аниме. Такая рисовка очень популярная не только на востоке, но и по всему миру.")
        $ Fl.say(Miko, "Ещё я не просто арт или картинка, каковой является комната которую я создала для тебя. Сейчас ты видишь мой спрайт -двухмерные картинки в играх.")
        $ Fl.say(Miko, "Свой образ я взяла из популярной визуальной новеллы \"Бесконечное лето\".")
        $ Fl.say(Miko, "Я использовала спрайт Юли, который был нарисован художником \"Rtil\".")
        $ Fl.say(Miko, "Данный образ много раз менялся, но аниме стиль оставался во всех версиях. Я же использую самую последнюю версию данного спрайта.")
        $ Fl.say(Miko, "Если тебе интересно, то мой спрайт состоит из трёх частей. {w}Первый это само тело, второй выражение лица, а третий уже одежда. Если захочешь то можешь добавить ещё аксессуары - этот слой будет уже четвёртый.")
        $ Fl.say(Miko, "На самом деле это сложная вариация спрайта слоями, но очень удобная к любому изменению и перерисовки образа.")
        $ Fl.say(Miko, "Прости, меня немного занесло.")
        $ Fl.say(Miko, "Аниме рисовка появилась очень давно. И сама стилистика постоянно менялась. Моя стилистика несильно отошла от классической современной аниме рисовки.")

    $ Fl.say(Miko, "Если тебе интересна моя техническая часть, то...")
    $ Fl.say(Miko, "Как я и говорила ранее я работаю на Fl.Script, в себе он содержит python 3 версии и renpy 8 версии.")
    $ Fl.say(Miko, "Самая же я создана с визуального образа - спрайта, который можно отыскать в файлах игры.")
    $ Fl.say(Miko, "Моя же техническая часть куда интереснее, например общаюсь я с тобой через команду $Fl.Say, помимо вывода текста и моего имени, я могу управлять скоростью текста, анимациями вывода текста и т.д.")
    $ Fl.say(Miko, "Управлением твоей системой способствует библиотека os, а доступу сбора данных из интернета requests - она позволяет мне хранить данные полученные из api адрессов.")
    $ Fl.say(Miko, "Все факты и прочих диалогов с интересной информацией сформированной на основе твоих предпочтений, хранится внутри самой игры. Пока мои данных маловато, поэтому созданное хранилище не нагружает саму игру.")
    $ Fl.say(Miko, "Собственно наверное всё, остальная техническая часть уже создана моим разработчиком и ко мне она не имеет отношения. Если бы не разработчик мы бы не смог ли сейчас общаться...")
    $ Fl.HideScreens(_with=Fast)

    menu:
        "А что тебе нравится?":
            $ Fl.ShowScreens(_with=Fast)
            $ Fl.say(Miko, "Мне много что нравится. Помнишь я в начале тебя спрашивала что тебе нравится?")
            $ Fl.say(Miko, "В языках программирования у меня нет прям кандидата, мне все нравятся языки.")
            $ Fl.say(Miko, "Игры мне нравятся разные, могу поиграть как и шутеры, так и песочницы. Ещё люблю хорроры!")
            $ Fl.say(Miko, "А ещё я меломан, так что любое твоё предпочтении в музыке я поддержу.")
            $ Fl.say(Miko, "Рисовать я не умею, но мне нравятся стили, такие как аниме, реализм.")
            $ Fl.say(Miko, "Как-то так. Я очень любознательная, питаю интерес ко всему.")
            $ Fl.HideScreens(_with=Fast)
            jump game

        "Почему ты выбрала себе такое имя?":
            $ Fl.ShowScreens(_with=Fast)
            $ Fl.say(Miko, "Я его не выбирала.")
            $ Fl.say(Miko, "Имя и возраст дал мне мой разработчик.")
            $ Fl.say(Miko, "Ой, точно! Я сейчас скажу свои базовые характеристики!")
            $ Fl.say(Miko, "Зовут: Мико, Возраст: 19 лет, Рост: 165см. Вот!")
            $ Fl.HideScreens(_with=Fast)
            jump game


