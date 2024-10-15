# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.
define mc = Character("[MC]", color="#13c14a")
define sam = Character("[sam]", color="#da28e4")
define sam2 = Character("[sam]", color="#4334cb")
define pushright = PushMove(1.0, "pushright")
define pushleft = PushMove(1.0, "pushleft")
define pushup = PushMove(1, "pushup")
define pushdown = PushMove(1.0, "pushdown")
define gc =  Character("GrimCiri (Dev)", color="#303030")

$ istrap = 0
$ isknown = 1
$ isoral = 0
$ isfoot = 0
default iscumout = 0
$ DevCom = 0

# Fade to black and back.
define fade = Fade(0.5, 0.0, 0.5)

# Hold at black for a bit.
define fadehold = Fade(0.5, 1.0, 0.5)

# Camera flash - quickly fades to white, then back to the scene.
define flash = Fade(0.1, 0.0, 0.5, color="#fff")

define gui.about = _("""\
Created by GrimCiri.

Renders made in DAZ Studio 4.21""")

define config.version = "1.3"

# For legal reasons
label age_restriction_menu:
    menu:
        "Yes.":
            jump begin
        "No.":
            jump exit_to_menu

# For legal reasons
label start:
    $ DevCom = 0
    label variables:
    stop music fadeout 4.0
    "This game is intended for adults. By playing this game, you agree that you
    are at least 18 years of age, and that it violates no laws in your country of residence."
    "All characters depicted within this game are at least 18 years of age."
    "You understand that this is a work of fiction anything seen in game is fantasy and does not represent real life."
    jump age_restriction_menu

# For legal reasons
label DevTrack:
    $ DevCom = 1
    "Developer commentary has been enabled!"
    show grim1
    gc "This is not mean for your first play though if you have somehow enabled this and not already played though the game I suggest you return to the main menu"
    "Here is a brief run down of Developer commentary mode, think of it like a director commentary on a DVD, the game will play out like normal except I will interject periodically to include little development tidbits"
    "This probably {b}won't{/b} be interesting for most people you have been warned."
    hide grim1
    jump begin


# The game starts here.
label begin:
    scene whiteroom

    "Now is the love interest a Woman or Dickgirl?"
    $ isoral = 0
    $ isfoot = 0
    menu:
        "Woman":
            $ istrap = 0
            $ isknown = 1
            
        "Trap":
            $ istrap = 1
            $ isknown = 1
            # menu:
            #     "Suprise":
            #         $ isknown = 0
            #     "Friend":
            #         $ isknown = 1
        "I'm Feeling Lucky!"   :
            $ isknown = 0
            $ istrap = renpy.random.randint(1, 2)
            if istrap == 1:
                $ istrap = 0
            elif istrap == 2:
                $ istrap = 1

                "its [istrap]"


    "Great! lets start"

    jump Prologue

    menu:
        "Start":
            jump Prologue
        "Coffee":
            jump coffee
        "Kiss":
            jump kiss
        "BJ":
            jump blowjob
        "Sex":
            jump sex
        "Testing":
            jump sex2
        "Ending":
            jump ending

label Prologue:
    scene fd888
    $ MC = "Guy"
    "What is his name (This is you)..."
    $ MC = renpy.input("Name{i}{size=-10}{color=#B0E0E6}{/color=#B0E0E6}{/size=-10}{/i} (Default Guy)", length=15) or "Guy"
    $ MCcap = MC.upper()
    scene prologue
    if DevCom == 1:
        show grim1
        gc"So This prologue perhaps unsurprisingly was actually one of the last parts of the story, when I wrote the script it originally started 'post' the date and kind of jumped right into the action"
        gc"However, as I play tested I realized that I left a lot too ambiguous, stuff that I basically head canoned but never actually wrote backstory for."
        gc"I didn't want to make the game overly long, so a prologue was I think the easiest way to build up the characters without becoming too wordy."
        hide grim1
    else:
        gc"Sorry I couldn't think of a more clever way to integrate this into the story."
    scene fd_prolog_1
    "When [MC] was still a child, he grew up in the small town of Springfield"
    scene fd_prolog_2
    "You were popular in school"
    if DevCom == 1:
        show grim2
        gc"I was originally going to add the LI as an Easter egg to the background here but, since I used these grey figures as extras I thought it would stand out too much"
        hide grim2
    
    scene fd_prolog_2a
    "Well liked by all"
    if DevCom == 1:
        show grim2
        gc"If it's not clear this is supposed to be the Sarah the other barista you reconnect with later in the story"
        hide grim2        
    scene fd_prolog_3b
    "However after high school you made the tough decision to leave for the big city for a better education to pursue your dream career"
    if DevCom == 1:
        show grim1
        gc"Perhaps this is cheap, but using IRL photos for minor scenes like this is way easier to render and saves a tone of time."
        hide grim1       
    scene fd_prolog_4
    "it wasn't easy you had to keep your head down and study hard"
    scene fd_prolog_5
    "but it all paid off in the end as you managed to achieve your dream and land the career opportunity of your life"
    "After a few years at the company, a promotion came up as a lead on a new product that also happened to allow you to return home"
    scene fd_prolog_6
    "You jumped at the opportunity as a little way to see the homestead once again and catch up with old friends"
    scene fd_prolog_7
    "while back home you met up with Sarah a once girlfriend but now just friends she owns a cafe in town"
    scene fd_prolog_7a
    "after a few visits and catching up, she tell you that you have attracted a secret admirer"
    scene fd889
    "Her name is..."
    $ sam = renpy.input("Name{i}{size=-10}{color=#b0e6d1}{/color=#b0e6d1}{/size=-10}{/i} (Default Sam)", length=15) or "Sam"
    "[sam] the barista who works for Sarah is very shy but has developed a crush on you."
    "Sarah tell you she is a nice quite girl but far too shy to ask you out on her own and knows you are too thick headed to notice"
    "She is not the type of girl you normally hang with, as years in the city has made you accustom to girls who are much bolder and brash"
    "'At the very least she needs the experience.' Sarah tell you"
    if DevCom == 1:
        show grim1
        gc"Sam was picked as the default name (in code too) because its short and gender ambiguous."
        hide grim1       
    scene fd_prolog_8
    "Well you've got nothing to lose and she is cute 'Why not' you think"
    "because of your awkward work schedule you settle on a lunch date, you worry [sam] might think you are not trying but seem happy nonetheless."
    scene fd_prolog_9a
    "You take her out to a restaurant you remembered liking from your childhood, it has gotten more upscale since you were last in town...{w} you are under dressed"
    scene fd_prolog_9b
    "The Date seems to go well but you can't help but feel you are the one doing all the talking"
    scene fd_prolog_9c
    ##scene fd_prolog_9d
    "You decide to also take her out to a movie of her choice, maybe that will make her feel a little more comfortable and open up"
    show postera
    "To your surprise, she picks a movie you've never heard of 'Rock 'n' Roll Zombies 5: Undead Encore'"
    ##add a new render here of sam looking happy and movie poster
    hide postera

    "The is where our game picks up from leaving the movie theatre."

    jump date

label date:
    scene theatrepan
    $ renpy.pause ()
    scene fd_theatre_li_100 with dissolve
    sam"So what did you think?"
    scene fd_theatre_li_200 with dissolve
    mc"Of the movie? well, it's certainly... different."
    scene fd_theatre_li_101
    sam"Oh..."
    scene fd_theatre_li_201
    mc"No! In a good way, it's just not something I would have thought to watch on my own."
    scene fd_theatre_li_102
    sam"Oh."
    scene fd_theatre_li_202
    mc"You know, I would have though, I would've needed to have seen the first four first,"
    scene fd_theatre_li_204
    mc"but with such a cute aficionado with me I think I was just about was able to follow the deep lore of 'Rock 'n' Roll Zombies universe"
    scene fd_theatre_li_103
    sam"Please, maybe you were having trouble following along because of all the drinks you were downing."
    scene fd_theatre_li_207
    mc"Hey when Reel Deal Tuesday extends to the drinks, how can I {b}not{/b} capitalize on it?"
    scene fd_theatre_li_105a
    sam"Uh maybe by correcting the kid, he clearly made a mistake on the pricing"
    scene fd_theatre_li_206
    mc"Mmm that's his fault...{w} though maybe I shouldn't get into the habit of day drinking"
    scene fd_theatre_li_208
    mc"It's not a good look, is it?"
    scene fd_theatre_li_106
    sam"I won't tell if you don't"
    scene fd_theatre_li_209
    mc"Haha thanks but, I think the smell of booze on my breath might just give me away."
    if DevCom == 1:
        show grim1
        gc"I wanted a justification for [sam] to become curious in [mc]'s smell this was the best I could come up with."
        hide grim1   
    scene fd_theatre_li_211
    mc"Maybe I can just keep a safe distance between me an my clients think that will do the trick?"
    scene fd_theatre_li_210
    mc"They are not the most observant you know that might work"
    mc"Plus it not like I'm even the worst smelling guy in the office"
    scene fd_theatre_li_109
    sam"hmmm"
    scene fd_theatre_li_214
    mc"Do you know Jerry? I tell you that guy is-"
    scene fd_theatre_li_313
    mc"*Ramble* *Ramble* *Ramble*"
    scene fd_theatre_li_314
    mc"*Ramble* *Ramble* *Ramble*"
    scene fd_theatre_li_315
    mc"*Ramble* *Ramble* *Ramble*"
    scene fd_theatre_li_214a
    mc"(Uh oh I'm getting pretty rambley I probably shouldn't talk her ear off just when she was opening up)"
    "*Sniff* *Sniff*"
    scene fd_theatre_li_115
    mc"What?!"
    scene fd_theatre_li_116
    sam"ah-"
    scene fd_theatre_li_316
    ""
    scene fd_theatre_li_117
    sam"I was just smell{size=-5}ing{/size}-"
    scene fd_theatre_li_120
    sam"{size=-10}(OMG OMG OMG){/size}"
    scene fd_theatre_li_317
    sam"{size=-10}(Why did I do that){/size}"
    scene fd_theatre_li_121b
    sam"Well it's been great, but I should probably go"
    scene fd_theatre_li_219
    mc"[sam]"
    scene fd_theatre_li_122a
    sam"I know you're probably busy and- {size=-10}(I just want to curl up and die please){/size}"
    scene fd_theatre_li_122b
    mc"[sam] stop"
    scene fd_theatre_li_123a
    mc"[sam] don't make me chase you down the street"
    sam"{size=-10}*Sorry*{/size}"   
    mc"Do you wanna get out of here?"
    scene fd_theatre_li_123c
    sam"{size=-10}Yes{/size}"   
    mc"let me take you home then"
    scene fd_theatre_li_123b   
    $ renpy.pause ()
    sam"{size=-5}Okay{/size}"
    jump demo




label demo:   
    scene hallway2 
    $ renpy.pause ()
    scene hallway1
    $ renpy.pause ()
    scene fd001 with dissolve
    if DevCom == 1:
        show grim1
        gc"This is where the game originally started."
        gc"and where most of the exposition was originally going to be put before everything else was added instead."
        hide grim1     
    mc"(God just when I thought I was getting her to open up it looks like I pushed too far and embarrassed her in the process.)"
    mc"(I hope I didn't mess things up she's just far more shy and reserved than I'm used to.)"
    scene fd002 with dissolve
    mc"(I can't help hope I didn't ruin the experience for her, maybe I need to rethink my tact.)"
    scene fd003 with dissolve
    if DevCom == 1:
        show grim2
        gc"These are some of my earliest renders left in the game, most of all the renders in game got redone two or three times"
        gc"I debated redoing these too but I felt I might just never finish the game if I kept remaking scenes"
        hide grim2      
    mc"(She's been silent since we got in the car, maybe she {i}did{/i} want to get away from me and now I'm just following her back to her house.)"
    scene fd004 with dissolve
    mc"(Suddenly she glances back at me,{w} it kind of feels like I'm stalking her, now I feel like a creep.)"
    scene fd005 with dissolve
    "but she's actually slowing down are you both approach her apartment door"
    scene fd009
  
    #scene fd001 with dissolve
    #"I went on a date with [sam] tonight she is not my usual type"
    #scene fd002 with dissolve
    #"but a friend of mine who owns the local coffee shop [sam] works at asked me to do this as a favour to her."
    #scene fd003 with dissolve
    #"I thought the date when pretty well, she is very shy on our date but now walking her home we haven't shared a single word together"
    #scene fd004 with dissolve
    #"Suddenly she glances back at me,{w} it kind of feels like I'm stalking her, great now I feel like a creep"
    #scene fd005 with dissolve
    #"but she's actually slowing down we must be at place now{w}, finally she stops and turns to me"
    #scene fd009

    $ renpy.movie_cutscene("fdturn.mkv")



    scene fd007 with dissolve
    if DevCom == 1:
        show grim1
        gc"That animation and the upcoming walking animation are the only pre-made animations I used, everything else I animated myself."
        gc"which is why the quality is a little sporadic"
        hide grim1        
    "She breaks the silence"
    sam"This is my place."  
    sam"Thanks for walking me home."
    mc"It was a pleasure!"
    sam"I had a really nice time with you... {size=-5} until I umm.{/size}"
    mc"Don't even worry about it{w} if you'd like we can end it on a better note instead?" 
    "Normally I would end a date with a kiss but she seems to purposely have distanced herself from me now."
    scene fd008 with dissolve
    sam"Really? err...{w} would you like to come inside"
    scene fd013 with dissolve
    sam"For a coffee... or something?"
    "Oh wasn't expecting that."
    scene fd009 with dissolve
    mc"Sure a coffee sound great about now."
    "She lights up."
    scene fd010 with dissolve
    sam"Great!"
    "...I wait for her to let us in."
    sam"Oh right! Hold on."
    scene fd011 with dissolve
    "Then promptly spins back around to open the door"
    scene fd012 with pushup
    "While she fiddles with the knob, I can't help but drift my gaze"
    sam"Sorry!"
    mc"No worries..."
    jump coffee

label coffee:
    scene hallway2 with dissolve
    "Finally we get into her apartment"
    
    scene fd_landing_0 with dissolve

    #$ renpy.movie_cutscene("fddance1.mkv", delay=None, loops=-1, stop_music=True)
    "Huh maybe the date when better than I thought, but even still I never though [sam] would be the type to invite someone in on the first date"
    scene fd_landing_1 with dissolve
    "Maybe there's more to her than I thought"
    "Or maybe she really did just offer me coffee and I'm reading into this way too much..."
    scene fd_landing_4a with dissolve
    "hmm{w} say we haven't even been standing here that long but it looks like she's already lost in thought."
    "I guess I am too but I've been monologue-ing to myself, what could she be thinking I wonder?"
    scene fd_landing_4 with dissolve 
    "Suddenly see seems to snap back to reality a little embarrassed it seems"
    scene fd_landing_5 with dissolve
    sam"Oh sorry right the uh... coffee"
    scene fd_landing_6 with dissolve
    "You haven't even taken your shoes off yet but she quickly hurries off to the kitchen."
    scene Walk1
    $ renpy.pause (1.4)
    scene fd_landing_6a with dissolve
    $ renpy.pause ()
    "you hurry your shoes off to catch up"
    "While you catch up you look around at the apartment it's nice, it's very...{w} pink."
    scene fd_landing_7 with dissolve
    sam"I'm really glad you {i}finally{/i} took me out tonight I had a really nice time."
    scene fd_landing_7a with dissolve
    $ renpy.pause ()
    scene fd_landing_7ca with dissolve
    mc"Finally?"
    scene fd_kitchen01 with dissolve     
    sam"Huh?"
    scene fd_kitchen02a with dissolve  
    sam"Oh,{w} well it's just that from when I first saw you at the shop {size=-10}I thought...{/size}"
    sam"I just {i}kept{/i} seeing you in the mornings at the coffee shop and I kept thinking that today would be the day when you'd {i}finally{/i} ask me out."
    #scene fd104 with dissolve     
    ## sam"You know no better way to end a night than with a nightcap right?" ## I don't know what this means?
    scene fd_appt_m_react1 with dissolve        
    mc"from the first time you saw me?"
    scene fd_kitchen0304 with dissolve        
    if isknown == 1:
        sam "hehe {size=-10}yeah...{/size} I guess in my mind I've been waiting...{w} a {i}while{/i} for this date."
    else : 
        sam "hehe {size=-10}yeah...{/size} I guess in my mind I've been waiting weeks for this date."
    scene fd_kitchen0305 with dissolve     
    sam"I just kept seeing you, in the morning, and it was I all I could think about."
    scene fd_kitchen0306 with dissolve        
    sam"I thought you were..{w} cute"
    
    sam"I grabbed the wrong order{w} three times {w} last week, because I was just {i}so{/i} distracted looking at you wondering..."
    scene fd_appt_wide_1 with dissolve        

    #scene fd109 with dissolve      
    sam"Okay, don't laugh {w} but I've just been daydreaming of how you could ask me out, a bouquet of flowers, secret messages passed in the coffee, on a lone hill during the sunset those kinds of things"
    
    #I was kind of had this little dream walking in with a single rose leaning in and asking me out and then we blow off work and ride off right then and there"
    #sam"wondering if you even noticed me and that you would just one day{w} man up, take charge and ask me out"
    scene fd_appt_mc_sit_talka00000 with dissolve    
    mc"And you get asked out like this...{w} often?"

    ##mc"'take charge?'{w} you don't get out much do you?"
    scene fd_appt_f_walk1a with dissolve 
    sam"{size=-9}*He he*{/size} no I...{w} it's from this this romance novel I'm reading."   
    #sam"Haha yeah no I...{w} I don't get asked out a lot"
    scene fd_appt_mc_sit_talka00001 with dissolve    
    mc"Ah, well how can I compete with the great E. L. James"
    if DevCom == 1:
        show grim1
        gc"If this joke didn't land E. L. James is the author of 50 Shades of Grey. I had to look it up to when I realized I didnt know a single author."
        hide grim1     
    scene fd_appt_mc_sit_talka00003 with dissolve    
    sam"No not that book you goof"
    scene fd_appt_f_cute1a with dissolve
    sam"but still now that I've tried it I like the real thing way more."

    scene fd_appt_m_react6 with dissolve   
    mc"So you've never been on a date before?"
    sam"Umm I guess you could say well...{w} no."

    mc "Really why is that?"
    show fd_cute_pan_new:
        subpixel True
        yalign 1.0
        linear 6.0 yalign 0.0
    $renpy.pause(delay = 3.0, hard = True)
    sam"I mean I don't know why I get asked out more...{w} I think I'm pretty cute"      
    #scene pancute1
    #$ renpy.pause ()
    scene fd_appt_m_react12 with dissolve  
    mc "You certainly are!"
    scene fd_stand_react1_pan19
    sam"Thanks"
    scene fd_stand_react1_pan18
    $ renpy.pause ()
    scene fd_appt_m_react3 with dissolve        
    mc"Well whatever their loss. It'll just have to remain one of those unsolved mysteries."
    scene fd_appt_mc_sit_flust100000 with dissolve  
    sam"Okay,"
    scene fd_appt_mc_sit_flust100001 with dissolve  
    sam"Well,"  
    if DevCom == 1:
        show grim1
        gc"One of the issues I noticed in a lot of other Daz3d games is characters can sometimes have very 'dead' expressions I tried to make them look very expressive here."
        hide grim1       
    scene fd_appt_mc_sit_flust100002 with dissolve   
    sam"I mean..." 
    scene fd_appt_mc_sit_flust2100 with dissolve
    $ renpy.pause ()
    scene fd_appt_m_react8 with dissolve
    "Clearly a little uncomfortable she squirms in her seat"
    scene fd_appt_mc_sit_flust2_camera with dissolve   
    sam"Okay so in high school there were, these girls who were always making stuff up and spreading these nasty rumours about me."
    scene fd_appt_mc_sit_flust2b00028 with dissolve   
    sam"and it kind of just scared off all the guys"
    scene fd_appt_mc_sit_flust2b00029 with dissolve       
    sam"Then there was college..."
    scene fd_appt_mc_sit_flust100017 with dissolve   
    sam"And I was so busy with my studies and never had time for dates"
    scene fd_appt_mc_sit_flust100015 with dissolve
    sam"and there's now, and I'm busy working to pay off my student loans"
    scene fd_appt_mc_sit_flust100016 with dissolve
    sam"{size=-10}*So many student loans*{/size}"
    scene fd_appt_mc_sit_flust100018 with dissolve  
    sam"And that's basically of my life summed up, I guess I never found time for boys"
    scene fd_appt_m_react5 with dissolve  
    mc"Well I'll help you make up for lost time."
    if DevCom == 1:
        show grim2
        gc"It was around here I realized I was doing a new render for almost every line of dialogue and that it was perhaps a little overkill"
        hide grim2      
    # mc"Well none of that matters now and I can help you make up for lost time."
    scene fd_appt_mc_sit_flust100019 with dissolve  
    sam"{size=-9}*Giggles*{/size} Yeah..."
    scene fd_appt_mc_sit_flust100022 with dissolve  
    sam"umm so you know I have {b}never{/b} brought someone back to my place after a first date before"
    scene fd_appt_m_react3 with dissolve
    python:  
        if MC.upper() == "MC" :
            namer = 1
        elif MC.upper() == "GUY" :   
            namer = 2
        else : 
            namer = 0

    if namer == 1 :
        mc"Well don't you just know how to make me feel like the {i}main character{/i}." ## possibly a funny pun if default name
    elif namer == 2 :
        mc"Well don't you just know how to make this {i}Guy{/i} feel special"  
    else : 
        mc"Well don't you know how to make a guy feel special"  

    scene fd_appt_mc_sit_flust100020 with dissolve 
    sam"Gosh this is just moving so quickly"
    #mc touches sam's hand or something in a reassuring way
    scene fd_appt_mc_sit_flust_g22 with dissolve 
    mc"Hey"
    scene fd_appt_mc_sit_flust_g23 with dissolve 
    mc"Hey, we don't have to do anything you don't want to do"
    #bits lip
    jump kiss

label kiss:   
    scene horny
    sam"Yeah but..."
    scene fd_appt_mc_sit_flust100026 with dissolve 
    sam"I {b}do{/b} want to"
    scene fd_appt_mc_sit_flust100028 with dissolve
    sam"But maybe, do you think we could uh start by kissing{w} a little?"
    scene fd_appt_mc_laugh02 with dissolve 
    mc"*Chortle*"
    scene fd_appt_mc_laugh03 with dissolve 
    mc"How do you kiss just a little?"
    scene fd_appt_mc_sit_flust2b_camera4_31 with dissolve 
    sam"Hey shut up!"
    scene fd_appt_mc_sit_flust2b_camera4_33 with dissolve    
    sam"{size=-10}it's just{w} I'm shy okay?{/size}"
    scene horny2
    sam"I told you I'm...{w} {size=-10}{b}new{/b} at this.{/size}"
    scene fd_appt_mc_sit_flust2b_camera4_35 with dissolve
    mc"*Chuckles* Alright I'm sorry come sit next to me and I'll make it up to you"
    scene fd_appt_mc_sit_flust2b_camera4_36 with dissolve
    $ renpy.pause ()   
    scene fd_appt_mc_sit_flust2b_camera5_39 with dissolve
    mc"We can start by getting nice and close"
    scene fd_appt_mc_sit_flust2b_camera5_38 with dissolve
    sam"oh!"
    mc"Like this"
    sam"{size=-10}{b}Yeah{/b}"
    mc"Then lean and-{nw}"
    scene fd_appt_kiss_new00001 with dissolve
    $ renpy.pause ()
    scene fd_appt_kiss_new00003 with dissolve
    $ renpy.pause ()
    scene fd_appt_kiss_new00004 with dissolve    
    "*Mwwwa*"
    scene fd_appt_kiss_new00005 with dissolve
    sam"*hmmm*"
    scene fd_appt_kiss_new00006 with dissolve    
    $ renpy.pause ()
    scene fd_appt_kiss_new00007 with dissolve 
    mc"How was it?"
    scene fd_appt_kiss_new00000 with dissolve   
    sam"{size=-10}{b}wow{/b}"   
    sam"Good"  
    mc"Again?"
    sam"{size=-10}{b}Yes please{/b}"      
    scene fd_appt_kiss_new_3rd00000 with dissolve    
    $ renpy.pause ()
    scene fd_appt_kiss_new_3rd00001 with dissolve    
    $ renpy.pause ()
    scene fd_appt_kiss_new_3rd00002 with dissolve    
    $ renpy.pause ()
    scene fd_appt_kiss_new_3rd00003 with dissolve    
    $ renpy.pause ()
    scene fd_appt_kiss_new_3rd00004 with dissolve    
    $ renpy.pause ()
    scene fd_appt_kiss_new_3rd00005 with dissolve    
    "Smooch"
    scene fd_appt_kiss_new_3rd00006 with dissolve    
    sam"(´｡• ᵕ •｡`)"
    scene fd_appt_kiss_new_3rd00007 with dissolve    
    $ renpy.pause ()
    if DevCom == 1:
        show grim2
        gc"I've seen in other games POV kissing looks a little to much like 'duck face' so added a third person render to I hope improve the scene."
        hide grim2 
    scene fd_appt_kiss_new00001 with dissolve    
    mc"You're already a natural."
    mc"Well there you have it your {i}little{/1} kiss was what you were hoping for?"
    scene fd_appt_kiss_new00009 with dissolve 
    sam"{size=-10}{b}Yeah! but...{/b}"            
    scene fd_appt_kiss_new00010 with dissolve   
    sam"You know I'm not {i}so{/i} naive I was actually kind of...{size=-5}hoping...{/size}"
    $ renpy.end_replay()


label blowjob: 
    scene fd_appt_mc_offer_emb00011 with dissolve   
    mc"Oh yeah?"
    scene fd_appt_kiss_new00011 with dissolve   
    sam"Well you know do you think maybe...{w} {size=-5}maybe I could just look at your{/size}{w} {size=-10}{b}dick{/b}{/size}?"
    scene fd_appt_mc_offer_emb00012 with dissolve   
    mc"Just look at it huh?"
    scene fd_appt_sam_offer_emb_camera with dissolve       
    sam"Gah that sounded less weird in my head."
    scene fd_appt_mc_offer_emb00013 with dissolve     
    mc"I'm just teasing I get ya.{w} it's my best feature anyways."
    scene fd_appt_sam_offer_emb_camera with dissolve  
    mc"let me just get undressed first."
    scene fd_appt_sam_offer_emb_camerab with dissolve      
    sam"{size=-10}{b}Yay!{/b}"

    scene fd_appt_mc_undress0_camera with dissolve  
    $ renpy.pause ()   
    scene fd_appt_mc_undress100001 with dissolve   
    $ renpy.pause ()     
    scene fd_appt_mc_undress100002 with dissolve       
    sam"Thanks [MC]"
    scene fd_appt_mc_undress100003 with dissolve     
    mc"Hey don't get ahead of yourself haven't even seen it yet"
    scene reaction with dissolve      
    sam"No not this... {size=-5}well this too{/size} but for taking me out today and just being with me."
    sam"It's I know I'm pretty shy but around you it's worse, I say stupid things, trip over my words and get embarrassed"
    scene fd_appt_mc_undress00007 with dissolve  
    sam"Or flustered and I just start talking without {size=-10}thinking{/size} {size=-11} or,{/size} {size=-15} how to,{/size} {size=-20}stop...{/size}"
    scene shock
    "And with that, she is truly at a loss for words."            
    scene fdn3 with dissolve 
    "You can almost see the gears turning in her head."
    scene fdn5 with dissolve       
    "Without a word she starts to move"
    scene fdn6 with dissolve     
    sam"I can touch it right?"
    scene fdn7 with dissolve    
    mc"Well you weren't going to stop at just looking"
    scene fd_appt_mc_undress00004
    "She wastes no time"
    scene handy1
    "She looks really focused"
    $ renpy.pause () 
    sam"*mmmm*"
    $ renpy.pause () 

    scene lowkiss
    "Then She starts to lean in"
    scene fdn3117 with dissolve 
    sam"*Mooch*"
    scene fdn10 with dissolve 
    sam"MWaaah"
    scene fdn8 with dissolve 
    sam"{size=-16}Wow{/size}."  
    scene fdn11 with dissolve 
    sam"it's better, so much better than I thought!"
    scene fdn12 with dissolve 
    sam"You're already so hard and...{w} and {size=+10}{b}big{/b}{/size}."
    scene fdn16 with dissolve 
    sam"and the way the veins are throbbing its perfect{w} you're perfect."
    "Now you're at a loss for words you've never had a girl flatter you so much."
    scene fdn15a with dissolve 
    sam"It makes my mind go blank"
    scene fdn13 with dissolve 
    mc"Well...{w} do you want to continue your 'kisses'?"
    scene fdn14 with dissolve 
    sam"Desperately."

    $ renpy.end_replay()
    scene fd242a with dissolve
    "She moves in closer"
    scene nuzzle1 with dissolve
    "It almost looks like she nuzzles your cock"
    scene nuzzle2 with dissolve    
    sam"God it's intoxicating"

    $ renpy.end_replay()
    scene lowlick
    $ renpy.pause () 
    # scene fdn115a with dissolve
    # #pause .3
    # $ renpy.pause ()  
    # scene fdn115b with dissolve
    # $ renpy.pause ()  
    # scene fdn115c with dissolve
    # $ renpy.pause ()  
    # scene fdn115d with dissolve
    # $ renpy.pause ()  
    # scene fdn115e with dissolve
    # $ renpy.pause ()  
    # scene fdn115f with dissolve
    # $ renpy.pause ()  
    # scene fdn115g with dissolve
    # $ renpy.pause ()  
    # scene fdn115h with dissolve
    # $ renpy.pause ()  
    # scene fdn115i with dissolve
    # $ renpy.pause ()  
    # scene fdn115j with dissolve
    # $ renpy.pause ()  
    # scene fdn115k with dissolve
    # $ renpy.pause ()  
    # scene fdn115l with dissolve
    # $ renpy.pause ()  
    # scene fdn115m with dissolve
    # $ renpy.pause () 
    # scene fdn115p with dissolve
    # $ renpy.pause ()         
    # scene fdn115q with dissolve
    # $ renpy.pause ()  
    # scene fdn115p with dissolve
    # $ renpy.pause ()         
    # scene fdn115q with dissolve
    # $ renpy.pause ()  
    # scene fdn115p with dissolve
    # $ renpy.pause ()         
    # scene fdn115q with dissolve
    # $ renpy.pause ()  

    scene lowlick2
    $ renpy.pause () 
    sam"*Mwaah*"
    scene lowlick3
    $ renpy.pause () 

    scene fdn115kk with dissolve
    mc"Ready?"
    if DevCom == 1:
        show grim1
        gc"I mentioned this on twitter before but I've never played a porn game unmuted so I did not know what was expected sound-wise"
        gc"Ultimately I kept the game silent, not ideal but I have no method for creating sound effect, I thought it better be left for a future project."
        hide grim1
    scene fdn100b with dissolve
    sam"{size=-16}Yes{/size}."   

    scene fdn101a
    $ renpy.pause ()  
    scene fdn102a
    $ renpy.pause ()  
    scene fdn103a
    $ renpy.pause ()  
    scene fdn104a
    $ renpy.pause ()  
    scene fdn106a
    scene blow1
    sam" *Luuup*"  
    $ renpy.pause () 
    sam" *Shluck*"
    $ renpy.pause () 
    sam" *Slurp*" 

    # scene fdn101a
    # $ renpy.pause ()  
    # scene fdn102a
    # $ renpy.pause ()  
    # scene fdn103a
    # $ renpy.pause ()  
    # scene fdn104a
    # $ renpy.pause ()  
    # scene fdn106a
    # $ renpy.pause ()      
    # scene fdn105a
    # $ renpy.pause ()  
    # scene fdn107a
    # $ renpy.pause ()  
    # scene fdn107bba
    # sam" *Luuup*"  
    # scene fdn107bbb
    # $ renpy.pause ()  
    # scene fdn107bba
    # $ renpy.pause ()  
    # scene fdn107a
    # sam" *Schlop*" 
    # scene fdn106a
    # $ renpy.pause ()  
    # scene fdn107a
    # $ renpy.pause ()  
    # scene fdn107bba
    # $ renpy.pause ()  
    # scene fdn107bbb
    # $ renpy.pause ()  
    # scene fdn107bba
    # sam" *Shluck*"
    # scene fdn107a
    # $ renpy.pause ()  
    # scene fdn106a
    # $ renpy.pause () 
    # scene fdn107a
    # $ renpy.pause ()  
    # scene fdn107bba
    # sam" *Slurp*" 
    # scene fdn107bbb
    # $ renpy.pause () 

    scene fdn108
    "For someone so shy just a minute ago she is doing an amazing job"
    "though you can see she to be struggling to get any deeper"
    scene fdn109
    $ renpy.pause ()   
    scene fdn110
    pause .6  
    scene fdn111                              
    $ renpy.pause ()   
    scene fdn105a
    scene licknew
    ##$ renpy.movie_cutscene("fdn112.mkv")
    $ renpy.pause ()   
    scene fd_blow_mouth100000
    sam"Wow" 
    scene fd_blow_mouth100001
    pause .90  
    scene fd_blow_mouth100002

    sam"It's so big" 
    scene fd_blow_mouth100003 with dissolve  
    sam"But I don't think I can take it all, it's too much!" 
    mc"You're doing great just relax your throat why don't we try it again."
    scene fd_blow_mouth100001
    sam"okay..."
    scene fd_blow_mouth300000 with dissolve 
    "[sam] hops right back on." 
    scene fd_blow_mouth300001
    $ renpy.pause ()
    scene fd_blow_mouth4pov00001 with dissolve 
    $ renpy.pause ()
    scene fd_blow_mouth4pov00000 with dissolve   
    "and gets stuck at about the same spot."
    scene fd_blow_mouth400003 with dissolve 
    mc"Why don't I help you out."
    scene fd_blow_mouth4pov00002 with dissolve 
    sam"Mmmm?"
    scene fd_blow_mouth4pov00003 with vpunch 
    $ renpy.pause ()
    scene fd_blow_mouth400002 with vpunch 
    "[sam] is caught a little off guard"
    if DevCom == 1:
        show grim2
        gc"The game was originally going to have two paths a dominance and a romance path, ultimately i scraped it due to my poor writing skills"
        gc"however this scene remains pretty much the last hints of it."
        hide grim2     
    scene fd_blow_mouth400001 with vpunch 
    $ renpy.pause ()
    scene fd_blow_mouth5bpov00000 with vpunch 
    $ renpy.pause ()
    scene fd_blow_mouth5bpov00001 with dissolve 
    sam"Hmmnnh"
    scene fd267 with dissolve 
    $ renpy.pause ()
    scene fd268 with dissolve 
    $ renpy.pause ()    
    scene fd_blow_mouth400000 with dissolve 
    sam"*Gags*"
    scene fd_blow_mouth5bpov00002 with dissolve 
    mc"There we go a break through!..."
    mc"You okay?"
    scene fd_blow_mouth5bpov00003 at Shake((0,0,0,0), .8, dist=3)
    sam"♡ Ymm Hmmmm ♡"
    "Her attempt at speaking send vibrations down your shaft."
    scene fddt16
    mc"Fuck, that feels amazing [sam]."
    scene fddt15
    $ renpy.pause ()
    scene fddt14
    $ renpy.pause ()
    scene fddt13
    $ renpy.pause ()   
    scene fddt12
    $ renpy.pause ()                  
    scene deep1
    $ renpy.pause ()    
    sam" *moaning*"
    # scene fd266 with dissolve 
    # sam" *moaning*"
    # scene fd269 with dissolve 
    # $ renpy.pause ()
    # scene fd270 with dissolve 
    # $ renpy.pause ()
    # scene fd271 with dissolve 
    # $ renpy.pause ()
    # scene fd270 with dissolve 
    # $ renpy.pause ()
    # scene fd266 with vpunch 
    # $ renpy.pause ()
    # scene fd269 with dissolve 
    # $ renpy.pause ()
    # scene fd270 with dissolve 
    # $ renpy.pause ()
    # scene fd271 with dissolve 
    # $ renpy.pause ()
    # scene fd266 with vpunch 
    $ renpy.pause ()
    if DevCom == 1:
        show grim3
        gc"This was some if the final remade scenes, Originally I wasn't going to but as the rest of my renders imrpoved it started to stick out too much."
        hide grim3         
    menu:
        "Come down throat":
            scene deep1a
            "You ram your cock down her throat one final time"
            mc"Fuuuuck"
            scene fd_mouth100009 with flash 
            $ renpy.pause(delay = 0.5, hard = True)
            scene fd_mouth100010 with flash  
            $ renpy.pause(delay = 0.5, hard = True)
            scene fd_mouth100011 with flash 
            $ renpy.pause ()
            scene fd_mouth100012 with dissolve 
            sam"*Coughing*"
            mc"I'm sorry are you all right?"
            mc"I guess I got carried away"
            scene fd_mouth100013 with dissolve 
            sam"*Bwaa*"
            scene fd_mouth100014 with dissolve 
            sam"*Phew* No, that was awesome."
            scene fd_mouth100015 with dissolve
            sam"Just a little intense{w} maybe we can take a little break? so I can catch my breath."  
            scene fd290mm with vpunch  
            "Yeah actually even I'm a light headed from that." 
        "Come in mouth":
            mc"Oh Fuck babe I'm about to come!"
            scene fd_mouth100008 with dissolve  
            $ renpy.pause ()
            scene fd_mouth200007 with dissolve              
            $ renpy.pause ()
            scene fd_mouth200009 with dissolve   
            $ renpy.pause ()
            scene fd_mouth200009 with vpunch 

            $ renpy.pause ()
            scene fd_mouth100012 with dissolve  
            $ renpy.pause ()
            scene fd_mouth100017 with dissolve    
            mc"Did you swallow it?"
            scene fd_mouth100018 with dissolve    
            sam"Nuh uh"
            scene fd_mouth100024c with dissolve   
            sam"Bwaah" 
            mc"Fuck that's hot."
            scene fd_mouth100022 with dissolve   
            sam"ope"
            scene fd_mouth100013 with dissolve   
            sam"Ahhh."
            scene fd_mouth100019 with dissolve   
            sam"All gone."
            mc"Good girl."
            scene fd_mouth100020 with dissolve   
            sam"{size=-16}Thanks{/size}."
            scene fd_mouth100015 with dissolve
            sam"That was a lot more in intense than I though it would be I think I need to catch my breath."  
            scene fd290mm with vpunch  
            "You and me both I feel light headed from that." 
    scene fd290m with dissolve
    $ renpy.pause ()    
    scene fd280a with fade  
    sam"You know I've never done anything like that before."
    mc"No?{w} Hey scooch over I need a sit down too."   
    scene fd281a with dissolve        
    sam"hmmm"
    scene fd280c with dissolve        
    mc"That was amazing. You are amazing."
    scene fd280b with dissolve     
    sam"Thanks I've been wanting that for a long time."
    scene fd281a with dissolve 
    "She's never given a blowjob before? or maybe the technique?"
    "Would it be mood killer to ask for clarification?"
    scene fd280b with dissolve  
    sam"I wish I could say like this forever."
    scene fd280c with dissolve    
    mc"You really enjoyed it that much?"
    scene fd280b with dissolve      
    sam"Are you kidding? That was the most incredible thing that's ever happened to me,"
    "God this girl might give me a complex if she keeps this up."
    sam"I've never really liked it here, but with you here maybe I wont be so..."
    sam"Ah It feels like a dream come true"
    scene fd280c with dissolve    
    mc"I never thought we would do this on a first date."
    scene fd280b with dissolve 
    sam"Me neither."
    jump sex   

label sex:

    if isknown == 0 and istrap == 1:   
        scene fd_base_p_disco_suprise00000 with dissolve 
        "It was just a Blowjob but she looks like she is in pure bliss."
        "Though come to think on it, yeah I guess this was pretty much my ideal 'date' too."
        "Almost"
        "Maybe I should push my luck..."
        scene fd_base_mc_disco_suprise101 with dissolve
        mc"If you're up for it, I'd love to take things a little further."
        scene fd_base_p_disco_suprise00001 with dissolve ##Need an Original Render for this
        "She looks frightened at the idea"
        scene fd_base_mc_disco_suprise102 with dissolve
        mc"Sorry I'm pushing too much forget I said that"
        scene fd_base_p_disco_suprise1a00003 with dissolve
        sam"No I do really...{w} it's just..."   
        sam"Shit, I'm sorry [mc] maybe... maybe you should just go home"   
        scene fd_base_p_disco_suprise1a00004 with dissolve
        "She stands up"
        scene fd_base_p_disco_suprise_stand0001 with fade
        "Wow I really fucked up I thought things were going well but I guess I pushed too much"
        scene fd_base_p_disco_suprise_stand0002 with dissolve
        sam"*Sniffle"
        scene fd_base_p_disco_suprise_stand0003 with dissolve
        "Aw jeez she's crying?{w} way to go you turn a good date in to tears."
        mc"Hey [sam] I'm really sorry I didn't mean to push you like we can just call it a night I'll-"
        ## Turns to OP
        scene fd_300_blank_cry00009 with dissolve
        sam"I'm sorry [mc] I should have told you?"
        scene fd_300_blank_mc00012 with dissolve
        mc"Hey hey its okay, told me what?"
        scene fd_300_blank_cry00013 with dissolve
        sam"Promise you wont hate me?"
        "Uh oh"
        scene fd_300_blank_mcc00022 with dissolve
        mc"Hey look at me, I promise."
        scene fd_300_blank_cry00011 with dissolve
        sam"Sigh...okay."
        scene fd_300_blank_cry00011 with dissolve
        sam"you see those girls that were spreading rumours about me in high school"
        scene fd_300_blank_cry00018 with dissolve
        sam"Well they...{w} they weren't all lies"
        scene fd_300_blank_mcc00027 with dissolve
        "Wait"
        scene fd_300_blank_cry00017 with dissolve
        sam"I mean I'm a {i}girl{/i}"
        scene fd_300_blank_mcc00028 with dissolve
        "Hold on"
        scene fd_300_blank_cry00013 with dissolve
        sam"It's just that"
        sam"Ugh I really like you [mc] you were so nice to me."
        scene fd_300_blank_cry00010 with dissolve
        sam"But I...{w} I have a Cock"
        scene fd_mc_react_shock00004 with dissolve                 
        mc"Ssss-"
        scene fd_300_blank_crya00027 with dissolve                 
        sam"{b}Wait{/b} I promise I'm a girl but-"
        scene fd_mc_react_shock00005 with dissolve                    
        mc"When were you planning on tell me this?"
        scene fd_300_blank_crya00023 with dissolve                    
        sam"I'm sorry [MC] I wasn't thinking and things were moving so fast and-"
        scene fd_300_blank_crya00028 with dissolve                    
        sam"Please don't hate me [mc]{w} please I'm sorry"
        scene fd_300_blank_crya00031 with dissolve                    
        sam"Maybe you can just think of it like a really big clit?"
        show fd301sfp:
            subpixel True
            yalign 1.0
            linear 6.0 yalign 0.0    
        $ renpy.pause ()  
        scene fd_mc_react_shock0008 with dissolve                    
        mc"is this how you normally break the news?"
        scene fd_300_blank_crya00026 with dissolve                 
        sam"...{b}No!{/b} {size=-10}I mean I haven't...{/size}"
        scene fd_300_blank_crya00029 with dissolve                 
        sam"[mc] I'm still a virgin"
        sam"you're my first... anything [mc]"
        scene fd_300_blank_crya00030 with dissolve                 
        sam"please [mc] don't leave I..."
        ##sam"It's just I'm getting too old to still be a {b}virgin{/b} {size=-10}and you are so cute{/size} {size=-12}and I thought we were having such a good time{/size}"
        sam"I...{w} I just {b}need{/b} to feel you please."        
        ##sam"I...{w} I just {b}need{/b} you to bury your cock in me please"
        sam"I'm so wet just for you I just" 
        scene fd_300_blank_mcc00024 with dissolve                    
        mc"wait hold o-"
        sam"please? *whimpers*"
        scene fd304a with dissolve
        sam"Look I can prove I'm a girl you can...{w} fuck my tits!...{w} please!"
        sam"they are nice and big and- *Mmmm*"
        scene fd304c with dissolve
        sam"see!?"
        sam"*squirms*"
        sam"It's just you're so big and-"

        scene newpan1:  
            subpixel True
            yalign 1.0
            linear 6.0 yalign 0.0
        sam"I'm sorry, you were so nice to me, and I fucked up [mc] I'm sorry"        
        scene newpan3:  
            subpixel True
            yalign 0.0
            linear 6.0 yalign .7 
        sam"But I'm so pent up"
        sam"It's just your cock is so nice and you tasted {i}so good.{/i}"
        sam"I can't wait any longer."
        scene fd_300_nude00002 with dissolve                            
        sam"it's just, please will you {size=+10}{b}please{/b}{/size} just fuck me."
        scene fd_300_nude00001 with dissolve
        sam"I can cover it you don't even have to see my cock you can pretend its not there!"
        #"Hmm... ah fuck what the hell why not"
        scene fd_300_blank_mcc00029 with dissolve                    
        "{size=+10}{b}...{/b}{/size}"
        "Ah what the hell I've already come this far"
        scene fd_300_blank_mcc00030 with dissolve                    
        #you can see her desperation from still being a virgin 
        # her hips aching for it begging
        # Squirming in place
        #you grab her ass any spread her cheeks

    else:
        scene fd_base_p_disco_suprise00004 with dissolve 
        mc"Hey what's that book?"
        scene fd_base_p_disco_suprise00000 with dissolve 
        if DevCom == 1:
            show grim1
            gc"The game was originally written only for the DickGirl path but very quickly I decided to have both options and wrote the story variations in parallel."
            hide grim1  
        sam"hmm?"
        mc"The one under the chair it looks..."
        scene fd_base_p_disco_suprise00003 with dissolve 
        sam"oh shit"
        scene fd_base_p_disco_suprise00002 with dissolve 
        sam"[mc] wait!"
        scene fd_base_p_disco_suprise00005 with dissolve 
        mc"it looks almost like-"
        scene fd_base_p_disco_suprise00002a with dissolve 
        "[sam] tries to speak but nothing comes out"
        scene fd_base_p_disco_suprise00002b with dissolve 
        $ renpy.pause ()   
        scene fd_base_p_disco_suprise00006 with dissolve 
        mc"Yeah this is!{w} it's my Highschool yearbook"
        if DevCom == 1:
            show grim1
            gc"I don't know if it worked but my general idea with basically anything non essential was to make it purposely generic as to not draw attention away from our main characters."
            gc"so the grey background characters, the town name and high school book for example are all really unimportant there for left vague"
            hide grim1          
        scene fd286 with dissolve 
        mc"that's odd why would you have a..."
        scene fd286a with dissolve 
        mc"Didn't you say you moved here recently?"
        "She doesn't respond and when you turn to her you see."
        scene fd_300_blank_dry00000 with dissolve 
        "You can see she is upset"
        scene fd_300_blank_dry00002 with dissolve 
        sam"I didn't say when."
        "Slowly you are start to piece things together"
        scene fd_mc_react_shock00000b with dissolve 
        mc"Wait"
        scene fd_300_blank_dry00001 with dissolve 
        sam"[mc] please don't be mad at me?"
        mc"Please [sam] I could never-"
        scene fd_300_blank_cry00008 with dissolve 
        "And with that she bursts out crying"
        "Fuck I must have really struck a nerve, I should have just left the stupid book alone."
        ##sam"But{w} I have to tell you something... "
        mc"[sam] please don't cry"
        mc"Please uhh, deep breaths, just breathe and tell me what you have to say I wont be mad how could I ever"
        scene fd_300_blank_cry00009 with dissolve 
        sam"[mc] how can you always be so damn kind"
        scene fd_300_blank_cry00011 with dissolve 
        sam"*Exhales*"
        scene fd_300_blank_cry00012 with dissolve 
        sam"Okay, so... the coffee shop, it's not the first time we met"
        scene fd_300_blank_cry00015 with dissolve 
        sam"Do you remember third period in Ms. Wexler's class?"
        scene fd_mc_react_shock00000b with dissolve
        mc"yeah?... wait Yeah! I do remember I-"
        scene fd_mc_react_shock00001 with dissolve
        mc"wait so you were in that class? then you..."
        scene fd_mc_react_shock00000a with dissolve
        mc"WOAH, you look so...{w} different!"
        
        if istrap == 0 :
            scene fd_300_blank_cry00021 with dissolve
            sam"Listen none of the rumours where true I swear!"
            mc"what? course not I never thought for a secon-"
            scene fd_300_blank_cry00019 with dissolve
            sam"My dad just worked nights, I never when to Bangkok and I didn't even have a dog!"
            scene fd_mc_react_shock00007 with dissolve
            mc"[sam] you don't need to convince me I never believed any of it!"
            scene fd_300_blank_cry00017 with dissolve
            sam"You're just saying that, the cheer squad always told me-"
            scene fd_mc_react_shock00005 with dissolve
            mc"No they were lying like the always did"
            scene fd_300_blank_mc00008 with dissolve
            "God it was so long ago but I can see highschool is still eating at her everyday"
            "Kids are such dicks."  
            mc"Gosh I'm so sorry what you went through."  
            scene fd_300_blank_cry00018 with dissolve
            sam"You don't need to apologize [mc] you have {i}always{/i} the one person who has been nice to me"     
        elif istrap == 1 :
            scene fd_300_blank_crya00023 with dissolve
            sam"I'm sorry for tricking you like this I didn't mean to-"
            scene fd_300_blank_cry00012 with dissolve
            sam"[mc] do you remember the rumours about me back in school well they...{w} they weren't all lies"
            scene fd_300_blank_cry00010 with dissolve
            sam"I have a cock"
            scene fd_mc_react_shock00002 with vpunch
            $ renpy.pause ()  

            show fd301sfp:
                subpixel True
                yalign 1.0
                linear 6.0 yalign 0.0

            sam"I promise I can still be your girl maybe you can just think of it like a really big clit?"
            scene fd_300_blank_cry00013 with dissolve
            sam"I should have told you the moment you asked me out it's just..."
            scene fd_mc_react_shock00004 with dissolve
            sam"I didn't plan for us to get this {i}far{/i}, god it's still feels like a dream to me."
            mc"just- give me a second to think"
            scene fd_300_blank_cry00020 with dissolve
            sam"[mc] I'm sorry it's just you remember how they treated me in school I was scared you would-"
            scene fd_mc_react_shock00005 with dissolve
            mc"[sam] you know I would never do or say any of the nasty things they used to"
            scene fd_300_blank_cry00015 with dissolve 
            sam"I know [mc] you have always so nice to me I guess i've just gotten used to assuming the worst"


        sam"I think back on that sci-lab project we did when we got assigned partners"
        sam"You just treated me so nice, better than anyone else in the school, it was just so nice to be treated {i}normal{/i}"
        scene fd_300_blank_cry00017
        sam"It made me so happy even if the bullying got worse after that I could always think back to that week with you"
        scene fd_mc_react_shock00006 with dissolve
        "Jeez I barely remember that class had I know she was going through so much..."
        scene fd_mc_react_shock00007 with dissolve
        mc"Really I had no idea-"
        scene fd_300_blank_crya00024 with dissolve
        sam"You were such a nice guy to everyone but I was too scared to ever even try to talk with you again after that." 
        sam"I almost built up the courage one day but then I heard you were moving to go to that prestigious university"
        sam"It's selfish but I kind of resented everything for a while after that"
        scene fd_300_blank_mc00010 with dissolve
        sam"here we are years later I think I have finally built some confidence but then I say you again at the coffee shop, I felt was right back there all over again."
        sam"I got so nervous whenever you came in I could never say more then a few words"
        scene fd_300_blank_crya00025 with dissolve
        sam"But then just like back in school you approached me and not only that but a first date!"
        scene fd_300_blank_mc00010 with dissolve
        mc"[sam] I-"
        scene fd_300_blank_mc00009 with dissolve
        mc"... First?{w} [sam] have you? I mean, does this mean that you're a..."
        scene fd_300_blank_cry00006 with dissolve
        sam"God, [MC] don't make me say it... Yes"
        scene fd_300_blank_crya00023 with dissolve
        sam"but if you want maybe you{w}... maybe you can be my first?"
        "Oh fuck just hearing that gets you ticking again."
        scene fd_300_blank_mcc00023 with dissolve
        "On the other hand this is really quite a lot to drop on a first date maybe you shouldn't"
        scene fd_300_blank_mcc00024 with dissolve
        ##sam"but I'm getting way to old to still be a virgin [MC] and I really like you [MC] could you...{w} you now..."
        ##sam"would you like to be my first?{w} Please?"
        mc"[sam] I, this is so much to take in at once..."
        "I never knew she had it so hard and that I could have had such an impact on her life if only I had noticed I could have-"
        scene fd_300_blank_mcc00026 with dissolve
        sam"{size=-10}[MC] please?{/size}"        
        scene fd_300_blank_mcc00025 with dissolve
        "fuck how did you get undressed so fast!"
        scene fd304a with dissolve
        mc'F{sc=2}uuu{/sc}ck'
        scene fd304c with dissolve
        sam"{size=-10}please...{/size}"   
        scene fd305c with dissolve
        "Well I guess we i've been standing here naked too..."
        "God am I really going to do this? This is way more baggage than I expected."
        "Fuck this girl is crazy for me..."
        ## "I guess I {i}have{/i} to make it up to her now"

        if istrap == 1 :
            #show fd303p2:
            scene newpan1:  
                subpixel True
                yalign 1.0
                linear 6.0 yalign 0.0
        elif istrap == 0 :    
            #show fd303v1:
            scene newpan2:
                subpixel True
                yalign 1.0
                linear 6.0 yalign 0.0
        "Though judging by that look and her squirms of in almost desperation I don't think I could 'No' is even an option at this point."
        if istrap == 1 :
            #show fd303p2:
            scene newpan3:  
                subpixel True
                yalign 0.0
                linear 6.0 yalign .7
        elif istrap == 0 :    
            #show fd303v1:
            scene newpan4:
                subpixel True
                yalign 0.0
                linear 6.0 yalign .7      
        sam"It's just you're so big and-"

        sam"and I'm so wet for you ple-" 

    #mc"Why don't so start by bending over-"
    mc"Why don't so start by-"    
    "Her eyes light up"
    scene fd306b with dissolve
    sam"{size=+10}{b} YES!{/b}{/size}"
    scene fd306c with dissolve
    sam"Thank you"
    scene fd306 with dissolve
    sam"You have no idea how much this means to me!"
    scene transition with dissolve
    "She wastes no time and plonks herself down presenting herself to you"
    if istrap == 1 :
        scene fd456a with dissolve
        "God this is not how I thought this date was going to turn out"
        scene fd457 with dissolve
        "Not at all"
    elif istrap == 0 :   
        scene fd456va with dissolve
        "This is not how I thought this date was going to turn out"
        scene pussyplay
        "She seemed so shy not 20 minutes ago"
        "but I'm not complaining"


    menu:
        "Toe Sucking":
            $ isfoot = 1
            if istrap == 1 :
                scene fd458 with dissolve
                "While we are here I might as well start with her sexy feet"
                scene fd460a with dissolve
                mc"You have such cute feet I just want to kiss them all over"

            elif istrap == 0 :   
                scene fd_vback_start0b with dissolve
                "While we are here I might as well start with her sexy feet"
                scene fd_vback_start0 with dissolve
                mc"You have such cute feet I just want to kiss them all over"

            scene fd460 with dissolve
            sam"My feet? I never thought... what do you want to do with them?"
            if DevCom == 1:
                show grim1
                gc"I don't know what compelled me to add this I really don't understand the foot fetish so I hope this was sufficiently sexy."
                hide grim1               
            scene fd460a with dissolve
            mc"Why don't we start with some toe sucking first"
            sam"Okay"
            scene fd460d with dissolve
            mc"*Mwmmm*"
            scene fd460b with dissolve
            
            sam"Oh!"
            scene fd460c with dissolve
            sam"*mmmm*"
            scene toe1
            $ renpy.pause ()   
            scene fdlick06 with dissolve
            $ renpy.pause ()   
            scene fdlick07 with dissolve
            mc"*Schick*"
            scene fdlick08 with dissolve
            $ renpy.pause ()  
            scene fd_back_o_face006
            sam"*Oh mmm*"
            scene toe2
            $ renpy.pause ()  
            sam"Hehe it tickles"
            scene fd463 with dissolve
            sam"Wow"
            scene fd_back_orgasm_pull_pov106
            sam"I never thought feet were erotic before"
            scene fd_back_orgasm_pull_pov005
            sam"{cps=*100}I never thought feet were erotic before{/cps} but that was kinda hot [MC]"
            mc"Honestly I've never done that before either, maybe we can experiment more later."
            scene fd_back_orgasm_pull_pov105
            mc"Now on to the main event."
            if istrap == 1 :
                scene fd458 with dissolve
                jump sexp         
            elif istrap == 0 :   
                scene fd_vback_start0 with dissolve
                jump sexv



        "Skip":
            #penetrate

            if istrap == 1 :
                scene fd458 with dissolve
                jump sexp         
            elif istrap == 0 :   
                scene fd_vback_start0 with dissolve
                jump sexv

label sexp:

    $ renpy.pause () 
    scene fd466 with dissolve
    $ renpy.pause () 
    scene fd461 with dissolve
    $ renpy.pause () 
    scene fd467 with dissolve
    $ renpy.pause () 
    scene fdhelp8f with dissolve
    sam"*moan*"
    scene fd468 with dissolve
    $ renpy.pause () 
    scene fd469 with dissolve
    
    sam"Oh {sc}FUUUCK!{/sc}"
    scene fd470 with dissolve
    $ renpy.pause () 
    scene fdhelp8e with dissolve
    sam"Oh thank you!"
    sam"Oh god, thank you for fucking me"
    mc"We are just getting started"

    scene mission0
    $ renpy.pause () 

    scene mission1a
    $ renpy.pause () 

    menu:
        "faster":
            scene mission1
            sam"ohhhh"
            sam"Your cock feels so good in my pussy"
            sam"you're so big I can feel you {sc}stretching{/sc} me out"
            sam"I {b}god{/b} this already feels so {sc}gooood{/sc}"
            sam"Oh fuck, my cock is already leaking"
            scene fdj000 with dissolve
            
        "Side":
            scene mission1b
            sam"ohhhh"
            sam"Your cock feels so good in my pussy"
            sam"your so big I can feel you {sc}stretching{/sc} me out"
            sam"I {b}god{/b} this already feels so {sc}gooood{/sc}"
            sam"Oh fuck, my cock is already leaking"
            scene fdc009 with dissolve

    #this part needs major re-write and improvement to length 
    #more variety of text and stuff

    menu:
        "[MC] Jerks her off":   
            "Initially you were unsure about but now you get help but want to touch her dick"
            scene fdhelp10b
            $ renpy.pause ()    
            scene fdhelp11b
            mc"Why don't you let me help."       
            scene fd471cc   
            sam"{size=-10}Gasp{/size} Really!"
            mc"I want to make you feel good."
            scene fd471dd   
            sam"{size=-10}Thank you{/size}"
            scene sexjerk2
            $ renpy.pause () 
            sam"Oh fuck"
            $ renpy.pause () 
            sam"{sc}*uhggn*{/sc}"
            $ renpy.pause () 
            sam"It's so good!"
            menu:
                "[MC] sucks her off":   
                    scene fdblower01 
                    sam"No!"
                    scene fd_stop_blow1
                    sam"I'm so close"
                    scene fdblower01c
                    sam"Wait what are you"
                    scene fd_stop_blow2
                    mc"*Shhh*"
                    if DevCom == 1:
                        show grim1
                        gc"This is another fetish I added that does not appeal to me, but I wanted wanted to make the game appeal to people beyond just myself."
                        gc"I also wanted to make sure it it was very optional nothing worse than being forced into a fetish you don't enjoy"
                        hide grim1                      
                    #scene fdblower01a
                    sam"You don't have"
                    scene fd_stop_blow3
                    mc"*Shh* let it happen"
                    scene fd_stop_blow4
                    sam"{size=-14}Okay{/size}"
                    scene fdblower2 with fade
                    "Well no backing down now"
                    scene fdblow3d01
                    $ renpy.pause (.25) 
                    scene fdblow3d01a
                    $ renpy.pause (.25) 
                    scene fdblow3d01b
                    $ renpy.pause (.25) 
                    scene fdblow3d02
                    $ renpy.pause () 
                    scene fdblower3
                    sam"{size=-14}Woah{/size}"
                    scene blowher1
                    $ renpy.pause () 
                    scene fdblow3d0305
                    $ renpy.pause (.20) 
                    scene fdblow3d0306
                    $ renpy.pause (.20) 
                    scene fdblow3d0307
                    $ renpy.pause (.20) 
                    scene sexjerk3
                    sam"*Oohh*"
                    $ renpy.pause () 
                    sam"Yes!"
                    scene sexjerk3a
                    "Suddenly you feel a small hand gently pushing on your head"
                    "You must be doing it right then"
                    $ renpy.pause () 
                    sam"Ahh!"
                    "You feel her tense up"
                    scene fdblower6
                    sam"*hmmm*"
                    sam"{size=-14}[MC]{/size}"
                    scene fdblow3d05
                    "You speed up"
                    $ renpy.pause () 
                    scene sexjerk3c
                    $ renpy.pause () 
                    sam"Wait I'm gonna-"
                    scene fdblow3d05a
                    "Before she can finish you feel her hands and feet tense up while clamping on you"
                    scene fdblow3d05b
                    sam"{sc}FUUCK{/sc}"
                    scene fd_back_orgasm_pull_pov004 with fade
                    sam"Oh"
                    scene fd_back_orgasm_pull_pov005
                    sam"[mc] that was"
                    scene fdblow3d06
                    sam"Oh shit"
                    scene fdblow3d06a
                    sam"[mc] I'm sorry I lost control"
                    scene fdblow3d06b
                    sam"fuck I'm so sorry I should have warned you"
                    scene fdblow3d07a
                    sam"please [mc] I so sorry I didn't mean t-"
                    scene fdblow3d07b
                    $ renpy.pause () 
                    scene fdblow3d07c
                    $ renpy.pause () 
                    scene fdblow3d07d
                    "You gently squeeze her mouth open"
                    scene fdblow3d07e
                    sam"Ahhh"
                    scene fdblow3d08
                    $ renpy.pause () 
                    scene fdblow3d09
                    "*Blep*" 
                    scene fdblow3d09a
                    $ renpy.pause () 
                    scene fdblow3d09f
                    $ renpy.pause () 
                    scene fdblow3d10
                    $ renpy.pause () 
                    scene fdblow3d10a
                    $ renpy.pause () 
                    scene fdblow3d10b
                    $ renpy.pause () 
                    scene fdblow3d10c
                    $ renpy.pause () 
                    scene fdblow3d11
                    sam"Thank you"
                    scene fdblow3d11a
                    sam"{size=-14}*Gulp*{/size}"
                    if DevCom == 1:
                        show grim1
                        gc"I don't mean to kink shame anyone but this was really hard for me to make as it kind of repulsed me really not into the whole cum swapping but I did it for {b}you{/b} ♡ ."
                        gc"I hope I made it good enough for those who are into it."
                        hide grim1                       
                    scene fdblow3d07
                    sam"So-"
                    scene fdblow3d11b
                    $ renpy.pause () 
                    scene fdblow3d11c
                    $ renpy.pause () 
                    scene fdblow3d12
                    "*Smooch*"
                    scene fdblow3d12a
                    $ renpy.pause () 
                    scene fdblow3d13a
                    mc"Now bend over"
                    sam"{size=-14}Yes Sir{/size}"

                    #cums
                "Move on": 
                    scene fdblower01 
                    sam"Wait no no!"
                    scene fd_stop_blow2
                    sam"don't stop I'm so close"
                    scene fd_stop_blow1
                    mc"*Shhh*"
                    scene fdblow3d07
                    sam"Please [MC] jus-"
                    "You give a wry smile"
                    scene fdblow3d11b
                    "and lean inwards her"
                    scene fdblow3d11c
                    mc"Greedy girl"
                    scene fdblow3d12
                    
                    "*Smooch*"
                    scene fdblow3d12a
                    $ renpy.pause () 
                    scene fdblow3d13a
                    mc"Come now bend over"
                    sam"{size=-14}Yes Sir{/size}"

            # scene fdhelp8e with dissolve   
            # sam"*Hmm*"
            # scene fdjerker09
            # sam"I think I liked yours better"
            # scene fdjerker10a
            # mc"You'll chance for more, we aren't finished yet{w} turn over"
            
            # sam"Okay"  



            # mc"Yeah do you like this?"
            # sam"Oh YES I love it"
            # mc"Does it make your little girlcock hard?"
            # sam" oh fuck"
            # sam" oh fuck yes"
            # sam" I'm leaking so much for you" 
            # sam" OH fuck"
            # sam" *moan*"
            # sam" please I'm so close already to cumming"
            # sam" please"
            # sam" please touch my cock"
            # sam" please just a little"
            # sam" oh fuck its leaking for you"
            # sam"no don't stop" 
            # sam"I promise you don't have to I just"
            # sam"you feel so good" 
            # sam"oh please cum in me I don't care I want your come to leak out of me"
            # sam"fuck me fuck me hard"
            # sam"oh thank you for touching it it feels so good"
            # sam"Thank you oh god oh christ"
            # sam"Moaning"
            # sam"I promise I will clean it up"
            # "*dazed from fuck*"
            # sam"thank you"


        "She Jerks off":
            scene fdhelp2 with dissolve
            #Need a ani of her holding her cock
            "Despite her covering her cock you can see she is practically bucking in to her hand."
            mc"[sam] I want you to touch yourself."
            scene fdhelp4 with dissolve
            sam"Really can I?"
            sam"I mean you are okay with that?"
            mc"Of course baby."
            scene fdhelp8d with dissolve
            sam"{size=-10}Okay.{/size}"
            scene sexjerk1d
            # $ renpy.pause () 
            # scene fd1jerk30 with dissolve
            $ renpy.pause ()  
            scene fd1jerk31 with dissolve
            $ renpy.pause ()  
            scene fd1jerk32 with dissolve
            $ renpy.pause ()  
            scene fd1jerk33 with dissolve
            $ renpy.pause ()  
            scene fd1jerk34 with dissolve
            $ renpy.pause ()  
            scene fd1jerk35 with dissolve
            $ renpy.pause ()  
            scene sexjerk1e
            $ renpy.pause ()  
            #scene sexjerk1
            #$ renpy.pause () 
            #scene sexjerk1a
            #$ renpy.pause () 
            scene sexjerk1b
            $ renpy.pause () 
            scene sexjerk1c
            $ renpy.pause () 
            menu:
                "[MC] Jerks her off":  
                    "Initially you were unsure about her dick but you let the intrusive thoughts win."
                    scene fdj105a
                    $ renpy.pause ()    
                    scene fdj105b
                    mc"Why don't you let me help."       
                    scene fdhelp8c   
                    sam"{size=-10}*ahh*{/size}"
                    scene fdhelp8d   
                    sam"{size=-10}Thank you{/size}"
                    scene sexjerk2
                    $ renpy.pause () 
                    sam"Oh fuck"
                    $ renpy.pause () 
                    sam"{sc}*uhggn*{/sc}"
                    $ renpy.pause () 
                    sam"It's so good!"
                    scene fdhelp8e with dissolve   
                    sam"*Mmmm*"       
                    scene sexjerk2a    
                    "I can feel her cock tensing up... maybe shes close to-"
                    scene fdhelp3
                    sam"Oh fuck [MC] Im-"
                    scene fdjerker02a with flash 
                    $ renpy.pause(delay = 0.5, hard = True)
                    scene fdjerker02b with dissolve
                    $ renpy.pause(delay = 0.5, hard = True)
                    scene fdjerker02c with flash
                    $ renpy.pause(delay = 0.5, hard = True)
                    scene fdjerker02d with dissolve 
                    "Fuck"
                    "She came buckets"
                    mc"Woah you really ca-"
                    scene fdjerker03d with dissolve
                    $ renpy.pause () 
                    scene fdjerker03e with dissolve
                    $ renpy.pause () 
                    scene fdjerker03b with dissolve
                    $ renpy.pause () 
                    mc"Shit"
                    scene fdjerker03c with dissolve
                    sam"*Giggles* Wow"
                    scene fdjerker03g with dissolve
                    sam"I've never cum so much before!"
                    scene fd_mclook000
                    mc"{size=-10}ya don't say{/size}"
                    scene fdjerker03f with dissolve
                    sam"Uh could you get me a towel"
                    scene fd_mclook000 
                    $ renpy.pause (.5) 
                    scene mclook
                    mc"Oh right uhh."
                    sam"In the bathroom door to your right."
                    scene fd_mclook006
                    mc"Right" 
                    scene fdjerker10 with fade
                    mc"Got it" 
                    scene fdjerker04
                    "God she really is covered"
                    scene fdjerker04c
                    sam"Thanks"
                    scene fdjerker04d
                    $ renpy.pause () 
                    scene fdjerker05
                    $ renpy.pause () 
                    scene fdjerker06
                    $ renpy.pause () 
                    scene fdjerker07
                    sam"Some extra"
                    scene fdjerker08
                    $ renpy.pause () 
                    scene fdjerker08b
                    $ renpy.pause () 
                    scene fdjerker08a
                    $ renpy.pause () 
                    scene fdjerker08f
                    sam"*Hmm*"
                    scene fdjerker09
                    sam"I think I liked yours better"
                    scene fdjerker10a
                    mc"You'll have chance for more, we aren't finished yet{w} turn over"
                    
                    sam"Okay"
                "Move on": 
                    scene sexjerkfin
                    $ renpy.pause () 
                    scene fd_back_o_face004
                    sam"Oh fuck!"
                    "*You pull out*"
                    scene fd_back_o_face002
                    sam"Are you done?"
                    scene fd_back_o_face003
                    sam"I mean it doesn't feel like you fin-"
                    "You lean in"
                    scene fd471a
                    mc"Relax"
                    scene backKiss
                    "*Smooch*"
                    scene fd471b
                    mc"We are just getting started"
                    mc"Now bend over for me."
       
        "Move on":    
            if isknown == 0: 
                scene fd_pback_mc0
                "*Wince*"
            elif isknown == 1: 
                scene fd_pback_mc1
                "*Wince*"                
                    # #you slow down
                    # scene fdhelp8e
                    # $ renpy.pause () 
                    # scene fd468
                    # $ renpy.pause () 
                    # scene fd467
                    # $ renpy.pause () 
                    # scene fd466
                    # $ renpy.pause () 
                    # scene fdhelp8f
                    # sam"hmm?"
                scene pback_penhold
                $ renpy.pause () 
                scene fdhelp4
                sam"What's wrong?"

            if isknown == 0: 
                mc"Please don't mention {i}that{/i}"
                scene fdhelp8
                sam"No don't stop I'm sorry please I wont ever mention it again"
                #light sobbing/tears
                scene fdhelp8a
                sam"I swear I'll be good... please"
                #resume
                scene fdhelp8c
                mc"It's alright its just... why don't you bend over for me then."
                scene fdhelp4
                $ renpy.pause () 
            elif isknown == 1: 
                mc"Sorry It's just, I'm still a little uncomfortable with you mentioning {i}that{/i}."
                scene fdhelp4
                sam"I'm sorry I didn't mean too"
                scene fdhelp6
                sam"...do you want to stop then?"

                mc"No it's fine can we just try a different position though."           


            ##sam"Thank you [MC] I'm sorry Its just, you made me feel so good"
            ##mc"You really a little nympho aren't you"
            scene fdhelp3c with dissolve
            sam"{b}Yes{/b} I can do that for you"
            
            # sam"Oh fuck"
            # sam"i'll {b}do{/b} anything for you"
            # sam"just please keep going"
            # sam"oh [MC] your so big I can barely take it"
            # sam"but,{w} but this feeling its so, so"
            # sam"sc}Ooohhhhh{/sc}"
            # sam"I can feel every inch of you inside of me"
            # sam"pounding me over and over"
            # sam"and i can feel it throbbing I can feel {i}you{/i} getting hard{w} getting closer"
    #scene fd308b with fade
    jump sexp2

label sexv:
    menu:
        "Go down on her":   
            scene fd_vback_present_0
            $ renpy.pause () 
            scene fd_vback_present_0a
            $ renpy.pause () 
            scene fd_vback_cum1a
            mc"Why don't we start with a finger"
            scene fd_vback_cum1
            $ renpy.pause () 
            scene Thumb1
            sam"You're such a tease"           
            menu:
                "Easy":     
                    scene FinTwo1 
                    sam"*Hmm*"
                    scene FinTwo2  
                    $ renpy.pause () 
                    "*Shlick*{w} *Shlick*{w} *Shlick*"
                    "She is already soaking wet"
                    scene fd_vback_cum4
                    $ renpy.pause () 
                    mc"Ready for some more stimulation"    
                    scene fdhelp8d
                    sam"Hmm?"
                    scene fd_vback_cum3
                    $ renpy.pause () 
                    scene Thumb2
                    sam"Oh fuck!"
                    $ renpy.pause () 
                    scene FinThree3b
                    $ renpy.pause () 
                    sam"Yes{w} Yes{w} Yes!"
                    scene fd_vback_cum_finger3rd_56  with vpunch
                    sam"oh{w} oh!{w} {sc}Fuuck{/sc}"
                    "She forced your head down thrusting you Tongue into her pussy"
                    scene fd_vback_squirt112 at Shake((0,0,0,0), 1.8, dist=3)    
                    sam"ah eeei!"
                    scene fd_backv_pen412
                    "finally she releases"
                    sam"*panting*"
                    sam"Oh god!"
                    "Clearly dazed you give her a second to catch her breath"
                    scene fdhelp4 with fade
                    # mc"I think I already know the answer but I take it you've never been tongue fucked before?"
                    # sam"nu uh"
                    # mc"So you liked it then?"
                    sam"Sorry I forced your head like that I guess I got carried away."
                    mc"Nah its fine, but I take it you enjoyed your first tongue fucking then?"
                    scene fdhelp7
                    #"in a shallow breath she speaks"
                    sam"{sc}Magical{/sc}"
                    # sam"Your kidding? your tongue, was {sc}Magical{/sc}"
                    scene fdhelp5
                    mc"Ready to go again?"

                    jump sexv1

                "Hard":                     
                    scene FinThree1 
                    $ renpy.pause (1.8) 
                    scene FinThree2   
                    "*Shlick*{w} *Shlick*{w} *Shlick*"
                    "She is already practically dripping wet"
                    sam"Ahh!"
                    scene FinThree3
                    $ renpy.pause () 
                    scene FinThree3a
                    $ renpy.pause () 
                    scene fd_vback_oralfin_005
                    $ renpy.pause (.3) 
                    scene FinThree4
                    $ renpy.pause () 
                    "Now just speed up and bring her to a-"
                    sam"mmmm"
                    scene fdhelp8f
                    sam"I'm Gonna-"
                    scene fdhelp8e

                    scene fd_vback_squirt104
                    sam"{size=+10}Oh Shit!{/size}"
                    scene fd_vback_squirt108
                    mc"wah-"
                    scene fd_vback_squirt109
                    sam"ahhh!"
                    scene fd_vback_squirt111
                    mc"*Blaa*"
                    scene fdhelp3
                    sam"[MC] I'm Sor-"
                    mc"*blurb* *blurb*"
                    $ renpy.pause () 
                    scene fd_back_o_face009a with fade
                    mc"It's fine though I wish I had know you were a squirter before"
                    if DevCom == 1:
                        show grim1
                        gc"Squirting is another fetish I added that I don't really understand the appeal, I hope it worked for those who like it."
                        hide grim1  
                    scene fd_back_o_face003
                    sam"I swear its never happ-"
                    sam"I mean when I masterb- I guess its just never this intense."
                    scene fd_back_orgasm_pull_pov108
                    sam"[mc] I really am sorry" 
                    scene fd_back_o_face010a
                    mc"Don't even worry, but uhh do you have a towel I can use?"
                    scene fd_back_o_face011
                    sam"Oh right, in the bathroom behind you"
                    mc"Alright I'll just be a moment stay right were you are."
                    scene fd_back_o_face012 with fade
                    mc"Well now that, that's sorted out"
                    mc"Where were we?"
                    scene fd_back_pen_00
                    sam"{size=-14}Umm the Sex?{/size}"
                    mc"Oh that's right! legs up missy"
                    scene fd_back_pen_01
                    sam"Yes Sir!"

                    jump sexv1



        "Straight to sex": 
            $ isoral = 1 
            jump sexv1
    

label sexv1:
    if isoral == 1 :
        scene vback_slap
        sam"*mmmmn*"
        scene fd_back_o_face003  with dissolve
        sam"You are such a tease"
        scene vback_pen111
        mc"Just getting you warmed up is all"
    elif isoral == 0 : 
        scene fd_back_o_face003 with dissolve
        mc"Now that your all warmed up"
        sam"Please I'm so ready"
        scene vback_pen111
        sam"Yes!"
        
    if DevCom == 1:
        show grim1
        gc"Maybe this is stupid but I'm pretty proud of that animation."
        hide grim1  
    scene fdhelp2
    sam"*Hnnnh*"
    scene missionpovv1
    sam"Oh fuck!"
    scene missionclose1
    $ renpy.pause ()  
    scene fd_pull_cut_01
    sam"AaaaAaa mnnn"
    scene fdhelp2
    $ renpy.pause ()      
    scene fdhelp8e
    $ renpy.pause ()  
    scene missionclose1
    $ renpy.pause ()      
    scene pen_top1
    $ renpy.pause ()  
    scene missionpovv2
    $ renpy.pause ()   

    if isoral == 1 :
        mc"(better pull out before I get too clo-)"
        "before you can react she goes quite"
        scene fd_back_o_face003
        mc"{size=-10}eip!{/size}"
        $ renpy.pause(delay = 0.5, hard = True)
        scene fd_back_o_face004 with flash
        $ renpy.pause(delay = 0.5, hard = True)
        scene missionwrapped with flash
        sam"Ohh FUUUCK!"
        "Suddenly she pulls you in close with her legs"
        "Moving her own hips on you to finish herself off"
        scene fd_back_orgasm_pull_pov000 with dissolve
        mc"You naughty little minx"
        scene fd_back_orgasm_pull_pov002 with dissolve
        mc"I was going to edge you a little longer but you pulled me in with your feet like a little monkey"
        scene fd_back_orgasm_pull_pov005 with dissolve
        sam"but like a cute monkey, right?"
        "(so quickly she seems to have learn how to push you just right)"
        scene backKiss
        "*Smooch*"
        scene fd_back_orgasm_pull_pov105 with dissolve
        mc"yup certifiably adorable"
        mc"Now get on your knees I still have another round in me"
        scene fd_back_orgasm_pull_pov004  with dissolve
        sam"Hnnn yes sir!"

        jump sexv2

        $ renpy.pause ()    
    elif isoral == 0 :   
        mc"(better pull out before I get too close)"
        scene vback_penhold   
        $ renpy.pause ()
        scene fdhelp4
        sam"But I was {sc}SO{/sc} close"
        mc"Now now, don't wanna get greedy gotta pace yourself"
        scene fdhelp8d
        sam"So we're not done?"
        mc"Come here"
        scene backKiss
        "*Smooch*"
        scene fd_back_orgasm_pull_pov105 with dissolve
        mc"Of course not, now lets see you on your knees"
        scene fd_back_orgasm_pull_pov004  with dissolve
        sam"Hnnn yes daddy"        

        jump sexv2

    # jump ending

    # sam"Oh fuck, Yes {b}Yes{/b} {b}{size=+10}YES!{/size}{/b}"
    # sam"I can feel you getting tense, getti-"
    # sam"you must be close!"
    # menu:
    #     "Come inside":
    #         $ iscumout = 0
    #         "TBA"
    #     "Come Outside":
    #         $ iscumout = 1
    #         "TBA"

label sexv2:
    scene fd_vdoggy_present_0a with fade
    sam"Like this?"
    mc"Perfect"
    if DevCom == 1:
        show grim1
        gc"Originally the game was going to be this position first then on her back but I thought the 'finish' animations looked better in this position"
        hide grim1      
    scene fd_pdoggy_penface_new_002a    
    mc"Absolutely beautiful"
    scene buttslap01
    $ renpy.pause ()  
    if DevCom == 1:
        show grim2
        gc"Really not happy with this animation but I couldn't get the hand and dick in sync."
        hide grim2       
    scene fd_pdoggy_penface_new_005a
    mc"You ready?"
    sam"Hmmm"
    scene vdoggypen
    $ renpy.pause ()  
    scene fd_pdoggy_penface_new_005
    sam"nggguu"
    scene vdoggy2
    $ renpy.pause ()  
    if DevCom == 3:
        show grim1
        gc"I tried mixing sounds and using sqiggle text to convey emotion but, really their are only so many variations."
        hide grim3      
    #scene vdoggy3
    #$ renpy.pause ()  
    scene vdoggy3c
    $ renpy.pause ()  
    scene doggyvunder
    $ renpy.pause ()  
    scene vdoggy3a
    $ renpy.pause ()       
    scene fd_pdoggy_penface_new_010
    $ renpy.pause ()  
    scene vdoggy3b
    $ renpy.pause () 
    if DevCom == 1:
        show grim1
        gc"The game game originally had completely separate and unique animations between each version however,"
        gc"after my third remake I realized it was just way to hard to get equally good looking renders for both as my animation skills basically made it random chance if they turned out"
        hide grim1  

    menu:
        "Pull her up":     
            scene vpullUp
            $ renpy.pause ()  
            scene fd_doggy_up_add00000
            $ renpy.pause ()  
            scene SidecloseU
            $ renpy.pause ()  
            scene Vside1
            $ renpy.pause ()  
            scene fd_doggy_up_v_base
            $ renpy.pause ()  
            ##scene fd_doggyv_up_add_camera
            ##"Animation Missing"
            menu:
                "Touch her":  
                    scene fd_doggyv_up_add_touch_1
                    sam"Wait its sensi-"
                    scene uptouch2
                    $ renpy.pause ()  
                    scene fd_doggyv_up_add_touch_2
                    sam"Ahhhhnn"
                    scene sideclose2v with fade
                    $ renpy.pause ()                          
                "Cont.":     
                    scene Upfront1
                    sam"ahhhnn"
                    scene sideclose2v
                    $ renpy.pause ()    
            menu:
                "Grab Neck":   
                    $ renpy.pause () 
                    scene fd445d
                    mc"you want it a little rougher?"
                    scene fd445  
                    sam"*mmm* Yes daddy"
                    scene VsideChoke
                    sam"Ah!"
                    scene VarialC
                    $ renpy.pause () 
                    sam"Are- are you close [mc]?"
                "Grab Mouth": 
                    scene fd445d
                    mc"let me give you something to suck on?"    
                    scene fd443c  
                    $ renpy.pause ()  
                    scene fd443d
                    sam"*mmm*"
                    scene VsideFinger
                    $ renpy.pause () 
                    scene Varialf
                    $ renpy.pause () 
                    mc"I'm Close"
                "Cont.":   
                    scene Varial
                    $ renpy.pause ()  
                    scene fd_doggy_up_kiss00000
                    mc"you are gorgeous babe"
                    scene fd_doggy_up_kiss00001
                    $ renpy.pause ()  
                    scene fd446
                    "*Smooch*"
                    scene fd447a with dissolve        
                    $ renpy.pause ()    
                    scene fd447b with dissolve     
                    $ renpy.pause () 
                    scene Varial2 
                    $ renpy.pause () 
                    sam"Are- are you close [mc]?"
            
            mc"*Grunting* [sam] Where do you want it?"            

            menu:
                "Come inside":    
                    sam"Oh please fill me!"
                    sam"with your hot load" 
                    scene fd_vdoggy_up_fin100000 with flash
                    sam"Ahhh!"
                    scene fd_vdoggy_up_fin100001 with flash
                    $ renpy.pause(delay = 0.9, hard = True)                   
                    scene fd_vdoggy_up_fin100002 with flash
                    $ renpy.pause(delay = 0.9, hard = True)
                    scene fd_vdoggy_up_in_close01
                    $ renpy.pause ()  
                    scene fd_vdoggy_up_in_close02
                    $ renpy.pause ()  
                    scene fd_vdoggy_up_in_close03a
                    $ renpy.pause ()  
                    scene fd_vdoggy_up_in_close04
                    $ renpy.pause () 

                    scene fd_vdoggy_up_fin200004
                    sam"*ngggh*"
                    sam"So full"
                    scene fd_vdoggy_up_in_close04a
                    "*Twitch*"                 
                    scene twitch
                    "*Twitch* *Twitch*" 
                    scene fd_vdoggy_up_in_close05
                    $ renpy.pause ()  
                    scene fd_vdoggy_up_in_close06a
                    "Sploosh"
                    scene fd_vdoggy_up_fin200007
                    sam"Oh Fuck"
                    mc"welp you {i}were{/i} full"
                    if DevCom == 1:
                        show grim1
                        gc"This is a little over the top maybe but I thought the finish inside option was a little plain otherwise compared to the outside option"
                        hide grim1                      
                "Come outside":  
                    $ iscumout = 2
                    sam"Oh please cover me"
                    sam"with your Sticky load"   
                    scene pullout1v                  
                    $ renpy.pause () 
                    scene backhand1
                    mc"Almost there" 
                    scene backhand2
                    sam"Yes!"
                    scene fd_vdoggyup_cum201 with flash
                    $ renpy.pause(delay = 0.22, hard = True)
                    scene fd_vdoggyup_cum201a with flash
                    $ renpy.pause(delay = 0.18, hard = True)
                    scene fd_vdoggyup_cum202a with flash
                    $ renpy.pause () 
                    scene fd_vdoggyup_cum203a 
                    sam"There is so much!"
                    scene fd_vdoggyup_cum204a 
                    sam"and it's so hot"
                    scene fd_upcumout018a with fade
                    sam"*Lick*"
                    mc"Didn't you get your fill earlier already?"
                    sam"but it tastes so good"
                    if DevCom == 1:
                        show grim1
                        gc"I tried to make sure that no path had seemingly less effort put into it, as I feel there is nothing worse then picking an option that locks you out of most content."
                        gc"well that and game over option in a sex game."
                        
                        hide grim1   
                    # scene fd_upcumout016
                    # mc"Hnn"
                    # scene fd_upcumout017
                    # $ renpy.pause ()  
                    # scene fd_upcumout017a
                    # $ renpy.pause ()
                    # scene fd_upcumout017b
                    # $ renpy.pause ()
                    # scene fd_upcumout017c
                    # $ renpy.pause ()
                    # scene fd_upcumout018a
                    # $ renpy.pause ()
                    # scene fd_upcumout018a
                    # sam"*Lick*"           

            $ renpy.pause ()  
        "Push her down":   
            "lets get some more leverage"
            scene fd448  with dissolve
            mc"Alright"
            scene fd449  with dissolve
            sam"Eep!"
            scene fd449b  with dissolve
            $ renpy.pause ()   
            scene fd450  with dissolve
            mc"Head down"
            scene legsupheaddown
            mc"Ass up"
            scene legsupheaddown1
            $ renpy.pause ()   
            sam"Aaaahh hhnng"   
            #legs dropRR
            #grab leg 
            scene vdownrotate
            $ renpy.pause ()   
            scene doggydown1
            $ renpy.pause ()   
            scene doggydownface
            $ renpy.pause ()   
            scene doggydown_alttouch
            $ renpy.pause ()   
            scene doggydownjill1
            $ renpy.pause ()            
            scene doggypov
            $ renpy.pause ()   
            menu:
                "Grab Hair":   
                    sam"*aghh* {size=-10}{b}deep{/b}{/size}"
                    scene fd_doggy_down_pov200000
                    mc"let me really show you how deep I can go"                    
                    scene doggydownface3
                    $ renpy.pause ()  
                    sam"*Ah* fuck! *hnnn*"
                    $ renpy.pause ()
                    sam"Are you close?"  
                "Grab Mouth":     
                    sam"*aghh* {size=-10}{b}deep{/b}{/size}"
                    scene fd_doggy_down_pov200000
                    mc"Deep? let me really show you how deep I can go"
                    scene doggydownface2
                    sam"Ah *gnnnnmh*"
                    $ renpy.pause ()
                    sam"Arn yng clooagh (Are you close)"  
                "Cont.":    
                    scene fd_doggy_down_face_200001
                    sam"Are you close?"
                    sam"I can feel you tensing up"  


            menu:
                "Come inside":
                    $ iscumout = 0
                    mc"Fuck!"
                    scene doggypovfin   
                    sam"Oh fuck yes! fill me with your Cum!"    
                    scene doggydownpulloutv
                    $ renpy.pause ()    
                    scene fd_vdoggy_down_spank_0000 with dissolve
                    $ renpy.pause () 
                    sam"I feel so full"   
                    menu:
                        "Spank":
                            scene vslapbutt
                            sam"eeik!"
                            mc"Sorry couldn't resist"
                            scene doggydownvspread1

                        "Don't":
                            mc"Lets get a closer look"
                            scene doggydownvspread2
                            $ renpy.pause () 
                    mc"Wow you {i}were{/i} full" 
                            
                    
                "Come outside":  
                    $ iscumout = 1
                    scene fd_doggy_down_pov200001                    
                    mc"Almost there" 
                    scene doggydownpulloutv2
                    sam"Yes! please cover me with your sticky load"
                    if isfoot == 1 :
                        scene doggydownJerk3v
                        $ renpy.pause () 
                        mc"hnnn"
                        sam"Yes Cum for me!"
                        scene doggypovfin2 
                    elif isfoot == 0 :                  
                        scene doggydownJerk1
                        $ renpy.pause ()                         
                        if DevCom == 1:
                            show grim3
                            gc"Another Late addition to the game."
                            gc"Again I don't find feet sexy and was going to leave it at the toe scene earlier but last minuite I realized I could fit this in."
                            gc"its not prefect but the game isnt a foot fetish focused game I hope it was good enough."
                            hide grim3                            

                        scene fdpulloutb017 at Shake((0,0,0,0), .8, dist=3)
                        mc"hnnn"
                        sam"Yes cum for me!"
                        scene doggypovfino with flash 
                    $ renpy.pause ()                   


    jump wrapup

label sexp2:
    scene transition with fade
    $ renpy.pause (1)  
    scene fd_pdoggy_present_0 with fade
    sam"Like this?"
    mc"Perfect"
    scene fd_pdoggy_penface_new_002a    
    mc"Absolutly beautiful"    
    scene buttslap01
    $ renpy.pause ()  
    if DevCom == 1:
        show grim3
        gc"Really not happy with this animation but I couldn't get the hand and dick in sync."
        hide grim3      
    scene fd_pdoggy_penface_new_005a
    mc"You ready?"
    sam"Hmmm"
    scene pdoggypen
    $ renpy.pause ()  
    scene fd_pdoggy_penface_new_005
    sam"nggguu"
    scene vdoggy2
    $ renpy.pause ()  
    if DevCom == 3:
        show grim1
        gc"I tried mixing sounds and using sqiggle text to convey emotion but, really their are only so many variations."
        hide grim3       
    #scene vdoggy3
    #$ renpy.pause ()  
    scene vdoggy3c
    $ renpy.pause ()  
    
    scene pdoggy4
    $ renpy.pause ()  
    scene doggypunder   
    sam"Nnnnngg"
    scene vdoggy3a
    $ renpy.pause ()       
    scene fd_pdoggy_penface_new_010
    $ renpy.pause ()  
    scene vdoggy3b
    $ renpy.pause () 
    if DevCom == 1:
        show grim1
        gc"Originally the game was going to be entirely first person First person but I found it limited my camera angle."
        gc"even still I tried to minimize the amount of Male face, balls and ass when possible as I figure you probably don't want to see that."
        hide grim1       
    menu:
        "Pull her up":     
            scene ppullUp
            $ renpy.pause ()  
            scene fd_doggy_up_add00000
            $ renpy.pause ()  
            scene SidecloseU
            $ renpy.pause ()  
            scene Pside1
            $ renpy.pause ()  
            scene fd_doggy_up_p_base
            menu:
                "Touch her":  
                    scene fd_doggyp_up_add_touch_1
                    sam"Wait its sensi-"
                    scene uptouch1
                    $ renpy.pause ()  
                    scene fd_doggyp_up_add_touch_2
                    sam"Ahhhhnn"
                    scene sideclose2p with fade
                    $ renpy.pause ()                     
                "Cont.":     
                    scene Upfront2
                    sam"Ahhhhnnm"
                    scene sideclose2p
                    $ renpy.pause ()  
            ##scene fd_doggyv_up_add_camera
            ##"Animation Missing"

            menu:
                "Grab Neck":   
                    $ renpy.pause () 
                    scene fd445d
                    mc"you want it a little rougher?"
                    scene fd445  
                    sam"*mmm* Yes daddy"
                    scene PsideChoke
                    sam"Ah!"
                    scene ParialC
                    $ renpy.pause () 
                    sam"Are- are you close [mc]?"
                "Grab Mouth": 
                    scene fd445d
                    mc"let me give you something to suck on?"    
                    scene fd443c  
                    $ renpy.pause ()  
                    scene fd443d
                    sam"*mmm*"
                    scene PsideFinger
                    $ renpy.pause () 
                    scene Parialf2
                    $ renpy.pause () 
                    mc"I'm Close"
                "Cont.":   
                    scene Parial
                    $ renpy.pause ()  
                    scene fd_doggy_up_kiss00000
                    mc"you are gorgeous babe"
                    scene fd_doggy_up_kiss00001
                    $ renpy.pause ()  
                    scene fd446
                    "*Smooch*"
                    scene fd447a with dissolve        
                    $ renpy.pause ()    
                    scene fd447b with dissolve     
                    $ renpy.pause () 
                    scene Parial2 
                    $ renpy.pause () 
                    sam"Are- are you close [mc]?"
            
            mc"*Grunting* [sam] Where do you want it?"            

            menu:
                "Come inside":    
                    sam"Oh please fill me!"
                    sam"with your hot load" 
                    scene fd_pdoggy_up_fin100000 with flash
                    sam"Ahhh!"
                    scene fd_pdoggy_up_fin100001 with flash
                    $ renpy.pause(delay = 0.9, hard = True)                   
                    scene fd_pdoggy_up_fin100002 with flash
                    $ renpy.pause(delay = 0.9, hard = True)
                    scene fd_vdoggy_up_fin200007
                    sam"So full"
                    scene fd_upcum02
                    mc"I bet"
                    scene fd_upcum03
                    $ renpy.pause () 
                    scene fd_upcum04
                    $ renpy.pause () 
                    scene fd_upcum06               
                    $ renpy.pause () 
                    scene fd_upcum07  
                    sam"*ngggh*"
                    scene fd_upcum09 
                    $ renpy.pause () 
                    scene fd_upcum10
                    $ renpy.pause () 
                    scene fd_upcum11
                    $ renpy.pause () 
                    scene fd_upcum12                
                    sam"Oh Fuck"
                    mc"welp you {i}were{/i} full"
                    menu:
                        "Spank":   
                            scene fd_upcum13
                            $ renpy.pause () 
                            scene fd_upcum14 with flash
                            sam"Eeip!"   
                            scene fd_upcum16
                            mc"Sorry I couldn't help myself"                            

                        "Don't":   
                            scene fd_upcum12   
                            $ renpy.pause () 
                            scene fd_vdoggy_up_fin200001      
                            sam"I think I need to lay down for a bit."        
                    
                "Come outside":  
                    $ iscumout = 1
                    sam"Oh please cover me"
                    sam"with your Sticky load"   
                    scene pullout1p                
                    $ renpy.pause () 
                    mc"I almost there" 
                    scene pullout2p   
                    sam"Yea?"
                    sam"Please Cum for me!"
                    scene fd_doggy_up_jerk_outc1_camera with flash
                    $ renpy.pause(delay = 0.22, hard = True)
                    scene fd_doggy_up_jerk_outc2_camera
                    $ renpy.pause(delay = 0.32, hard = True)
                    scene fd_doggy_up_jerk_outc3_camera with flash
                    $ renpy.pause(delay = 0.22, hard = True)
                    scene fd_doggy_up_jerk_outc4_camera
                    $ renpy.pause(delay = 0.32, hard = True)
                    scene fd_doggy_up_jerk_outc5_camera with flash
                    $ renpy.pause(delay = 0.22, hard = True)
                    scene fd_doggy_up_jerk_outc6_camera
                    $ renpy.pause ()
                    scene fd_vdoggy_up_fin200001
                    sam"It's so hot"

            $ renpy.pause ()  
        "Push her down":   
            "lets get some more leverage"
            scene fd448  with dissolve
            mc"Alright"
            scene fd449  with dissolve
            sam"Eep!"
            scene fd449a  with dissolve
            $ renpy.pause ()   
            scene fd450  with dissolve
            mc"Head down"
            scene legsupheaddown
            mc"Ass up"
            scene legsupheaddown1
            $ renpy.pause ()   
            sam"Aaaahh hhnng"   
            #legs dropRR
            #grab leg 
            scene pdownrotate
            $ renpy.pause ()   
            scene doggydown2
            $ renpy.pause ()   
            scene doggydownface
            $ renpy.pause ()  
            scene doggydown_alttouch
            sam"Nnnnngg" 
            scene doggydownJerk2
            $ renpy.pause ()            
            scene doggypov
            $ renpy.pause ()     
            scene fd_doggy_down_face_200001
            menu:
                "Grab Hair":   
                    sam"*aghh* {size=-10}{b}deep{/b}{/size}"
                    scene fd_doggy_down_pov200000
                    mc"let me really show you how deep I can go"                    
                    scene doggydownface3
                    $ renpy.pause ()  
                    sam"*Ah* fuck! *hnnn*"
                    $ renpy.pause ()
                    sam"Are you close?"  
                "Grab Mouth":     
                    sam"*aghh* {size=-10}{b}deep{/b}{/size}"
                    scene fd_doggy_down_pov200000
                    mc"Deep? let me really show you how deep I can go"
                    scene doggydownface2
                    sam"Ah *gnnnnmh*"
                    $ renpy.pause ()
                    sam"Arn yng clooagh (Are you close)"  
                "Cont.":    
                    scene fd_doggy_down_face_200001
                    sam"Are you close?"
                    sam"I can feel you tensing up"  


            menu:
                "Come inside":
                    $ iscumout = 0
                    mc"Fuck!"
                    scene doggypovfin   
                    sam"Oh fuck yes! fill me with your Cum!"    
                    scene doggydownpulloutp

                    $ renpy.pause ()    
                    scene fd_pdoggy_down_spank_0000 with dissolve
                    $ renpy.pause () 
                    sam"I feel so full"   
                    mc"Lets get a closer look"
                    scene doggydownpspread2
                    $ renpy.pause () 
                    mc"Wow you {i}were{/i} full" 
                            
                    
                "Come outside":  
                    $ iscumout = 1
                    scene fd_doggy_down_pov200001
                    mc"Almost there" 
                    scene doggydownpulloutp3
                    sam"Yes! please cover me with your sticky load"
                    if isfoot == 1 :
                        scene doggydownJerk3p
                        $ renpy.pause () 
                        if DevCom == 1:
                            show grim3
                            gc"Another Late addition to the game."
                            gc"Again I don't find feet sexy and was going to leave it at the toe scene earlier but last minuite I realized I could fit this in."
                            gc"its not prefect but the game isnt a foot fetish focused game I hope it was good enough."
                            hide grim3                         
                        mc"hnnn"
                        sam"Yes Cum for me!"
                        scene doggypovfin1 
                    elif isfoot == 0 :                     
                        scene doggydownJerk1
                        $ renpy.pause () 
                        scene fdpulloutb017 at Shake((0,0,0,0), .8, dist=3)
                        mc"hnnn"
                        sam"Yes Cum for me!"
                        scene doggypovfino with flash 
                    $ renpy.pause () 
                   




    jump wrapup

label wrapup:
    scene transition with fade
    "A few moments later"
    scene fd_mc_post3 with fade
    mc"Phew looks like we made quite a mess"
    if iscumout == 1:
        scene fd_cum_final_b:  
            subpixel True
            xalign 0.0
            linear 6.0 xalign .7 
        $ renpy.pause ()      

        if istrap == 1 and isfoot == 1:
            scene fd_cum_final_p2b
        elif istrap == 0 and isfoot == 1:
            scene fd_cum_final_v2b
        elif istrap == 1 and isfoot == 0:
            scene fd_cum_final_p2a1   
        elif istrap == 0 and isfoot == 0:
            scene fd_cum_final_v2a1                         

    elif  iscumout == 2:
        scene fd_cum_final_d:  
            subpixel True
            xalign 0.0
            linear 6.0 xalign .7  
        $ renpy.pause ()     

        if istrap == 1 and isfoot == 1:
            scene fd_cum_final_p2b
        elif istrap == 0 and isfoot == 1:
            scene fd_cum_final_v2b
        elif istrap == 1 and isfoot == 0:
            scene fd_cum_final_p2b1   
        elif istrap == 0 and isfoot == 0:
            scene fd_cum_final_v2b2 
           
    else:
        scene fd_cum_final_a:  
            subpixel True
            xalign 0.0
            linear 6.0 xalign .7  
        $ renpy.pause ()  

        if istrap == 1 and isfoot == 1:
            scene fd_cum_final_p2b
        elif istrap == 0 and isfoot == 1:
            scene fd_cum_final_v2b
        elif istrap == 1 and isfoot == 0:
            scene fd_cum_final_p2b1   
        elif istrap == 0 and isfoot == 0:
            scene fd_cum_final_v2b2    

    $ renpy.pause ()  
    scene fd_cum_final_face00002
    sam"hmmm..."
    scene fd_mc_post1
    mc"You don't mind if I use your shower do you?"
    scene fd_cum_final_face00001
    sam"Go ahead"
    scene fd_mc_post1
    mc"Care to join me?"
    scene fd_cum_final_face00000
    sam"I don't think I can move anymore"
    scene fd_mc_post2
    mc"Too bad, I guess that means you are too tired I discuss our next date then."
    sam"Huh!"
    scene fd_cum_final_face00003
    $ renpy.pause ()    
    scene fd_cum_final_face00004
    sam"Oh no! wait"
    if iscumout == 2:
        scene fd_final_up1
    else:
        scene fd_final_up1a
    
    sam"I'm up! I'm up!"

    mc"There's my girl"
    if iscumout == 2:
        scene fd_final_up2
    else:
        scene fd_final_up2a
        
    
    sam"So... a second date date?"
    "Too cute"
    if DevCom == 1:
        show grim3
        gc"I kind of got numb to what I was making at a point and lost all sense of what looked 'sexy', I hope I there were some good scene through out the game."
        hide grim3       
    scene fd_final_up3
    mc"I mean if your interested."
    scene fd_final_up3a
    sam"Duh!"
    scene fd_end05a with dissolve
    $ renpy.pause ()  
    scene fd_end06
    "Smooch"
    $ renpy.pause ()  
    scene fd_end06a
    $ renpy.pause ()  
    scene fd_end06b   
    $ renpy.pause ()  
    scene fd_end07
    $ renpy.pause ()  
    scene fd_end07a
    $ renpy.pause ()  
    if iscumout == 1:
        scene fd_end08
    else:
        scene fd_end08a
    $ renpy.pause ()  
    scene fd_end05a
    mc"we can plan it while we shower"
    scene transition with fade
    "The End"
    if DevCom == 1:
        show grim1
        gc"And that concludes the Commentary track, thanks for listening to my ramblings I hope they were insightful,"
        gc"If I didnt answer any questions you had feel free to message me on my {a=https://www.subscribestar.com/grimciri}SubscribeStar Or my {a=https://f95zone.to/members/grimciri.541897/}F95 Account"
        gc"as a little bonus here are some old outdated scenes that are still in code (there are also of plenty of un-used renders if you dig through the files.)"
        hide grim1   
        menu:
            "Old BJ":
                jump oldbj
            "Old HJ":
                jump oldhj
            "Old Date scene (Text only)":
                jump date_old
            "No I don't want to see any of this.":
                jump ending

    jump ending

label ending:
    window show
    scene 999end1 with dissolve:
        xzoom 0.5 yzoom 0.5
    $ persistent.completed_game = True
    $ renpy.save_persistent()
    "Thank you {sc}SO MUCH{/sc} for playing my game!"
    "I hope you enjoyed it"
    "This was my first making making an erotic game it was a lot of fun to make!"
    scene 999end3 with dissolve:
        xzoom 0.5 yzoom 0.5    
    "I'm not completely happy with how my dialogue flowed at times, writing was far more challenging than I thought it would be"
    "If you have any {b}feedback{/b} or {b}criticism{/b} please share it with me on my {a=https://www.subscribestar.com/grimciri}SubscribeStar{/a}"
    scene 999end2 with dissolve:
        xzoom 0.5 yzoom 0.5
    "This was also my first time using Daz 3D... I still have much to learn about this program."
    "I am very sorry not all the renders turned out great"
    "I hope with what I've learned there will be less mistakes and better animations in future"
    "In hindsight I should have watched, like, literally {i}any{/i} tutorials before starting this project"
    scene 999end3 with dissolve:
        xzoom 0.5 yzoom 0.5
    "Again and {b}tips{/b} or {b}feedback{/b} to improve is greatly appreciated at {a=https://www.subscribestar.com/grimciri}SubscribeStar{/a}"
    scene 999end1 with dissolve:
        xzoom 0.5 yzoom 0.5
    "I will take any feedback to heart to improve on my next game!"
    scene 999end4 with dissolve:
        xzoom 0.5 yzoom 0.5
    "Thank you again!"
    scene 999end6 with dissolve :
        xzoom 0.5 yzoom 0.5   
    "I love you all and be excellent to each other!"
    scene transition with fade
    $ renpy.pause ()  
    scene shower with fade
    "{sc=2}The End For Real{/sc}"
    $ renpy.pause ()  
    return

label date_old:

    mc"Man, this theater hasn't changed a bit. Still as sketchy as ever."
    sam"Oh you've been here before?"
    mc"Yeah, I grew up around here. I had to leave after high school because I got accepted into my dream university on the east coast. It was hard to leave, but it led me to my dream job."
    sam"So why are you back now? Did you miss it here? Ya homesick?"
    mc"Ha, maybe a little. Actually, I'm technically here for a business."
    menu:
        "Tech Job":
            mc"My company is looking to open a new semiconductor fabrication plant and I'm on the team to help find a location."    
            mc"see the location is really important because at this scale even the smallest variations in things like access to water for cooling or the cost of electricity during surge hours make a hug-"
            sam"Semiconductor fabrication? What's that?"
            mc"Oh sorry I guess I'm boring you with the unimportant details I got a little carried away."
            sam"No, it's interesting. I like that you have a job you're so passionate about. Beats working at a dead-end coffee shop."
            mc"Hey, baristas are cool. They're like coffee artists. Espresso wizards, even."
            sam"*giggles* No way. I can barely make latte art. Sarah has to do all of that. But let's talk about something else, I'd rather hear more about you."
            mc"Sure where was I now?"
            sam"Why you were back in town."
            mc"Oh right, so my company makes computers and we're looking for a new location for our second lab. Lo and behold, my hometown is on the shortlist. I took the assignment to scout it out, but it also gave me an excuse to visit the old place again."
            sam"So was this date just an excuse to check out our run-down theater?"
            mc"*laughs* No, this date was all for you. But now that you mention it, maybe I can write it off as a business expense. You could be a local consultant. and.... Kidding."# winks
        "Artist Job":
            mc"See I'm actually a writing a new novel, are you familiar with the 'The Crime Chronicles' series?"
            sam"Oh yeah I think I have heard of that aren't they like super popular?"
            mc"Well I don't know about that but thank you."
            mc"Well I'm writing my newest book in the series 'The Shadowy Figure' and the plot takes up to a town similar to home so I thought I would return here for inspiration"
            sam"So then what this one going to be about?"
            mc"Well Detective Williams series is presented with case unlike anything she's encountered before."
            mc"A string of violent crimes are takes place across the city, with no discernible link between them, Sarah struggles to find a lead well all of a sudden she meets this-"
            mc"Hmmm I've said too much already, its bad luck to talk about a book before its finished."
            sam"Awe you tease!"
            mc"Tell I will send you an early copy when its finished"
    mc"So are you a local girl then?"
    sam"Yup lived all my life in this 100 mile bubble."
    sam"I know the dinner like the back of my hand though finishing a movie when there is still daylight is a new experience for me."
    mc"Sorry again about the timing I really wanted to take you out to dinner and a movie but our head office is in Taiwan and they've got us working weird hours"
    mc"what am I saying I shouldn't be making excuses,"    
    sam"It's fine. I had a good time. Don't worry about it."
    mc"Now that we've walked the block twice, what's next?"
    sam"Oh, Well maybe I should be going home I need to catch anyways."
    mc"You didn't drive here after work? Ugh, I feel so stupid. I should have picked you up. Please Let me drive you home."
    sam"No, it's okay."
    mc"No, I insist. I can't let myself get away with being such a dickhead."
    sam"*giggles*Okay, then. Thank you."

    jump ending

label oldhj:
    scene fd228 with dissolve   
    "And with that, she is truly at a loss for words."
    scene fd228a with dissolve  
    "You can almost see the gears turning in her head."
    scene fd228b with dissolve      
    "Without a word she starts to move"
    scene fd229 with dissolve    
    sam"I can touch it right?"
    scene fd230 with dissolve    
    mc"Well you weren't going to stop at just looking"
    "She wastes no time"
    scene fd231 with dissolve   
    $ renpy.pause ()
    scene fd232 with dissolve   
    $ renpy.pause ()
    scene fd233 with dissolve   
    $ renpy.pause ()
    scene fd232 with dissolve   
    $ renpy.pause ()
    scene fd231 with dissolve   
    $ renpy.pause ()
    scene fd232 with dissolve   
    $ renpy.pause ()
    scene fd233 with dissolve                   
    sam"*mmmm*"
    scene fd232 with dissolve   
    $ renpy.pause ()
    scene fd231 with dissolve  
    $ renpy.pause ()   
    scene fd234 with dissolve    
    "She starts to lean in"
    scene fd235 with dissolve  
    $ renpy.pause ()  
    scene fd237 with dissolve          
    sam"*Mooch*"
    scene fd240c with dissolve 
    sam"MWaaah"
    scene fd239 with dissolve 
    sam"{b}Wow{/b}"
    scene fd240 with dissolve
    sam"it's better, so much better than I thought!"
    scene fd240 with dissolve 
    sam"You're already so hard and...{w} and {size=+10}{b}big{/b}{/size}."
    scene fd241 with dissolve 
    sam"and the way the veins are throbbing its perfect{w} you're perfect."
    "Now your at a loss for words you've never had a girl flatter you so much."
    scene fd241d with dissolve
    sam"It makes my mind go blank"
    scene fd241e with dissolve
    mc"Well do you want to continue your 'kisses'?"
    scene fd241f with dissolve
    sam"Desperately."   
    jump ending

label oldbj:
    scene fd244 with dissolve
    $ renpy.pause ()  
    scene fd245a with dissolve
    "she looks at you seemly expecting you to tell what to do next"
    mc"ready?"
    sam"mmmhmm"
    scene fdt101 with dissolve
    $ renpy.pause () 
    scene fdt102 with dissolve
    $ renpy.pause () 
    scene fdt103 with dissolve
    $ renpy.pause () 
    scene fdt104 with dissolve
    sam" *Schlop*"
    scene fdt105 with dissolve
    $ renpy.pause ()   
    scene fdt106 with dissolve
    sam" *Shluck*" 
    scene fdt107 with dissolve
    $ renpy.pause ()   
    scene fdt109 with dissolve
    sam" *Luuup*"  
    scene fdt110 with dissolve
    $ renpy.pause () 
    scene fdt111 with dissolve
    $ renpy.pause () 
    scene fdt110 with dissolve
    sam" *Shluck*" 
    scene fdt109 with dissolve
    mc"Your tongue is incredible."
    scene fdt110 with dissolve
    $ renpy.pause () 
    scene fdt109 with dissolve
    sam" *Slurp*" 
    scene fdt110 with dissolve
    $ renpy.pause () 
    scene fdt109 with dissolve
    $ renpy.pause () 

    scene fdt107 with dissolve
    $ renpy.pause () 
    scene fdt105 with dissolve
    $ renpy.pause () 
    scene fdt101 with dissolve
    $ renpy.pause () 
    sam"Mmm you taste so good"

    scene fd245 with dissolve
    $ renpy.pause ()  
    scene fd247 with dissolve    
    $ renpy.pause ()  
    scene fd251 with dissolve  
    $ renpy.pause ()  
    scene fd252 with dissolve  
    $ renpy.pause ()      
    scene fd251 with dissolve  
    $ renpy.pause ()  
    scene fd250 with dissolve  
    $ renpy.pause ()  
    scene fd249a with dissolve  
    $ renpy.pause ()     
    scene fd249 with dissolve  
    $ renpy.pause () 
    scene fd249b with dissolve  
    $ renpy.pause () 
    scene fd250 with dissolve  
    $ renpy.pause () 
    scene fd252 with dissolve  
    $ renpy.pause () 
    scene fd251 with dissolve  
    $ renpy.pause ()  
    scene fd250 with dissolve  
    $ renpy.pause ()  
    scene fd252 with dissolve  
    $ renpy.pause () 
    scene fd253 with dissolve  
    $ renpy.pause () 
    scene fd256 with dissolve  
    sam"Wow" 
    scene fd256b with dissolve  
    jump ending


# label sex2:

#     scene dickslap1
#     $ renpy.pause () 


#     scene blow2
#     $ renpy.pause () 
#     scene deep1
#     $ renpy.pause () 

#     scene pdog1
#     $ renpy.pause () 
#     scene pdog2
#     $ renpy.pause () 
#     scene pdog3
#     $ renpy.pause () 


#     scene fd456 with dissolve

#     $ renpy.pause ()  

#     scene mission0
#     $ renpy.pause () 

#     scene mission1a
#     $ renpy.pause () 
#     menu:
#         "faster":
#             scene mission1
#             $ renpy.pause ()  

#         "Closer":
#             scene mission1b
#             $ renpy.pause ()  

#     menu:
#         "Jerk 01":
#             scene fdj105 with dissolve
#             $ renpy.pause ()   
#             scene sexjerk1
#             $ renpy.pause ()  
#         "Jerk 02":
#             scene fdj105 with dissolve
#             $ renpy.pause ()   
#             scene sexjerk2
#             $ renpy.pause ()  
#         "Change Pos":
#             scene pdog1
#             $ renpy.pause ()  

#             scene pdog1
#             $ renpy.pause ()      
#             scene pdog2
#             $ renpy.pause ()      
#             scene pdog3
#             $ renpy.pause ()     


# you look so sexy like that
# You Like that?
# Good Girl
# You feel good
# ahnnn
# Mhph!
# Aaahnn
# her hole squeezes firm 
# Grasping each inch
# Nnh-nfaah
# Her hole tightens around your cock
# Jolt of pleasure
# tight squeeze at hearing that
# Whimper
# Ahh, thats it!
# tits bounce
# Hips smacking against her ass
# Keep going I can take it
# I need this
# My ass feels soo good
# you make me feel so good
# I love it 
# I love you
# so do you think we can do this again sometime
# I'm yours 
# please breed me
# yes use me as you please
