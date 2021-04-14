label day_one:
    #Event 1

    show ignias at left:

    ignias "{i}Ah, blissful silence for once. This is how every day should be. Now I only need a good cup of infernal joe and-"

    play sound knock
    pause

    ignias "...yes?"

    "Moira enters"
    show moira at right with dissolve:

    moira "Have you been doing anything at all since I last saw you?
    {i}sigh{/i}
    You need to learn to work on your own dear, or Lucifer will make sure to find someone who can."

    ignias "Yes, you are probably right…"

    moira "Anyways, the imps seem to be getting uppity-"

    play sound crashing
    pause

    hide moira with dissolve
    "Imp enters"
    show fish at right with dissolve

    imp "Oi boss! Some ladz sent me here to tell ya that they want more to do.
    They are all done for the day and are faffing about, lookin’ for somethin’ to lighten your workload, sendin’ little old me to ask the master what they could do.
    {i}the imp smiles, all teeth{/i}"

    hide fish with dissolve
    show moira at right with dissolve
    moira "You should probably give them some more work, but that could give them some ideas on how they could run this place without us.
    Although, knowing you that would probably be exactly what you want {i}sigh{/i}"
    moira "Or you could just let them laze around for now, although there is also no telling of what they would do with all this time on their hands…"

    hide ignias
    hide moira
    with dissolve

    call impmorework from _call_impmorework

    #Event 2
    show imp_event with dissolve
    pause
    hide imp_event with dissolve

    "Moira rushes in"
    show moira at right with moveinright
    pause

    show ignias at left with dissolve
    ignias "Can't you at least knock?"
    moira "There's a problem."
    ignias "Again? What is going on these days? Can’t you deal with it?" #SFX groans
    moira "{size=27}{i}half annoyed, half mockingly{/i}You’re the archdemon? Remember?
    Anyway, some souls which don’t belong in hell got accidentally extracted.
    I think some Imps checked the wrong box on the delivery form.
    The souls were just shortly stored here, ‘cause heaven had some storage capacity problems.
    What do you want to do?"

    hide moira
    hide ignias
    with dissolve

    call wrongSouls from _call_wrongSouls

    #Event 3
    show soul_event2 with dissolve
    pause
    hide soul_event2 with dissolve

    "Infernal noises and screams waft into the room, at least more so than usual"

    show ignias at left with dissolve

    ignias"What is this racket? Can’t a demon at least get some rest and relaxation in their own office?"
    #SFX A knock rings through the cacophony*
    ignias "You may enter."
    ignias "..."
    ignias "{size=60}YOU MAY ENTER!"

    "an imp flutters into to room, bedecked in soul splotches and dust"

    show fish at right with dissolve
    imp "Master! It’s terrible! Never seen anythin’ like it!"
    ignias "Calm down and tell me exactly what’s going on.
    {i}Don’t think I have ever seen one of the little buggers so rattled, except maybe at their own demotion."
    imp "It’s the soul vats Milord. Since you ordered us to run extract more souls,
    they have been runnin’ all day now, and they are getting hotter and hotter.
    I myself have seen them glowing, Milord, {b}glowing{/b}. That has never been seen before. {i}sweats nervously"
    ignias "{size=27}{i}I will never get anywhere close to meeting todays numbers if the vats get damaged.
    That would be most disastrous for my meeting later.Or I could order the imps to try and cool the vats somehow,
    because without overshooting the amount of souls that got extracted yesterday,
    I can forget about getting the quota. What in the heavens am I supposed to do here?!"

    hide ignias
    hide fish
    with dissolve

    call soulVat from _call_soulVat

    #Event 4
    show hellhound_event with dissolve
    pause
    hide hellhound_event with dissolve

    #(SFX)some Imps scream, hellhound barks
    "Imp runs into the office through the already open door"

    show ignias at left with dissolve
    ignias "Who in hell left the door open? Where is Kerberos?"
    show fish at right with moveinright
    imp "Milord, your beloved dog ran wild and was chasing some of us. He ran off to somewhere."
    ignias "What? Why didn’t you stop him? Get out of my sight."
    "Imp hastily leaves the room {nw}"
    pause 0.5
    hide fish with moveoutright
    ignias "{i}Kerberos must be so scared. I need to get him back, before he gets into trouble."

    hide ignias with dissolve

    call cerb from _call_cerb

    #Event 5
    show rival_event with dissolve
    pause
    hide rival_event with dissolve

    "imp saunters into the room"

    show fish at right with moveinright
    imp "Oi boss, ‘ere is the form you requested."
    show ignias at left with dissolve
    ignias "What form? I didn’t request any form. Hmm… says here \"Form to Release Working Imps (FRWI)\",
    which holds records of me having released Imps 354 through 489 this morning… Wait, 354 through 489?"
    ignias "Moira! Do you remember which imps were assigned to handling the extraction vats as the current shift?"
    hide fish with dissolve
    show moira at right with dissolve
    moira "Shouldn’t you just KNOW those things instead of asking me all the time?"
    ignias "Well, probably, but-"
    #SFX sigh
    moira "Okay, but this is the last time.
    If I recall correctly, imps 354 through 489 were assigned as extraction workers by yours truly.
    Why? Did you want to assign them somewhere else?"
    ignias "{i}And they are doing nothing since this morning? Then who is manning the vats? And this signature… this couldn’t have come from me!"
    "another imp flies through the still open door"
    hide moira with dissolve
    show fish at right with moveinright
    imp "Milord, there has been an explosion in the extraction area! One of the vats seems to be damaged!"
    hide fish with dissolve
    show moira at right with dissolve
    moira "{size=27}That can’t be good.
    Without that vat it will be exceedingly difficult to meet today’s soul quota, and you know how the old coot likes his souls.
    You could probably overwork the other ones to make up for it, but that would strain them a lot.
    Or you could send some imps to repair the broken one and just accept a decrease in output for today."

    hide ignias
    hide moira
    with dissolve

    call sabotage from _call_sabotage
