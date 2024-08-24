# -*- coding: ひきこもり -*-

###ТРАНСФОРМЫ
transform rotate(r):
    rotate r subpixel True

transform alpha(a):
    alpha a subpixel True

transform zoom_anim(z, x, y, e, zz, xx, yy):
    subpixel True
    zoom z xalign x yalign y
    ease zoom zz xalign xx yalign yy

transform Fl_zoom(z, x, y):
    subpixel True
    zoom z xpos x ypos y

transform zoom_pr(z):
    zoom z

transform Fl_xalign(x):
    xalign x subpixel True

transform Fl_yalign(y):
    yalign y subpixel True

transform Fl_xoffset(x):
    xoffset x subpixel True

transform Fl_yoffset(y):
    yoffset y subpixel True



transform blink_rage(imgn):
        subpixel True
        contains:
            ImageReference(imgn)
        contains:
            im.MatrixColor(ImageReference(imgn), im.matrix.brightness(0.5))
            truecenter
            alpha 0.9
            zoom 1.25
            ease 6.0 alpha 0.0 zoom 1.0
        contains:
            im.MatrixColor(ImageReference(imgn), im.matrix.brightness(0.5))
            truecenter
            alpha 0.9
            zoom 1.15
            ease 6.0 alpha 0.0 zoom 1.0



transform leftside:
    subpixel True
    xoffset -1500 
    ease 1.5 xoffset 0.0


transform rightside:
    subpixel True
    xoffset 1500 
    ease 1.2 xoffset 0.0
    
    
transform frombottom:
    subpixel True
    yoffset 1500 
    ease 1.5 yoffset 0.0


transform fromtop:
    subpixel True
    yoffset -1500
    ease 1.5 yoffset 0.0  


transform fromtop_per(y, t):
    subpixel True
    yoffset y
    ease t yoffset 0.0   


transform rightside_per(x, t):
    subpixel True
    xoffset x
    ease t yoffset 0.0   



transform rightside:
    subpixel True
    xoffset 1500 
    ease 3.7 xoffset 0.0


#Анимации для счётчика
transform rightside_podsk:
    subpixel True
    xoffset 1500 
    ease 0.5 xoffset 0.0

transform leftside_podsk:
    subpixel True
    xoffset -1500 
    ease 0.5 xoffset 0.0


transform message_move:
    subpixel True
    yoffset 0 pos (0.5, 0.9) xanchor 0.5 alpha 0
    ease 0.2 alpha 1
    ease 0.1 yoffset 20
    ease 0.1 yoffset 0
    pause 2
    ease 1.0 alpha 0


transform arrow_right_anim:
    subpixel True
    xoffset 200 alpha 0
    ease 1.0 xoffset 0 alpha 1
    on hide:
        ease 1.0 xoffset 200 alpha 0
    on idle:
        ease 0.5 xoffset 0 alpha 1
    on hover:
        ease 0.8 xoffset 50
        ease 0.8 xoffset 0
        repeat

transform arrow_left_anim:
    subpixel True
    xoffset -200 alpha 0
    ease 1.0 xoffset 0 alpha 1
    on hide:
        ease 1.0 xoffset -200 alpha 0
    on idle:
        ease 0.5 xoffset 0 alpha 1
    on hover:
        ease 0.8 xoffset -50
        ease 0.8 xoffset 0
        repeat


transform new_item_move:
    subpixel True
    parallel:
        xpos 0.02 ypos 0.45 zoom 0.9
        ease 0.3 ypos 0.55
        ease 0.3 ypos 0.5
    parallel:
        alpha 0.0
        ease 1.0 alpha 1.0
        pause 3.0
        ease 1.0 alpha 0.0


transform loading_bg_move:
    subpixel True
    parallel:
        ease 3.0 alpha 1.0
    parallel:
        ease 15.0 xalign 1.0
        

transform menu_rotate_min:
    subpixel True
    ease 2.5 rotate 0.0 alpha 1.0
    ease 2.5 rotate 0.0 alpha 1.0
    repeat

transform choice_anim:
    subpixel True
    xalign 0.5 yalign 0.4 alpha 0.0
    easein 0.5 yalign 0.5 alpha 1.0

transform menu_rotate:
    subpixel True
    ease 2.5 rotate 3.2 alpha 1.0
    ease 2.5 rotate -3.2 alpha 1.0
    repeat

transform menu_hover:
    subpixel True
    on idle:
        ease 0.65 zoom 1.0 alpha 1.0
    on hover:
        ease 0.45 zoom 1.07 alpha 1.0


transform main_menu_hover:
    subpixel True
    yoffset 1500 
    ease 1.5 yoffset 0.0
    on idle:
        ease 0.65 zoom 1.0 alpha 1.0
    on hover:
        ease 0.45 zoom 1.07 alpha 1.0


transform strel_zoom1:
    subpixel True
    zoom 0.81 xpos 1815 ypos 500

transform strel_zoom2:
    subpixel True
    zoom 0.81 xpos 15 ypos 500
        


transform gallery_lych_anim:
    subpixel True
    align(1.0,0.0)
    ease 3.5 align(1.2,-0.3)
    pause(0.5)
    ease 3.5 align(1.35,-0.1) 
    pause(0.5)
    ease 3.5 align(1.0,0.0)
    pause(0.5)
    repeat
        
        

transform screen_attack_bg(z=1.2, rr=-1.9, zz=1.0, x=0.5, y=0.5):
    subpixel True
    xalign x yalign y
    parallel:
        ease 0.25 zoom z
        ease 0.5 zoom zz
    parallel:
        ease 0.25 rotate rr
        ease 0.25 rotate 1.0
        ease 0.25 rotate 0.0
    repeat


transform exit_bg_move:
    subpixel True
    parallel:
        ease 3.0 alpha 1.0
    parallel:
        ease 15.0 xalign 1.0
    repeat   


transform menu_move(z=1.0, y=0.5, yy=0, x=0.5):
    subpixel True
    zoom z xalign 0.5 yalign y yoffset yy alpha 1.0
    on show:
        zoom z xalign x yalign y yoffset yy-100 alpha 0.0
        ease 0.5 zoom z xalign x yalign y yoffset yy alpha 1.0
    on hide:
        zoom z xalign x yalign y yoffset yy alpha 1.0
        ease 0.5 zoom z xalign x yalign y yoffset yy-100 alpha 0.0
    on replace:
        zoom z


transform alpha_ease_repeat(a=0.0, aa=1.0, e=1.0):
    ease e alpha a subpixel True
    ease e alpha aa
    repeat

transform show_hide_alpha(e):
    on show:
        alpha 0.0
        ease e alpha 1.0
    on hide:
        alpha 1.0
        ease e alpha 0.0


transform menu_z(z=1.0, y=0.5, yy=0, x=0.5):
    subpixel True
    zoom z xalign 0.5 yalign y yoffset yy alpha 1.0


transform anim_frombottom_menu:
    subpixel True
    yoffset 1500
    ease 0.4 yoffset 0.0
    
    
transform anim_frombottom_menu_new:
    subpixel True
    yoffset 1500
    ease 1.5 yoffset 0.0


transform anim_anim_rightside_menu:
    subpixel True
    xoffset 1500 
    ease 0.4 xoffset 0.0    


transform name_move(e=0.5, x=-0.01, xx=0.3):
    xpos -0.5 ypos 0.0 alpha 0.0 subpixel True
    linear e xpos x alpha 1.0
    linear 40.0 xpos xx alpha 1.0


transform full_rotate_repeat(l, z, x, y):
    parallel:
        zoom z xalign x yalign y rotate_pad True rotate 0
        linear l rotate 360
        repeat

transform xoffset_ease(x, xx, e):
    xoffset x subpixel True
    ease e xoffset xx


transform avtobus_move:
    subpixel True
    choice:
        ease 0.02 pos (0.001, 0.001)
        ease 0.02 pos (0, 0)
    choice:
        ease 0.02 pos (-0.001, 0.001)
        ease 0.02 pos (0, 0)
    choice:
        ease 0.02 pos (0.001, 0.001)
        ease 0.02 pos (0, 0.001)
    choice:
        ease 0.02 pos (-0.001, 0.001)
        ease 0.02 pos (0, 0.001)
    repeat
        
        
#ЭФФЕКТ ДЛЯ BG  
transform zoom(t=0.0,  z=0.0, y=0.0, x=0.0):
    subpixel True
    ease t zoom z
    yalign y xalign x

transform bg_zoom_to_e(z=1.0, t=0.0, x=0.5, y=0.5, a=1.0):
    subpixel True
    ease t zoom z xalign x yalign y alpha a

transform bg_zoom_th(z=1.0, zz=0.92, t=0.0, x=0.5, xx=0.5, y=0.5, yy=0.5, a=1.0, aa=1.0):
    subpixel True
    zoom z xalign x yalign y alpha a 
    ease t zoom zz xalign xx yalign yy alpha aa

transform bg_zoom_e(z=1.0, zz=1.0, t=0.0, x=0.5, xx=0.5, y=0.5, yy=0.5, a=1.0, aa=1.0):
    subpixel True
    zoom z xalign x yalign y alpha a
    ease t zoom zz xalign xx yalign yy alpha aa


transform bg_zoom_rotate_e3(z=1.0, zz=1.0, t=0.0, x=0.5, xx=0.5, y=0.5, yy=0.5, r=0.0, rr=0.0, zzz=1.0, tt=0.0, xxx=0.5, yyy=0.5, rrr=0.0, zzzz=1.0, ttt=0.0, xxxx=0.5, yyyy=0.5, rrrr=0.0):
    subpixel True
    zoom z xalign x yalign y rotate r
    ease t zoom zz xalign xx yalign yy rotate rr
    ease tt zoom zzz xalign xxx yalign yyy rotate rrr
    ease ttt zoom zzzz xalign xxxx yalign yyyy rotate rrrr


transform bg_zoom(z=1.0, zz=1.0, t=0.0, x=0.5, xx=0.5, y=0.5, yy=0.5, zzz=1.0, tt=0.0, xxx=0.5, yyy=0.5, zzzz=1.0, ttt=0.0, xxxx=0.5, yyyy=0.5):
    subpixel True
    zoom z xalign x yalign y
    ease t zoom zz xalign xx yalign yy
    ease tt zoom zzz xalign xxx yalign yyy
    ease ttt zoom zzzz xalign xxxx yalign yyyy   


transform bg_zoom_otd(z=1.0, zz=1.0, t=0.0, x=0.5, xx=0.5, y=0.5, yy=0.5, c=1.0, cc=1.0):
    subpixel True
    zoom z xalign x yalign y alpha c
    ease t zoom zz xalign xx yalign yy alpha cc


transform bg_zoom_avtfin(z=1.0, x=0.5, y=0.5, t=0.0, zz=1.0, xx=0.5, yy=0.5):
    subpixel True
    zoom z xalign x yalign y
    ease t zoom zz xalign xx yalign yy
    

transform bg_zoom_r(z=1.0, zz=1.7, t=0.5, x=0.5, xx=0.7, y=0.5, yy=0.65, r=0.0, rr=2.75, zzz=1.3, tt=0.8, xxx=0.8, yyy=0.5, rrr=0.0): #rotate(вращать)
    subpixel True
    zoom z xalign x yalign y rotate r
    ease t zoom zz xalign xx yalign yy rotate rr
    ease tt zoom zzz xalign xxx yalign yyy rotate rrr

transform bg_rotate(t=1.0, tt=1.0, r=0.0, rr=0.0, z=1.0):
    subpixel True
    xalign 0.5 yalign 0.5
    ease t zoom z rotate r alpha 1.0
    ease tt rotate rr alpha 1.0
    repeat


transform Flash_zoom:
    subpixel True
    zoom 1.4 xalign 0.5 yalign 0.5 alpha 1.0
    ease 5 zoom 1.0 xalign 0.5 yalign 0.5 alpha 1.0


transform screen_attack(z=1.2, rr=-1.9, zz=1.0, x=0.5, y=0.5):
    xalign x yalign y subpixel True
    parallel:
        ease 0.25 zoom z
        ease 0.5 zoom zz
    parallel:
        ease 0.25 rotate rr
        ease 0.25 rotate 1.0
        ease 0.25 rotate 0.0

transform screen_attack_hard(z=1.5, r=-5.9):
    xalign 0.5 yalign 0.5 subpixel True
    parallel:
        ease 0.3 zoom z
        ease 0.5 zoom 1.0
    parallel:
        ease 0.3 rotate r
        ease 0.5 rotate 1.0
        ease 0.25 rotate 0.0


transform brightness_scale_png(img, b):
    subpixel True
    im.MatrixColor("visual/bg/" + str(img) + ".png", im.matrix.brightness(b))

transform brightness_scale_jpg(img, b):
    subpixel True
    im.MatrixColor("visual/bg/" + str(img) + ".jpg", im.matrix.brightness(b))


transform rotate_hand:
    subpixel True
    zoom 0.6 xalign 0.098 yalign 0.662 rotate -20 alpha 0.75
    parallel:
        ease 0.1 zoom 0.6 xalign 0.083 yalign 0.777 rotate 90 alpha 0.75
        ease 0.5 zoom 0.6 xalign 0.098 yalign 0.662 rotate -20 alpha 0.75
        ease 0.1 zoom 0.6 xalign 0.083 yalign 0.777 rotate 90 alpha 0.75
        ease 0.3 zoom 0.6 xalign 0.098 yalign 0.662 rotate -60 alpha 0.75
        pause 0.3
        repeat
    

transform four_contains_xyzoom_effects(name):
    subpixel True
    parallel:
        choice:
            "visual/animation/" + name + "1.png"
        choice:
            "visual/animation/" + name + "2.png"
        choice:
            "visual/animation/" + name + "3.png"
        choice:
            "visual/animation/" + name + "4.png"
    xanchor 0.5 yanchor 0.5 xpos 0.5 ypos 0.5
    parallel:
        parallel:
            choice:
                xzoom 1.0
            choice:
                xzoom -1.0
        parallel:
            choice:
                yzoom 1.0
            choice:
                yzoom -1.0
    pause 0.02
    repeat



transform pris1:
    subpixel True
    parallel:
        ease 1.0 ypos 0.23
    parallel:
        ease 0.75 zoom 1.05
        ease 0.5 zoom 1.0 


transform pris2:
    subpixel True
    parallel:
        ease 1.0 ypos 0.07
    parallel:
        ease 0.75 zoom 1.05
        ease 0.5 zoom 1.0              
   

transform ts:
    tcommon(1.5, 960)

transform tcommon(e, x):
    subpixel True
    on show:
        alpha 0.0 xcenter x
        easein e alpha 1.0
    on replace:
        alpha 1.0
        parallel:
            easein e xcenter x
        parallel:
            easein 0.5

transform up(e, x):
    subpixel True
    yoffset 1500 xcenter x
    ease e yoffset 0.0

transform walking1:
    subpixel True
    parallel:
        xanchor 0.5 yanchor 0.5 xpos 0.5 ypos 0.5
        ease 0.5 zoom 1.04 xpos 0.5 ypos 0.49
    parallel:
        ease 0.5 xpos 0.5 ypos 0.492
        ease 0.5 xpos 0.484 ypos 0.508
        ease 0.5 xpos 0.5 ypos 0.492
        ease 0.5 xpos 0.516 ypos 0.508
        repeat
   
transform walking2:
        subpixel True
        zoom 1.01 align (0.5, 0.5)
        ease 0.35 xalign 0.35 yalign 0.65
        ease 0.35 xalign 0.50 yalign 0.50
        ease 0.35 xalign 0.65 yalign 0.65
        ease 0.35 xalign 0.50 yalign 0.50
        repeat       

transform walking3:
        subpixel True
        align (0.5, 0.5)
        zoom 1.01
        ease 0.5 xalign 0.35 yalign 0.65
        ease 0.5 xalign 0.50 yalign 0.50
        ease 0.5 xalign 0.65 yalign 0.65
        ease 0.5 xalign 0.50 yalign 0.50
        repeat  
        
        
transform run:
        subpixel True
        zoom 1.05 anchor (48,27)
        ease 0.20 pos (0, 0)
        ease 0.20 pos (25,25)
        ease 0.20 pos (0, 0)
        ease 0.20 pos (-25,25)
        repeat
        
        
transform run_fast:
        subpixel True
        zoom 1.05 anchor (48,27)
        ease 0.12 pos (0, 0)
        ease 0.12 pos (25,25)
        ease 0.12 pos (0, 0)
        ease 0.12 pos (-25,25)
        repeat
        


transform punch(x=0,y=0):
        subpixel True
        anchor (0.5, 0.5)
        pos (0.5+x, 0.5+y)
        rotate 0
        parallel:
            ease 0.4 pos (0.75+x, 1.33+y)
        parallel:
            ease 0.5 rotate 90


transform bghorrorflicker(t=0):
    subpixel True
    truecenter
    t + 0.000
    parallel:
        zoom 1.05
        linear 0.2 zoom 1.04
        0.1
        zoom 1.035
        linear 0.1 zoom 1.05
        zoom 1.0
        1.19
        repeat
    parallel:
        easeout_bounce 0.3 xalign 0.6
        easeout_bounce 0.3 xalign 0.4
        repeat
    



        

transform linear_effects_repeat(a, x, xx, xxx, xxxx, xxxxx, xxxxxx, z=1):
    subpixel True
    xzoom z
    contains:
        "snow" 
        xanchor x yanchor 0.75 xpos 0.5 ypos 0.5
        linear 0.5 xanchor xxxx yanchor 0.25 alpha a
        repeat
    contains:
        "snow"
        xanchor xx yanchor 0.75 xpos 0.5 ypos 0.5 zoom 0.9
        linear 0.75 xanchor xxxxx yanchor 0.25 alpha a
        repeat
    contains:
        "snow"
        xanchor xxx yanchor 0.7 xpos 0.5 ypos 0.5 zoom 0.8
        linear 1.0 xanchor xxxxxx yanchor 0.3 alpha a
        repeat
#ПРИМЕЧАНИЕ!!!
#snow right - linear_effects_repeat(0.75, 0.7, 0.75, 0.25, 0.3, 0.25)
#snow right2 - linear_effects_repeat(0.65, 0.6, 0.65, 0.35, 0.4, 0.35)
#snow right3 - linear_effects_repeat(0.5, 0.6, 0.75, 0.4, 0.5, 0.65)
#snow left - linear_effects_repeat(0.75, 0.7, 0.75, 0.25, 0.3, 0.25, -1)
#snow left2 - linear_effects_repeat(0.65, 0.6, 0.65, 0.35, 0.4, 0.35, -1)
#snow left3 - linear_effects_repeat(0.5, 0.6, 0.75, 0.4, 0.5, 0.65, -1)

transform light_and_dust_contains(img):
    contains:
        "visual/dust/" + img + ".png"
        light_alpha_ease_repeat
    contains:
        "dust5"
        dust_alpha_ease_repeat
    contains:
        "dust6"
        dust_alpha_ease_repeat
    contains:
        "dust9"
        dust_alpha_ease_repeat
    contains:
        "dust10"
        dust_alpha_ease_repeat
    contains:
        "dust11"
        dust_alpha_ease_repeat
    contains:
        "dust12"
        dust_alpha_ease_repeat

transform dust_alpha_ease_repeat:
    alpha 0.6 subpixel True
    parallel:
        ease 7.0 alpha 0.8
        pause 12
        ease 7.0 alpha 0.01
        pause 5
        repeat

transform light_alpha_ease_repeat:
    alpha 0 subpixel True
    parallel:
        ease 7.0 alpha 0.48
        pause 12
        ease 7.0 alpha 0.05
        pause 5
        repeat

transform dust_alpha_linear_repeat(name, p, l):
    "visual/dust/dust" + str(name) + ".png"
    subpixel True
    parallel:
        alpha 0.48
        6.0
        linear 1.0 alpha 0.4
        1.0
        linear 1.0 alpha 0.62
        repeat
    parallel:
        alpha 0
        linear 2.0 alpha 0.48
        10.0
        linear 2.0 alpha 0
        repeat
    parallel:
        xoffset 100 yoffset -100
        linear l xoffset -100 yoffset 100
        linear 2.0 alpha 0
        repeat


transform Fl_ease_slowly_repeat:
    subpixel True
    contains:
        "visual/objects/smoke1.png"
        xalign 1.0 yalign 1.0
        parallel:
            linear 0.1 xalign 1.0 yalign 1.0
            linear 0.5 alpha 1.0 xalign 1.0 yalign 1.0
            linear 45.0 xalign 0.0
            linear 0.5 alpha 0.0
            repeat
    contains:
        "visual/objects/smoke1.png"
        xalign 1.0 yalign 1.0
        parallel:
            linear 0.6 alpha 0.0
            pause 45.0
            linear 0.5 alpha 1.0
            repeat
    contains:
        "visual/objects/smoke2.png"
        xalign 0.0 yalign 1.0
        parallel:
            linear 0.1 xalign 0.0 yalign 1.0
            linear 0.5 alpha 1.0 xalign 0.0 yalign 1.0
            linear 60.0 xalign 1.0
            linear 0.5 alpha 0.0
            repeat


transform Fl_head_heartbeat:
    linear 0.3 zoom 1.01 align (0.5, 0.5) subpixel True
    pause 0.2
    linear 0.3 zoom 1.0 align (0.5, 0.5)
    pause 0.2
    repeat

transform Fl_head_heartbeat_vignette_move:
    subpixel True
    linear 0.3 alpha 0.7
    pause 0.2
    linear 0.3 alpha 0.0
    pause 0.2
    repeat


#Для спрайтов
transform center:
    yalign 0.5 xalign 0.5

transform left:
    yalign 0.5 xalign 0.05

transform right:
    yalign 0.5 xalign 0.85

transform fleft:
    yalign 0.5 xalign 0.01

transform fright:
    yalign 0.5 xalign 0.98

transform cleft:
    yalign 0.5 xalign 0.2

transform cright:
    yalign 0.5 xalign 0.7




transform easeoutleft:
    subpixel True
    ease 0.5 ypos 0.0
    ease 2 xalign -2.0

transform easeoutright:
    subpixel True
    ease 0.5 ypos 0.0
    ease 2 xalign 2.0

transform easeinleft:
    subpixel True
    ease 0.5 xalign -2.0
    ease 2 ypos 0.0

transform easeinright:
    subpixel True
    ease 0.5 xalign 2.0
    ease 2 ypos 0.0




transform shake(s=10, z=1.05, x=0.5, y=0.5, t=0.07, rep=None):
    subpixel True
    zoom z-0.05 xalign x yalign y xoffset 0 yoffset 0
    parallel:
        linear 1.0 zoom z
    parallel:
        linear t xoffset 0+s
        linear t xoffset 0-s
        linear t xoffset 0
        repeat rep
    parallel:
        linear t-(t/7) yoffset 0+s
        linear t-(t/7) yoffset 0-s
        linear t-(t/7) yoffset 0
        repeat rep



transform screen_shake(sh):
    subpixel True
    xalign 0.5 yalign 0.5
    parallel:
        ease 0.1 xpos 0.505+sh
        ease 0.1 xpos 0.4975-sh
        ease 0.1 xpos 0.5095+sh
        ease 0.1 xpos 0.495-sh
        ease 0.1 xpos 0.505+sh
        ease 0.1 xpos 0.4975-sh
        ease 0.1 xpos 0.5095+sh
        ease 0.1 xpos 0.495-sh
        ease 0.1 xpos 0.505+sh
        ease 0.2 xpos 0.4975-sh
        ease 0.2 xpos 0.5095+sh
        ease 0.2 xpos 0.5
    parallel:
        ease 0.11 ypos 0.5+sh
        ease 0.11 ypos 0.489-sh
        ease 0.11 ypos 0.5+sh
        ease 0.11 ypos 0.489-sh
        ease 0.11 ypos 0.5+sh
        ease 0.11 ypos 0.489+sh
        ease 0.11 ypos 0.5-sh
        ease 0.11 ypos 0.489-sh
        ease 0.11 ypos 0.5+sh
        ease 0.2 ypos 0.489-sh
        ease 0.2 ypos 0.5+sh
        ease 0.2 ypos 0.5
    parallel:
        ease 0.10 rotate -0.3
        ease 0.10 rotate -0.17
        ease 0.10 rotate -0.2
        ease 0.10 rotate 0.17
        ease 0.10 rotate 0.3
        ease 0.10 rotate 0.2
        ease 0.10 rotate 0.17
        ease 0.10 rotate -0.3
        ease 0.10 rotate -0.17
        ease 0.10 rotate -0.2
        ease 0.10 rotate 0.17
        ease 0.10 rotate 0.3
        ease 0.10 rotate 0.2
        ease 0.15 rotate 0.17
        ease 0.15 rotate -0.2
        ease 0.15 rotate 0.17
        ease 0.15 rotate 0.3
        ease 0.15 rotate 0.2
        ease 0.15 rotate 0.0
    parallel:
        ease 0.05 zoom 0.99
        ease 0.05 zoom 1.03
        ease 0.05 zoom 0.99
        ease 0.05 zoom 1.02
        ease 0.05 zoom 0.99
        ease 0.05 zoom 1.03
        ease 0.05 zoom 1.01
        ease 0.05 zoom 0.99
        ease 0.05 zoom 1.03
        ease 0.05 zoom 0.99
        ease 0.05 zoom 1.03
        ease 0.05 zoom 0.99
        ease 0.05 zoom 1.02
        ease 0.05 zoom 0.99
        ease 0.05 zoom 1.03
        ease 0.05 zoom 1.01
        ease 0.05 zoom 0.99
        ease 0.05 zoom 1.03
        ease 0.05 zoom 0.99
        ease 0.05 zoom 1.03
        ease 0.05 zoom 0.99
        ease 0.05 zoom 1.02
        ease 0.05 zoom 0.99
        ease 0.05 zoom 1.03
        ease 0.05 zoom 1.01
        ease 0.05 zoom 0.99
        ease 0.05 zoom 1.00
        ease 0.1 zoom 0.99
        ease 0.1 zoom 1.03
        ease 0.1 zoom 1.01
        ease 0.1 zoom 0.99
        ease 0.1 zoom 1.00


#Экраны
transform screen_attack(z=1.2, rr=-1.9, zz=1.0, x=0.5, y=0.5):
    subpixel True
    xalign x yalign y
    parallel:
        ease 0.25 zoom z
        ease 0.5 zoom zz
    parallel:
        ease 0.25 rotate rr
        ease 0.25 rotate 1.0
        ease 0.25 rotate 0.0

transform screen_attack_hard(z=1.5, r=-5.9):
    subpixel True
    xalign 0.5 yalign 0.5
    parallel:
        ease 0.3 zoom z
        ease 0.5 zoom 1.0
    parallel:
        ease 0.3 rotate r
        ease 0.5 rotate 1.0
        ease 0.25 rotate 0.0




transform shake_motion(s=10, z=1.0, x=0.5, y=0.5, t=0.07, p=0):
    subpixel True
    circular_motion(p)
    ease 0.1 anchor (0.5, 0.5) rotate 0 zoom z xalign x yalign y xoffset 0 yoffset 0
    parallel:
        linear t xoffset 0+s
        linear t xoffset 0-s
        repeat
    parallel:
        linear t-(t/7) yoffset 0+s
        linear t-(t/7) yoffset 0-s

transform circular_dizziness(p=0):
    subpixel True
    circular_motion(p)
    ease 0.1 anchor (0.5, 0.5) rotate 0
    parallel:
        ease 0.1 xoffset 0
        ease 0.1 xoffset -10
        ease 0.1 xoffset -20
        ease 0.1 xoffset -30
        ease 0.1 xoffset -20
        ease 0.1 xoffset -10
        ease 0.1 xoffset 0
        ease 0.1 xoffset 10
        ease 0.1 xoffset 20
        ease 0.1 xoffset 30
        ease 0.1 xoffset 20
        ease 0.1 xoffset 10
        repeat
    parallel:
        ease 0.15 yoffset 0
        ease 0.15 yoffset -8
        ease 0.15 yoffset -16
        ease 0.15 yoffset -24
        ease 0.15 yoffset -16
        ease 0.15 yoffset -8
        ease 0.15 yoffset 0
        ease 0.15 yoffset 8
        ease 0.15 yoffset 16
        ease 0.15 yoffset 24
        ease 0.15 yoffset 16
        ease 0.15 yoffset 8
        repeat


transform circular_motion(p=0):
    subpixel True
    bg_zoom_e(1.0, 1.0, 0.0, 0.5, 0.5, 0.5, 0.5)
    pos (0.5, 0.5)
    pause p
    block:
        parallel:
            parallel:
                choice:
                    xanchor 0.2
                choice:
                    xanchor 0.3
                choice:
                    xanchor 0.4
                choice:
                    xanchor 0.5
                choice:
                    xanchor 0.6
                choice:
                    xanchor 0.7
                choice:
                    xanchor 0.8
            parallel:
                choice:
                    yanchor 0.2
                choice:
                    yanchor 0.3
                choice:
                    yanchor 0.4
                choice:
                    yanchor 0.5
                choice:
                    yanchor 0.6
                choice:
                    yanchor 0.7
                choice:
                    yanchor 0.8
        parallel:
            choice:
                rotate -2
            choice:
                rotate -1
            choice:
                rotate 0
            choice:
                rotate 1
            choice:
                rotate 2
        pause 0.02
        repeat 20
    ease 0.1 anchor (0.5, 0.5) rotate 0 zoom 1.0 xalign 0.5 yalign 0.5 xoffset 0 yoffset 0



transform hidescreens(e):
    subpixel True
    xpos 0.0 ypos 0.0 alpha 1.0
    ease e xpos 0.0 ypos 0.1 alpha 0.0

transform screen_normal(l=2.0):
    subpixel True
    linear l xalign 0.5 yalign 0.5 zoom 1.0


transform preview_anim:
    contains:
        "#00000000"
        subpixel True
        zoom 0.7 xalign 0.6 yalign 0.56 xoffset -50
        pause 1.5
        "visual/preview/text.png" with ImageDissolve("visual/move/Fl_effect_right.png", 1, alpha=True)
        ease 0.7 xoffset 0
    contains:
        "visual/preview/logo.png"
        zoom 0.6 xalign 0.5 yalign 0.5 xanchor 0.5 yanchor 0.5 xoffset 0 subpixel True rotate 0 rotate_pad True
        ease 1.0 zoom 0.6 rotate 1440
        pause 0.2
        ease 0.7 xoffset -280









