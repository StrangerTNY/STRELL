#CHOICES EVENT 1

label impshift:
    #VARIABLES
    $sabotage = True
    $overheat = False
    $increaseImpeachment(14.2)
    $increaseSouls(50)
    $ignias_mood = "DefaultTalk"
    show ignias at left with dissolve

    ignias "Moira, how many imps do we have that could immediately be reassigned to soul extraction without plunging everything else into chaos?"

    $moira_mood = "DefaultTalk"
    show moira at right with dissolve
    play soundMoi "audio/Moira/Yes 1.mp3"

    narrator "Moira quickly looks over a report"
    moira "… according to the latest imp count conducted this morning, imps 354 through 489 are currently assigned minor bureaucratic
    tasks and could probably be reassigned safely."

    $ignias_mood = "Happy"

    narrator "Ignias yells loudly in the vague direction of the door"
    ignias "{size=70}Get in here !!"
    narrator "{i}The door opens with a crash as one tumbles through the door{/i}"

    hide moira with dissolve
    $imp_mood = "Default"
    show imp at right with moveinright

    imp "Yes, Milord?"

    $ignias_mood = "DefaultTalk"

    ignias "Gather 354 through 489 and tell them to start working the soul extraction vats immediately;
    until I give orders for them to labor elsewhere."

    narrator "The imp smiles mischievously, bows and flutters out the door"

    hide imp with moveoutright
    $moira_mood = "DefaultTalk"
    play soundMoi "audio/Moira/0h 3.mp3"
    show moira at right with dissolve

    narrator "Moira digs through some scrolls and sighs"
    moira "These records seem incomplete at best.
    Will you be able to hold your own while I go and try to find the missing pieces?"
    narrator "Ignias nods, and Moira leaves the room"

    hide moira with moveoutright
    hide ignias with dissolve
    jump ImpasWantMore

label equipment:
    #VARIABLES
    $sabotage = False
    $overheat = True
    $increaseSouls(50)
    $increaseStress(14.2)
    $ignias_mood = "DefaultTalk"
    show ignias at left with dissolve
    play sound "audio/Ignias/huh2.mp3"

    ignias "Are you sure that the soul vats can shoulder the increased load?"

    $moira_mood = "DefaultTalk"
    show moira at right with dissolve
    play soundMoi "audio/Moira/hmm 9.mp3"

    narrator "Moira shrugs"
    moira "Again, extracting souls is not my field of expertise.
    But I have never heard of accidents where the vats could not be repaired afterwards. As for the imps…"

    $moira_mood ="Happy"
    play soundMoi "audio/Moira/haha 1.mp3"

    moira "There always are  more imps, right?"
    ignias "Well, it’s not like we have many options here. Where are the work order forms? And could you fetch me an imp while I write?"
    narrator "Moira sighs, points Ignias in the right direction in the chaos that consumes the desk,
    and leaves the room in search of a suitable subordinate"

    hide ignias
    hide moira
    with dissolve
    jump ImpasWantMore

    #CHOICES EVENT 2
label workload:
    $increaseImpeachment(14.2)
    $ignias_mood = "DefaultTalk"
    show ignias at left with dissolve

    ignias "Fine, tell them to start overseeing the soul transport to the shores of Styx.
    But no letting them empty the barrels, got it?"

    show imp at right with dissolve

    narrator "The Imp nods, then scurries out of the throne room"

    play sound "audio/Imp/ImpAnnoyed.mp3"
    hide imp with moveoutright

    $moira_mood = "Default"
    show moira at right with dissolve
    play soundMoi "audio/Moira/hmm 1.mp3"
    moira "Try to sort the documents into their designated stacks. Just keep an eye on the symbols and you should be good! Be careful to not mix them up, these are directly connected to our daily flow of souls!"
    hide ignias
    with dissolve
    hide screen soulbar
    hide screen stressbar
    hide screen impeachmentbar
    hide screen baroverlay
    with dissolve
    jump minigame

label keepbusy:
    $increaseStress(14.2)
    $ignias_mood = "DefaultTalk"
    show ignias at left with dissolve

    ignias "Let them have some free time, they earned it after working so hard.
    Tell them they can get drinks on me at Morning Star’s later."

    show imp at right with dissolve

    narrator "The imp eyes Ignias suspiciously, then makes a mocking bow and scampers out the door"

    
    hide imp with moveoutright

    $moira_mood = "Default"
    show moira at right with dissolve
    play soundMoi "audio/Moira/hmm 1.mp3"
    moira "Try to sort the documents into their designated stacks. Just keep an eye on the symbols and you should be good! Be careful to not mix them up, these are directly connected to our daily flow of souls!"
    
    hide moira
    hide ignias
    with dissolve
    hide screen soulbar
    hide screen stressbar
    hide screen impeachmentbar
    hide screen baroverlay
    with dissolve
    jump minigame 

    #CHOICES EVENT 3
label pesticide:
    $increaseImpeachment(14.2)
    $ignias_mood = "DefaultTalk"
    show ignias at left with dissolve

    ignias "213, gather some of your ilk and get me that pesticide!"

    show imp at right with dissolve

    narrator "The imp nods and runs out of the room"

    hide imp with moveoutright
    $moira_mood = "SadTalk"
    show moira at right with dissolve
    play soundMoi "audio/Moira/hmm 7.mp3"

    narrator "Moira sighs"
    moira "Let’s hope that they manage to get it sooner rather than later…"

    hide ignias
    hide moira
    with dissolve
    jump competition

label relocate:
    $increaseStress(14.2)
    $ignias_mood = "DefaultTalk"
    show ignias at left with dissolve

    ignias "213! Gather as many imps as you can, get them to the records room and tell them to move as
    many scrolls as they can to the dungeon!"

    show imp at right with dissolve

    imp "But what about the moths, Milord?"
    ignias "Order the imps to shield the scrolls with their bodies.
    I will personally hold you responsible for every record we lose on the move, understood?"
    imp "Y-yes, sire!"
    narrator "The imp practically flees the room"

    hide imp with moveoutright
    play sound "audio/Ignias/ts4.mp3"

    ignias "{i}Let’s hope that decision doesn’t come back to bite me. Literally.{/i}"

    hide ignias with dissolve
    jump competition

    #CHOICES EVENT 4
label goig:
    $increaseStress(14.2)
    $increaseSouls(50)
    $ neighbourhoodBeef = True
    $ignias_mood = "DefaultTalk"
    show ignias at left with dissolve

    ignias "Wouldn’t it put me in greater danger if the Queen of Eyes perceived it as a slight if
    I do not show up to receive her gift personally?"

    $moira_mood ="SadTalk"
    show moira at right with dissolve

    moira "Well, maybe, but-"
    ignias "Don’t worry, I promise to be extra careful. Take care of the office until my return, would you?"
    narrator "Ignias leaves the room and an exasperated Moira behind"

    hide ignias
    hide moira
    with dissolve
    jump endDayOne

label goimp:
    $increaseImpeachment(14.2)
    $ignias_mood = "DefaultTalk"
    show ignias at left with dissolve

    ignias "You are right, I should not deal lightly with the Queen."

    $moira_mood = "Happy"
    show moira at right with dissolve
    play soundMoi "audio/Moira/oh really 4.mp3"

    narrator "Moira nods"
    moira "I am glad to see you act responsibly. Such a rare sight to behold!"
    ignias "Can you manage the office for a bit while I go and gather some imps?"
    moira "Sure, but do not take too long or might take a liking to you chair."
    narrator "Ignias leaves the room"
    hide ignias with moveoutleft
    hide moira with dissolve
    $ignias_mood = "MadTalk"

    narrator "Ignias returns after a while, cursing under his breath"

    show ignias at left with moveinleft
    play sound "audio/Ignias/sad.sigh1.mp3"

    ignias "Those fools be damned!"

    $moira_mood = "MadTalk"
    play soundMoi "audio/Moira/hmm 9.mp3"
    show moira at right with dissolve

    moira "Did something happen to the delivery?"
    ignias "Yes, those idiots bungled it! Instead of taking the main road on their way back,
    they tried a shortcut, hit a bad spot of pavement and spilled the payload!"

    hide ignias
    hide moira
    with dissolve

    jump endDayOne


##########################################################################################################



    #CHOICES FOR DAY 36
label standstill:
    $increaseStress(14.2)
    show ignias at left
    show imp at right
    with dissolve

    ignias "You! Tell the imps at the extraction area to stop the vats until they look workable again! And tell me the minute they run this hot again."
    imp "{i}the Imp bows hastily, then flutters out into the hallway{/i}"

    hide imp with moveoutright
    if impeachment > 99:
        jump impeachmentend
    elif stress > 99:
        jump stressend
    else:
        jump heavensouls

label coolvats:
    $increaseImpeachment(14.2)
    $increaseSouls(12.5)
    show ignias at left
    show imp at right
    with dissolve

    ignias "They may glow, but they work all the same. Tell the ones manning the vats to try and cool them off. Use anything you can think off!"
    narrator "The imp nods eagerly and nearly tumbles as he hastily leaves to tell the others"

    hide imp with moveoutright
    if impeachment > 65:
        jump impeachmentend
    elif stress > 65:
        jump stressend
    else:
        jump heavensouls


label workextra:
    $increaseSouls(12.5)
    $increaseStress(14.2)
    $ignias_mood = "DefaultTalk"
    show ignias at left
    show imp at right
    with dissolve

    ignias "What are you still standing here for? Go gather some of you ilk and get to extracting!
    We need to get more souls out of the vats, and we need them now!"
    narrator "the imps nod hastily and retreat down the corridor"

    hide imp with moveoutright
    if impeachment > 99:
        jump impeachmentend
    elif stress > 99:
        jump stressend
    else:
        jump heavensouls


label repairvats:
    $increaseSouls(12.5)
    $increaseImpeachment(14.2)
    $ignias_mood = "DefaultTalk"
    show ignias at left
    show imp at right
    with dissolve

    ignias "You! You know how the extractors work, right?"
    imp "Yes boss, at least in theory-"
    ignias "Good enough, you are now in charge of repairing the broken vat. Grab some other imps if you need help,
    but get it done as quickly as you can!"

    play sound "audio/Imp/impLaugh2.mp3"

    narrator "the imp, nearly glowing with pride, flutters out of the hall, followed by its less fortunate cousin"

    hide imp with moveoutright
    show moira at right with dissolve
    pause 1.0

    narrator "Afterwards, Moira leaves to oversee a delivery of new imps, leaving Ignias to brood"

    hide moira with moveoutright

    narrator "Alone with his thoughts, he manages to get little work done over the next couple of hours."
    if impeachment > 99:
        jump impeachmentend
    elif stress > 99:
        jump stressend
    else:
        jump heavensouls


    #CHOICES EVENT Souls which actually belong in heaven got extracted
label keepsouls:
    $increaseSouls(12.5)
    $increaseStress(14.2)
    $ignias_mood = "DefaultTalk"
    show ignias at left with dissolve
    show moira at right with dissolve

    ignias """I think I’ll keep ‘em. Otherwise our quota for today will be too low. I don’t think someone will recognize that, it’s just a few right?

    {i}I just hope this doesn’t fall back on me.{/i}"""

    $moira_mood ="Default"

    narrator "Moira eyes him with concern and leaves"

    hide moira with moveoutright
    if impeachment > 99:
        jump impeachmentend
    elif stress > 99:
        jump stressend
    else:
        hide ignias
        with dissolve
        hide screen soulbar
        hide screen stressbar
        hide screen impeachmentbar
        hide screen baroverlay
        with dissolve
        jump minigame2

label callheaven:
    $increaseImpeachment(14.2)
    $increaseStress(14.2)
    $ignias_mood ="MadTalk"
    show ignias at left with dissolve
    show moira at right with dissolve
    play sound "audio/Ignias/ts4.mp3"

    ignias "Damnit! I need to send a message up there and send the souls over. I just hope that Lucifer doesn’t notice it.
    Can you get some at least semi reliable imps in here that can send a message up through backchannels?"

    $moira_mood ="Default"

    narrator "Moira nods and leaves Ignias to sort that problem out"

    hide moira with moveoutright
    $ignias_mood ="Sad"

    ignias "{i}Ignias pinches the bridge of his nose, wondering how he will make it through the day at this rate{/i}"
    if impeachment > 99:
        jump impeachmentend
    elif stress > 99:
        jump stressend
    else:
        hide ignias
        with dissolve
        hide screen soulbar
        hide screen stressbar
        hide screen impeachmentbar
        hide screen baroverlay
        with dissolve
        jump minigame2

    #CHOICES EVENT Lucifer wants specific souls
label corrupt:
    $increaseSouls(12.5)
    $increaseStress(14.2)
    $ignias_mood = "DefaultTalk"
    show ignias at left with dissolve
    show moira at right with dissolve

    ignias "Thanks for the advice Moira. I’m off topwards then to make sure we get the souls in before tonight’s closure.
    Can I count on you to step in for me until I return?"

    $moira_mood ="Happy"

    moira "Always, dear. Go have fun up there!"
    narrator "Ignias exits the room, and Moira makes herself comfortable in the big chair"

    hide ignias with moveoutleft
    play soundMoi "audio/Moira/yawn.mp3"
    hide moira with dissolve
    if impeachment > 99:
        jump impeachmentend
    elif stress > 99:
        jump stressend
    else:
        jump hellhoundescape
label impsearch:
    $increaseSouls(12.5)
    $increaseImpeachment(14.2)
    $ignias_mood = "DefaultTalk"
    show ignias at left with dissolve
    show moira at right with dissolve

    ignias "Moira, can you get some Imps to go up there and search for suitable candidates? I think I should remain here for the moment;
    in case our benevolent Overlord shows up again."

    $moira_mood ="SuprisedTalk"
    play soundMoi "audio/Moira/hmm 2.mp3"

    moira "Are you sure that move won’t embolden them too much?"
    narrator "Ignias nods, and Moira exits the room in search for imps"

    hide ignias with moveoutleft
    hide moira with dissolve

    if impeachment > 99:
        jump impeachmentend
    elif stress > 99:
        jump stressend
    else:
        jump hellhoundescape



    #CHOICES EVENT Hellhound escapes
label askmoira:
    $increaseStress(14.2)
    $ignias_mood = "DefaultTalk"
    show ignias at left with dissolve
    show moira at right with dissolve

    ignias "Moira, you always had a special bond with that mutt. Would you mind trying to lead him back to his quarters?"

    $moira_mood = "DefaultTalk"

    moira "I can certainly try."
    narrator "Moira leaves the room, shouting at imps to get them back to work"
    hide moira with moveoutright
    hide ignias with dissolve

    jump end
label sendimps:
    $increaseStress(14.2)
    $decreaseImpeachment(14.2)
    $ignias_mood = "DefaultTalk"
    show ignias at left with dissolve

    ignias """{i}I should send some imps to get him back. They messed this up and deserve to be the ones to solve this mess.{/i}

    47, gather some of your kind and get Kerberos back. It’s your fault he’s gone.
    Do a good job for once, or you will be considered for the position of handler."""
    show imp at right with dissolve
    narrator "The Imp starts sweating bullets"
    imp "But Master,Kerberos probably hasn’t been fed since his escape-"

    $ignias_mood = "MadTalk"

    ignias "You will face much worse than a hungry Hellhound for insubordination. Now get going!"
    narrator "47 bows hastily and scurries out of the office"

    play sound "audio/Imp/ImpAnnoyed.mp3"
    hide imp with moveoutright

    ignias "{i}I hope Kerberos eats him.{/i}"

    hide ignias with dissolve


    jump end



###############################################
#DAY 18 


#CHOICES FORM KERFUFFLE
label busymorework:
    $increaseStress(14.2)
    $increaseSouls(25)
    $ignias_mood = "DefaultTalk"
    show ignias at left with dissolve
    ignias "Moira, how many imps do we have that could immediately be reassigned to soul extraction without plunging everything else into chaos?"
    $moira_mood = "DefaultTalk"
    show moira at right with dissolve
    play soundMoi "audio/Moira/Yes 1.mp3"
    narrator "Quickly performs some mental calculations"
    moira "… Well, the records department could probably spare a few wretches to man the vats."
    $ignias_mood = "Happy"
    play sound "audio/Ignias/I_see.mp3"
    narrator "Yells loudly in the vague direction of the doo"
    ignias "Get in here 1!"
    narrator "The door opens with a thud as an imp hastily enters the office"
    hide moira  with dissolve
    show imp at right with moveinright
    imp "Yes, Milord?"
    $ignias_mood = "DefaultTalk"
    play sound "audio/Ignias/go_ahead.mp3"
    ignias "Go to those fools in records and tell them to send half of their staff to man the extraction vats."
    narrator "The imp bows haphazardly and flutters out the door"
    hide imp with moveoutright
    show moira at right with dissolve
    play soundMoi "audio/Moira/0h 3.mp3"
    narrator "Rubs her hands and sighs"
    moira "Well, let’s hope this will keep them busy."
    narrator "Ignias nods, and Moira leaves the room"
    hide moira with moveoutright
    hide ignias with dissolve

    if impeachment > 99:
        jump impeachmentend
    elif stress > 99:
        jump stressend
    else:
        jump queenly

label a38:
    $increaseImpeachment(14.2)
    $increaseStress(14.2)
    $ignias_mood = "DefaultTalk"
    $moira_mood = "DefaultTalk"
    show ignias at left
    show moira at right 
    with dissolve
    play sound "audio/Ignias/hold_on.mp3"
    ignias "Moira, since you have been working on our delivery contracts: Can you draw up an A38 for me dated on our first day at the office?"
    play soundMoi "audio/Moira/hmm 9.mp3"
    narrator "Moira Shrugs"
    moira "That shouldn’t be too hard. I cannot make any guarantees as to how long such a contract would be able to fool the old coots in records, though."
    ignias "Well, it’s not like we have many options here. Let me worry about the imps, just draw up the contract and hand it to me."
    narrator "Moira leaves and returns a little later with the requested document in hand. Ignias quickly signs it and sends it of the archive."

    hide moira
    hide ignias
    with dissolve

    if impeachment > 99:
        jump impeachmentend
    elif stress > 99:
        jump stressend
    else:
        jump queenly


#CHOICES FROM QUEENLY DEALINGS  
label takedeal:
    $increaseSouls(25)
    $increaseSouls(25)
    $increaseSouls(25)
    $increaseStress(14.2)
    $ignias_mood = "DefaultTalk"
    $qoe_mood = "Happy"
    show ignias at left
    show qoe at right
    with dissolve

    play sound "audio/Ignias/Yes.mp3"
    ignias "Queen, you have my support."
    play sound "audio/QueenOfEyes/AFavourableBargain.mp3"
    qoe "You are wise beyond your centuries, young Firestarter. The delivery of freshly harvested souls will continue to run via the docks, starting today."
    play sound "audio/QueenOfEyes/Yes.mp3"
    qoe "I will send word when the time is right. Be sure that should you tell anyone of what happened in this room, there will be a punishment that even Lucifer himself could not afflict on you."
    narrator "Ignias Bows slightly."
    ignias "Perish the thought dear colleague."

    hide ignias
    hide qoe 
    hide screen baroverlay
    hide screen soulbar
    hide screen stressbar
    hide screen impeachmentbar
    scene black
    with dissolve

    scene bgHell
    show screen baroverlay
    show screen soulbar
    show screen stressbar
    show screen impeachmentbar
    with fade
    show ignias at left with dissolve
    narrator "Ignias leaves the queen behind, mulling over what just transpired. Back at his office he commits himself to mundane paperwork, to clear his mind of errant thoughts."
    

    if impeachment > 99:
        jump impeachmentend
    elif stress > 99:
        jump stressend
    else:
        hide ignias
        hide screen baroverlay
        hide screen soulbar
        hide screen stressbar
        hide screen impeachmentbar
        with dissolve
        jump minigame3


label decline:
    $increaseStress(14.2)
    $increaseStress(14.2)
    $ignias_mood = "DefaultTalk"
    $qoe_mood = "Mad"
    show ignias at left
    show qoe at right
    with dissolve

    play sound "audio/Ignias/no.mp3"
    ignias "I thank you for your offer, but fear that I must decline."
    play sound "audio/QueenOfEyes/No.mp3"
    narrator "Her gaze turns icy. "
    qoe "Are you sure that this is the path you want to choose? There are many in the underworld that would gladly stab you thrice over to be where you are right now."
    ignias "In this I am certain. I will of course remain silent about your offer and will bid my leave."
    play sound "audio/QueenOfEyes/Tss.mp3"
    qoe "Be sure that should you tell anyone of what happened in this room, there will be a punishment that even Lucifer himself could not afflict on you. Also know that there will not be opportunities like this in the future. Now, you are as the rest: On your own. Prey."

    hide ignias
    hide qoe 
    hide screen baroverlay
    hide screen soulbar
    hide screen stressbar
    hide screen impeachmentbar
    scene black
    with dissolve

    scene bgHell
    show screen baroverlay
    show screen soulbar
    show screen stressbar
    show screen impeachmentbar
    with fade
    show ignias at left with dissolve
    narrator "Ignias leaves the queen behind, mulling over what just transpired. Back at his office he commits himself to mundane paperwork, to clear his mind of errant thoughts."

    

    if impeachment > 99:
        jump impeachmentend
    elif stress > 99:
        jump stressend
    else:
        hide ignias
        hide screen baroverlay
        hide screen soulbar
        hide screen stressbar
        hide screen impeachmentbar
        with dissolve
        jump minigame3

label impkilling:
    $increaseSouls(25)
    $increaseImpeachment(14.2)
    $ignias_mood = "DefaultTalk"
    $twins_mood = "Default"
    show ignias at left
    show twins at right
    with dissolve

    play sound "audio/Ignias/yes.mp3"
    ignias "Corruption, or Wish-Fulfillment, is our most sacred tradition."
    play soundTwinf "audio/TwinF/Hmm interesting.mp3"
    twinf "For a grub barely dry of Styx water you sure talk like old man Lucifer himself."
    ignias """{i} Ignoring the sarcastic demon {/i}

    I will send my most devious imps to twist their souls, and the matter will soon be resolved. Wardens, you can return to your post
    """
    narrator "The twins leave the office with mocking bows, and both parties are glad to be rid of each other. Ignias soon gets bogged down again in the minutia of running hell, partially."
    hide twins with moveoutright

    if impeachment > 99:
        jump impeachmentend
    elif stress > 99:
        jump stressend
    else:
        jump goodboy

label collapse:
    $increaseStress(14.2)
    $ignias_mood = "DefaultTalk"
    $twins_mood = "Suprised"
    show ignias at left
    show twins at right
    with dissolve

    ignias "I like your way of thinking, Modean."
    play soundTwinm "audio/TwinM/interesting.mp3"
    twinm "You do? That’s the first time in a long time someone said that."
    ignias """ {i}Ignoring the sarcastic demon{/i}
    
    You can engineer an overflow of ichor from the gate, right? That should collapse their measly attempts at architecture."""
    $twins_mood ="Suprised"
    play soundTwinf "audio/TwinF/Copy that.mp3"
    twinf "Yes, that should work. You sure are quick on the uptake, for a seatwarmer. Although Heaven will surely try to get back at us this way, but that’s more your concern than ours"
    play sound "audio/Ignias/understood.mp3"
    ignias """ {i}Ignoring the sarcastic demon{/i}
    
    I will deal with it when the time comes."""

    narrator "The twins leave the office with mocking bows, and both parties are glad to be rid of each other. Ignias soon gets bogged down again in the minutia of running hell, partially. "
    hide twins with moveoutright

    if impeachment > 99:
        jump impeachmentend
    elif stress > 99:
        jump stressend
    else:
        jump goodboy

label traindog:
    $increaseStress(14.2)
    $ignias_mood = "DefaultTalk"
    $cerberus_mood = "Happy"
    show ignias at left
    show cerberus at right
    with dissolve

    ignias "Boy, I promise that this is the last time I let someone else try to tame my dog. How would you feel about me doing it for a change, hmm?"
    play sound "audio/Cerb3.mp3"
    cerb "Woof!"
    $ignias_mood = "Happy"
    play sound "audio/Ignias/Yes.mp3"
    ignias "{i}Bows slightly to reach through the bars and pet the dog{/i}"
    ignias "Good boy! Now, let me find your leash…"
    
    if impeachment > 99:
        jump impeachmentend
    elif stress > 99:
        jump stressend
    else:
        jump endDay18
    

label seekexpert:
    $increaseImpeachment(14.2)
    $ignias_mood = "DefaultTalk"
    $cerberus_mood = "Happy"
    show ignias at left
    show imp at right
    with dissolve

    ignias "Well, his appetite is bound to run out eventually. Do you know where one could find beast masters in the city?"
    imp "Well, sire, there is this old place down in the slums where the old guard gets together to talk about the good old days. We would be certain to find one among them who could train your dog for you."
    $ignias_mood = "Happy"
    play sound "audio/Ignias/go_ahead.mp3"
    ignias "Great! Make it so!"
    narrator "The Imp Hastily moves up the stairs"
    hide imp with moveoutright
    show cerberus at right with dissolve
    cerb "{i}Winces{/i}"
    $ignias_mood = "DefaultTalk"
    play sound "audio/Ignias/sorry.mp3"
    ignias "Do not worry boy, the next one will be better than the last. I promise to come down here more often as well, it has been a while since I last played with you…"

    if impeachment > 99:
        jump impeachmentend
    elif stress > 99:
        jump stressend
    else:
        jump endDay18
