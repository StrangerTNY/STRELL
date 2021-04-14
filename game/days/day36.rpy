label day36:
    $ignias_mood = "Sad"
    show ignias at left with dissolve
    play sound "audio/Ignias/sad.sigh1.mp3"

    ignias "{i}What I wouldn’t give to have the last few days be like the first day at the office.
    A most generous quota, respectful imps and a full night's sleep…{/i}"
    narrator "{i}Frantic knocking noises{/i}"

    play sound knock loop
    pause 2.0
    stop sound
    $moira_mood = "DefaultTalk"
    play soundMoi "audio/Moira/my apologies 1.mp3"

    moira "Ig, are you awake?"

    show moira at right with moveinright
    play sound "audio/Ignias/sad.sigh1.mp3"

    ignias "Yes, {i}still{/i} awake that is. Moira, I don’t know if I can do this anymore.
    Every time we hit the quota he raises the bar even higher…"

    $moira_mood = "SadTalk"
    play soundMoi "audio/Moira/hmm 1.mp3"

    moira "I know the job isn’t easy, but we can do this. Together. Like in the old days, remember?"

    $ignias_mood = "Happy"
    play sound "audio/Ignias/yes2.mp3"

    ignias "Thanks, Moira."
    narrator "{i}The two of them begin working{/i}"

    if sabotage:
        jump sabotageflag
    elif overheat:
        jump overheatflag

label overheatflag:
    narrator "Moira leaves the room in search of some document, and Ignias promptly begins to slack off.
    Shortly after, Infernal noises and screams waft into the room, at least more so than usual"

    hide moira with moveoutright
    hide screen soulbar
    hide screen stressbar
    hide screen impeachmentbar
    with dissolve
    scene black
    with dissolve
    pause .5
    show screen soulbar
    show screen stressbar
    show screen impeachmentbar
    scene bgHell
    with fade
    $ignias_mood = "MadTalk"
    show ignias at left with dissolve

    ignias "What is this racket? Can’t a demon at least get some rest and relaxation in their own office?"
    narrator "A knock rings through the cacophony"

    play sound knock

    ignias """You may enter.

    ...

    {size=60} YOU MAY ENTER!"""
    narrator "an imp flutters into to room, bedecked in soul splotches and dust"

    show imp at right with moveinright

    imp "Master! It’s terrible! Never seen anythin’ like it!"

    $ignias_mood = "DefaultTalk"
    play sound "audio/Ignias/listening3.mp3"

    ignias """Calm down and tell me exactly what is going on.
    {i}Don’t think I have ever seen one of the little buggers so rattled, except maybe at their own demotion.{/i}"""
    imp "It’s the soul vats milord. Since you ordered us to extract more souls, they have been runnin’ all day now,
    and they are getting hotter and hotter. I myself have seen them glowing, Milord, {b}glowing{/b}.
    That has never been seen before. {i}sweats nervously{/i}"
    ignias """{i}I will never get anywhere close to meeting today's numbers if the vats get damaged.
    That would be most disastrous for my meeting later.{/i}

    {i}Or I could order the imps to try and cool the vats somehow, because without overshooting the amount of souls that got extracted yesterday,
    I can forget about getting the quota. What in the heavens am I supposed to do here?!{/i}"""

    #CHOICE MENU START
    hide ignias
    hide imp
    with dissolve
    $ time = 4
    $ timer_range = 4
    $ timer_jump = 'standstill'

    narrator "The soul extraction vats are overheating, how do you deal with it? \n
    Choose quickly, or STRELL will choose for you!"
    show screen countdown
    menu:
        extend ''
        "Let the vats stand still for time to prevent equipment damage":
            hide screen countdown
            jump standstill
            #+Stress

        "Order imps to cool the vats":
            hide screen countdown
            jump coolvats
            #+Souls, +impeachment



label sabotageflag:
    hide screen soulbar
    hide screen stressbar
    hide screen impeachmentbar
    with dissolve
    scene black
    with dissolve
    pause .5
    show screen soulbar
    show screen stressbar
    show screen impeachmentbar
    scene bgHell
    with fade
    hide moira with dissolve
    show ignias at left with dissolve
    narrator "An Imp saunters into the room"

    show imp at right with moveinright

    imp "Oi boss, ‘ere is the form you requested."

    $ignias_mood ="SuprisedTalk"

    ignias """What form? I didn’t request any form. Hmm… says here
    {i}Form to Release Working Imps (FRWI){/i},
    which holds records of me having released Imps 354 through 489 this morning… Wait, 354 through 489?

    Moira! Do you remember which imps were assigned to handle the extraction vats as the current shift?"""

    $ignias_mood ="Suprised"
    $moira_mood = "MadTalk"
    hide imp
    show moira at right
    with dissolve
    play soundMoi "audio/Moira/no 3.mp3"

    moira "Shouldn’t you just KNOW those things instead of asking me all the time?"

    $moira_mood = "Mad"
    $ignias_mood ="SuprisedTalk"
    play sound "audio/Ignias/huh2.mp3"

    ignias "Well, probably, but-"

    $ignias_mood ="Suprised"
    play soundMoi "audio/Moira/0h 3.mp3"
    $moira_mood = "MadTalk"

    moira "Okay, but this is the last time. If I recall correctly, imps 354 through 489 were assigned as extraction workers by the current Overseer.
    Why? Did you want to assign them somewhere else?"

    $ignias_mood ="SuprisedTalk"

    ignias "{i}And they are doing nothing since this morning? Then who is manning the vats? And this signature… this couldn’t have come from me!{/i}"
    narrator "Another imp flies through the still open door"

    hide moira with dissolve
    show imp at right with moveinright

    imp "Milord, there has been an explosion in the extraction area! One of the vats seems to be damaged!"

    hide imp
    show moira at right
    with dissolve
    $moira_mood = "SuprisedTalk"
    play soundMoi "audio/Moira/0h 1.mp3"

    moira """That can’t be good. Without that vat it will be exceedingly difficult to meet today’s soul quota,
    and you know how the old coot likes his souls.
    You could probably overwork the other ones to make up for it, but that would strain them a lot.

    Or you could send some imps to repair the broken one and most likely just accept a decrease in output for today."""

    #CHOICE MENU START
    hide ignias
    hide moira
    with dissolve
    $ time = 4
    $ timer_range = 4
    $ timer_jump = 'workextra'

    narrator "A soul extraction vat is damaged, how do you deal with it? \n
    Choose quickly, or STRELL will choose for you!"

    show screen countdown
    menu:
        extend ''
        "Order imps to work the other vats extra hard":
            hide screen countdown
            jump workextra
            #+Souls, +Stress
        "Try and repair broken vat":
            hide screen countdown
            jump repairvats
            #+impeachment, +Souls


    #NEXT EVENT
label heavensouls:
    hide screen soulbar
    hide screen stressbar
    hide screen impeachmentbar
    with dissolve
    scene black
    with dissolve
    pause .5
    show screen soulbar
    show screen stressbar
    show screen impeachmentbar
    scene bgHell
    with fade
    $ignias_mood = "MadTalk"
    $moira_mood ="DefaultTalk"

    narrator "{i}Moira rushes in{/i}"
    show moira at right with moveinright
    show ignias at left with dissolve
    play sound "audio/Ignias/sad.sigh1.mp3"

    ignias"Can’t you at least knock?"

    play soundMoi"audio/Moira/no 1.mp3"

    moira"Don’t give me that, there’s a problem!"

    $ignias_mooda = "DefaultTalk"
    play sound "/audio/Ignias/ts4.mp3"

    ignias "Again? What is going on these days? Can’t you deal with it?"
    #*half annoyed, half mockingly*
    play soundMoi "audio/Moira/oh really 3.mp3"

    moira "You’re the Overseer! Remember?
    Anyway, some souls which don’t belong in hell got accidentally extracted.
    I think some imps checked the wrong box on the delivery form. The souls were just shortly stored here,
    ‘cause heaven had some storage capacity problems. What do you want to do?"

    #CHOICE MENU START
    hide ignias
    hide moira
    with dissolve
    $ time = 4
    $ timer_range = 4
    $ timer_jump = 'keepsouls'

    narrator "How do you fare with the illegally acquired souls? \n
    Choose quickly, or STRELL will choose for you!"
    show screen countdown
    menu:
        extend ''
        "Keep the souls, you still need some to meet your daily quota.":
            hide screen countdown
            jump keepsouls
            #+soul, stress
        "Call heaven and try to make it right":
            hide screen countdown
            jump callheaven
            #+stress, impeachment


    #NEXT EVENT
label lucifersouls:
    hide screen soulbar
    hide screen stressbar
    hide screen impeachmentbar
    with dissolve
    scene black
    with dissolve
    pause .5
    show screen soulbar
    show screen stressbar
    show screen impeachmentbar
    scene bgHell
    with fade
    show ignias at left with dissolve
    narrator "Hell-phone rings"

    $ignias_mood ="Suprised"

    ignias "{i}Let’s hope this is not who I think it is…{/i}"
    narrator "Ignias picks up the phone, and an imposing image of Lucifer {nw}"

    show lucifer at right with flash
    play sound "audio/Lucifer/hmgr 1.mp3"

    narrator "{i}Ignias picks up the phone, and an imposing image of Lucifer{fast} manifests
    itself in the middle of the room {/i}"
    lucifer "GREETINGS, OVERSEER 26. IT HAS COME TO MY ATTENTION THAT YOUR DEPARTMENT
    HAS BEEN LACKING IN THE DELIVERY OF CERTAIN SOULS RECENTLY."

    $ignias_mood = "SuprisedTalk"
    play sound "audio/Ignias/huh2.mp3"

    ignias "Lacking in certain souls, my lord? I thought we had reached yesterday’s quota-"
    narrator "{i}Lucifer interrupts him, caring little for the mundane objections of his lessers{/i}"
    lucifer "THAT WAS YESTERDAY. TODAY I HAVE ALTERED THE QUOTA. HOPE AGAINST HOPE THAT I DON’T ALTER IT FURTHER.
    YOU ARE TO DELIVER THE SOULS WHO HAVE COMMITTED SINS MOST FOUL. SEE IT DONE."
    narrator "The transmission ends, and the image of Lucifer vanishes"

    hide lucifer with flash
    $ignias_mood = "Sad"

    ignias "{i}How in the heavens am I supposed to meet such an insane demand? Is this going to be a regular occurrence?
    No wonder the last demon in my position did not last very long…{/i}"
    narrator "Moira enters the room and immediately notices the foul mood"

    $moira_mood = "DefaultTalk"
    show moira at right with moveinright
    play soundMoi "audio/Moira/0h 1.mp3"

    moira "Oh Ig, what is it now?"

    $ignias_mood = "SadTalk"

    ignias "Its Lucifer. He just showed up remotely and, just like that,
    demanded that I deliver the souls of sinners in addition of today's quota.
    But there is no way I could get this done in time…"

    play soundMoi "audio/Moira/alright 3.mp3"

    moira "Well, you could always try to facilitate some sinners yourself up there.
    Just try to find some desperate souls in dark places, make appropriate suggestions and arrange an accident.
    Or just waltz into the nearest government building, you are almost guaranteed to find some black sheep there."

    #CHOICE MENU START
    hide ignias
    hide moira
    with dissolve
    $ time = 4
    $ timer_range = 4
    $ timer_jump = 'corrupt'

    narrator "Lucifer wants specific souls; how do you get them for him? \n
    Choose quickly, or STRELL will choose for you!"

    show screen countdown
    menu:
        extend ''
        "Corrupt mortals personally":
            hide screen countdown
            jump corrupt
            #+stress, +souls

        "Send some imps to search for suitable candidates":
            hide screen countdown
            jump impsearch
            #+impeachment, +souls



    #NEXT EVENT
label hellhoundescape:
    narrator "The two reunite a few hours after and have a quick bite in the office"

    hide screen soulbar
    hide screen stressbar
    hide screen impeachmentbar
    with dissolve
    scene black
    with dissolve
    pause .5
    show screen soulbar
    show screen stressbar
    show screen impeachmentbar
    scene bgHell
    with fade
    narrator """some Imps scream

    hellhound barks

    Imp runs into the office through the already open door"""

    show imp at right with moveinright
    $ignias_mood ="MadTalk"
    show ignias at left with dissolve
    play sound "audio/Ignias/ts4.mp3"

    ignias "Who in hell left the door open? What is it now?"
    imp "Milord,
    your beloved dog ran wild, and after one of his handlers went to check on
    Kerberos he devoured him!"

    play sound "audio/Ignias/sad.sigh1.mp3"

    narrator "Ignias sighs and makes a mental note to acquire more imps"
    ignias "And what happened afterwards?"
    imp "I am afraid your dog broke free , Milord. We have no idea where he currently is."
    ignias "And why are you still here and have not gone after him already?"
    imp "Well, sire, the lads are a bit squeamish when it comes to the beas- your lovely dog."


    #CHOICE MENU START
    hide ignias
    hide imp
    with dissolve
    $ time = 4
    $ timer_range = 4
    $ timer_jump = 'askmoira'

    narrator "Your hellhound has broken loose, how do you contain the situation? \n
    Choose quickly, or STRELL will choose for you!"
    show screen countdown
    menu:
        extend ''
        "Ask Moira to go and calm down your dog":
            hide screen countdown
            jump askmoira
            #+stress

        "Send some Imps.":
            hide screen countdown
            jump sendimps
            #-Impeachment,+stress


    #ENDING
label end:

    if impeachment > 65:
        jump impeachmentend
    elif stress > 65:
        jump stressend
    else:
        jump goodend
label goodend:
    hide screen soulbar
    hide screen stressbar
    hide screen impeachmentbar
    with dissolve
    scene black
    with dissolve
    pause .5
    show screen soulbar
    show screen stressbar
    show screen impeachmentbar
    scene bgHell
    with fade

    narrator "Ignias sits at his desk, containing within him all the stress, sadness and anger that have been his constant companions since
    his promotion to Overseer. The great phone on his desk begins to ring"

    $ignias_mood = "MadTalk"
    show ignias at left with dissolve
    play sound "audio/Ignias/ts4.mp3"

    ignias "Not him again…"
    narrator "He picks up the phone nonetheless, and a familiar large, looming shape starts materialising in the room"

    play sound "audio/Lucifer/growling 2.mp3"
    show lucifer at right with flash

    lucifer "OVERSEER 26."

    $ignias_mood = "DefaultTalk"
    play sound "audio/Ignias/listening3.mp3"

    ignias "Lucifer"

    narrator "There is no change in the image portrayed, but Ignias can almost taste the scorn in the
    malignant gaze of his superior"

    play sound "audio/Lucifer/growling 3.mp3"

    lucifer "THE AMOUNT OF SOULS DELIVERED TODAY DOES NOT MEET THE PREMEDITATED QUOTA.
    ARE YOU AWARE OF WHAT HAPPENS TO THOSE THAT DISAPPOINT THE GREAT-"
    narrator "As he hears the words, something in Ignias breaks. And then, slowly, steadily, all the pain,
    all the suffering, all that he has held within him since his first day in this office, starts to leak out"

    $ignias_mood = "MadTalk"

    ignias "Disappointed? Disappointed!? Have you in your infinite wisdom ever considered how it is,
    working oneself everyday to the bone, trying to meet target numbers that only ever go up,
    regardless of how one previously performance?"

    play sound "audio/Lucifer/growling 2.mp3"

    lucifer "YOU DARE TALK TO ME IN {i}SUCH{/i} A WAY?"
    ignias "I dare, and I will. Yes, I know, you will now promptly punish me. Reduce me to cinders,
    turn me into a grub, banish me – I no longer care."
    narrator "Ignias rounds his desk and exits the office, leaving the speechless projection of the Devil himself behind.
    He almost reaches the end of the corridor when he runs into Moira"

    hide ignias with moveoutright
    scene Hallway with fade
    show ignias at left with moveinleft
    show moira at right with dissolve
    $moira_mood = "SuprisedTalk"

    moira "Hey Ignias, what are you doing out here? Isn’t this usually the time for
    your meeting with Lucifer? Anyways, there is a problem in-"

    $ignias_mood = "Happy"
    play sound "audio/Ignias/yes2.mp3"

    ignias "Yes, usually this is the time. But not any longer."
    narrator "Ignias grabs the paper that Moira is holding, rips it up and lets it fall to the floor"
    ignias "I quit."

    play soundMoi "audio/Moira/hmm 6.mp3"

    moira "You what!?"
    narrator "Ignias starts striding down the corridor with Moira in tow"
    ignias "Yes, just a few moments ago. Come on, let's get out of here."

    play soundMoi "audio/Moira/oh really 4.mp3"

    moira "But what about Lucifer? He didn’t exactly let you go Ig, did he?"
    ignias "No, I just walked out. I know that he will do something -  anything to punish me.
    But I no longer care. And neither should you!"

    hide ignias
    hide moira
    with moveoutright

    narrator "They walk down the stairs to the front door"

    scene black
    hide screen soulbar
    hide screen stressbar
    hide screen impeachmentbar
    with fade
    scene black
    with Pause(1)

    show text "GOOD END" with dissolve
    with Pause(2)

    hide text with dissolve
    with Pause(1)
    $renpy.movie_cutscene('images/LoadingScreenNoLoop.ogv', loops = 3  )
    return

label impeachmentend:
    hide screen soulbar
    hide screen stressbar
    hide screen impeachmentbar
    with dissolve
    scene black
    with dissolve
    pause .5
    show screen soulbar
    show screen stressbar
    show screen impeachmentbar
    scene bgHell
    with fade
    show ignias at left with dissolve
    narrator """Ignias sits at his desk when he hears loud chanting in the hallway. He can’t quite make out the words,
    but it sounds like someone shouting words which get repeated by a dozen other voices shortly after.

    The voices grow louder, until the door to the office is slammed open and a dozen imps start pouring into the room,
    wearing black armbands with a red symbol on it. The first imp to enter takes point directly in front of the desk"""

    show imp at right with moveinright
    play sound "audio/Imp/impLaugh2.mp3"

    narrator "The Imp flashes a toothy grin"

    imp "Oi boss, thanks for providin’ us with all this extra work, much appreciated. Without it,
    we would probably never have realized how much of the show we were already runnin’. Records, Extraction,
    we finally got that its us who do all the work around ‘ere, right lads?"

    narrator "The imp looks over his shoulder, and the others start cheering and shouting"

    $ignias_mood = "Suprised"
    show ignias at left with dissolve

    narrator "Ignias visibly stressed out by the whole situation"

    $ignias_mood = "SuprisedTalk"
    play sound "audio/Ignias/listening3.mp3"

    ignias "That’s great! So now you probably want more benefits in return, right?
    How about two free rounds at Morning Star’s after shift end-"

    play sound "audio/Imp/ImpAnnoyed.mp3"

    imp "Nope bossdemon, that just isn’t cutting it anymore. You see, after talkin’ about all this,
    some of us asked ourselves: ‘When we do all the work around here,
    what does that prickly hornhead behind his fancy desk actually do that we couldn’t also do?’ And, you know,
    that’s what we are ‘ere to find out."

    narrator "The Imp motions to two strong looking imps, who promptly grab Ignias and start
    dragging him out of his chair"

    $ignias_mood ="MadTalk"

    ignias "You can’t do this! This is madness! Lucifer won’t stand for this!"
    narrator "The Imp makes a clawwave"

    imp "Oh, he already knows. First thing we did after talking was contact him, to explain the situation.
    He gave us the go ahead with the only one condition: That we send you to him,
    so he can tell you in person how {i}disappointed{/i} he is."

    play sound "audio/Imp/impLaugh2.mp3"
    hide ignias with moveoutright
    show imp at center with moveinright

    narrator "Ignias’ wailing and screaming grow quieter after the big door closes behind him as his two guards drag him down the hallway.
    At the desk, the imp leader contently puts his clawed feet on the desk and begins to contemplate a glorious future for impkind"

    scene black
    hide screen soulbar
    hide screen stressbar
    hide screen impeachmentbar
    with fade
    scene black
    with Pause(1)

    show text "BAD END" with dissolve
    with Pause(2)

    hide text with dissolve
    with Pause(1)
    $renpy.movie_cutscene('images/LoadingScreenNoLoop.ogv', loops = 3  )
    return

label stressend:
    hide screen soulbar
    hide screen stressbar
    hide screen impeachmentbar
    with dissolve
    scene black
    with dissolve
    pause .5
    show screen soulbar
    show screen stressbar
    show screen impeachmentbar
    scene bgHell
    with fade
    show ignias at left with dissolve

    narrator "Ignias sits at his desk, the day quickly becoming a blur. Problems are springing up everywhere, rearing their ugly,
    multifaceted heads like an arthropodal hydra. The imp that is fifteen seconds late on its report.
    The form that where a word in a table cell slightly crosses over into another"
    narrator "How could Lucifer expect him to work under these conditions?
    There is simply not enough time in the day to fix everything, but everything needs to be fixed for him to continue his labours"

    $moira_mood = "Default"
    show moira at right with moveinright
    $moira_mood = "DefaultTalk"

    moira "Hey Ignias, bad news: There is a problem in the extraction section, one of the imps that works there-"

    $moira_mood = "SuprisedTalk"
    play soundMoi "audio/Moira/ahem 2.mp3"

    moira "Ig? Are you listening?"

    $ignias_mood = "MadTalk"
    play sound "audio/Ignias/huh2.mp3"

    ignias "Am I listening? Of course, I am listening. But you see, there a million other things that demand my attention.
    Demand that I fix them. Do you see this?"

    play soundMoi "audio/Moira/hmm 9.mp3"

    moira "The corner of your desk? What is wrong with it?"

    play sound "audio/Ignias/ts4.mp3"

    ignias "Everything! See, it is not completely rounded. See this? This indentation? It marks the entire table!"

    $moira_mood = "SadTalk"

    narrator "Moira slowly begins to back away from Ignias"
    moira "Ignias, you are scaring me…"
    ignias """Tell me Moira, how am I supposed to solve problems without solving this desks problem first!?

    And I haven’t even started on the doors, or this form, or…"""
    narrator "As Ignias’ mind unwinds before her, Moira leaves the room and quietly closes the door,
    deafening out her friend’s mad ravings"

    hide moira with moveoutright
    hide ignias with dissolve
    scene Hallway
    show Flip at left with dissolve
    show imp at right with dissolve

    imp "Oi mistress, see what I meant about the boss earlier?"

    show FlipTalk at left
    play soundMoi "audio/Moira/hmm 8.mp3"

    moira "Yes, it is… hard to miss."

    narrator "Moira holds back her tears"

    moira "Get a message to Lucifer, tell him… tell him he needs a new Overseer."



    scene black
    hide screen soulbar
    hide screen stressbar
    hide screen impeachmentbar
    with fade
    scene black
    with Pause(1)

    show text "BAD END" with dissolve
    with Pause(2)

    hide text with dissolve
    with Pause(1)
    $renpy.movie_cutscene('images/LoadingScreenNoLoop.ogv', loops = 3  )
    return
