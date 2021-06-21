label day18:
    #Start of Day18

    narrator "Ignias wakes up at his desk, head nearly buried in the heap of documents littered across the worn desktop"

    "He rubs his eyes and barely manages to stifle a yawn"

    $ignias_mood = "Default"
    show ignias at left with dissolve
    ignias "{i}That was almost a complete all-nighter. Again. 
    And we just manage to hit the quota just so, which of course meant another raise in the delivery of expected souls AGAIN. 
    How does any archdemon put up with this?{/i}"

    play sound knock loop
    pause 2.0
    stop sound
    narrator "{i}Frantic knocking noises{/i}"

    $moira_mood = "DefaultTalk"
    show moira at right with moveinright
    narrator "Moira enters the room without waiting for an invitation"
    play soundMoi "audio/Moira/haha 4.mp3"
    moira "Good morning! I thought that I would find you here rather than in your bedchamber."
    "42!"

    hide moira with dissolve
    show imp at right with moveinright
    play sound "audio/Imp/ImpAnnoyed.mp3"
    narrator "An Imp stumbles into the office, struggling to carry a silver tray containing various types of bread, jams, and sliced meats, as well as a carafe styled after a human skull"
    hide imp
    $moira_mood = "Happy"
    show moira at right with dissolve
    moira "This should help you get ready for the day ahead. I’ll leave you to enjoy your breakfast in peace, your first meeting is in 20 minutes from now."
    $ignias_mood = "Happy"
    play sound "audio/Ignias/Yes.mp3"
    ignias "Thanks Moira, you are literally a soulsaver!"
    hide moira with dissolve
    narrator "Ignias begins to savour his breakfast until a knock at his office door interrupts his revelry"

    #Form Kerfuffle
    play sound knock loop
    pause 1.0
    stop sound

    $ignias_mood = "SadTalk"
    ignias "Enter!"
    show imp at right with moveinright
    narrator "An Imp cautiously makes his entrance, his advanced age evident in the slight graying of the horns and the lines around his eyes"
    imp "Oi boss! Me and the lads o’er at records were clearing out some of the old forms when 27 stumbled upon A38, which was issued by your predecessor. 
    You wouldn’t happen to have a copy signed by yours truly lying around? To add to the archive, ‘course."
    $ignias_mood = "SuprisedTalk"
    play sound "audio/Ignias/what.mp3"
    ignias "Well, I do not recall having signed the A38 recently. I will send for one of your archivists when and if it resurfaces."
    narrator "The creature smiles, all teeth"
    play sound "audio/Imp/impLaugh2.mp3"
    imp "Of course, sire!"                    
    narrator "With a bow, the old codger hobbles out of the office"
    hide imp with moveoutright
    ignias "Moira!"
    $moira_mood = "MadTalk"
    narrator "The succubus enters the office, splattered in ink"
    show moira at right with moveinright
    play soundMoi "audio/Moira/hmm8.mp3"
    moira "Is this important? These soul-delivery contracts do not write themselves I will have you know!"
    ignias "An old Imp just asked me after my own copy of A38, which I do not recall ever issuing. Is this another one of their little games?"
    $moira_mood = "SadTalk"
    play soundMoi "audio/Moira/0h 2.mp3"
    moira "Ig, please tell me you have signed A38 on your first day. It is THE most important document in the entire department, since it contains the aeon-old contract between an overlord and their imps. 
    Without a proper A38, set up at your first day, we will be sitting just by ourselves in these musty rooms until Lucifer comes down on us."
    $ignias_mood = "Default"
    ignias "{i}Seems typical for this job that the most important details are ever only revealed in hindsight. Well, no sense in complaining now. How to mollify my procedure-loving underlings? I could try to forge a replacement and claim that I just misplaced it, which could probably fool them for a while.
    {/i}"

    "{i}Or I could try to order even more of them to the man the soul extraction tract, to try and keep too busy to act on the lack of an A38. This would probably just be kicking the barrel down the Styx, though.{/i}"

    # CHOICE MENU START
    hide ignias
    hide moira
    with dissolve

    narrator "Your Imps have found a legal loophole, how do you keep them from causing trouble?
    Choose quickly, or STRELL will choose for you!"

    $ time = 7.5
    $ timer_range = 7.5
    $ timer_jump = 'a38'
    show screen countdown
    play timer "audio/Timer.mp3"
    queue timer timerrunout
    menu:
        
        extend ''
        "Keep them busy by making them work even more":
            hide screen countdown
            stop timer
            jump busymorework #+stress, +souls 
        "Try to forge an A38":
            hide screen countdown
            stop timer
            jump a38
            #+impeachment, +stress 

###################################################################################################

#Queenly Dealings
label queenly:
    $moira_mood = "DefaultTalk"
    $ignias_mood = "SuprisedTalk"
    show ignias at left with dissolve
    show moira at right with moveinright

    narrator "Moira enters the room, a letter in her hand."
    play soundMoi "audio/Moira/hmm 9.mp3"
    moira "Ig, it’s her again."
    play sound "audio/Ignias/what.mp3"
    ignias "Who?"
    narrator "Hands the letter over"
    moira "Your fellow Overlord, the Queen of Eyes."
    $ignias_mood ="Suprised"
    narrator "Ignias reads the letter"
    ignias "{i}She requests a personal meeting, to help further our cooperation for mutual benefit.{/i}"
    $moira_mood = "MadTalk"
    moira "You are not actually thinking of going over there, are you?"
    $ignias_mood = "SadTalk"
    play sound "audio/Ignias/sorry.mp3"
    ignias "What choice do I have? Every single day the big man increases our quota, and she helped us out on the first day."
    $moira_mood = "SadTalk"
    moira "Just… be careful, alright? She IS dangerous, even, and especially to other demons."
    narrator "Ignias enters a shady seeming compound a good half hour later. The building seems ramshackle, even compared to his own domain. Purple skinned imps scamper down the long halls, and after a quick, cautious exchange with one of the little devils, he stands before a big iron door."

    hide ignias 
    hide moira 
    hide screen baroverlay
    hide screen soulbar
    hide screen stressbar
    hide screen impeachmentbar
    scene black
    with dissolve

    scene qoeoffice
    show screen baroverlay
    show screen soulbar
    show screen stressbar
    show screen impeachmentbar
    with fade

    $qoe_mood = "Happy"
    show qoe at right with dissolve
    play sound "audio/QueenOfEyes/Greetings.mp3"
    qoe "Please do come in! I have been expecting you. I hope my little welcome gift a little while back has been put to good use, yes?"

    if neighbourhoodBeef:
        qoe "You even went to the trouble of collecting it yourself. It gladdens me to see my gesture of support appreciated."
    
    $ignias_mood = "Default"
    show ignias at left with moveinleft
    play sound "audio/Ignias/Yes.mp3"
    ignias "Thank you for your kindness. Rest assured that the souls you send me were put to good use."
    $qoe_mood = "Default"
    qoe "Yes, I have seen as much. Now, let us continue to develop our mutual bond. The delivery of souls from my domain to yours could become a more regular occurrence – provided, of course, that we can reach a bargain."
    ignias "And what kind of service would the Queen of Eyes demand of me for her favor?"
    play sound "audio/QueenOfEyes/Hmm.mp3"
    qoe "As you should well now, nothing that goes on around these parts evades my gaze for long. Clandestine meetings such as this, whispered words in the shadows of the docks down at the styx, the chatter of palace imps at the throne of Lucifer itself… All will be known to me, in time."
    play sound "audio/QueenOfEyes/JustAsIHaveForseenIt.mp3"
    narrator "The Queen of Eyes fixates Ignias with a glare. "
    qoe "Know, for the first time in aons, the boss has shown weakness. I spare you the details, but these are my terms: Enjoy some of the fruits of my court, and in exchange, when I come calling, you will be there by my side to enact a… let us phrase it as changing of the guard"
    $ignias_mood = "Suprised"
    ignias "{i}She is talking about treason, openly. This could be bad. Or good, depending on if she can indeed act on her grand vision. If I ally with her in this conspiracy, her constant channeling of souls to meet my quota could be just what is needed to satisfy Lucifer for a few days at least.{/i}"
    "{i}On the other hand, if he catches wind of what just transpired here, my days are numbered, quota be damned. I cannot even sell her out, since it would be my word as the newest Overlord against the Queens, one of Lucifer's oldest vassals. But I could still decline and limit the damage, should he declare Armageddon on her.{/i}"

    # CHOICE MENU START
    hide ignias
    hide qoe
    with dissolve

    narrator "The Queen of Eyes is promising you souls in exchange for your support against Lucifer, what will you do?
    Choose quickly, or STRELL will choose for you!"

    $ time = 7.5
    $ timer_range = 7.5
    $ timer_jump = 'decline'
    show screen countdown
    play timer "audio/Timer.mp3"
    queue timer timerrunout
    menu:
        
        extend ''
        "Take the deal":
            hide screen countdown
            stop timer
            jump takedeal #+stress, +++souls
        "Decline her offer":
            hide screen countdown
            stop timer
            jump decline
            #+impeachment, +stress 

################################################################################################
#MINIGAME
label minigame3:
    #Minigame Test
    $ minigame_jump = 'gates'
    play minigame "audio/Minigame.mp3"
    call screen minigame 

#############################################################################################

label gates:
    stop minigame
    play music "audio/myuu-dark-creature.mp3" loop

    scene bgHell
    show screen baroverlay
    show screen soulbar
    show screen stressbar
    show screen impeachmentbar
    with fade   
    show ignias at left with dissolve

    $ignias_mood = "Happy"
    ignias "{i}I must say, doing paperwork can be relaxing from time to time…{/i}"
    narrator "Ignias idle musings are interrupted by ring of the bright red hellphone on his desk, and soon after a familiar shape begins to form in his office."
    play sound "audio/Lucifer/hmgr 1.mp3"
    show lucifer at right with flash
    lucifer "GREETINGS, OVERSEER 26."
    lucifer "IT SEEMS LIKE THERE IS TROUBLE AT THE GATES. I TRUST YOU ARE FAMILIAR WITH MODEAN AND MASTEMA?"
    ignias "{i}These are some hell's most senior demons. They are tasked with guarding all entrances to the underworld and take pride in their duties. I have only ever seen them from afar.{/i}"
    play sound "audio/Ignias/no.mp3"
    ignias "No,Lord, I was not granted that privilege in my previous profession and have yet to meet them as Overlord." 
    play sound "audio/Lucifer/hmgr 1.mp3"
    lucifer "YOU AS THE MOST JUNIOR OVERSEER ARE HEREBY CHARGED WITH THEIR OVERSIGHT. THEY WILL SOON ATTEND YOUR OFFICE"
    hide lucifer with flash
    narrator "The apparition of the ruler of hell vanishes, and a knock resounds through the room"
    play sound knock
    play sound "audio/Ignias/yes_inviting.mp3"
    ignias "You may enter!"
    show twins at right with moveinright
    narrator "The demonic twins enter the office, looking stressed"
    $twins_mood = "Suprised"
    play sound "audio/TwinM/ts.mp3"
    twinm "They put you in charge of US? I thought the old guy thought more of us than that."
    play sound "audio/TwinF/tsk pathetic.mp3"
    twinf "Maybe he still has not forgiven us for that stunt a while back. Do you remember, brother?"
    play sound "audio/TwinM/boring.mp3"
    twinm "Well, if he keeps this up, he is going to have another thing coming."
    $ignias_mood = "Suprised"
    play sound "audio/Ignias/what.mp3"
    narrator "Having trouble interrupting the siblings, Ignias finally finds an opening"
    ignias "I can understand that you are not happy working under me, but this is how Lucifer ordered it. Now, he mentioned something was troubling you?"
    $twins_mood = "Default"
    play sound "audio/TwinF/snort.mp3"
    twinf "{i}Turning to her brother{/i}"
    twinf "Should we even bother telling him? It's not like this grub could even do anything."
    twinm "Well, at least for the time being Big L still calls the shots around here, so we gotta do it. Even if this sorry excuse for an Overlord is involved"
    $ignias_mood = "SadTalk"
    play sound "audio/Ignias/I_see.mp3"
    ignias "{i}Resigned{/i}"
    ignias "Please just tell me what is going on. The sooner you tell me, the sooner we can all go our separate ways again."
    $twins_mood = "Mad"
    play sound "audio/TwinF/hmph.mp3"
    twinf "{i}Pouting{/i}"
    twinf "Fine! The trouble is as follows: Its those damned mortals! But not in their delicious, soft, and squishy form after shedding the coil, no, these grunts are still in the flesh. They have somehow gotten close to locating one of the ancient entrances to hell"
    play sound "audio/TwinM/no.mp3"
    twinm "They apparently think of using hell as an energy source. Imagine that! Cattle seeking to cage and milk the wolves. Pathetic."#
    ignias "Well, if these mortals are indeed so pathetic, then why not go deal with them? Offer one of them all his desires, to, say, kill all the others. You now, the standard stuff?"
    play sound "audio/TwinM/sigh.mp3"
    twinm "Don’t you think if it were that easy for us, we would not have done so already? We are bound to the gates of hell; we cannot do that stuff on our own."
    $twins_mood = "Default"
    play sound "audio/TwinF/pathetic.mp3"
    twinf "That’s where you come in, lardass. Now, these mortals are already very close to the entrance, so there probably will not be much time in offering contracts yourself, so you will send some of your minions to do the dirty work."
    $twins_mood = "Happy"
    play sound "audio/TwinM/bad laugh.mp3"
    twinm "There is also the possibility of simply collapsing their compound, killing the lot in one fell swoop. Now, Heaven would probably not be happy with that, since that would bending the rules a little too much for the featherfaces up there, but it would be the quickest way to deal with the situation."
    $twins_mood = "Default"
    twinf "Well, little Overseer? What’s the plan?"

    # CHOICE MENU START
    hide ignias
    hide twins
    with dissolve

    narrator "Mortals have come close to discovering hell, how do you stop them?
    Choose quickly, or STRELL willchoose for you!"

    $ time = 7.5
    $ timer_range = 7.5
    $ timer_jump = 'collapse'
    show screen countdown
    play timer "audio/Timer.mp3"
    queue timer timerrunout
    menu:
        
        extend ''
        "Send some imps to tempt some of them into killing the others":
            hide screen countdown
            stop timer
            jump impkilling #+impeachment, +souls
        "Collapse their compound, reducing them and their ambitions to rubble":
            hide screen countdown
            stop timer
            jump collapse
            #+stress
    
 #################################################################################################

label goodboy:
    $ignias_mood = "Happy"
    show ignias at left with dissolve
    ignias "{i}Finally, some peace and quiet as the day comes to a close. Surly nothing could interrupt-{/i}"
    play sound "audio/Cerb1.mp3"
    narrator "Loud barking cuts through the serene silence of the office"
    ignias "{i}Must be Cerberus. Didn’t the imps say that their old beast master would handle my boy
    and train him thoroughly? I’d better take a look.{/i}"
    
    hide ignias
    hide screen baroverlay
    hide screen soulbar
    hide screen stressbar
    hide screen impeachmentbar
    scene black
    with dissolve

    scene cerbcell
    show screen baroverlay
    show screen soulbar
    show screen stressbar
    show screen impeachmentbar
    with fade
    show ignias at left with dissolve

    narrator "Ignias hastily leaves his desk, walking swiftly though long corridors and down cold and damp stone stairways until he reaches the dungeons, where his dog is currently confined"
    $ignias_mood = "Suprised"
    $cerberus_mood = "Happy"
    show ignias at left with moveinleft
    narrator "{i}Cerberus sits happily in his cage, mouths smeared with imp blood. Gory bits of imp also litter his cage and are also smeared on the walls{/i}"
    ignias "By the seven heavens, what has happened here?"
    show imp at right with dissolve
    imp "A disaster, sire! Old 89 grew tired with the, ah, temper of you dog, and tried to take a more direct approach to his training…"
    $ignias_mood = "SadTalk"
    ignias "You have really done it now, boy. That is how many trainers in a row?"
    hide imp with dissolve
    show cerberus at right with dissolve
    play sound "audio/Cerb2.mp3"
    cerb "Growl!"
    play sound "audio/Ignias/I_see.mp3"
    ignias "I suppose there are not any other beast masters currently around, are there?"
    hide cerberus
    show imp at right
    with dissolve
    imp "No, sire. 89 was the last one. You see, your predecessor had this brilliant idea of trying to breed Hydras down here. That convinced a lot of us to seek, ah, other areas of expertise!"
    ignias "{i}that puts me in a bit of a bind. Should I try to train the dog myself? That would put a strain on my other tasks. Alternatively, I could try to find another expert in Helltropolis to tame Cerberus.{/i}"
    
    # CHOICE MENU START
    hide ignias
    hide imp
    with dissolve

    narrator "Your dog has eaten his last trainer, do you want to try your hand or seek someone else to do it for you?
    Choose quickly, or STRELL willchoose for you!"

    $ time = 7.5
    $ timer_range = 7.5
    $ timer_jump = 'seekexpert'
    show screen countdown
    play timer "audio/Timer.mp3"
    queue timer timerrunout
    menu:
        
        extend ''
        "Train the dog yourself":
            hide screen countdown
            stop timer
            jump traindog #+stress
        "Seek another expert":
            hide screen countdown
            stop timer
            jump seekexpert
            #+impeachment



