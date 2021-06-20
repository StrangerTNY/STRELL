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
define twins = Character("Gatekeepers")
define qoe = Character ("Queen of Eyes")

#IMAGES
image bgHell = im.Scale("OfficeBG.jpg", 1920, 1080)
image Hallway = im.Scale("HallwayBG.jpg", 1920, 1080)
image ThroneRoom = im.Scale("ThroneRoomBG.jpg", 1920, 1080)
image cerbcell = im.Scale("Dungeon.jpg", 1920, 1080)
image qoeoffice = im.Scale("QueenOfficeBG", 1920, 1080)
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

#Queen of Eyes

default qoe_mood = "Default" #Moods: Default Happy Mad

image qoe Default:
    "QueenOfEyes/[qoe_mood]/Blink0.png"
    1.5
    "QueenOfEyes/[qoe_mood]/Blink1.png"
    .1
    "QueenOfEyes/[qoe_mood]/Blink2.png"
    .1
    "QueenOfEyes/[qoe_mood]/Blink1.png"
    .1
    "QueenOfEyes/[qoe_mood]/Blink0.png"
    1.5
    repeat

image qoe Happy:
    "QueenOfEyes/[qoe_mood]/Blink0.png"
    1.5
    "QueenOfEyes/[qoe_mood]/Blink1.png"
    .1
    "QueenOfEyes/[qoe_mood]/Blink2.png"
    .1
    "QueenOfEyes/[qoe_mood]/Blink1.png"
    .1
    "QueenOfEyes/[qoe_mood]/Blink0.png"
    1.5
    repeat

image qoe Mad:
    "QueenOfEyes/[qoe_mood]/Blink0.png"
    1.5
    "QueenOfEyes/[qoe_mood]/Blink1.png"
    .1
    "QueenOfEyes/[qoe_mood]/Blink2.png"
    .1
    "QueenOfEyes/[qoe_mood]/Blink1.png"
    .1
    "QueenOfEyes/[qoe_mood]/Blink0.png"
    1.5
    repeat

image qoe:
    LiveComposite(
    (980,1200), #(width, height)
    (0,0), ConditionSwitch(
    "qoe_mood == 'Default'", "qoe Default",
    "qoe_mood == 'Mad'", "qoe Mad",
    "qoe_mood == 'Happy'","qoe Happy",)
    )
    zoom 0.78

#GATEKEEPER TWINS
default twins_mood = "Default" #Moods: Default, DefaultTalk, Happy, Mad, Suprised

image twins Default:
    "GatekeeperTwins/[twins_mood]/Blink0.png"
    1.5
    "GatekeeperTwins/[twins_mood]/Blink1.png"
    .1
    "GatekeeperTwins/[twins_mood]/Blink2.png"
    .1
    "GatekeeperTwins/[twins_mood]/Blink3.png"
    1.5
    "GatekeeperTwins/[twins_mood]/Blink4.png"
    .1
    "GatekeeperTwins/[twins_mood]/Blink5.png"
    .1
    "GatekeeperTwins/[twins_mood]/Blink6.png"
    .1
    "GatekeeperTwins/[twins_mood]/Blink0.png"
    1.5
    repeat

image twins DefaultTalk:
    "GatekeeperTwins/[twins_mood]/Blink0.png"
    1.5
    "GatekeeperTwins/[twins_mood]/Blink1.png"
    .1
    "GatekeeperTwins/[twins_mood]/Blink2.png"
    .1
    "GatekeeperTwins/[twins_mood]/Blink3.png"
    1.5
    "GatekeeperTwins/[twins_mood]/Blink4.png"
    .1
    "GatekeeperTwins/[twins_mood]/Blink5.png"
    .1
    "GatekeeperTwins/[twins_mood]/Blink6.png"
    .1
    "GatekeeperTwins/[twins_mood]/Blink0.png"
    1.5
    repeat

image twins Happy:
    "GatekeeperTwins/[twins_mood]/Blink0.png"
    1.5
    "GatekeeperTwins/[twins_mood]/Blink1.png"
    .1
    "GatekeeperTwins/[twins_mood]/Blink2.png"
    .1
    "GatekeeperTwins/[twins_mood]/Blink3.png"
    1.5
    "GatekeeperTwins/[twins_mood]/Blink4.png"
    .1
    "GatekeeperTwins/[twins_mood]/Blink5.png"
    .1
    "GatekeeperTwins/[twins_mood]/Blink6.png"
    .1
    "GatekeeperTwins/[twins_mood]/Blink0.png"
    1.5
    repeat

image twins Mad:
    "GatekeeperTwins/[twins_mood]/Blink0.png"
    1.5
    "GatekeeperTwins/[twins_mood]/Blink1.png"
    .1
    "GatekeeperTwins/[twins_mood]/Blink2.png"
    .1
    "GatekeeperTwins/[twins_mood]/Blink3.png"
    1.5
    "GatekeeperTwins/[twins_mood]/Blink4.png"
    .1
    "GatekeeperTwins/[twins_mood]/Blink5.png"
    .1
    "GatekeeperTwins/[twins_mood]/Blink6.png"
    .1
    "GatekeeperTwins/[twins_mood]/Blink0.png"
    1.5
    repeat

image twins Suprised:
    "GatekeeperTwins/[twins_mood]/Blink0.png"
    1.5
    "GatekeeperTwins/[twins_mood]/Blink1.png"
    .1
    "GatekeeperTwins/[twins_mood]/Blink2.png"
    .1
    "GatekeeperTwins/[twins_mood]/Blink3.png"
    1.5
    "GatekeeperTwins/[twins_mood]/Blink4.png"
    .1
    "GatekeeperTwins/[twins_mood]/Blink5.png"
    .1
    "GatekeeperTwins/[twins_mood]/Blink6.png"
    .1
    "GatekeeperTwins/[twins_mood]/Blink0.png"
    1.5
    repeat

image twins:
    LiveComposite(
    (710,1000), #(width, height)
    (0,0), ConditionSwitch(
    "twins_mood == 'Default'", "twins Default",
    "twins_mood == 'DefaultTalk'", "twins DefaultTalk",
    "twins_mood == 'Happy'", "twins Happy",
    "twins_mood == 'Mad'", "twins Mad",
    "twins_mood == 'Suprised'", "twins Suprised",)
    )
    zoom 0.78

#CERBERUS

default cerberus_mood = "Default" #Moods: Default Happy 

image cerberus Default:
    "Cerberus/[cerberus_mood]/Blink0.png"
    1.5
    "Cerberus/[cerberus_mood]/Blink1.png"
    .1
    "Cerberus/[cerberus_mood]/Blink2.png"
    .1
    "Cerberus/[cerberus_mood]/Blink3.png"
    .1
    "Cerberus/[cerberus_mood]/Blink4.png"
    .1
    "Cerberus/[cerberus_mood]/Blink0.png"
    1.5
    repeat

image cerberus Happy:
    "Cerberus/[cerberus_mood]/Blink0.png"
    1.5
    "Cerberus/[cerberus_mood]/Blink1.png"
    .1
    "Cerberus/[cerberus_mood]/Blink2.png"
    .1
    "Cerberus/[cerberus_mood]/Blink3.png"
    .1
    "Cerberus/[cerberus_mood]/Blink4.png"
    .1
    "Cerberus/[cerberus_mood]/Blink0.png"
    1.5
    repeat

image cerberus:
    LiveComposite(
    (1040,1200), #(width, height)
    (0,0), ConditionSwitch(
    "cerberus_mood == 'Default'", "cerberus Default",
    "cerberus_mood == 'Happy'","cerberus Happy",)
    )
    zoom 0.78


#AUDIO
define audio.knock = "audio/knock1.mp3"
define audio.crashing = "audio/crashing.mp3"
define audio.timerrunout = "audio/Failure.mp3"
define audio.choicesound = "audio/Good_Choice.wav"

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

screen baroverlay:
    zorder 1
    frame:
        xalign 0.0
        yalign 0.0
        background None
        vbox:
            image "Meter_Overlay.png"
#Stressbar
screen stressbar:
    
    #text "Stress" vertical True size 20 xalign 0.02 yalign 0.05  outlines [ (absolute(2), "#000", absolute(0), absolute(0)) ]
    bar value StaticValue (stress, 100):
        xalign 0.018 yalign 0.16
        xmaximum 254
        ymaximum 72
        left_bar Frame("Stress_meter2.png", 0, 00 )
        right_bar Frame("Stress_meter2_empty.png", 0, 0)
        #thumb "_theme_bordered/brvslider_thumb.png"
        thumb_shadow None
    


#Soulbar
screen soulbar:
    
    #text "Souls" vertical True size 20 xalign 0.05 yalign 0.05  outlines [ (absolute(2), "#000", absolute(0), absolute(0)) ]
    bar value StaticValue (souls, 100):
        xalign 0.018 yalign 0.035
        xmaximum 500
        ymaximum 56
        left_bar Frame("Soul_meter2.png", 0, 0)
        right_bar Frame("Soul_meter2_empty.png", 0, 0)
        #thumb "_theme_marker/inkvslider_thumb.png"
        thumb_shadow None

#Impeachmentbar
screen impeachmentbar:
    
    #text "Impeachment" vertical True size 11 xalign 0.08 yalign 0.05  outlines [ (absolute(2), "#000", absolute(0), absolute(0)) ]
    bar value StaticValue (impeachment, 100):
        xalign 0.018 yalign 0.09
        xmaximum 254
        ymaximum 72
        left_bar Frame("Impeachment_meter2.png", 0, 0)
        right_bar Frame("Impeachment_meter2_empty.png", 0, 0)
        #thumb "_theme_regal/revslider_thumb.png"
        thumb_shadow None

#Decision Countdown
screen countdown:
    timer 0.01 repeat True action If(time > 0, true=SetVariable('time', time - 0.01), false=[Hide('countdown'), Jump(timer_jump)])
    bar value time range timer_range xalign 0.5 yalign 0.5 xmaximum 300 at alpha_dissolve # This is the timer bar.

default countermg = 0

init python:
    def minigamecallback (drags,drop):    
        global countermg
        if countermg > 6:
            countermg = 1
        if not drop:
            return

        if(drags[0].drag_name == "Ignias1"):
            drags[0].draggable = False
            drags[0].droppable = True
            drags[0].bottom()
            countermg += 1
        elif(drags[0].drag_name == "Ignias2"):
            drags[0].draggable = False
            drags[0].droppable = True
            drags[0].bottom()
            countermg += 1
        elif(drags[0].drag_name == "Imp1"):
            drags[0].draggable = False
            drags[0].droppable = True
            drags[0].bottom()
            countermg += 1
        elif(drags[0].drag_name == "Imp2"):
            drags[0].draggable = False
            drags[0].droppable = True
            drags[0].bottom()
            countermg += 1
        elif(drags[0].drag_name == "Lucifer1"):
            drags[0].draggable = False
            drags[0].droppable = True
            drags[0].bottom()
            countermg += 1
        elif(drags[0].drag_name == "Lucifer2"):
            drags[0].draggable = False
            drags[0].droppable = True
            drags[0].bottom()
            countermg += 1
        else:
            return

        if countermg == 6:
            return True
        else:
            return

        
screen minigame:
    # A map as background.
    $countermg = 0
    add "/Minigame/MinigameBG.jpg"
    zorder 99
    frame:
        xalign 0.95
        yalign 0.05
        add DynamicDisplayable(countdownmg, length=31)
   
    $ ui.timer(33.0, ui.jumps(minigame_jump)) #Label to jump to after countdown ends

    draggroup:
        #Where the Paper needs to be on IGNIAS
        drag:
            drag_name "IgniasDeck"
            child "/Minigame/AblageIgnias.png"
            droppable True
            draggable False
            xpos 900 ypos 140

        drag:
            drag_name "Ignias1"
            child "/Minigame/PaperIgnias.png"
            draggable True
            droppable False
            dragged minigamecallback
            xpos 920 ypos 600
        
        drag:
            drag_name "Ignias2"
            child "/Minigame/PaperIgnias.png"
            draggable True
            droppable False
            dragged minigamecallback
            xpos 950 ypos 600
    

    draggroup:
        #Where the Paper needs to be on IMPS
        drag:
            drag_name "ImpDeck"
            child "/Minigame/AblageImps.png"
            droppable True
            draggable False
            xpos 500 ypos 140

        drag:
            drag_name "Imp1"
            child "/Minigame/PaperImps.png"
            draggable True
            droppable False
            dragged minigamecallback
            xpos 530 ypos 600

        drag:
            drag_name "Imp2"
            child "/Minigame/PaperImps.png"
            draggable True
            droppable False
            dragged minigamecallback
            xpos 560 ypos 600

    draggroup:
        #Where the Paper needs to be on LUCIFER
        drag:
            drag_name "LuciferDeck"
            child "/Minigame/AblageLucifer.png"
            droppable True
            draggable False
            xpos 100 ypos 140

        drag:
            drag_name "Lucifer1"
            child "/Minigame/PaperLucifer.png"
            draggable True
            droppable False
            dragged minigamecallback
            xpos 100 ypos 600

        drag:
            drag_name "Lucifer2"
            child "/Minigame/PaperLucifer.png"
            draggable True
            droppable False
            dragged minigamecallback
            xpos 130 ypos 600


#Initializing all flags functions etc.
init:
    

    #Variablse for Decision Timer
    $ timer_range = 0
    $ timer_jump = 0
    $ minigame_jump = 0

    #Custom Music Channels
    $renpy.music.register_channel("soundMoi", mixer ="voice", loop = False)
    $renpy.music.register_channel("timer", mixer ="music", loop = False)
    $renpy.music.register_channel("minigame", mixer ="music", loop = False)
    
    #Custom Image effect
    transform flip:
        xzoom -1.0

    python:
        #Bar functions
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

        #Countdown for Minigame
        def countdownmg(st, at, length=0.0):

            remaining = length - st

            if remaining > 2.0:
                return Text("%.1f" % remaining, color="#fff", size=72), .1
            elif remaining > 0.0:
                return Text("%.1f" % remaining, color="#f00", size=72), .1
            else:
                return anim.Blink(Text("0.0", color="#f00", size=72)), None
    # Show a countdown for 10 seconds. for Minigame
    image countdownmg = DynamicDisplayable(countdownmg, length=5.0)
    

transform alpha_dissolve:
    alpha 0.0
    linear 0.5 alpha 1.0
    on hide:
        linear 0.5 alpha 0
    # This is to fade the bar in and out, and is only required once in your script



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
    call callDay 
    scene bgHell
    show screen baroverlay
    show screen soulbar
    show screen stressbar
    show screen impeachmentbar
    with fade
    call dayONE 

    #End Day 1
    hide ignias
    hide screen baroverlay
    hide screen soulbar
    hide screen stressbar
    hide screen impeachmentbar
    scene black
    with dissolve

    #Start Day 36
    $ souls = 0
    call callDay2 
    scene bgHell
    show screen baroverlay
    show screen soulbar
    show screen stressbar
    show screen impeachmentbar
    with fade
    call day36

label credits:
    
#    image splash = Text("{size=90}Company Name", text_align=0.5, ypos=0.5) #Placeholder code if you don't have anything to use as a splash image or are just pure lazy.
    image splash = "GUI/Logo.png" #This is usually going to be located in an init block executed early in the code to show it when the game loads up as a splash screen.
#    image cred = Text(credits_s, font="myfont.ttf", text_align=0.5) #use this if you want to use special fonts
    image cred = Text(credits_s, text_align=0.5)
    image theend = Text("{size=80}The End", text_align=0.5)
    image thanks = Text("{size=80}Thanks for Playing!", text_align=0.5)
    $ credits_speed = 25 #scrolling speed in seconds
    scene black #replace this with a fancy background
    show cred at Move((0.5, 5.0), (0.5, 0.0), credits_speed, repeat=False, bounce=False, xanchor="center", yanchor="bottom")
    show theend:
        yanchor 0.5 ypos 0.5
        xanchor 0.5 xpos 0.5
    with dissolve
    with Pause(3)
    hide theend
    with dissolve
    with Pause(credits_speed - 5)
    show splash:
        yanchor 0.5 ypos 0.5
        xanchor 0.5 xpos 0.5
    with dissolve
    with Pause(3)
    hide splash
    with dissolve
    with Pause(1)
    show thanks:
        yanchor 0.5 ypos 0.5
        xanchor 0.5 xpos 0.5
    with dissolve
    with Pause(4)
    hide thanks
    with dissolve
    

init python:
    credits = ('Backgrounds', 'Svean Wandt'), ('Character Design', 'Svean Wandt'), ('GUI', 'Svean Wandt'), ('Writing', 'Lukas Even'), ('Programming', 'Tony Tu'), ('Music', 'Fabian Braun'), ('Ignias', 'Sascha Clausen'), ('Moira', 'Kristin Kmietzak'), ('Imp', 'Lukas Even') , ('Lucifer', 'Sascha Clausen'), ('Queen Of Eyes', ''), ('Gatekeeper Twins', 'Svea Wandt & Lukas Büsen')
    credits_s = "{size=80}STRELL\n\n"
    c1 = ''
    for c in credits:
        if not c1==c[0]:
            credits_s += "\n{size=60}" + c[0] + "\n"
        credits_s += "{size=40}" + c[1] + "\n"
        c1=c[0]
    credits_s += "\n{size=60}Engine\n{size=40}" + renpy.version()

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
