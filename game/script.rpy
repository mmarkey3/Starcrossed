# You can place the script of your game in this file.

init 1:
    # Declare images below this line, using the image statement.
    image bg atrium = Transform("images/bg/atrium.png", size=(1920,1080))
    $ genevaW = 550
    $ genevaH = 961
    image geneva = Transform("images/winters_neutral.png", size=(genevaW, genevaH))
    image geneva shock = Transform("images/winters_shock.png", size=(genevaW, genevaH))
    image geneva blush = Transform("images/winters_blush.png", size=(genevaW, genevaH))
    image geneva frown = Transform("images/winters_frown.png", size=(genevaW, genevaH))
    $ hannahW = 587
    $ hannahH = 1000
    image hannah = Transform("images/hannah_neutral.png", size=(hannahW, hannahH))
    image hannah grin = Transform("images/hannah_grin.png", size=(hannahW, hannahH))
    image hannah laugh = Transform("images/hannah_laugh.png", size=(hannahW, hannahH))
    image hannah pang = Transform("images/hannah_pang.png", size=(hannahW, hannahH))
    image hannah verge = Transform("images/hannah_verge.png", size=(hannahW, hannahH))
    image willow = Transform("images/willow_neutral.png", size=(600,883))

    # Declare characters used by this game.
    define mc = Character('mc', dynamic=True, color="#ffffff")
    define gw = Character('Geneva', color="#C9E6F0")
    define hs = Character('Hannah', color="#F29D83")
    define we = Character('Willow', color="#BBEDB2")
    define ab = Character('Undecided', color="#FC79AC")
    define who = Character('???', color="#FFFFFF")
    define th = Character('Therald', color="#FFFFFF")

    define audio.creepy = 'music/bensound/bensound-creepy.mp3'
    define audio.dance = 'music/bensound/bensound-dance.mp3'
    define audio.enigmatic = 'music/bensound/bensound-enigmatic.mp3'
    define audio.funky = 'music/bensound/bensound-funkyelement.mp3'
    define audio.loss = 'music/bensound/bensound-november.mp3'
    define audio.darkspace = 'music/bensound/bensound-scifi.mp3'
    define audio.dawn = 'music/bensound/bensound-slowmotion.mp3'
    define audio.school = 'music/bensound/bensound-straight.mp3'
    define audio.love = 'music/bensound/bensound-love.mp3'
    define audio.menuscreen = 'music/bensound/bensound-memories.mp3'
    define audio.hopeless = 'music/bensound/bensound-ofeliasdream.mp3'

    define audio.maelstrom = 'music/purplePlanet/Maelstrom.mp3'
    define audio.shenanigans = 'music/purplePlanet/Shenanigans.mp3'

    define audio.awkward = 'music/incompetech/monkeysSpinningMonkeys.mp3'

    define whiteflash = Fade(.25, 0.0, .75, color="#fff")
    return

# The game starts here.
label start:
    
    $ mc = "Mark"
    
    jump test
    
    "Required Credits for Royalty Free Music"
    "Music: Creepy, Dance, Enigmatic, Funky Element, Novemer, Scifi, Slow Motion, Love, Memories, Ophelia's Dream, and Straight - www.bensound.com"
    "Music: Maelstrom, Shenanigans - www.purple-planet.com"
    "Music: Monkeys Spinning Monkeys - incompetech.com"
    
    return
label prologue:
    scene black with dissolve
    
    stop music fadeout 3.0
    $ renpy.pause(3.0)
    
    "There is no solitude, no helplessness, no terror like floating through the void of space."
    
    $ renpy.pause(1.0)
    play music maelstrom
    
    show text "Shiny Rabbit presents...." with dissolve
    $ renpy.pause(3.0)
    hide text with dissolve
    
    
    "Most of all, I remember the smell, while I gasped for oxygen. A metallic smell, like rust, but organic. The smell of rich iron. The smell of blood."

    "I fumbled hopelessly for a light. The core wasn't responding to my voice commands. I had to find a switch."

    "I hissed in pain when my fingers touched a sharp edge that sparked, sending a jolt down my arm. A damaged circuit. Even if I found a light, it might not have power."

    "I heard a weak voice call out to me near my feet."

    who "Who’s… There? "

    mc "It's me, %(mc)s."

    who "Thank…Odin…."

    "I almost don't recognize the shaking voice, but there's no mistake."

    mc "Therald! Is that you?! Are you okay?!"

    th "I've…had better days. In the hospital…with a hangover…"

    "Therald’s wise-ass humor gave me a shred of false hope. I searched for a switch even more frantically."

    mc "Everything's going to be okay. We can fix the breach in the hull. We're going to be fine."

    "Even as I spoke, I started to get dizzy. It didn’t matter how much air I gulped down. I couldn't seem to get enough to focus."

    "My fingers brushed against a manual power switch. I didn't stop to think. I flipped it on."

    scene bg atrium with dissolve

    mc "Oh God…!"

    th "Hey…what's…that look for…?"

    "I couldn't answer."

    "I already knew Therald was going to die. Even if I was a better healer, his wounds were unreal. And yet…he still had that wry smile stuck on his face."

    "It didn't feel like it was happening. I told myself it had to be a dream. Or a drug. Or a hallucination created by oxygen deprivation."

    "That was the coldest, most horrible truth. Even if there was any hope of saving him…we were both going to die when the air drained from the cabin."
    
    th "...%(mc)s…."

    stop music fadeout 3.0

    "I heard a shrill, panicked voice behind me."

    who "My air…!"

    "My heart stopped."

    "No one else was on this ship with us.  Heirman, Gallus, and Melchai escaped in the teleporter before it blew.  So, the only ones left should have been Therald and I…and I didn't recognize the other voice."

    who "You're...taking my air!!"

    scene bg atrium with whiteflash
    $ renpy.pause(1.0)
    scene black with dissolve
    
    jump prologue_trial
    
    return

label prologue_trial:
    
    play music hopeless
    
    scene bg atrium with dissolve
    
    "That's the last thing I remember before. I lost consciousness."
    
    return
label test:
    scene bg atrium
    show geneva
    gw "I am Geneva Winters."
    show geneva shock
    gw "I have never been introduced to a lower class human before."
    show geneva frown
    gw "Do you...speak to elvish nobility often?"
    show geneva blush
    gw "What am I saying?  Of course you don't."
    
    show hannah at right
    
    hs "My name is Hannah.  What's up?  Don't hold me back!"
    show hannah grin
    hs "Sometimes I'm happy."
    show hannah laugh
    hs "Really happy!!"
    show hannah pang
    hs "But sometimes..."
    show hannah verge
    hs "I get very sad..."
    show hannah
    hs "Just kidding! I'm never sad!"
    
    play music maelstrom
    
    show willow at left
    
    we "...Willow.  It's a pleasure."
    
    "I hear a crazed voice from somewhere in the distance."
    
    play music awkward
    
    ab "My name is undecided!  Sup, bitch?  Haha~"
    
    hs "That's the rogue.  You'll meet her later."
    
    $ house = "Swords"
    $ element = "air"
    
    play music love
    
    gw "I'll go ahead and set up initial variables for you.  You are in the house of %(house)s.  Your name is %(mc)s.  Your core spirit is %(element)s type."
    
    play music dawn
    
    gw "By now you've already made me very angry."
    
    play music school
    
    "...Gulp."

    return
