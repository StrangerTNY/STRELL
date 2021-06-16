label dayONE:
    #TUTORIAL / DAY 1
    #*Frantic knocking noises*
    play sound knock
    pause

    narrator "..."

    #*Frantic knocking noises intensify*
    play sound knock loop
    pause 2.0
    stop sound

    narrator    "..."

    $moira_mood = "MadTalk"
    show moira at right with dissolve

    narrator "Moira screams against the door"

    play soundMoi "audio/Moira/ahem 2.mp3"

    moira "Ig, WAKE UP! I am not going to let you sleep at your desk on your first day as an overseer!
    Remember, starting today, you are the youngest Overseer Hell as ever seen,
    so {i}please{/i} try to not screw it up!"

    $ignias_mood = "Mad"
    show ignias at left with dissolve
    play sound "audio/Ignias/ts4.mp3"

    ignias "{i}By the seven realms of heaven, why did I agree to this job?
    It’s not like I had a choice in the matter…{/i}"

    hide moira
    hide ignias
    with dissolve
    show Hallway with fade
    hide bgHell with dissolve

    narrator "A few hours ago…"

    $ignias_mood = "Happy"
    show ignias at left with dissolve

    narrator "Ignias walks down a hallway in Helltropolis"
    ignias """{i}Man, this whole soul collecting business is easier than I thought.
    We just take a quick trip to the surface, visit mortals that are about to have their coil severed,
    take their spirit, and send them back down.
    And if those winged fools from up above spring up, we just show them the contracts.{/i}

    {i}Since those are always airtight, there is nothing they can do.
    And the look on the faces of humans when they realise that they literally made a deal with a devil
    some years back… Never gets old!{/i}"""

    play sound "audio/coins.wav"

    ignias "{i}Also, it pays really well. Now, I hope that Moira hasn’t started drinking without-{/i}"

    $ignias_mood = "SuprisedTalk"
    show ignias with vpunch

    ignias "{size=50} MEEEE?"
    narrator "Suddenly, a huge, glowing figure materialises out of thin air in front of Ignias"

    play sound "audio/Lucifer/chuckle 1.mp3"
    show lucifer at right with flash

    narrator "The apparition begins to talk in a booming voice"
    lucifer "ACQUISITION AGENT 25789,
    IT HAS COME TO MY ATTENTION THAT YOU HOLD A SPOTLESS RECORD IN THE DELIVERY OF SOULS THUS FAR."
    narrator "Ignias subserviently falls to his knees"
    ignias "Yes, O Lucifer, First of the Fallen, the Seven headed Goat, Greatest of all Justiciars,
    Binder of Mortals, Ruler of Hell, Corrupter of-{nw}"
    #*Cuts Ignias off*
    lucifer """ENOUGH WITH THE TITLES. YOUR TALENTS ARE WASTED AS A MERE DELIVERDEMON FOR HELLS FOREMOST
    ENERGY SOURCE. DUE TO A RECENT INCIDENT, THE POSITION OF OVERSEER 26 HAS BEEN LEFT VACANT.

    BY THE POWERS BESTOWED UPON ME AS SUPREME OVERLORD OF HELL, I HEREBY AWARD YOU THE POSITION OF ARCHDEMON.
    YOU ARE TO START AT YOUR NEW OFFICE TOMORROW. I SHALL FOLLOW WORD OF YOUR ACCOMPLISHMENTS WITH GREAT INTEREST."""
    narrator "The Apparition fades as quickly as it manifested"

    hide lucifer with dissolve

    narrator "Ignias rises slowly to his feet, still weak in the knees from the recent promotion"
    ignias "{i}Overseer?! Me? This must be some kind of mistake…{/i}"

    hide ignias with dissolve
    show bgHell with fade
    hide Hallway with dissolve
    $ignias_mood = "MadTalk"

    narrator "Back in the present"

    show ignias at left with dissolve

    narrator "Ignias raises his head slowly from the pile of scrolls"

    play sound "audio/Ignias/ts4.mp3"

    ignias "The doors are open!"

    $moira_mood = "Happy"
    show moira at right with moveinright
    play soundMoi "audio/Moira/0h 1.mp3"

    narrator"Moira enters, either oblivious or wilfully ignorant of the glare Ignias throws her way"
    moira "Come on, cheer up Ig. I knew you were special on the first day we met.
    Do you remember the first mortal whose spirit we collected? I will never forget the look on his face!"
    ignias """{i}This is Moira, a demon. She was my partner at my old job and has become my best friend
    over the long years we worked together.{/i}

    {i}First thing she did was tell me she would accompany me,
    because there would be no way I could ever manage this job on my own.
    She is probably right on that…{/i}"""

    $moira_mood = "DefaultTalk"

    narrator "Moira stops reminiscing about old times"

    play soundMoi "audio/Moira/ahem 2.mp3"

    moira "So anyways, have you been told your responsibilities as Overseer?"
    narrator "Ignias shakes his horned head"

    play soundMoi "audio/Moira/hmm 2.mp3"

    moira "Your one and only duty is to extract souls from human spirits and send them to Lucifer himself.
    He will probably be checking in at the end of the day,
    so it would be best if we have the required amount ready by then.{p=3.0}"

    hide screen soulbar with dissolve
    pause 0.1
    show screen soulbar with dissolve
    hide screen soulbar with dissolve
    pause 0.1
    show screen soulbar with dissolve
    hide screen soulbar with dissolve
    pause 0.1
    show screen soulbar with dissolve

    moira "If we don’t manage that… Well, then Lucifer will probably have another
    Overseer sitting at this very desk the next day, so we should probably make this our top priority."
    narrator "Imp scampers into the room, carrying some scrolls"

    hide moira with dissolve
    $imp_mood = "Default"
    show imp at right with moveinright
    play sound "audio/Imp/ImpAnnoyed.mp3"

    imp "Oi, where should these forms go?"

    hide imp with dissolve
    $moira_mood = "DefaultTalk"
    show moira at right with dissolve
    play soundMoi "audio/Moira/hmm 10.mp3"

    narrator "Moira waves to last surface in the office that is not drowning in paper"
    moira "Just put them somewhere over there, 56."

    hide moira
    show imp at right
    with dissolve

    narrator "The Imp relieves his load and hurries out of the room"

    hide imp with moveoutright
    show moira at right with dissolve

    moira """These imps are your direct subordinates, as you probably already now.
    They are amazing little buggers and do most of the work around here. From accounting,
    soul extraction and even cleaning, they are the glue that holds this place together.

    But like all demons, they are ambitious to a fault.
    Be careful giving them too many responsibilities,
    or they will get the idea things would be better without an Overseer at the helm.
    It has been a long time since the last imppeachment, and we wouldn’t want to break too many records now,
    would we?{p=3.0}"""

    hide screen impeachmentbar with dissolve
    pause 0.1
    show screen impeachmentbar with dissolve
    hide screen impeachmentbar with dissolve
    pause 0.1
    show screen impeachmentbar with dissolve
    hide screen impeachmentbar with dissolve
    pause 0.1
    show screen impeachmentbar with dissolve

    moira "Lastly, even demons can feel the effect of overwork.
    While we are basically immortal, we are not immune to stress.
    As you have probably guessed, there will be little time to relax as a direct underling of Lucifer himself.{p=3.0}"

    hide screen stressbar with dissolve
    pause 0.1
    show screen stressbar with dissolve
    hide screen stressbar with dissolve
    pause 0.1
    show screen stressbar with dissolve
    hide screen stressbar with dissolve
    pause 0.1
    show screen stressbar with dissolve
    #$ignias_mood = "SuprisedTalk"
    play sound "audio/Ignias/curious1.mp3"

    ignias "How come you know so much about the work of an Overseer?"

    $moira_mood = "Happy"
    play soundMoi "audio/Moira/0h sweetie 2.mp3"

    moira "Honey, I have been around these parts a lot longer than you and over the years picked up some knowledge.
    This is all just common sense."

    $ignias_mood = "DefaultTalk"
    play sound "audio/Ignias/huh2.mp3"

    narrator "Ignias still in a bit of disbelief over what his friend calls “public knowledge”"
    ignias "Well, I guess we should first get to work on reading these scrolls and get a grasp on the situation…"

    hide ignias
    hide moira
    with dissolve

    narrator "a few hours later"

    # FIRST EVENT
    $ignias_mood = "Suprised"
    show ignias at left with dissolve

    narrator "Ignias looks in disbelief at stacks of scrolls, grabs one and reads it"

    ignias "{i}They only made THIS much under the last guy? No wonder the boss had him demoted…{/i}"
    $ignias_mood = "DefaultTalk"
    play sound "audio/Ignias/sad.sigh1.mp3"

    narrator "Ignias glances over at Moira, who is reading a different scroll"
    ignias "Do you have any ideas as to how to boost the extraction rates? If we continue at this pace…"

    $moira_mood = "SuprisedTalk"
    play soundMoi "audio/Moira/ahem 1.mp3"
    show moira at right with dissolve

    moira "Well, while I am no expert on the subject, there are basically two ways
    commonly used throughout Hell to temporarily increase production."

    $moira_mood = "DefaultTalk"

    moira "You could either order the imps to skimp on equipment maintenance.
    Or simply make them work more around the clock. The first option would likely lead to complications down the line,
    and the second one would probably embolden the little buggers."

    # CHOICE MENU START
    hide ignias
    hide moira
    with dissolve

    narrator "How do you want to increase the amount of souls extracted? \n
    Choose quickly, or STRELL will choose for you!"

    $ time = 7.5
    $ timer_range = 7.5
    $ timer_jump = 'equipment'
    show screen countdown
    play timer "audio/Timer.mp3"
    queue timer timerrunout
    menu:
        
        extend ''
        "Order more shifts for imps":
            hide screen countdown
            stop timer
            jump impshift #+impeachment, +souls setFlag: Sabotage by rival
        "Overwork the equipment":
            hide screen countdown
            stop timer
            jump equipment
            #+souls, +stress setFlag: Soul vats overheating


    # NEXT EVENT Imps want more to do
label ImpasWantMore:
    #Minigame Test
    $ minigame_jump = 'ImpasWantMore'
    call screen minigame

    narrator "Ignias works on his own for a bit, before succumbing to an overly long break"
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

    $ignias_mood = "Happy"
    show ignias at left with dissolve

    ignias "{i}Ah, blissful silence for once. This is how every day should be.
    Now I only need a good cup of infernal joe and-{/i}"

    play sound knock

    narrator "{i}frantic knocking{/i}"

    $ignias_mood = "Sad"
    play sound "audio/Ignias/listening3.mp3"

    ignias "... yes?"

    $moira_mood = "MadTalk"

    narrator "Moira enters"
    show moira at right with moveinright
    play soundMoi "audio/Moira/no 3.mp3"

    moira "Have you been doing anything at all since I last saw you?"

    play soundMoi "audio/Moira/hmm8.mp3"

    moira "You need to learn to work on your own, dear, or Lucifer will make sure to find someone who can."

    play sound "audio/Ignias/sad.sigh1.mp3"
    $ignias_mood = "SadTalk"

    ignias "Yes, you are probably right…"

    $moira_mood = "DefaultTalk"

    moira "Anyways, the imps seem to be getting uppity-"

    play sound crashing
    hide moira with dissolve
    show imp at right with moveinright
    queue sound "audio/Imp/impLaugh2.mp3"

    imp "Oi, boss! Some ladz sent me here to tell ya that they want more to do.
    They are all done for the day and are faffing about, lookin’ for somethin’ to lighten your workload,
    sendin’ little old me to ask the master what they could do. {i}the imp smiles, all teeth{/i}"

    hide imp
    show moira at right
    with dissolve
    play soundMoi "audio/Moira/oh really 2.mp3"

    moira "You should probably give them some more work, but that could give them some ideas on how they could run this place without us.
    Although, knowing you that would probably be exactly what you want"

    queue soundMoi "audio/Moira/hmm 9.mp3"

    moira "Or you could just let them laze around for now, although there is also no telling what they would do with all this time on their hands…"

    # CHOICE MENU START
    hide ignias
    hide moira
    with dissolve
    $ time = 4
    $ timer_range = 4
    $ timer_jump = 'keepbusy'

    narrator "Some imps are getting restless, how do you keep them busy? \n
    Choose quickly, or STRELL will choose for you!"

    show screen countdown
    menu:
        extend ''
        "Share some of your own workload":
            hide screen countdown
            jump workload
            # + impeachment
        "Keep them busy on your own dime":
            hide screen countdown
            jump keepbusy
            # + stress


    # NEXT EVENT
label infestation:
    narrator "They both resume reading through the sheer endless amount of records"
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

    $ignias_mood = "SadTalk"
    show ignias at left with dissolve

    play sound "audio/Ignias/sad.sigh1.mp3"

    ignias "Is it only me or does it seem like more paper is magically appearing out of nowhere whenever
    we get anywhere close to being finished?"

    $moira_mood = "DefaultTalk"
    show moira at right with dissolve
    play soundMoi "audio/Moira/0h 3.mp3"

    narrator "Moira rolls together the scroll she just finished reading"
    moira "Don’t be such a Debbie downer! I’m sure we will get through this.
    After all, you wouldn’t want to read only some of these and overlook some
    problem that could draw Lucifer's ire, right?"

    play sound "audio/Ignias/yes2.mp3"

    narrator "Ignias sighs dejectedly and grabs another piece of parchment"
    ignias "Yes, you are probably right, as always… Hey, why does this look like something took a bite out of it?"

    $moira_mood = "SuprisedTalk"
    play soundMoi "audio/Moira/hmm 6.mp3"

    narrator "Moira quickly walks over and investigates the bite marks"

    show moira at center with moveinright

    moira "It looks more like multiple small nibbles instead of one big bite. Now, what creature would cause such-"

    narrator "Moira is interrupted by the less than elegant entrance of a small imp bursting through the door"

    hide moira with dissolve
    show imp at right with moveinright

    imp "Boss! Boss! We ‘ave a problem! They’re back!"

    $ignias_mood = "MadTalk"
    play sound "audio/Ignias/ts4.mp3"

    ignias "Slow down! Who or what is back?"

    narrator "The imp looks anxiously through the room"

    imp "The moths Sire! We thought we got rid of ‘em a while back, under the old boss actually,
    but seems like a few nests must ‘ave avoided the cleansing!"

    narrator "It shudders"

    imp "The worst part, sire… They love paper! You should see the records room.
    Makes some of the battlefields the mortals love so much look like a stroll in heaven.
    They even ate some of the lads…"

    narrator "Ignias visibly pales"

    ignias "You do not, by any chance, mean the records room where we just sent the accounts of today’s extraction, right?"

    narrator "Imp confused"

    imp "There are other records rooms ‘ere?"

    hide imp
    show moira at right
    with dissolve
    $moira_mood = "SuprisedTalk"

    moira "Enough with this! 213, tell us how you dealt with the infestation the last time."

    hide moira
    show imp at right
    with dissolve

    imp "Well, we got some special mixture from the Lower Quarters and started spraying that around.
    Seems like while it didn’t fully eradicate ‘em, it at least held them back for a while.
    Oh, and they didn’t eat any of us while we sprayed the stuff. Ugh, the dungeon still reeks of it…"

    $ignias_mood = "DefaultTalk"

    ignias "Hmm, so we could task some imps with getting more of the pesticide and try to get rid of the moths that way…"

    $moira_mood = "DefaultTalk"
    hide imp
    show moira at right
    with dissolve
    play soundMoi "audio/Moira/haha 5.mp3"

    narrator "Moira smiles sadistically"
    moira "… and lose more accounts until it arrives?I propose ordering imps to transport as many
    records as possible to the dungeon while they shield them with their own bodies."

    #CHOICE MENU START
    hide ignias
    hide moira
    with dissolve
    $ time = 4
    $ timer_range = 4
    $ timer_jump = 'relocate'

    narrator "Hellmoths are feeding on the soul extraction efforts, how do you deal with them? \n
    Choose quickly, or STRELL will choose for you!"

    show screen countdown
    menu:
        extend ''
        "Order some imps to get pesticide":
            hide screen countdown
            jump pesticide
            #+ impeachment
        "Order the records relocated while imps shield them":
            hide screen countdown
            jump relocate
            #+ stress

    #NEXT EVENT
label competition:
    narrator "Luckily, few records seem to have fallen victim to the ravenous swarm, and so the work continues"
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

    narrator "The flapping of wings interrupts the studious silence, and an imp enters the room"

    show imp at right with moveinright
    play sound "/audio/Imp/impLaugh2.mp3"

    narrator "The Imp performs a quick bow"
    imp "Master, I have a letter for you. Say’s here it’s from someone called “the Queen of Eyes”."

    $ignias_mood = "DefaultTalk"
    show ignias at left with dissolve
    play sound "audio/Ignias/curious1.mp3"

    narrator "Ignias takes the proffered letter"
    ignias "The name doesn’t exactly ring a bell. Moira?"

    $moira_mood = "SadTalk"
    hide imp
    show moira at right
    with dissolve
    play soundMoi "audio/Moira/0h 3.mp3"

    moira "Did you pay attention to anything before this job?
    The Queen of Eyes is a fellow Overseer who has held the office for longer than the years you or I have been alive for.
    I hear she is extremely skilled at manipulating others to get what she wants."

    $moira_mood = "DefaultTalk"

    moira "Be careful with that one, Ig."
    narrator "Ignias takes the proffered letter"
    ignias """{i}Dear Ignias, \n
    I congratulate you emphatically on your recent promotion to Overseer.
    While what happened to your predecessor saddens me greatly,
    I am looking forward to witnessing the career of the youngest Overseer to date.{/i}

    {i}I have taken the liberty to help with your first delivery of souls.
    Enclosed in this letter you shall find an address at the lower docks,
    where six barrels full of already extracted material await their retrieval.
    Think of it as a welcome gift to our illustrious trade.{/i}

    {i}Yours sincerely \n The Queen of Eyes{/i}"""

    $ignias_mood = "Happy"
    play sound "audio/Ignias/yes2.mp3"

    ignias "She wants to help me with my first delivery! According to the letter,
    there will be five barrels full of souls waiting for me down by the docks."
    moira "But we are still a few barrels short of today’s deadline, so I suppose her intent on the matter isn’t the most pressing concern now.
    Could you at least do me the favour of sending imps to retrieve our windfall instead of going yourself?"

    #CHOICE MENU START
    hide ignias
    hide moira
    with dissolve
    $ time = 4
    $ timer_range = 4
    $ timer_jump = 'goig'

    narrator "A colleague has offered to chip in with your first delivery, how do you want to retrieve it? \n
    Choose quickly, or STRELL will choose for you!"
    show screen countdown
    menu:
        extend ''
        "Go yourself":
            hide screen countdown
            jump goig
            #+souls, +stress
        "Order the imps to retrieve it":
            hide screen countdown
            jump goimp
            #+impeachment

    #NEXT EVENT
label endDayOne:
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

    if souls < 85:
        jump soulend

    narrator "After long hours of work, the day draws to a close.
    Shortly after Ignias receives confirmation from his imps that today's quota of souls has been delivered,
    he gets summoned to the throneroom"

    $ignias_mood = "DefaultTalk"
    show ignias with dissolve

    ignias "{i}Let's get this over with....{/i}"

    hide ignias with moveoutright
    scene ThroneRoom with dissolve
    show lucifer at right with dissolve
    play sound "audio/Lucifer/growling 3.mp3"

    lucifer "GOOD EVENING, OVERSEER 26. I HOPE THE FIRST DAY AT YOUR NEW TRADE IS FARING WELL?"

    show ignias at left with moveinleft

    narrator "Ignias biws his head"

    ignias "So far there have been no complications my Lord. The department operates smoothly and without delay."

    lucifer """THIS IS MOST PLEASING TO HEAR. KEEP UP THE GOOD WORK, 26, AND REMEMBER, NOT TO DISAPPOINT ME.
    SINCE YOUR DELIVERY ON YOUR FIRST DAY WAS MOST SPLENDID, CONSIDER YOUR QUOTA FOR TOMORROW TO BE THE DOUBLE OF TODAY.

    YOU CAN LEAVE NOW"""

    play sound "audio/Lucifer/chuckle 1.mp3"
    hide ignias with dissolve
    scene Hallway
    show igSadFlip with moveinright

    ignias "{i}How in the heavens am I supposed to deliver double? We barely scraped by today!
    I hope this is not how every following day will go; I am beginning to understand
    what could have led to the demise of my predecessor…"

    return

label soulend:
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
    $gameOver = True
    narrator "After long hours of work, the day draws to a close.
    Shortly after Ignias receives confirmation from his imps that today’s souls has been delivered,
    he gets summoned to the throneroom"

    $ignias_mood ="Default"
    show ignias at left with dissolve
    play sound "audio/Ignias/sad.sigh1.mp3"

    ignias "{i}Let's get this over with....{/i}"

    hide ignias with moveoutright
    scene ThroneRoom with dissolve
    show lucifer at right with dissolve
    show ignias at left with moveinleft
    play sound "audio/Lucifer/growling 3.mp3"

    lucifer "GOOD EVENING, OVERSEER 26. I HOPE THE FIRST DAY AT YOUR NEW TRADE IS TREATING YOU WELL?"

    $ignias_mood ="DefaultTalk"

    narrator "Ignias smiles nervously"
    ignias "Yes, O Devious One, it has been going well, mostly. You see, there was a tiny problem regarding the delivery of-"
    narrator "Lucifer interrupts him with casual ease"
    lucifer "SO I HAVE NOTICED, OVERSEER 26. A PITY. I THOUGHT YOU ARE SMARTER THAN TRYING TO SHORTCHANGE THE
    MOST POWERFUL ENTITY IN THE ENTER REALM ON THE MOST IMPORTANT THING IN HELL."
    narrator "Ignias is visibly distressed"
    ignias "But Great Horned One, there wasn’t any possibility for me to make do on today’s-"
    lucifer "SILENCE, INSIGNIFICANT WORM. IF YOU CANNOT DELIVER ON THE ONLY TASK I HAVE GIVEN YOU,
    THEN THERE MIGHT BE OTHER TRADES MORE SUITED TO YOUR SKILLSET. OR PERHAPS EVEN ANOTHER EXISTENCE ALTOGETHER."

    $ignias_mood ="Suprised"

    narrator "Ignias grows pale"

    ignias "{i}He cannot possibly mean to demote to a lower form of demon! That punishment is only meant for the most-
    But that would explain why no one ever heard from my predecessor again-{/i}"
    lucifer "YOU WILL SPEND THE REST OF ETERNITY AS A SINGLE MINDED GRUB, LIVING OF THE REFUSE OF THE RIVER STYX,
    YOUR MIND TO SIMPLE TO EVEN BEGIN TO GRASP THE EXTENT OF YOUR FAILURE."

    play sound "audio/Lucifer/chuckle 1.mp3"

    narrator "Ignias begins to scream as his form starts to change, growing more maggotlike with every passing moment,
    reeling in his mind until even conscious thought is ripped away from him."

    hide ignias with dissolve
    show lucifer at center with moveinright

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
    $renpy.full_restart()
    return
