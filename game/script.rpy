# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

#sample character
define e = Character("Eileen")

#CHARACTERS
define ignias = Character("Ignias", who_color="#B29782")
define moira = Character("Moira", who_color="#c285e0")
define imp = Character("Imp")
define lucifer = Character("Lucifer")

#IMAGES
image bgHell = im.Scale("OfficeBG.jpg", 1920, 1080)
image Hallway = im.Scale("HallwayBG.jpg", 1920, 1080)
image ThroneRoom = im.Scale("ThroneRoomBG.jpg", 1920, 1080)
image lucifer :
     im.Scale("Boss.png",989,1194)

     #yoffset 1.5
transform rightt:
    xalign 1.0
    yalign 0.3
image loadscreen = Movie(play = "LoadinScreenNoLoop.mp4")
#image ignias = im.Scale("Ignias100.png",631,872)
#image moira = im.Scale("Moira100.png",690,813)
#image fish = im.Scale("Fish100.png",340,629)



#Animated Characterstates

    #IGNIAS
default ignias_mood = "Default" #Moods: Default, DefaultTalk, Happy, Mad, MadTalk, Sad, SadTalk, Suprised, SuprisedTalk

image ignias Default:
    "Ignias/[ignias_mood]/BlinkF0.png"
    2.0
    "Ignias/[ignias_mood]/BlinkF1.png"
    .1
    "Ignias/[ignias_mood]/BlinkF2.png"
    1.0
    "Ignias/[ignias_mood]/BlinkF1.png"
    .1
    "Ignias/[ignias_mood]/BlinkF0.png"
    .8
    "Ignias/[ignias_mood]/BlinkF1.png"
    .1
    "Ignias/[ignias_mood]/BlinkF2.png"
    .1
    "Ignias/[ignias_mood]/BlinkF1.png"
    .1
    "Ignias/[ignias_mood]/BlinkF0.png"
    2.0
    repeat

image ignias DefaultTalk:
    "Ignias/[ignias_mood]/BlinkF0.png"
    2.0
    "Ignias/[ignias_mood]/BlinkF1.png"
    .1
    "Ignias/[ignias_mood]/BlinkF2.png"
    1.0
    "Ignias/[ignias_mood]/BlinkF1.png"
    .1
    "Ignias/[ignias_mood]/BlinkF0.png"
    .8
    "Ignias/[ignias_mood]/BlinkF1.png"
    .1
    "Ignias/[ignias_mood]/BlinkF2.png"
    .1
    "Ignias/[ignias_mood]/BlinkF1.png"
    .1
    "Ignias/[ignias_mood]/BlinkF0.png"
    2.0
    repeat

image ignias Happy:
    "Ignias/[ignias_mood]/BlinkF0.png"
    2.0
    "Ignias/[ignias_mood]/BlinkF1.png"
    .1
    "Ignias/[ignias_mood]/BlinkF2.png"
    .5
    "Ignias/[ignias_mood]/BlinkF1.png"
    .1
    "Ignias/[ignias_mood]/BlinkF0.png"
    1.0
    "Ignias/[ignias_mood]/BlinkF1.png"
    .1
    "Ignias/[ignias_mood]/BlinkF2.png"
    .1
    "Ignias/[ignias_mood]/BlinkF1.png"
    .1
    "Ignias/[ignias_mood]/BlinkF0.png"
    2.0
    repeat

image ignias Mad = "Ignias/[ignias_mood]/[ignias_mood].png"

image ignias MadTalk = "Ignias/[ignias_mood]/[ignias_mood].png"

image ignias Sad = "Ignias/[ignias_mood]/[ignias_mood].png"
image igSadFlip:
    im.Flip("Ignias/Sad/Sad.png", horizontal="True")
    zoom 0.78

image ignias SadTalk = "Ignias/[ignias_mood]/[ignias_mood].png"

image ignias Suprised:
    "Ignias/[ignias_mood]/BlinkF0.png"
    1.5
    "Ignias/[ignias_mood]/BlinkF1.png"
    .1
    "Ignias/[ignias_mood]/BlinkF2.png"
    .1
    "Ignias/[ignias_mood]/BlinkF3.png"
    .1
    "Ignias/[ignias_mood]/BlinkF2.png"
    .1
    "Ignias/[ignias_mood]/BlinkF1.png"
    .1
    "Ignias/[ignias_mood]/BlinkF0.png"
    1.0
    "Ignias/[ignias_mood]/BlinkF1.png"
    .05
    "Ignias/[ignias_mood]/BlinkF2.png"
    .05
    "Ignias/[ignias_mood]/BlinkF3.png"
    .05
    "Ignias/[ignias_mood]/BlinkF2.png"
    .05
    "Ignias/[ignias_mood]/BlinkF1.png"
    .05
    "Ignias/[ignias_mood]/BlinkF2.png"
    .05
    "Ignias/[ignias_mood]/BlinkF3.png"
    .05
    "Ignias/[ignias_mood]/BlinkF2.png"
    .05
    "Ignias/[ignias_mood]/BlinkF1.png"
    .05
    "Ignias/[ignias_mood]/BlinkF0.png"
    1.5
    repeat

image ignias SuprisedTalk:
    "Ignias/[ignias_mood]/BlinkF0.png"
    1.5
    "Ignias/[ignias_mood]/BlinkF1.png"
    .1
    "Ignias/[ignias_mood]/BlinkF2.png"
    .1
    "Ignias/[ignias_mood]/BlinkF3.png"
    .1
    "Ignias/[ignias_mood]/BlinkF2.png"
    .1
    "Ignias/[ignias_mood]/BlinkF1.png"
    .1
    "Ignias/[ignias_mood]/BlinkF0.png"
    .8
    "Ignias/[ignias_mood]/BlinkF1.png"
    .05
    "Ignias/[ignias_mood]/BlinkF2.png"
    .05
    "Ignias/[ignias_mood]/BlinkF3.png"
    .05
    "Ignias/[ignias_mood]/BlinkF2.png"
    .05
    "Ignias/[ignias_mood]/BlinkF1.png"
    .05
    "Ignias/[ignias_mood]/BlinkF0.png"
    .05
    "Ignias/[ignias_mood]/BlinkF1.png"
    .05
    "Ignias/[ignias_mood]/BlinkF2.png"
    .05
    "Ignias/[ignias_mood]/BlinkF3.png"
    .05
    "Ignias/[ignias_mood]/BlinkF2.png"
    .05
    "Ignias/[ignias_mood]/BlinkF1.png"
    .05
    "Ignias/[ignias_mood]/BlinkF0.png"
    1.5
    repeat

image ignias:
    LiveComposite(
    (819,1133), #(width, height)
    (0,0), ConditionSwitch(
    "ignias_mood == 'Default'", "ignias Default",
    "ignias_mood == 'DefaultTalk'", "ignias DefaultTalk",
    "ignias_mood == 'Happy'", "ignias Happy",
    "ignias_mood == 'Mad'", "ignias Mad",
    "ignias_mood == 'MadTalk'", "ignias MadTalk",
    "ignias_mood == 'Sad'", "ignias Sad",
    "ignias_mood == 'SadTalk'", "ignias SadTalk",
    "ignias_mood == 'Suprised'", "ignias Suprised",
    "ignias_mood == 'SuprisedTalk'", "ignias SuprisedTalk",)
    )
    zoom 0.78

    #MOIRA
default moira_mood = "Default" #Moods: Default, DefaultTalk, Happy, Mad, MadTalk, Sad, SadTalk, Suprised, SuprisedTalk

image moira Default:
    "Moira/[moira_mood]/BlinkF0.png"
    1.5
    "Moira/[moira_mood]/BlinkF1.png"
    .1
    "Moira/[moira_mood]/BlinkF2.png"
    .8
    "Moira/[moira_mood]/BlinkF1.png"
    .1
    "Moira/[moira_mood]/BlinkF0.png"
    .8
    "Moira/[moira_mood]/BlinkF1.png"
    .1
    "Moira/[moira_mood]/BlinkF2.png"
    .1
    "Moira/[moira_mood]/BlinkF1.png"
    .1
    "Moira/[moira_mood]/BlinkF0.png"
    1.5
    repeat

image moira DefaultTalk:
    "Moira/[moira_mood]/BlinkF0.png"
    1.5
    "Moira/[moira_mood]/BlinkF1.png"
    .1
    "Moira/[moira_mood]/BlinkF2.png"
    .8
    "Moira/[moira_mood]/BlinkF1.png"
    .1
    "Moira/[moira_mood]/BlinkF0.png"
    1.0
    "Moira/[moira_mood]/BlinkF1.png"
    .1
    "Moira/[moira_mood]/BlinkF2.png"
    .1
    "Moira/[moira_mood]/BlinkF1.png"
    .1
    "Moira/[moira_mood]/BlinkF0.png"
    1.5
    repeat

image moira Happy:
    "Moira/[moira_mood]/BlinkF0.png"
    1.5
    "Moira/[moira_mood]/BlinkF1.png"
    .1
    "Moira/[moira_mood]/BlinkF2.png"
    .8
    "Moira/[moira_mood]/BlinkF1.png"
    .1
    "Moira/[moira_mood]/BlinkF0.png"
    1.0
    "Moira/[moira_mood]/BlinkF1.png"
    .1
    "Moira/[moira_mood]/BlinkF2.png"
    .1
    "Moira/[moira_mood]/BlinkF1.png"
    .1
    "Moira/[moira_mood]/BlinkF0.png"
    1.5
    repeat

image moira Mad = "Moira/[moira_mood]/[moira_mood].png"
image moira MadTalk = "Moira/[moira_mood]/[moira_mood].png"
image moira Sad = "Moira/[moira_mood]/[moira_mood].png"
image Flip :
    im.Flip("Moira/Sad/Sad.png", horizontal="True")
    zoom 0.78
image FlipTalk :
    im.Flip("Moira/SadTalk/SadTalk.png", horizontal="True")
    zoom 0.78
image moira SadTalk = "Moira/[moira_mood]/[moira_mood].png"

image moira Suprised:
    "Moira/[moira_mood]/BlinkF0.png"
    1.5
    "Moira/[moira_mood]/BlinkF1.png"
    .04
    "Moira/[moira_mood]/BlinkF2.png"
    .04
    "Moira/[moira_mood]/BlinkF3.png"
    .04
    "Moira/[moira_mood]/BlinkF2.png"
    .04
    "Moira/[moira_mood]/BlinkF1.png"
    .04
    "Moira/[moira_mood]/BlinkF0.png"
    .04
    "Moira/[moira_mood]/BlinkF1.png"
    .04
    "Moira/[moira_mood]/BlinkF2.png"
    .04
    "Moira/[moira_mood]/BlinkF3.png"
    .04
    "Moira/[moira_mood]/BlinkF2.png"
    .04
    "Moira/[moira_mood]/BlinkF1.png"
    .04
    "Moira/[moira_mood]/BlinkF0.png"
    1.5
    repeat

image moira SuprisedTalk:
    "Moira/[moira_mood]/BlinkF0.png"
    1.5
    "Moira/[moira_mood]/BlinkF1.png"
    .04
    "Moira/[moira_mood]/BlinkF2.png"
    .04
    "Moira/[moira_mood]/BlinkF3.png"
    .04
    "Moira/[moira_mood]/BlinkF2.png"
    .04
    "Moira/[moira_mood]/BlinkF1.png"
    .04
    "Moira/[moira_mood]/BlinkF0.png"
    .04
    "Moira/[moira_mood]/BlinkF1.png"
    .04
    "Moira/[moira_mood]/BlinkF2.png"
    .04
    "Moira/[moira_mood]/BlinkF3.png"
    .04
    "Moira/[moira_mood]/BlinkF2.png"
    .04
    "Moira/[moira_mood]/BlinkF1.png"
    .04
    "Moira/[moira_mood]/BlinkF0.png"
    1.5
    repeat

image moira:
    LiveComposite(
    (867,1016), #(width, height)
    (0,0), ConditionSwitch(
    "moira_mood == 'Default'", "moira Default",
    "moira_mood == 'DefaultTalk'", "moira DefaultTalk",
    "moira_mood == 'Happy'", "moira Happy",
    "moira_mood == 'Mad'", "moira Mad",
    "moira_mood == 'MadTalk'", "moira MadTalk",
    "moira_mood == 'Sad'", "moira Sad",
    "moira_mood == 'SadTalk'", "moira SadTalk",
    "moira_mood == 'Suprised'", "moira Suprised",
    "moira_mood == 'SuprisedTalk'", "moira SuprisedTalk",)
    )
    zoom 0.78

#IMP
default imp_mood = "Default" #Moods: Default, Mad

image imp Default:
    "Imp/[imp_mood]/BlinkF0.png"
    3.0
    "Imp/[imp_mood]/BlinkF1.png"
    .1
    "Imp/[imp_mood]/BlinkF2.png"
    .1
    "Imp/[imp_mood]/BlinkF1.png"
    .1
    repeat

image imp Mad:
    "Imp/[imp_mood]/BlinkF0.png"
    1.5
    "Imp/[imp_mood]/BlinkF1.png"
    .1
    "Imp/[imp_mood]/BlinkF2.png"
    .1
    "Imp/[imp_mood]/BlinkF1.png"
    .1
    "Imp/[imp_mood]/BlinkF0.png"
    1.5
    repeat

image imp:
    LiveComposite(
    (1000,1200), #(width, height)
    (0,0), ConditionSwitch(
    "imp_mood == 'Default'", "imp Default",
    "imp_mood == 'Mad'", "imp Mad",)
    )
    zoom 0.78

#AUDIO
define audio.knock = "audio/knock1.mp3"
define audio.crashing = "audio/crashing.mp3"

#Flags
$ impStrike = False
$ heavenCalls = False
$ neighbourhoodBeef = False
$ sabotage = False
$ overheat = False

#titles
#image soul_event = Text(_("Souls which actually belong in heaven got extracted"), size=70, yalign=.35,color="#fff")
#image imp_event = Text(_("Imps want more to do"), size=70, yalign=.35,color="#fff")
#image soul_event2 = Text(_(" Soul extraction vets overheating"), size=70, yalign=.35,color="#fff")
#image hellhound_event = Text(_(" Hellhound escapes"), size=70, yalign=.35,color="#fff")
#image rival_event = Text(_(" Sabotage by rival"), size=70, yalign=.35,color="#fff")

#StatusBar
init:
    $ stress = 0 #max 65
    $ impeachment  = 0 #max 65
    $ souls = 0 #max 85
    $ counter = 0
    $ newval = 0
    $ day = 1
    $ gameOver = False

#Stressbar
screen stressbar:
    #text "Stress" vertical True size 20 xalign 0.02 yalign 0.05  outlines [ (absolute(2), "#000", absolute(0), absolute(0)) ]
    bar value StaticValue (stress, 100):
        xalign 0.0165 yalign 0.13
        xmaximum 200
        ymaximum 75
        left_bar Frame("StressFULL2.png", 0, 00 )
        right_bar Frame("StressEMPTY.png", 0, 0)
        #thumb "_theme_bordered/brvslider_thumb.png"
        thumb_shadow None


#Soulbar
screen soulbar:
    #text "Souls" vertical True size 20 xalign 0.05 yalign 0.05  outlines [ (absolute(2), "#000", absolute(0), absolute(0)) ]
    bar value StaticValue (souls, 100):
        xalign 0.0195 yalign 0.00
        xmaximum 500
        ymaximum 75
        left_bar Frame("SoulsFULL2.png", 0, 0)
        right_bar Frame("SoulsEMPTY.png", 0, 0)
        #thumb "_theme_marker/inkvslider_thumb.png"
        thumb_shadow None

#Impeachmentbar
screen impeachmentbar:
    #text "Impeachment" vertical True size 11 xalign 0.08 yalign 0.05  outlines [ (absolute(2), "#000", absolute(0), absolute(0)) ]
    bar value StaticValue (impeachment, 100):
        xalign 0.016 yalign 0.07
        xmaximum 200
        ymaximum 75
        left_bar Frame("ImpeachmentFULL2.png", 0, 0)
        right_bar Frame("ImpeachmentEMPTY.png", 0, 0)
        #thumb "_theme_regal/revslider_thumb.png"
        thumb_shadow None

#Increase Bar function
init python:
    def increaseStress(val):
        global stress
        global counter
        counter = 0
        while counter < val:
            if(stress < 0 or stress > 100):
                renpy.jump("gameover")
            stress += 1
            counter += 1
            renpy.pause(0.01)
    def increaseSouls(val):
        global souls
        global counter
        counter = 0
        while counter < val:
            #if(souls < 0 or souls > 100):
            #    renpy.jump("gameover")
            souls += 1
            counter += 1
            renpy.pause(0.01)
    def increaseImpeachment(val):
        global impeachment
        global counter
        counter = 0
        while counter < val:
            #if(impeachment < 0 or impeachment > 100):
            #    renpy.jump("gameover")
            impeachment += 1
            counter += 1
            renpy.pause(0.01)
    def decreaseStress(val):
        global stress
        global counter
        while counter < val:
            #if(stress < 0 or stress > 100):
            #    renpy.jump("gameover")
            stress -= 1
            counter += 1
            renpy.pause(0.01)
    def decreaseSouls(val):
        global souls
        global counter
        counter = 0
        while counter < val:
            #if(souls < 0 or souls > 100):
            #    renpy.jump("gameover")
            souls -= 1
            counter += 1
            renpy.pause(0.01)
    def decreaseImpeachment(val):
        global impeachment
        global counter
        counter = 0
        while counter < val:
            #if(impeachment < 0 or impeachment > 100):
            #    renpy.jump("gameover")
            impeachment -= 1
            counter += 1
            renpy.pause(0.01)

transform alpha_dissolve:
    alpha 0.0
    linear 0.5 alpha 1.0
    on hide:
        linear 0.5 alpha 0
    # This is to fade the bar in and out, and is only required once in your script

screen countdown:
    timer 0.01 repeat True action If(time > 0, true=SetVariable('time', time - 0.01), false=[Hide('countdown'), Jump(timer_jump)])
    bar value time range timer_range xalign 0.5 yalign 0.5 xmaximum 300 at alpha_dissolve # This is the timer bar.
    
init:
    $ timer_range = 0
    $ timer_jump = 0
    $renpy.music.register_channel("soundMoi", mixer ="voice", loop = False)
    transform flip:
        xzoom -1.0


#{i}{/i}
# The game starts here.
label start:
    stop music fadeout 1.0
    $renpy.movie_cutscene('images/LoadingScreenNoLoop.ogv', loops = 3)
    $renpy.music.set_volume(0.1,channel=u"music")
    $renpy.music.set_volume(0.4,channel=u"soundMoi")
    play music "audio/myuu-dark-creature.mp3" loop

    #Start of the Game
        #Start Day One
    call callDay from _call_callDay
    scene bgHell
    show screen soulbar
    show screen stressbar
    show screen impeachmentbar
    with fade
    call dayONE from _call_dayONE

    #End Day 1
    hide ignias
    hide screen soulbar
    hide screen stressbar
    hide screen impeachmentbar
    scene black
    with dissolve

    #Start Day 36
    $ souls = 0
    call callDay2 from _call_callDay2
    scene bgHell
    show screen soulbar
    show screen stressbar
    show screen impeachmentbar
    with fade
    call day36 from _call_day36



#label gameover:
#    $ stress = 0
#    $ impeachment  = 0
#    $ souls = 0
#    $ newval = 0
#    $ gameOver = False
#    scene black
#    hide screen soulbar
#    hide screen stressbar
#    hide screen impeachmentbar
#    with fade
#    scene black
#    with Pause(1)

#    show text "Game Over" with dissolve
#    with Pause(2)

#    hide text with dissolve
#    with Pause(1)
#    $renpy.movie_cutscene('images/LoadingScreenNoLoop.ogv', loops = 5  )
#    return
