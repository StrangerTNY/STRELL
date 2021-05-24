#Event 1
label impmorework:
    play music "audio/Timer.mp3"
    menu: #dilemmata1
        "Share some of your own workload": #impeachment +
            jump shareWork
        "Refuse to give them something to do": #stress +, impstrike flag
            jump impStrike

    return
#Choice 1
label shareWork: #dilemmata1
    $ increaseImpeachment(5)
    show ignias at left with dissolve

    ignias "Fine, tell them to start overseeing the soul transport to the shores of Styx. But not letting them empty the barrels, got it?"

    "{i}the Imp nods, then scurries out of the throne room"

    hide ignias with dissolve

    return
#Choice2
label impStrike: #dilemmata1
    $ impStrike = True
    $ increaseStress(5)

    show ignias at left with dissolve

    ignias "Let them have some free time, they earned it after working so hard. Tell them they can get drinks on me at Morning Star’s later."
    "{i}the imp eyes Ignias suspiciously, then makes a mocking bow and scampers out the door"

    hide ignias with dissolve

    return

#Event 2
label wrongSouls:

    menu: #dilemmata2
        "Keep the souls, you still need some to meet your daily goal.": #souls +
            jump keepSouls
        "Call heaven and try to make it right.": #stress + , souls -
            jump callHeaven

    return
#Choice 1
label keepSouls:
    $ heavenCalls = True
    $ increaseSouls(5)

    show ignias at left with dissolve
    ignias "I think I’ll keep ‘em. Otherwise our quota for today will be too low.
    I don’t think someone will recognize that, it’s just a few right?
    {i}I just hope this doesn’t fall back on me."

    "Moira eyes him with concern and leaves"

    hide ignias with dissolve
    return
#Choice 2
label callHeaven:
    $ increaseStress(5)
    $ decreaseSouls (5)
    show ignias at left with dissolve
    ignias "Damnit! I need to send a message up there and send the souls over.
    I just hope that Lucifer doesn’t notice it."

    "{i}Moira nods and leaves Ignias to sort that problem out"

    hide ignias with dissolve

    return

#Event 3
label soulVat:
    menu: #dilemmata 3
        "Let the vats stand still for time to prevent equipment damage": #+Souls, +Stress

            jump vatStill
        "Order imps to cool the vats":
            jump coolVats

#Choice 1
label vatStill:
    $increaseSouls(5)
    $increaseStress(5)

    show ignias at left with dissolve
    ignias "You! Tell the imps at the extraction area to stop the vats until they look workable again!
    And tell me the minute they run this hot again."
    "the Imp bows hastily, then flutters out into the hallway"
    hide ignias with dissolve

    return
#Choice 2
label coolVats:
    $increaseSouls(5)
    $increaseImpeachment(5)

    show ignias at left with dissolve
    ignias "They may glow, but they work all the same.
    Tell the ones manning the vats to try and cool them off. Use anything you can think off!"
    "the imp nods eagerly and nearly tumbles as he hastily leaves to tell the others"
    hide ignias with dissolve

    return

#Event 4
label cerb:
    menu: #dilemmata 4
        "Call for Moira and ask her to rescue Kerberos.": #+ Set flag for some other dilemmata possibly the scientists thing, +stress
            jump askMoira
        "Send some Imps.": #-Impeachment, +stress
            jump sendImp
        "Go yourself.":
            jump igniasGo
#Choice 1
label askMoira:
    $increaseStress(5)

    show ignias at left with dissolve
    ignias "Moira! I need your help!"
    "Moira rushes worried into his office"
    show moira at right with moveinright
    ignias "Kerberos ran away, because one of these fools left my door open. Can you rescue him?"
    moira "Oh, poor thing, he must be so scared. I’m on my way!"
    "Moira shouting from outside"
    moira "{size=50}Get back to work, you fools!"

    hide ignias
    hide moira
    with dissolve

    return
#Choice 2
label sendImp:
    $decreaseImpeachment(5)
    $increaseStress(5)

    show ignias at left with dissolve
    ignias "{i}I should send some imps to get him back. They requested more work anyway."
    ignias "Imp 44 get back here! Gather some of your kind and get Kerberos back.
    It’s your fault he’s gone. Do a good job for once, otherwise there will be serious consequences."
    show fish at right with dissolve
    imp "But Master, Kerberos wasn’t fed this morning…"
    "Imp looks scared"
    ignias "I’ll degrade you to an unworthy worm if you don’t follow my orders!"
    "Imp nods and scurrys out of the office"
    hide fish with moveoutright
    ignias "{i}I hope Kerberos eats him."

    hide ignias with dissolve
    return
#Choice 3
label igniasGo:
    show ignias at left with dissolve
    "{i}Oh my poor Kerberos! I should get him myself.."
    "jumps out of his office chair"
    ignias "{size=36} Moira!"
    "Moira walks into room"
    show moira at right with moveinright
    ignias "Can you take care of things? I need to find Kerberos!"
    moira "Are you sure? I can fill in for you, but if Lucifer catches wind of this, there will be heaven to pay."
    ignias "Thank you, just try to keep a low profile."
    "Ignias leaves Moira in his office"
    hide ignias with moveoutleft
    show moira at center with move
    #*SFX Moira sighs*
    pause 2.0
    hide moira with dissolve

    return
#Event 5
label sabotage:
    menu:
        "Order imps to work the other vats extra hard": #+Souls, +Stress
            jump orderImps
        "Try and repair broken vat": #+impeachment, +Souls
            jump repairVat
        "Order imps to investigate explosion, forged work order": # +Stress, set flag: neighbourhood beef
            jump investigateImp
#Choice 1
label orderImps:
    $increaseSouls(5)
    $increaseStress(5)

    show ignias at left with dissolve
    ignias "What are you still standing here for? Go gather some of you ilk and get to extracting!
    We need to get more souls out of the vats, and we need them now!"

    "the imps nod hastily and retreat down the corridor"
    hide ignias with dissolve
    return
#Choice 2
label repairVat:
    $increaseImpeachment(5)
    $increaseSouls(5)

    show ignias at left with dissolve
    ignias "You! You know how the extractors work, right?"
    show fish at right with dissolve
    imp "Yes boss, at least least in theory-"
    ignias "Good enough, you are now in charge of repairing the broken vat.
    Grab some other imps if you need help, but get it done as quickly as you can!"
    "the imp, nearly glowing with pride, flutters out of the hall, followed by its less fortunate cousin"

    hide ignias
    hide fish
    with dissolve

    return
#Choice 3
label investigateImp:
    $increaseStress(5)
    $neighbourhoodBeef = True

    show ignias at left with dissolve
    ignias "Something is off about this form. And a vat that just happens to explode when no imp is around to see it happen? You! When was the last time a vat exploded?"
    show fish at right with dissolve
    imp "Well, to my knowledge, that kinda stuff hasn’t happend in the last 500 years…"
    ignias "Moira, I want you to grab some more imps and investigate where this workorder came from and what caused the damage to vat. Something seems off about all of this…"
    hide fish with dissolve
    show moira at right with dissolve
    "Moira nods and strides out of the room, imps following behind, struggling to keep up with her long-legged walk"
    hide moira with moveoutright
    #sfx steps
    hide ignias with dissolve


    return
