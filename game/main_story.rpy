rpy monologue single

label chapter_1:
    # $ nar("In this video game, you will be transported to a fantastic world full of magic, brave warriors, and above all, a real academy for adventurers! You will play the role of a student at the -Dungeon Academy-, the most prestigious academy for adventurers on the entire continent. Your dream: to become the greatest adventurer of all time!")
    """
    In this video game, you will be transported to a fantastic world full of magic, brave warriors, and above all, a real academy for adventurers!
    You will play the role of a student at the -Dungeon Academy-, the most prestigious academy for adventurers on the entire continent.\nYour dream: to become the greatest adventurer of all time!
    """

    # CHOOSE ABILITIES
    "We will now define your abilities scores."
    python:
        score_array = [15, 14, 13, 12, 10, 8]
        for ability in ABILITIES:
            narrator(f"Choose your {ability} score:")
            choices = []
            for score in score_array:
                choices.append((str(score), score))
            choice = renpy.display_menu(choices)            
            Player.set_ability(ability, choice)
            score_array.remove(choice)

    "Your adventure begins."
    scene road1
    alt """
    The background image portrays an enchanting cobblestone street, bathed in twilight's ethereal glow. A gentle mist weaves through the air, softening the outlines of stone buildings lining the thoroughfare.
    Warm light spills from lanterns and windows, casting a golden hue that dances upon the stones. People traverse this dreamlike avenue, their forms hazy and mysterious in the fog-laden atmosphere."
    """
    window hide
    pause
    """
    You walk with a light step as you make your way down the tree-lined path that leads to your dream destination: the Academy! You inhale deeply the fresh morning air as you scan the horizon. Yes, it's a beautiful day.
    The best of all: your first day of academy.\nYou left early to avoid the risk of being late.
    In fact, waiting outside the academy would be a wonderful moment. Will you perhaps meet future classmates there? Will they become friends and valuable allies for the years to come at the academy, or even lifelong companions?
    As you think about these things, staring up at the sky, something trips you up and you fall heavily to the ground, your face smacked against the stone-paved path.
    """
    c "Ahi!"
    "You pick yourself up, a bit confused, trying to figure out what you had tripped over: a small white-haired female creature is in front of you, crawling next to a backpack and some fallen books. With one hand, she is now rubbing her head."
    p "{i}(A gnome girl?){/i}"

    menu:
        "I'm so sorry... I didn't see you at all!":
            $ Ciry.approval += 10
            "(Unknown's approval: +10)"
        "Hey! Watch out!":
            pass

    # scene bg room
    show ciry at topleft with dissolve
    alt """
    A portrait image appears, showing a young female character with big eyes and a gentle smile. Her long, flowing white hair is elegantly gathered at the top, secured by a single braid that winds around the locks.
    Pointed ears hint at a non-human race, adding an air of mystery and otherworldliness. The character wears a golden armor adorned with intricate detailing—an ensemble befitting high rank or noble status.
    """
    c """
    Hehe, my fault, sorry! I'm a bit clumsy and I always end up dropping things...
    I am Ciry, by the way...
    """
    p "Well, I'm "

    python:
        Player.sheet.name = renpy.input("ENTER YOUR NAME:", length=32)
        Player.sheet.name = Player.sheet.name.strip()
        if not Player.sheet.name:
            Player.sheet.name = "Lite"

    p "[Player.sheet.name]"
    c "Nice to meet you, [Player.sheet.name]!"
    c "You are a..."
    
    $ race_choice = "Human"
    menu:
        "Human\n+1 to all abilities":
            $ race_choice = "Human"
            $ Player.sheet.dexterity += 1
            $ Player.sheet.charisma += 1
            $ Player.sheet.constitution += 1
            $ Player.sheet.strength += 1
            $ Player.sheet.wisdom += 1
            $ Player.sheet.intelligence += 1
        "Half-Elf\n+2 Charisma\nChoose two other +1":
            $ race_choice = "Half-Elf"
            $ Player.sheet.dexterity += 1
            $ Player.sheet.charisma += 2
        "Half-Orc\n+2 Strength\n+1 Constitution":
            $ race_choice = "Half-Orc"
            $ Player.sheet.constitution += 1
            $ Player.sheet.strength += 2
        "Dwarf\n+2 Constitution\n+1 Wisdom)":
            $ race_choice = "Dwarf"
            $ Player.sheet.wisdom += 1
            $ Player.sheet.constitution += 2
        "Halfling\n+2 Dexterity\n+1 int)":
            $ race_choice = "Halfling"
            $ Player.sheet.intelligence += 1
            $ Player.sheet.dexterity += 2
        "Elf\n+2 Dexterity\n+1 int)":
            $ race_choice = "Elf"
            $ Player.sheet.intelligence += 1
            $ Player.sheet.dexterity += 2
        "Gnome\n+2 Intelligence\n+1 Constitution)":
            $ race_choice = "Gnome"
            $ Player.sheet.constitution += 1
            $ Player.sheet.intelligence += 2
        "Tiefling\n+2 Charisma\n+1 Intelligence)":
            $ race_choice = "Tiefling"
            $ Player.sheet.intelligence += 1
            $ Player.sheet.charisma += 2

    $ Player.race = race_choice
    if race_choice == "Half-Elf":
        "Choose your first stat bonus (+1)"
        $ first_bonus = ""
        menu:
            "Strength":
                $ Player.sheet.strength += 1
                $ first_bonus = "Strength"
            "Dexterity":
                $ Player.sheet.dexterity += 1
                $ first_bonus = "Dexterity"
            "Constitution":
                $ Player.sheet.constitution += 1
                $ first_bonus = "Constitution"
            "Intelligence":
                $ Player.sheet.intelligence += 1
                $ first_bonus = "Intelligence"
            "Wisdom":
                $ Player.sheet.wisdom += 1
                $ first_bonus = "Wisdom"

        "Choose your second stat bonus (+1)"
        menu:
            "Strength" if first_bonus != "Strength":
                $ Player.sheet.strength += 1
            "Dexterity" if first_bonus != "Dexterity":
                $ Player.sheet.dexterity += 1
            "Constitution" if first_bonus != "Constitution":
                $ Player.sheet.constitution += 1
            "Intelligence" if first_bonus != "Intelligence":
                $ Player.sheet.intelligence += 1
            "Wisdom" if first_bonus != "Wisdom":
                $ Player.sheet.wisdom += 1

    $ Player.save_json()           

    c "...[race_choice], aren't you?"
    if race_choice == "Gnome":
        c "I didn't expect to meet a fellow Gnome like this, hihihi!"
        c "You know, Gnomes like us are quite rare in the City..."
    """
    You reach out your hand to help her up, but she doesn't notice it, completely busy picking up her precious
    books and scattered pages of handwritten notes.
    """
    menu:
        "Wait, I'll help you":
            $ Ciry.approval += 10
            "You pick up a book and you read the title with surprise: 'Basics of the adventure'"
            p "I know this book! I've read it three times!"
            "(Ciry's approval: +10)"
            p "Wait, are you..."
        "Try to ignore her":
            pass

    c "(smiling) I'm going to Dungeon Academy. This is my first year!"
    p "Cool! I'm going there too! Firt year, first day."
    c "We can walk together to the academy!"
    p "(surprised) Oh.. Ok, sure!"
    c "Sooo, I'm so excited for my first day! What class are you gonna take?"
    p "Hmmm... I'm not sure yet."
    p "I think I'll try to be a..."

    # "### THIS CHOICE WILL NOT AFFECT Player CLASS ###"
    $ class_choice = ""
    menu:
        "Ranger":
            $ class_choice = "Ranger"
            
        "Paladin":
            $ class_choice = "Paladin"

        "Wizard":
            $ class_choice = "Wizard"
        
        "Fighter":
            $ class_choice = "Fighter"
            
        "Cleric":
            $ class_choice = "Cleric"

        "Barbarian":
            $ class_choice = "Barbarian"

        "Sorcerer":
            $ class_choice = "Sorcerer"
            
        "Warlock":
            $ class_choice = "Warlock"

        "Bard":
            $ class_choice = "Bard"
    
    if class_choice == "Cleric":
        "A Cleric, really? Just like me!"
    else:
        c "[class_choice] is a good class, I'd definitely need one in my party."
        p "And what about you?"
        c "Oh, I'm gonna be a Cleric. I decided it years ago."
    c """
    The Cleric has always been my favourite class!
    She can Heal, fight, use magic to defend or attack!
    A Cleric is so adaptable to any circumstance, she must be solid, realiable, and she often is the pivot around
    which all the party revolves."
    And this is the reason why a Cleric should also be well prepared, she must study a lot to get to know the
    strengths and weaknesses of each other class in order to coordinate the party's actions in the best way!
    """
    p "Wow, ehm, that amazing Ciry! You know a lot of stuff."
    p "And it's clear that you really love and admire the Cleric class."
    "And so, talking with your new friend, you go on walking toward the Academy."

    # python:
    #     p("My attack bonus is: " + str(Player.get_attack_bonus()))
    #     c("My attack bonus is: " + str(Ciry.get_attack_bonus()))
    #     Player.save_json()
    
    scene courtyard
    alt """
    The background changes.
    The background image depicts a vast, grand hall filled with a large crowd of people.
    The architectural style of the hall is gothic, characterized by tall, pointed arches, and intricate stonework.
    The hall is bathed in a soft, ethereal light streaming through high windows, creating a majestic atmosphere.
    The crowd, composed of individuals with diverse appearances, is gathered,
    suggesting an important event or ceremony is taking place.
    The overall scene exudes a sense of reverence and awe, enhanced by the grandeur of the surroundings.
    """
    $ renpy.save("autosave")
    pause
    
    "The school courtyard is so full of people you are astounded."
    "So many students waiting there, talking in little groups here and there."
    show ciry at topleft with dissolve
    c "(noticing you expression) These are students from all the classes, all the years."
    p "Why are there so many groups lining in front of those tables?"
    c "Their trying to sign up for a class."
    p "Oh, I didn't know that I had to sign up for a class."
    p "Wait, why did you say they are 'trying'?"
    c "Well, each class has a closed number of students for the first year."
    p "Whoa! So I'm late! I thought I could talk to people, listen to presentation and decide a class,"
    p "but now I risk to be cut out..."
    p "And what about you? Aren't you late too?"
    c "No, I'm not. Some classes need references to accept students."
    c "The Cleric class is one of them, they want to know that your faith in a deity is sincere, and they need to"
    c "know it from another Cleric."
    c "Same goes for Paladins."
    c "And that means there's not a queue for entering those classes."
    c "To obtain a reference is a rare thing, I'm lucky to have one, thanks to my mother being a cleric of the Blessed Eve."
    c "I just need to show my reference and I will be accepted."
    p "Wow, good for you, Ciry!"
    p "But... I think this also means no Cleric or Paladin class for me. Alright. What can you tell me about the"
    p "other classes?"
    c "The other classes usually make you take entrance tests."
    p "Entrance tests??"    
    c "The Barbarian class test is a strength test, Rangers ask for good reflexs."
    c "While the Fighter class requires a mix of the two."
    hide ciry with dissolve
    $ test_taken = []
    while len(test_taken) < 3:
        menu:
            "Take the Fighter test" if "Fighter" not in test_taken:
                show tolomeus at topright with dissolve
                alt """
                A portrait appears, showing the image of an authoritative figure, seemingly of noble or warrior descent.
                He has a distinguished presence with a sharply chiseled face, a stern expression, and penetrating eyes.
                His hair is neatly combed back, revealing a touch of grey that adds to his dignified aura.
                A prominent, meticulously groomed beard frames his face.
                A golden, ornate headpiece adorns his forehead, adding to his majestic appearance.
                His attire is equally impressive: a suit of armor adorned with intricate gold embellishments,
                particularly a striking emblem resembling a radiant sun at the center of his chest.
                The pauldrons on his shoulders are robust and angular, signifying strength and readiness for battle.
                The overall aesthetic of the portrait exudes a sense of power, wisdom, and authority,
                capturing the essence of a seasoned leader or a revered knight.
                """
                python:
                        test_taken.append("Fighter")
                        tol("The Fighter class is full. I'm sorry young student.")
                hide tolomeus with dissolve


            "Take the Ranger test" if "Ranger" not in test_taken:
                show robin at topright with dissolve
                alt """
                A portrait appears, showing the image of a confident and vibrant female character with an unmistakable
                aura of strength and individuality.
                Her striking pink hair cascades in layers, framing a face marked by a mischievous, self-assured smile.
                Her eyes, partially concealed by her hair, exude a sense of playful defiance.
                She is dressed in a distinctive outfit that blends practicality with style.
                The ensemble includes a fitted, green top that accentuates her form,
                overlaid with a unique harness that adds an element of edginess.
                Her shoulders are protected by light blue pauldrons, contributing to the warrior-like aesthetic.
                Her arms are adorned with leather bracers and gloves, indicating readiness for combat.
                A sturdy belt at her waist, further enhances her dynamic and battle-ready appearance.
                """
                $ test_taken.append("Ranger")
                rob "Hello Cutie!"
                p "Ehm, I'd like to enter the Ranger class..."
                rob "Oh dear I'm sorry, we already have too many requests. I'm so so sorry I cannot accept you."
                rob "You're so ccuute!!"
                hide robin with dissolve

            "Take the Barbarian test" if "Barbarian" not in test_taken:
                $ test_taken.append("Barbarian")
                "A huge half-orc, like a mountain, looks down on you."
                show dragon at topright with dissolve
                alt """
                A portrait appears showing a fearsome and imposing warrior exuding raw power and fierce determination.
                His face, framed by a wild mane of dark hair and a rugged beard, is contorted in a menacing snarl,
                revealing sharp teeth that enhance his intimidating presence.
                His eyes burn with an intense, almost supernatural glow, further emphasizing his ferocity.
                His muscular physique is prominently displayed, showcasing a body built for battle.
                The warrior is clad in minimal but striking armor: intricately designed pauldrons adorn his shoulders,
                and his chest is protected by a harness that features a central, luminous emblem.
                His stance suggests readiness for combat, as if caught in the midst of a battle cry.
                Overall, a formidable and relentless barbarian, embodying both primal rage and indomitable spirit.
                """
                dra "And who should YOU be?"
                p "I... I'm [Player.sheet.name]. I would like to... ehm... enter the Barbarian class."
                dra "HAHA"
                dra "HAHAHA"
                dra "HAHAHAHAHAHAHA!!!"
                dra "I don't think you have what it takes to be a barbarian..."
                p "Is there... ehm... is there a test I should pass?"
                dra "Oh yeah, here's the test."
                "You look around, but you see nothing relevant."
                p "Where?"
                dra "ME!"
                dra "You have to arm wrestle me!"
                "You look at the enormous arms of the man."
                c "Don't do it [Player.sheet.name]..."
                p "I... I will try!"
                dra "I usually limit my strength to 20 percent, but with you I promise to only use a 10 percent of my strength"
                p "Let's do it!"
                menu:
                    "Roll D20 on Strength":
                        $ roll = randint(1, 20) + Player.get_modifier("strength")
                "ROLL: [roll]"
                "You fail the test."
                "The huge arm of the man in front of you crashes into yours mercilessly,"
                "almost as if you had put up no resistance at all."
                "I'm sorry. I suggest you try another class."
                hide dragon with dissolve

    show ciry at topleft with dissolve
    c "I'm sorry [Player.sheet.name]"
    p "Oh, and what about the Bard class?"
    c "To enter the Bard class you must be able to play a musical instrument, or sing. Do you know how to play a"
    c "musical instrument?"
    p "Ehm..."
    p "Maybe... I can... try to sing?"
    c "(rolling her eyes) I would rather not, If I were you. Unless you REALLY know how to sing..."
    p "Ok... Oh! I found it! I could be a Sorcerer or a Warlock!"
    c "Do you carry a magical birthright conferred by an exotic bloodline, some otherworldly influence, or exposure"
    c "to unknown cosmic force?"
    p "Well..."
    c "Did you seal a pact with a mysterious being of supernatural power?"
    p "(lowering your head) No."
    c "Just like I feared."
    p "So, that's it? I..."
    p "I won't be able to enter the academy this year?"
    c "Hmmm that might be true. But... Hey! Technically, there's still one class you didn't try to sign up for."
    c "The Rogue class!"
    p "The... Rogue class? Is that even a real class?"
    c "Oh yes it is. Right there!"
    "When you look in the direction pointed by Ciry, you notice a woman in her forties, with a kind face and a bored"
    "expression, sitting alone by a table."
    "No one was queuing in front of her."
    p "But... I though Rogues grew up as criminals, and only then some of them joins some party ad adventurer."
    c "Well, that's indeed true for most of the Rogues adventurers, and it's surely the way the most renowned"
    c "Rogues have grown up."
    c "But the Academy opened the Rogue class some year ago. It's the most recent class to have been established,"
    c "right after the High City Council acknowledged the Rogue as an official class."
    p "Ok then, so be it. I won't be left behind. My biggest dream has always been to become an adventurer..."
    p "I'll sign up for the Rogue class!"
    c "See you later then, I'm gonna go show my reference and sign up for the Cleric class."
    p "Thanks for everything, Ciry! I'm glad I made friend with you on my first day here... Let's meet again later!"
    c "(blushing) Good luck!"
    hide ciry with dissolve
    window hide
    pause

    "You approach the lady indicated by Ciry with caution and a little hesitation"
    p "Hello, I... I'm here to sign up."
    "The woman looks at you slightly bewildered, as if your words had brought her back to reality, distracting her"
    "from a long chain of thoughts."
    show tris at topright with dissolve
    alt """
    A portrait appears, showing a cheerful middle-aged woman wearing a green dress with brown accents.
    She shows a low neckline and short puffed sleeves, emphasizing her curvy physique.
    Her eyes are large and a striking shade of pink, adding a playful element to her expression.
    She has vibrant green hair styled in a loose, flowing manner, adorned with a small flower on one side.
    Her overall appearance radiates warmth and friendliness.
    """
    tri "Oh, hello! My name is Tris, what can I do for you?"
    p "I mean, I'm here to sign up for the Rogue class."
    tri "(curious) For the Rogue class? Really?"
    p "{i}(She seems surprised too. There's really no one here to sign up for the Rogue class?){/i}"
    tri "Oh, wait! I get it! You couldn't find a place in any other class, could you?"
    p "(embarrassed) Well, actually..."
    p "{i}(I don't want her to fell like a fallback... What if she refuses too?){/i}"
    p "This is the last class I'm trying to sign up for, it's true. But I'll proudly be a Rogue if you accept me!"
    tri "Proudly be a Rogue? Hmmm... Interesting... Well, one student is still better than zero."
    tri "Furthermore, you look skinny. You could make a good Rogue for a human."
    p "...Thanks"
    tri "I used to be so skinny too, you know?"
    tri "Then three children happened, and the fourth's inside my belly! Ahahaha!"
    tri "Anyway... Just sign here, and here. Here's a pen!"
    stop music fadeout 1.0
    hide tris with dissolve    
    
    label before_rector_intro:
    "After signing up for the Rogue class, you are told to walk inside the Academy hall."
    scene main hall
    alt """
    The background changes.
    The background image presents a grand and opulent hall, steeped in architectural splendor.
    High ceilings adorned with wooden carvings weave a complex and ornate pattern across the entire expanse.
    Equally detailed columns and arches stand as testament to the craftsmanship involved in their creation.
    Large, arched windows line the walls, allowing streams of soft, natural light to filter in,
    casting a warm and inviting glow throughout the room.
    The interplay of light and shadow enhances the hall's majestic atmosphere, highlighting the woodwork details.
    Chandeliers hang from the ceiling, their lights adding a golden hue to the space, complementing the natural light.
    Numerous candles contribute to the room's illumination and adds to its regal feel.
    The flooring is smooth and reflective, providing a contrasting simplicity to the elaborate surroundings,
    further amplifying the hall's sense of grandeur. The overall atmosphere is one of timeless beauty,
    evoking a sense of awe and reverence for the architectural mastery displayed within this magnificent space.
    """
    window hide
    pause
    play music arcadia
    "You look around trying to find your new friend Ciry in the midst of all those people."
    menu:
        "Roll a D20 on Perception":
            $ roll = Player.roll_skill("perception")
    "ROLL: [roll.result]"
    if roll.result >= 7:
        $ Player.achievements.append("Found Ciry in the crowd")
        "Despite her short stature, being a gnome, you manage to recognize Ciry's hair in the middle of the crowd."
        "But you are too distant and there's no easy way to reach her."
    else:
        "You can't find Ciry. She's a gnome, afer all. It's not an easy task to notice a gnome in the middle of a crowd."
    
    "In the meantime, you hear a bell ring and a murmur of voices becoming more and more understandable:"
    "The Rector! He's the Rector Almar himself!"
    "The Rector is gonna speak!"
    rec "Dear students..."
    show rector at top with dissolve
    alt """
    A portrait appears, showing the image of a distinguished elderly man.
    He has a flowing white beard and tousled white hair, giving him an air of wisdom.
    His attire is formal and ornate, featuring a blue and black robe with gold accents and tassels.
    He wears a yellow necktie over a maroon shirt, complemented by a ceremonial blue and gold headdress.
    His black-framed glasses add a scholarly touch to his appearance.
    The overall impression is that of a high-ranking academic or a university rector.
    """
    rec """
    Welcome to Dungeon Academy!
    THE Academy!
    I suppose I'm now mostly talking to first year students, since all the other students should already be
    in their classes now.
    """
    "After the Rector's last words, you can see a certain amount of students halfheartedly leave the main hall."
    rec """
    Each one of you did choose a class this morning. Someone with a reference, someone else as a result of a hard
    work or good luck.
    To all of you I'm here to explain how it will work for the months and years to come.
    As many probably know, every year here at the Academy is divided in two terms, each of them lasting four months.
    The first four months are considered a kind of trial period, in which you will experiment what it means to
    study in a certain class.
    During this first term, you will still be able to apply for a class change.
    Notice that a 'class change request' needs the approval of both the class-masters of the class you are leaving
    and the one you want to enter.
    The class-masters are the main teachers, one for each class. Their judgment is absolute.
    The lessons will be divided in class lessons and optional lessons.
    Every student will need to follow thier class-specific lesson, which will help you consolidate the basics that
    define your class, as well as to internalize the role that each class plays within a party.
    On the other hand, optional lessons are no less important.
    You will need to follow the optional lessons to gain enough credits to be promoted to the next year.
    Thier 'optional' nature will let you choose, at the beginning of every week, the course that will be added to
    your study plan.
    Each course will focus on developing certain skills and abilities. You are free to stick to those most closely
    related to you class, or to acquire a more hybrid mix of competences
    You are here to 'build' yourselves into great adventurers. So make the most of this opportunity.
    With this I say goodbye and good luck to all of you. May the power of the gods be upon you in the time to come.
    """
    hide rector with dissolve
    stop music fadeout 1.0
    """
    And without giving room for questions, the rector turned and walked away.
    Another woman, maybe the vice principal, started to talk in his place: 'the lessons will start right now'.
    With too many questions still on your mind, you hear the woman saying that each student should move to their
    class's classroom for an initial briefing, and that the following day will be possible to choose the study plan
    for the current month.
    """
    
    $ visited = []
    label after_rector_intro:            
        menu:
            "Where do you want to go?"

            "Try to reach out Ciry (before losing her in the crowd)" if ("Reach Ciry" not in visited and "Found Ciry in the crowd" in Player.achievements and len(visited) == 0):
                $ visited.append("Reach Ciry")
                $ Ciry.approval += 10
                "You managed to reach Ciry through the crowd, who almost overwhelmed her due to her short stature."
                p "Ciry! I'm here!"
                show ciry at topleft with dissolve
                c "(smiling with surprise) Oh! [Player.sheet.name]!"
                c "You managed to find me even here throung all these people! Hehe, I was starting to fear being trampled."
                p "I just wanted to say goodbye before we all went to our respective classes"
                c "Oh, thank you [Player.sheet.name]..."
                c "Well, being a gnome girl usually means going unnoticed and feeling ignored."
                c "(blushing) So I'm... glad you came to say goodbye!"
                c "I'm looking forward to meet you after our first lessons!"
                p "Yes, see you later Ciry!"
                hide ciry with dissolve
                "(Ciry's approval: +10)"                    
                jump after_rector_intro
            
            "Explore Academy" if ("Explore Academy" not in visited):
                $ visited.append("Explore Academy")
                $ Player.achievements.append("Explored academy")
                """
                As the crowd of students disperse, you start exploring the academy.
                The Academy, a colossal structure reminiscent of a castle, looms majestically before you.
                You are astounded by the the multitude of rooms and then you notice its towering spires reaching towards
                the heavens...
                With a cacophony of voices filling the air, students disperse into the labyrinthine corridors, each one
                brimming with the promise of knowledge and adventure.
                """
                scene 2024-04-25_11-04-48_5772 with dissolve
                pause
                "Some head towards the Hall of Deities, where statues of ancient gods and goddesses stand sentinel, their"
                "watchful gaze is said to impart wisdom and guidance to those who seek it."
                scene 2024-03-30_13-07-37_1127 with dissolve
                pause
                """
                Others make their way to the Training Grounds, where the clash of steel against steel resounds through the
                air as aspiring warriors hone their combat skills under the watchful eye of seasoned instructors.
                Swordplay, archery, hand-to-hand combat...
                """
                scene 2024-03-30_13-25-35_7058 with dissolve
                pause
                """
                In the Arcane Chambers, young wizards and sorcerers gather to practice the intricate arts of magic.
                The air crackles with energy as spells are cast and incantations whispered, each student striving to unlock
                the mysteries of the arcane and harness its power.
                """
                scene 2024-03-30_13-11-02_1104 with dissolve
                pause
                """
                You then enter the dining room, now empty except for a single figure seemingly eating with brute force and anger.
                As soon as she notices your presence, she turns towards you, giving you a dirty look,
                but then immediately ignores you.
                You recognize the unmistakable traits of a half-orc in that tall, robust-looking girl.
                """
                menu:
                    "Approach her and try to introduce yourself":
                        $ Theo.approval -= 10
                        "You approach the girl with an uncertain step."
                        "She pretends not to notice you, but then."
                        "But when you wave your hand and try to speak to get her attention, she immediately gives you a grim look."
                        # $ Player.race = "Elf"
                        if Player.race == "Half-Orc":
                            uk "(speaking with her mouth full) Just 'cause ye're a fellow Half-Monster don't mean I gotta like ye."
                        elif Player.race == "Elf":
                            uk "(speaking with her mouth full) Can't stand seein' fairies like ya."
                            uk "For yer own good, don't come near me, 'specially when I'm eatin', or you'll be sorry."
                        else:
                            uk "(speaking with her mouth full) I know not who thou art, but I don't care for company whilst I'm eatin'."
                        uk "...now get outta here 'fore I lose me cool."
                        "(Unknown's approval: -10)"
                        
                    "Ignore her (she seems comfortable alone)":
                        $ Theo.approval += 10
                        "(Unknown's approval: +10)"

                jump after_rector_intro

            "Skip (go to Rogue classroom)":
                scene 00004-1923438760 with dissolve
                
    pause
    window show
    "You enter the Rogue's classroom."
    "The first thing you notice is that it's empty, except, of course, for the teacher."
    show tris at topright with dissolve
    tri "Oh, hello my only student!"
    if "Explored academy" in Player.achievements:
        tri "(smiling) It's a bit late, hehe, did you get lost in the depths of the academy?"
        p "Well..."
    play music etherealrelaxation fadein 2.0
    tri "It's [Player.sheet.name], isn't it?"
    p "Yes..."
    tri "Well, as you already know I'm the class-master of the Rogue class, and so on..."
    tri "I won't annoy you with formalities now."
    tri "Oh, and don't you dare address me 'Ma'am', just call me teacher or Tris."
    p "Oh, ok"
    tri "So, you are probably asking yourself why there's no one else here."
    tri "It's no mistery: Rogue is not a class many desire."
    tri "Not that what I teach would be useless. On the contrary, a lot of students from the other classes follow"
    tri "my optional courses."
    tri "I'm always overbooked!"
    p "So... people just avoid choosing the Rogue as their official class?"
    p "To be honest, I didn't even know it was a real class...."
    tri """
    That's exactly the point. Rogues started to fit in famous parties of adventurers for their stealth and trickery
    skills, very valuable in dungeons, especially to disarm traps, steal treasures from monsters without fighting,
    or to get informations about enemies.
    But those Rogues usually learnt their skills growing up in the slums as criminals.
    I don't wanna say that they were all bad. Many were just abandoned children with no home and no food...
    Well, anyway, time passed and the Rogue skills became sought after in all parties.
    Many rangers, bards, or even other classes started to train in how to slink, or how to pick a lock, just to
    have more chances of entering strong parties and become rich, famous adventurers.
    But to be called 'Rogue'? Nah! No one wanted it...
    and most adventurers still don't want it now, even if the Rogue has officially been recognized as an Adventurer
    Class by the Council, with a real license and everything else.
    You can now graduate as a Rogue adventurer. Still, in the last years I only had very few students.
    And some years I even had no students. Like THIS year, if it wasn't for you! Hahaha
    People, villagers, kings, everyone still tend to think of rogues as criminals...
    There's no glory in fulfilling a mission if you are a Rogue. No one will acclaim you.
    Or at least not as much as being a proud Paladin, a fierce Fighter, a talented Wizard, or else.
    And if there's one thing an adventurer wants even more than gold or rare items, it's glory, you know?
    But to be stealthy or picking a lock is just the tip of the iceberg. There's so much more in being a Rogue.
    That's what many adventurers miss...
    And that's what I'll teach you. If you are willing to learn, of course.
    """
    p "Well, I... I am!"
    p "{i}(So, this is the reason why no one wants to be a Rogue){/i}"
    p "{i}(But I... I won't care about reasons like these!){/i}"
    p "I mean, being an adventurer has always been my dream. I've always been uncertain about which class to choose,"
    p "and I was sure that coming here the first day would have helped me taking a decision."
    p "{i}(Yes, I will... I will be an adventurer no matter what!){/i}"
    p "Even if I never thought to choose the Rogue class, as long as I will have the opportunity to be an adventurer,"
    p "I will do my best. I promise!" 
    tri "Very well. It's a good start."
    tri "Now..."
    tri "Tell me, [Player.sheet.name], what you think better describes the abilities of a Rogue?"
    
    window hide
    menu:
        "Dexterity? to be precise and agile?":
            tri "Dexterity is important for a Rogue, of course, but it's not just that."
        
        "To be stealthy and strike the enemies from behind?":
            tri "The Sneak Attack is, indeed, a powerful attack,"
            tri "but other classes have powerful attacks too, and with a better defense, or a broader choice for effect area."
        
        "I think a mix of many things... I can't figure out just now":
            tri "That's... somehow a good answer."
        
    tri """
    Memorize the location of all the traps in a dungeon,"
    distract an enemy so that a fellow adventurer can find an opening in his guard."
    Find a way out of a bad situation with an unpredictable trick,
    when everyone else in the party has already lost hope..."
    These are some of the things that could make you a 'real' Rogue."
    And here come the basic principles of the Rogue class. Try to always focus on these three words:"
    AWARENESS"
    FLEXIBILITY"
    CREATIVITY!"
    You are always aware of your surroundings, you can adapt to every situation, you can find creative solutions
    to unsolved problems... All this would make you a good Rogue."
    So what do you think?"
    """
    p "Wow... I think, I never imagined there could be so much behind the Rogue class. It's amazing!"
    tri "And that's also so much for a first lesson. Let's just call it a day and go home now."
    p "Oh, ok..."
    tri "Yeah, I need to buy food and start cooking for my family..."
    tri "Take this book and read it in your spare time."
    p "{i}('Instinct of the Cunning Rogue - Part 1'){/i}"
    p "Thanks."
    tri "Oh, and don't forget to choose your study plan for the current month!"
    stop music fadeout 2.0
    tri "You'll start your first optional course tomorrow morning."    
    
    hide tris with dissolve
    scene 00010-1467134838
    pause    
    "Your first day at the Academy has come to an end."
    "You walk out of the classroom and see the corridors rapidly fill up with students, along with a growing murmur"
    "of voices."
    "A little disoriented, you decide to follow the flow of people to reach the exit and then head home."
    scene dice academy1 with dissolve
    "Just outside the Academy, you hear a familiar voice call out your name"
    "[Player.sheet.name]!"
    c "[Player.sheet.name]!"
    show ciry at topleft with dissolve
    play music onmyway fadein 1.0
    c "There you are!"
    p "Oh, Ciry! It's nice to see you again! How was your first lesson?"
    c "Oh [Player.sheet.name], it was amazing! We started talking about out different deities and faiths."
    c "It was so fascinating..."
    c "I think I won't sleep at all tonight! I have so much questions in my head!"
    c "Let's head home together! Where do you live?"
    scene 00027-1515435079 with dissolve
    alt """
    The background changes. It shows the cobblestone road of the city.
    """
    p "Uhm, I live near the Mushroom Forest, not really near the city..."
    show ciry at topleft with dissolve
    c "The Mushroom Forest? I didn't know there was a village there."
    p "Well, it's not exactly a village, it's just me and my aunt. I live with her, my..."
    p "my parents died when I was child."
    c "Oh, I'm so sorry [Player.sheet.name]..."
    p "Don't worry, it's all in the past now."
    c "Anyway, isn't it dangerous to live near the Mushroom Forest?"
    c "I heard stories about strange creatures living there..."
    p "I guess it happens when your aunt is the Druid-guardian of a Forest..."
    c "Wh... WHAT?!"
    c "So your aunt is the famous Mushroom-Druid?"
    p "Hehe, yes, even though she hates when people call her like that."
    c "Oh, sorry, hahaha!"
    c "You must invite me to study something together, so I can ask her sooo many questions!"
    p "Haha! Ok, I think it will be fun. She is a funny person, I think she'd like you!"
    p "But, you are in the Cleric class while I'm in the Rogue class, what should we study together?"
    c "Don't forget the complementary subjects! Geography, History and Laws of the City, and so on."
    c "Furthermore, you can teach me your Rogue stuff while I teach you about the Cleric class!"
    c "Yes, it's a brilliant idea!"
    c "This way we can learn things about two different classes, and be more prepared when we'll work in parties!"
    p "It's a deal then"
    c "GREAT!"
    c "So... What about YOUR first day at the academy?"
    c "Now that I'm thinking about it, I'm so curious about what is thought in the Rogue class..."
    p "It... It was interesting. Teacher Tris explained me why no one ever chooses the Rogue as their class."
    p "But we hope that this will change in the future."
    p "She sad that a real Rogue is all about Awareness, flexibility and..."
    p "Oh yes, Creativity."
    p "And then she lent me this book"
    "You show Ciry the tome 'Instinct of the Cunning Rogue - Part 1'"
    c "WOW! That's a Rogue's manual! I've never seen one before!"
    c "Can I look at it?"
    p "Sure!"
    c "Let's see..."
    "Ciry frantically flips through the book, then stopping on a random page."
    if Player.race == "Half-Elf":
        c "'Wood Elves, too, can make outstanding rogues thanks to both their racial bonus to Dexterity and the"
        c "Mask of the Wild feature, which allows them to easily hide in the natural world.'"
        p "Well, I'm a Half-Elf... Even though, I can't use Mask of the Wild."
    if Player.race == "Dwarf" or Player.race == "Half-Orc":
        c "'Dwarves and Half-Orcs would be unusual races for rogues, but nonetheless, they can find a mix of"
        c "abilities that can make them work effectively as Rogues.'"
        p "Well, I didn't expect to end up in the Rogue class so... I guess I'll have to come up with some ideas"
        p "about this 'mix of abilities'."
        c "I'm sure you're gonna do a great job, [Player.sheet.name]!"
    c "..."
    p "..."
    stop music fadeout 2.0
    pause

    label debug:
    c "I'm home! I live right there, near the eastern City wall, Thanks you for walking with me!"
    p "Oh, so... Have a nice evening and... see you tomorrow at the Academy!"
    c "Thanks [Player.sheet.name], you too!"
    hide ciry with dissolve
    "After saying goodbye to Ciry, you walk outside the city walls. It takes nearly an hour to walk from your house"
    "to the center of the City, but you are well used to it."
    "You take the usual avenue that crosses more peripheral houses, the houses of the farmers. Then you cut through"
    "a field up a hill until in the distance you see a mushroom-shaped house."
    scene 00028-45450802 with dissolve
    pause
    play music averybradyspecial fadein 2.0
    alt """
    The background changes.
    A mushroom shaped house with a green roof completely covered by moss, nestled in a magical forest.
    Warm yellow lights shine inside and colorful flowers surround the edges of the windows.
    Curved, organic shapes with roofs covered in lush green moss, seamlessly blending with the surrounding nature.
    Warm, golden light spills from the arched windows and doorways, casting a welcoming glow.
    The forest itself is otherworldly, with whimsical, oversized mushrooms that enhance the fantastical ambiance.
    A gentle stream winds through the scene, reflecting the warm light from the houses.
    Flowers and greenery surround the houses, completing the picturesque and inviting woodland retreat.
    """
    "A house you call home."
    show bella at topright with dissolve
    alt """
    A portrait appears, depicting a vibrant and cheerful female character.
    She has long, flowing black hair that frames her face and curls slightly at the ends.
    Her eyes are a striking shade of blue, full of energy and sparkle, complementing her wide, joyful smile.
    She is dressed in a stylish outfit that features shades of blue and black.
    The high-collared garment is adorned with intricate lace details around the neckline,
    adding a touch of elegance to her bold and spirited demeanor.
    Overall, her expression and pose convey a sense of positivity and determination,
    suggesting a character who is both approachable and strong-willed.
    """
    bel "[Player.sheet.name]!"
    bel "Welcome home! How was your longed-for first day?"
    p "Hi auntie! It was good"
    bel "Which class which class?? Did you finally choose?"
    p "I didn't actually choose but... I ended up in the Rogue class."
    bel "The... The Rogue class? Uhm, you never mentioned it in our long one-sided discussion about pros and cons"
    bel "of each class..."
    bel "How cute!"
    p "Yes... It seems interesting"
    bel "And did you make any friend?"
    p "I'm the only one in the Rogue class, actually, but I did make a friend today. She's in the Cleric class."
    bel "So there's a girl-friend now! Hahaha!"
    bel "And... is she cute? IS SHE CUTE??"
    p "(blushing) Ye... Yes... I guess she is cute..."
    bel "(kissing you on the forhead) I'm so proud of you!"
    "With your sleeve, you wipe the glaring mark of her lipstick on your forehead."
    p "(still blushing) Auntie... Stop!"
    bel "Oh I know, I had many friends too, both boys and girls you know? Hihi!"
    bel "Or at least I used to call them 'friends'... Hihihi!"
    p "Ok, stop now... By the way, she asked me to meet you, she's a real adventurer-nerd and she wants to ask you"
    p "a lot of questions."
    bel "Invite her to study here! I'd be so happy!"
    p "Oh don't worry, she already invited herself..."
    scene 00004-1773495918 with dissolve
    "You spend a pleasant evening in the company of your aunt, telling her everything you saw today at the academy"
    "and explaining to her that you would also start your optional courses the next day."
    show dining_1 at left with dissolve
    "You enjoy the delicious dinner she prepared. Her skill in the kitchen surprises you every time."
    show bedroom_1 with dissolve
    "Then you go to bed, feeling that like Ciry you won't be able to sleep."
    "But as you start dreaming the advetures of tomorrow, your eyes close,"
    "and a deep sleep drags you into its embrace..."
    pause
    scene bg black with annoytheuser
    alt "The background fades out in darkness."
    p "{i}...{/i}"
    window hide
    show 00008-3630713263 with annoytheuser:
        blur 75
    pause
    alt "A blurred image appears, maybe the face of a beautiful woman with long white hair?"
    p "{i}Is this a dream?{/i}"
    window hide
    show 00008-3630713263 with annoytheuser:
        blur 25
    pause
    alt """
    The image is more nitid now: a young woman with platinum blonde hair flowing gracefully around her.
    """
    scene bg black with annoytheuser    
    window hide
    scene bg white with annoytheuser
    stop music fadeout 2.0


label chapter_2:
    label first_days_academy:
        "You wake up with a lot of energy and optimism"
        scene 00028-45450802 with dissolve
        play music firefliesandstardust fadein 2.0
        "While you eat breakfast and prepare yourself for the day, you can't shake the vague feeling that you've dreamt"
        "about something: a scent, a light, a warm feeling of calm, like a hug from a beloved friend."
        "But soon your mind fills with excitement, questions and expectations"
        p "{i}(Which optional course should I choose?){/i}"
        "You say goodbye to your aunt Bella and start walking towards the Academy."
        scene dice academy1 with annoytheuser
        "As soon as you arrive at the Academy, you see many students in turmoil inside the Main Hall."
        "But this time you know why: everyone should choose his optional course for the current month."
        show ciry at topleft with dissolve
        "You notice Ciry not too distant from you. She seems completely lost in her own thoughts."
        p "Oh, Ciry! Good to see you!"
        c "Hi [Player.sheet.name]!"
        c "I'm so excited!"
        c "I couldn't sleep the whole night. Should I go with 'History of Magic' or 'Principles of the Faithful'?"
        c "I still can't decide wheter to focus on pure Cleric stuff or expand my knowledge in complementary subjects..."
        menu:
            "You should focus on cleric stuff":
                p "A solid foundation is the key to becoming a great adventurer:"
                p "perhaps you should first focus on the knowledge and skills central to your class."
                $ Ciry.sheet.wisdom += 2
                $ Ciry.courses_taken.append("religion")
                $ Ciry.sheet.skills_intelligence["religion"] = True

            "You should expand your knowledge":
                p "I think flexibility is a good thing for every adventurer, not just for Rogues."
                p "Maybe expanding your knowledge will save you from a bad situation one day."
                $ Ciry.sheet.intelligence += 2
                $ Ciry.sheet.skills_intelligence["arcana"] = True
                $ Ciry.courses_taken.append("arcana")
        
        c "Thanks, I will take your suggestion into consideration!"
        c "Let's go sign up for the optional courses!"
        hide ciry with dissolve
        "You follow Ciry inside the Main Hall where, in front of a long wooden table, a row of students waited their"
        "turn to write their name on the sheet relating to the chosen optional course."
        "Finally, it's you turn to sign up for a course."
        call study_plan_1 from _call_study_plan_1

        # $ PARTY = [store.Player, store.Ciry]
        "Day after day, you follow the lessons at the Academy with great interest."
        "One of the things you notice in your first days at the Academy is that many students carry weapons with them,"
        "someone in their bags, others attached to their bodies, as if to display them,"
        "not to talk about those wearing shining heavy armors all the day long."
        show ciry at topleft with dissolve
        c "I can see your curious face, hihi"
        c "Students with rich families use to flaunt their weapons in front of the teacher and the other students."
        c "Those weapons and armors are usually of fine workmanship, and sometimes even magical artifacts."
        c "It's like to say: (mocking the voice of a guy)"
        c "'hey, I'm so rich and powerful that I can bring this at school' hihi!"
        c "I think it's just stupid, unless you really need to train in their use."
        c "Wearing a heavy armor all the day, though, can make sense: for a heavy armor user, the sooner you get used"
        c "to moving around effortlessly in armor the better."
        hide ciry with dissolve

        # scene bg academy_courtyard with fade
        "One day, the Academy's courtyard is buzzing with activity as students disperse to their classes."
        "Amid the crowd, a girl approaches you."    
        gwe "Hey, you! You're new here, aren't you?"
        p "(nervous) Uh... me? Yes, I, uh, just started today."    
        gwe "(grinning) Thought so! You look a little lost. I'm Gwen. What's your name?"
        p "I'm [Player.sheet.name]. Nice to meet you."    
        gwe "Well, how about I give you the grand tour of this place?"
        gwe "Or better yet, why don't we skip the boring stuff and grab a bite at the Bazaar later? It'll be fun!"
        
        menu:
            "Agree hesitantly":
                p "Oh, um... sure. I guess that could be nice."
                gwe "Great! Meet me by the fountain at sunset. And don't worry, I'll try not to get us into too much trouble."
                gwe "Probably."
                $ Player.achievements.append("Gwen Date")

            "Decline politely":
                p "Thank you, but I really should focus on settling in. Maybe another time?"
                gwe "(pouting) Suit yourself, new boy. But you're missing out, you know. I'm very entertaining!"

            "(blushing) Get flustered and say nothing":
                p "Uh... I... um..."
                gwe "(chuckling) Cat got your tongue, huh?"
                gwe "Don't worry, I'll take that as a yes. Fountain. Sunset. Don't be late!"
                $ Player.achievements.append("Gwen Date")

        menu:
            "Go to the date with Gwen" if "Gwen Date" in Player.achievements:
                label gwen_date:
                    $ Player.achievements.append("First date with Gwen")
                    "The sun dips low, painting the Academy courtyard in hues of gold and crimson."
                    "You wait nervously by the fountain, until Gwen arrives, her usual mischievous grin in place."                
                    gwe "Glad you showed up, [Player.sheet.name]! I was starting to think you might bail."
                    
                    menu:                
                        "No, I wouldn't... I mean, I'm here, aren't I?":                
                            gwe "Relax, I'm just teasing. Now, come on. The Bazaar awaits!"                
                    scene bg fantasy_bazaar with dissolve
                    "You make your way to the bustling Bazaar, a vibrant market filled with magical trinkets, exotic foods, and performers displaying their talents. Gwen leads the way, pulling you into the crowd."                
                    gwe "This place has the best snacks. Try this!" 
                    gwe "Oh, and don't miss the fire juggler over there. He's always fun!"                
                    "As you wander, Gwen's enthusiasm is infectious, and you find yourself smiling and laughing more than he has in years. The evening passes in a blur of lights and sounds."

            "Skip (continue your studies for the week)":
                jump aryanna_rescue

    label aryanna_rescue:
        "The first week is now gone, and today Ciry will come to visit you at your home, as you both previously agreed."
        scene 00004-1773495918
        stop music fadeout 2.0
        pause
        "She is so happy and curious about your mushroom-house that she forces you to show her every single room"
        show ciry at topleft with dissolve
        c "But, where is your aunt? There are so many things I want to ask her!"
        p "I'm sorry, she's not here now... She wanted to meet you too, but this morning she said there was something"
        p "important and she left in hurry."
        p "She was very sorry to miss you. I promise you'll meet her another time!"
        c "Ok, no worries! I'll come back here maaaany other times! I love this Mushroomy house sooo much!"
        "Time passes, and you a Ciry go on talking about the things you've learnt at the Academy in past days."
        pause
        play music cheezeecave fadein 2.0 volume 0.5
        "Suddenly, you hear the sound of running steps approaching the house main door."
        "Knock knock!"
        "Someone is now knocking at the door, repeatedly and with hurry."
        c "Are you waiting for someone?"
        p "No... And aunt Bella would never knock at her own house, I guess."
        p "Let's go check who's out there"
        c "(with a malicious smile) Should I prepare some offensive spell, in case they're bandits?"
        p "Do you know offensive spells?"
        c "(disappointed) Actually, not yet... But I could try"
        p "Well, I don't think it will be necessary."
        "And with your last words you open the large wooden door. At first glance you see no one, then you lower your"
        "eyes, just to find a scared and out of breath gnome woman, dressed in simple clothes."
        "Her eyes suggesting she needed help."
        show dyana at topright with dissolve
        c "..."
        c "Mom?"
        dya "Ciry!"
        dya "Oh, Ciry, thanks the Morning Star I found you..."
        c "Mom, what happened?"
        dya "It's Aryanna..."
        c "Aryanna what?"
        dya "I can't find her!"
        p "Who's Aryanna?"
        c "She's my little sister"
        c "But where... where did you see her last time?"
        dya "She was playing adventurer at home, like usual, then she told me something like:"
        dya "'Mom, I'm going on a mission'"
        dya "I thought it was part of her play, not that she would actually leave!"
        dya "Oh Blessed Eve, please keep her safe!"
        dya "We need to find her before sunset! Oh... I should have watched her more closely,"
        dya "we know how exuberant she is..."
        dya "What if some bad people find her?!"
        c "Ok, mom, let's calm down..."
        c "Can you remember if she said something else about the mission?"
        dya "The mission?"
        dya "I... I don't know... Maybe..."
        dya "..."
        dya "... Oh! Yes, maybe... she was mumbling something about a treasure?"
        c "A treasure?..."
        c "Oh! Oh... Oh no."
        c "I think I know where she headed. But... The bad news is..."
        c "A few days ago I was telling her stories about adventurers, like always, and I told her the legend of the"
        c "treasure in the Cave of the Omens."
        dya "The Cave of the Omens? Do you really think she went there? But how could she find the place?"
        dya "It's far from our house, and Aryanna's just five!"
        c "I... may have drawn her a map to reach the cave..."
        dya "Ciry..."
        c "What? We were playing treasure hunt!"
        dya "I'll run back to the City, to ask the Guards for help, and you..."
        c "I'll go to the Cave of Omens, it's not so far from here, it's much closer than the City..."
        c "I'll probably meet her halfway, or in the Cave's surroundings"
        dya "Be careful! If you see something dangerous just wait for the Guards..."
        dya "We are not even completely sure Aryanna is there."
        p "I'll go with her! In two we'll search faster."
        dya "Thank you dear..."
        dya "May the Morning Star be with you both!"
        "And so Ciry's mom left, heading towards the City. You and Ciry, too, leave you house in hurry."
        hide ciry with dissolve
        stop music fadeout 2.0
        pause
        scene 00004-2040205780 with dissolve
        play music ancientwinds fadein 0.5
        pause
        $ PARTY = [Player, Ciry]
        p "So, you know the path from here to the Cave? I've never been there..."
        show ciry at topleft with dissolve
        c "More or less... I read it on a book once."
        p "(dubious) On a book?"
        c "..."
        p "..."
        p "So, is 'The Blessed Eve' the deity you draw your Cleric powers from?"
        c "Yes, in my family there are a lot of Clerics, and we have prayed to the Morning Star for generations."
        c "I grew up drawing her with my colored crayons, listening to goodnight stories about her before going to sleep"
        c "She's like a hero to me!"
        p "Every deity should have a favourite weapon, right? Which is the Morning Star's favourite weapon?"
        c "(narrowing her eyes) Well, the morning star"
        p "Oh. Right. I could have spared that question."
        c "Right, hahaha!"
        c "I always carry a morning star in my bag... Here, take a look!"
        "And she shows you a well made weapon, a short mace with a round head, adorned with dangerous spikes"
        p "I see. I guess it's comfortable to have a deity you can rely on, in moments of need..."
        p "or just when one feels alone"
        c "Yes, yes it is"
        c "[Player.sheet.name], you... Which deity do you use to pray and rely on?"
        
        menu:
            "I rely on good Deities":
                p "I use to rely on good Deities, though I don't specifically serve or pray one more than the another."
                "(Ciry's approval: +10)"
                $ Ciry.approval += 10
            
            "I don't have one":
                p "Me? Well I... I don't have one, to be sincere"
                c "No?! Why?"
                p "My aunt Bella always talks about Mother Nature, but never to refer to a specific Entity or Deity with a name"
                p "or a personality..."
                p "She just adore the balance of Nature, and she says that a Druid can draw power from that alone."
                c "You know, there are many Druids that pray a specific deity."
                p "I know, just, she isn't one of them."
                p "My mom and dad used to pray to Tosvald, the God protector of Merchants. Since they were Merchants too."
                p "But after my parents passed away... I don't know, It's just that somehow I could never feel connected to"
                p "any diety, that's all."
                c "I'm sorry [Player.sheet.name], you don't have to justify your feelings with me."

            "I don't like deities":
                p "To be sincere, I don't really like deities..."
                c "Oh... What a sad thing to say..."
                p "My parents use to pray their god, and they died anyway... It obviously didn't help."
                p "I don't need to pray anyone, I only rely on my own strengths."
        
        c "It's fine if you feel that way. Just remember that there are good deities, like Eve the Morning Star,"
        c "that will listen to you if you'll ever feel the need to pray."
        p "(smiling) Thank you Ciry, I'll take it into consideration."
        c "Talking about faiths, the Cave of Omens is a long abandoned mine, but before that it used to be a place of"
        c "worship, you know?"
        p "Really? How come it isn't anymore?"
        c "It was a sanctuary for the Silent Goddess."
        p "The... Silent Goddess? Never heard about her..."
        c "Not much is said about her anymore... Precisely because she is 'silent', no one prays in her name anymore"
        c "No a Church, no Clerics and not an order of Paladins..."
        c "She never granted her divine powers to those who worshipped her..."
        p "So there was no point in worshipping her if no divine power was granted, eh?"
        c """
        Well, in theory one should believe in the guiding principles of a Deity... And not worshipping just for recieve divine powers.
        But over time, even the most righteous and faithful men came to prefer praying to the deities that, despite sharing the same principles of Good and Justice, could grant them the powers to fight back evil.
        And honestly, I can't say it's wrong...
        """
        p "So, anyway, this Silent Goddess was on the good side?"    
        c """
        Oh yes, even if I don't know much about her principles and domains, I know for sure she was good. It's told that she fought valiantly in the last war between good and evil gods.
        And references to her are found in the sacred texts of many good deities. But no one knows why she never talked back to anyone. The knowledge about her was only handed down by legends and sacred texts.
        Now there are those who even question her very existence. Her devotees are scattered and her sanctuaries, ruins...
        """
        "Silence falls between you and Ciry..."
        c "(out of breath) I think we'd be close by now..."
        p "(out of breath) Yeah... It has been quite a walk!"
        c "There!"
        scene 00006-2040205782 with dissolve
        pause
        p "The Cave?"
        show ciry at topright with dissolve
        c "Yes! You see? That's the entrance, I'm sure."
        p "But, what about your sister?"
        c "If she found the way up here, she must be somewhere around"
        c "Or maybe she will arrive soon..."
        stop music fadeout 2.0
        "Suddenly, a sound behind you. Something moving in the tall grass"
        scene 00006-2040205782 with dissolve
        p "Hey, what was that?"
        c "Mah, just a rabbit, don't worry."
        c "..."
        c "There! It seems like a fate hare!"
        p "I don't know, I'm not sure it's a hare..."
        play music cheezeecave fadein 2.0 volume 0.5
        p "Now it's coming towards us"
        c "(disgusted) Oh, no, it's not a hare."
        p "It's more like a rat!"
        c "And a giant one... Do you have a weapon?"
        p "No, I... I don't, I only have my adventure bag!"
        $ battle(PARTY, [GiantRat])
        $ restore_party(PARTY)
        "You and Ciry manage to fight back the Giant Rat."
        label earthquake_ch1:
        "After some well-placed kicks and some hit with Ciry's 'morning star' mace, the evil animal retreats."
        show ciry at topright with dissolve
        c "Damn it! There shouldn't be this kind of monsters around here! We're still inside the City's external borders."
        c "There are supposed to be guards and adventurers patrolling all the borders... Ary!"
        with hpunch
        "As you try to think of something, a little jolt of the ground throws you off balance"
        p "An earthquake?"
        c "Please Ary, answer!"
        c "What if some beast like that one found my sister before us?"
        p "Let's not despair right now, we don't even know for sure if she really came here..."
        p "She might just be lost in the City"
        c "Ary is very smart... I bet she could read my map correctly and find this place if she wanted..."
        c "Aryanna!! Please answer"
        "As the two of you shout Ciry's little sister name, you walk closer to the cave's entrace."
        ary "Big sis?"
        c "Ary?!"
        c "Where are you?"
        ary "Here, this way big sis! Hehehe"
        c "Oh there she is! [Player.sheet.name]! We found her!"
        c "Oh thank The Blessed Eve!"
        p "I'm so relieved..."
        "You see a little figure moving in the tall grass, but she is so short that the grass completely covers her."
        "You finally see her when she emerges from the tall grass. A little funny gnome figure, with a big round head and a very small body, was waving with her hand. She was now right near the cave's entrace."
        show aryanna at topleft with dissolve
        ary "Big sis! I found the treasure cave!"
        c "Ary! How could you think of coming here alone?"
        c "You made us worry so much!"
        ary "I wanted to find the treasure of the dragon and bring it home!"
        c "Come here now, let's go home."
        c "(turning to you with a resigned expression) I'll teach her the difference between reality and games later."
        play sound rumble
        with hpunch
        "But as you draw closer to the entrance, and to the little Aryanna, a second, more violent, earthquake strikes!"
        with hpunch
        "This time it is followed by an eerie rumble coming from underground... and before anyone could react, the ground beneath Aryanna's feet begins to collapse. Ciry is petrified with fear."    
        
        menu:
            "React":
                $ Player.achievements.append("Reacted to save Aryanna")
                "Before even thinking about it, your body reacts, you sprint towards the little girl and you lunge to"
                "grab her with your hand..."
                $ roll = None
                menu:                
                    "Roll D20 on Atlethics":
                        $ roll = Player.roll_skill("atlethics")                    
                    "Roll D20 on Acrobatics":
                        $ roll = Player.roll_skill("acrobatics")
                "ROLL: [roll.result]"
                if roll.result > 10:
                    "Just in time! You manage to grab her arm and you are now holding her up. Below her, the void."
                    jump ary_grabbed
                else:
                    "You touch her fingers but you can't manage to grab her and you hear her scream while she falls down."
                    jump ary_fall

            "Stay still":
                "You want to move but your body doesn't, you helplessly watch the little girl disappear into the ground."
                jump ary_fall        

    label ary_grabbed:
        "You are holding the little gnome girl with your hand, but just when you are starting to pull her up,"
        "a huge earthquake shakes the ground!"
        "The earth beneath you crumbles and you fall down, rolling together with mud and rocks."        
        jump explore_cave_omens

    label ary_fall:
        "You are just starting to ask yourself if Ary is hurt, feeling guilty for not being able to help her,"
        "that a huge earthquake shakes the ground!"
        "The earth beneath your feet crumbles and you fall down, rolling together with mud and rocks."
        jump explore_cave_omens
    
    label explore_cave_omens:
        $ PARTY = [Player]
        stop music fadeout 2.0
        "When you open your eyes, a healty Ary stands before you..."
        show aryanna at topleft with dissolve
        ary "Are you my sister's friend?"
        ary "You fell down too!"    
        c "Ary!!"
        show ciry at topright with dissolve
        p "Aryanna! Aryanna! Are you ok?"
        ary "Hehe, it was fun!"
        p "Yes, Ciry... She... seems to be ok..."
        "Finally you can take a deep breath and try to calm down"
        c "[Player.sheet.name], are you ok?"
        p "Yes... I think, at least"
        c "What do we do now? You need to get back up here!"
        p "I know, I know..."
        scene 00005-827032856 with dissolve
        "As you look around, you realize that the place you fell into is net of natural underground tunnels"
        p "Maybe we can just walk through these tunnels and see if there is an exit somewhere else!"
        c "(worried) Walk throught the tunnels?"
        c "Well, it could be a good idea after all..."
        c "I'll try to walk around from up here and see if there is another exit!"
        hide ciry with dissolve
        p "Ok! Let's go south for now!"
        hide aryanna with dissolve
        "..."
        "And so, you and the little Aryanna set off walking inside those dimly lit tunnels"
        scene 00021-827032872 with dissolve
        play music ancientwinds fadein 2.0 volume 0.5
        $ renpy.pause()
        scene 00010-827032861 with dissolve    
        $ renpy.pause()
        "You go on and on, walking through this strange natural cave"
        show aryanna at topleft with dissolve
        ary "Big brother, look! There's a statue there!"
        "You follow with your eyes the direction Aryanna is pointing with her finger, and you see in the distance a"
        "white statue."
        hide aryanna with dissolve
        "As you get closer, you clearly distinguish a female body, half of the face was collapsed on the ground,"
        "but the other half was still clearly recognizable."
        "Something of that face triggered a memory in you, but you cannot immediately grasp it."
        p "{i}(This statue... is strangely familiar){/i}"
        window hide
        show 00008-3630713263 with annoytheuser:
            blur 75
        $ renpy.pause()
        scene 00010-827032861 with dissolve   
        p "{i}(That's it! This statue reminds me of that dream... But who is that woman?){/i}"
        p "{i}(Well, it's probably just a coincidence){/i}"
        """
        You walk and walk, through the tunnels of the cave.
        Sometimes there is water on the ground, little rivers. In the dimly lit depths of the cavern, you forge ahead, your small silhouettes barely discernible against the backdrop of the damp, rocky walls.
        The air hangs heavy with moisture, as if the very essence of the cavern seeped into your every breath.
        A gentle murmur echoes through the underground chamber, a symphony of droplets falling from stalactites to join the meandering streams tracing intricate patterns on the cavern floor.
        Armed with nothing but determination, the pair navigated the labyrinthine passageways, their steps reverberating softly in the vastness of the subterranean world.
        The occasional glistening pools reflected the feeble glow of their flickering torch, casting eerie shadows that danced across the ancient rock formations.
        As you venture deeper into the heart of the cavern, you notice a distant sound of rushing water, hinting at a potential exit. But as you delve deeper into the unknown, a menacing growl reverberates through the chamber.
        """
        play music cheezeecave fadein 2.0 volume 0.5
        show aryanna at topleft with dissolve
        ary "Gyaaaaaa!"
        show hobgoblin at topright with dissolve
        "A shadowy humanoid figure emerges from the darkness..."
        $ roll = 0
        $ creature = "creature"
        menu:
            "Roll D20 on Nature":
                $ roll = Player.roll_ability("intelligence")
        "ROLL: [roll.result]"
        if roll.result > 10:
            "You recognize the creature: it's an Hobgoblin!"
            p "{i}(What's a Hobgoblin doing here?){/i}"
            $ creature = "Hobgoblin"
        else:
            "You can't recognize the creature,"
            "even though you are sure you saw something similar on your beloved aventurer guide book."
        
        "The [creature]'s malicious eyes fixed upon you and the little gnome girl."
        hob "... Why YOU Heeere?"
        p "{i}(What? He... can speak?){/i}"
        "A beam of light illuminates the creature, revealing a metallic armor and a large unsheathed broadsword."
        hob "You... Witness..."
        p "{i}(What? Witness? Of What? What is he talking about?){/i}"
        hob "Witness... DIE!"
        p "Aryanna, run, RUN!"
        hide aryanna with dissolve
        hide hobgoblin with dissolve
        """
        You run through the cavernous surroundings, stumbling here and there on the uneven ground.
        You hear the hurried footsteps of the creature behind you. However, you manage to put some distance between you and the [creature], likely slowed down by the armor and the broadsword.
        Then, you find yourselves in a larger room, with a single rocky protrusion at the center, illuminated by light coming from an opening in the ceiling.
        """
        scene 00003-827032854 with dissolve
        $ renpy.pause()
        "There are no exits or tunnels"
        p "{i}(Oh no! It's a dead end!){/i}"
        "You hear the sounds of the approaching [creature] behind you, realizing there won't be time to go back to choose a different path."
        "You see the [creature] entering the room and slowing down it's pursuit. He's looking at the two of you like a cat with it's prey."  
        ary "Look, Big Bro! A sword!"
        p "I know Ary, he's got a big sword..."
        ary "No, there! There is a sword!"
        "You follow with your eyes the direction she is pointing with her hand."
        scene 00001 with dissolve
        pause
        "You realize that what you thought was just the upper part of that big rock at the center of the room, is instead something different. Almost entirely covered with moss and limestone deposits, it is barely recognizable:"
        "the hilt of an old sword lodged into the rock!"
        show aryanna at topleft with dissolve
        ary "Take the sword big Bro! You can fight with that sword!"
        hide aryanna with dissolve
        p "{i}(I don't think I can fight that [creature], but...){/i}"
        "And you rapidly look around, as for searching alternative solutions."
        p "{i}(Do I really have another choice?){/i}"        

        $ roll = 0
        $ pull_attempted = False
        $ drop_attempted = False
        menu:
            "Attempt to climb the wall to reach the opening (Athletics)":
                p "Aryanna, hurry! Maybe we can climb up and reach that hole in the ceiling!"
                $ roll = Player.roll_ability("strength")
                "ROLL: [roll.result]"
                "You attempt to climb the wall to reach the opening, but there are not enough handholds, and it's too steep."
                "You fall heavily to the ground."
                if roll.result < 10:
                    $ dmg = Roll("1d4").result
                    $ Player.take_damage(dmg)
                    "You take [dmg] points of damage!"
                else:
                    "But somehow you managed to fall without taking any damage."
                ary "Big Brother, get up please!"
                "The little gnome is worried, but she is not crying."
            "Attempt to pull the sword from the rock (Strength)":
                call pull_sword from _call_pull_sword
                
        ary "Hurry big Bro! Take the sword!"
        if not pull_attempted:
            menu:
                "Attempt to pull the sword from the rock (Strength)":
                    call pull_sword from _call_pull_sword_1
        p "(Breathing heavily due to the exertion) It's NOT... that... EASY!"
        p "{i}(Maybe I should stop this... maybe we can still run away!){/i}"    
        
        menu:
            "Attempt to run away":
                call drop_sword from _call_drop_sword
            "Attempt to pull the sword from the rock (Strength)":
                call pull_sword from _call_pull_sword_2

        p "{i}(It's no use!){/i}"
        if not drop_attempted:
            call drop_sword from _call_drop_sword_1
        "You can't pull the sword out of the rock. You can't let go of it and run away. You are trapped!"
        "But still, amidst this struggle, the warm sensation is there, weaving its way through you. A sensation of peace and harmony that seems paradoxically at odds with the imminent danger."

        menu:
            "Fight back the warm feeling and try to pull the sword (Strength)":
                call pull_sword from _call_pull_sword_3
                "In the meanwhile, the [creature] draws dangerously close: you have no choice but to fight!"
                pause
                $ battle(PARTY, [Hobgoblin])
            "Let the warm feeling possess you (Wisdom)":
                $ roll = Player.roll_ability("wisdom", advantage=True)
                "ROLL: [roll.result]"
                if roll.result > 1:
                    "SUCCESS"
                    stop music fadeout 1.0
                    scene bg black with annoytheuser
                    pause
                    "Silence"
                    "Void"
                    "There's nothing else around you now. Only Darkness. Then..."
                    window hide
                    scene bg white with annoytheuser
                    play music ascendingthevale fadein 2.0 volume 0.5
                    "Light"
                    window hide
                    "And in that light..."
                    window hide
                    show 00008-3630713263 with annoytheuser
                    alt """
                    Her eyes are closed, and she wears a calm, introspective expression. Her makeup is striking, with bold red lipstick and subtle eyeshadow that enhances her delicate features.
                    The background is a dreamy blend of deep blues and soft light streaks: a mystical or otherworldly setting.
                    """
                    pause
                    "Love"
                    "You sense the warmth emanating from the woman before you, like in a sunlit summer afternoon. The woman does not speak. Yet, you perceive meanings in your mind and through your emotions."
                    "{i}YOU ARE FINE JUST THE WAY YOU ARE{/i}"
                    "{i}YOU ARE LOVED{/i}"
                    scene bg white with annoytheuser
                    scene bg black with annoytheuser
                    "Afterward, you are once again abruptly pulled back into reality."
                else:
                    "In the meanwhile, the [creature] draws dangerously close: you have no choice but to fight!"
                    pause
                    $ battle(PARTY, [Hobgoblin])

        scene 00003-827032854 with dissolve
        play music heroicage fadein 2.0 volume 0.5
        "Before you realize it, the sword is coming out of the rock."
        ary "Yes big Bro! You can do it!"
        """
        But it's not really you pulling it, it's the sword itself pushing up to get out. And it's vibrating so hard that your arms ache! And still, you couldn't let go of the sword even if you would...
        You feel an otherworldly energy emanating from the sword. The little gnome girl watches in awe as the sword begins to glow, casting a soft, ethereal light.
        As the vibrations from the sword intensify, the air around you seems to shimmer, and an ancient power resonates through the cavern. The sword, once firmly embedded, now responds to an unseen force, as if it had a will of its own.
        As the vibrations peak, the sword leaps out of the rock, pushing you backward and almost causing you to lose your balance.
        You find yourself holding a weapon of extraordinary craftsmanship. The blade gleams with a radiant light, and a sense of purpose emanates from it.
        But the beauty of the sword lasts only for a moment... The blade reflects light into your eyes, dazzling you, and right after, you see it again as you had seen it before: an old, rusted, and heavily damaged sword.
        In the meanwhile, the [creature] draws dangerously close: you have no choice but to fight!
        """
        pause

        $ battle(PARTY, [Hobgoblin], can_lose=True)

        $ restore_party(PARTY)
        stop music fadeout 1.0
        "With his last mighty blow, the [creature] sends you sprawling across the cavern floor."
        "You struggle to open your eyes... Your head aches and your vision is compromised... "
        play music cheezeecave fadein 2.0
        show aryanna at topleft with dissolve
        ary "Big bro! Are you ok? You must get back on your feet!"
        hide aryanna with dissolve
        """
        Strangely, you find yourself still gripping the sword tightly in your hand.
        With the assistance of young Aryanna, you manage to rise on your feet.
        However, a multitude of doubts begin to weave through your mind, intertwining with a deep-seated fear that
        slowly takes hold, mingled with an overwhelming sense of desperation.
        As you stand there, sword in hand, your enemy slowly approaches, and a whispered uncertainty escapes your lips:
        """
        p "I don't know if I can win this fight..."

        menu:
            "{i}(Am I gonna die today?){/i}":
                p "{i}(Wait... I haven't done much of what I wanted to do in my life!){/i}"
                p "{i}(He will slay my flesh with that blade... It will be painful...){/i}"
                p "{i}(NO! I DON'T WANT! It can't HAPPEN!){/i}"
            "{i}(I Need to come up with something){/i}":
                p "{i}(This thing seems like a magic sword but...){/i}"
                p "{i}(I probably just don't know how to properly use it){/i}"

        p "{i}(Why am I in this situation? Was... Was it worth it?){/i}"

        menu:
            "{i}(Wait, maybe I can still run away...){/i}":
                p "{i}(Aryanna won't make it but WHO CARES... She will slow down the [creature], so that's even better){/i}"
                p "{i}(No one will ever know this... and I NEED TO SAVE MY LIFE!){/i}"
                p "{i}(There's nothing more important, right?){/i}"
                "You try to escape, but the sword get suddenly heavy, slowing you down."
                "You try to drop the weapon, but your hand is still locked on the hilt."
                "The [creature], sensing your desperate attempt to escape, launches another merciless attack!"
                $ battle(PARTY, [Hobgoblin])
            "{i}(I need to at least buy time for Aryanna to escape...){/i}":
                p "{i}(Yes, this way my death will not be in vain, at least...){/i}"

        play music heroicage fadein 1.0
        """
        Positioning yourself firmly between the menacing foe and the small gnome, an unwavering determination etches
        across your face.
        You take a deep breath and focus on the weapon tightly gripped in your hand.
        Strangely, you notice that the sword feels considerably lighter and more balanced than before.
        You never trained to wield a longsword, but now you feel it as if it has become a natural extension of your body.
        The air in the cavern becomes tense as you prepare for what is about to unfold.
        In a sudden onslaught, the enemy launches a ferocious attack!
        Drawing upon the agility and dexterity lessons from your days in the rogue's class, you skillfully use those
        teachings to avoid the enemy's blows
        """
        p "{i}(Wow, so this is how all those exercises pay off, huh?){/i}"
        "In a pivotal moment, a forceful blow, too potent to elude, hurtles towards you."
        "Aware that dodging would mean exposing Aryanna to peril, you instinctively use the sword to parry the blow."
        scene bg white
        "In an instant, a blinding surge of light pervades the cavern, as if the entire Sun chose that moment to unleash"
        "its brilliance."
        "An explosion propels you backward, leaving you sprawled on the ground, your senses awash in disorientation."
        scene bg white with dissolve
        pause    
        "As your senses gradually return, an enormous cloud of dust hangs in the air, obscuring the cavern."
        scene 00003-827032854 with dissolve
        p "Aryanna! Where are you?"
        "You rapidly scan the surroundings, searching for Ciry's little sister."
        ary "I'm here big bro... wha... what happened? There was that burst of light..."
        """
        She was just behind you. A bit dazed but ultimately unharmed.
        You notice you are still holding that strange sword.
        But the sword is not gleaming with light anymore, and it looks like a regular old rusty sword.
        Hundreds of metallic shards lie on the ground, likely the remnants of what once was the [creature]'s weapon.
        A harrowing scream echoes from the opposite side of the chamber. You then glance ahead to locate your enemy.
        The [creature] rises to its feet, cradling the arm that once wielded its weapon.
        To your astonishment, you realize that the arm is no longer there: it seems to have been disintegrated!
        The [creature] is now in a state of shock and agony.
        With one final snarl filled with rage and hatred, the [creature] flees, vanishing into the labyrinthine
        tunnels of the underground cave.
        """
        pause
        """
        You slowly shake off the dizziness, your head still spinning slightly from the impact.
        Suddenly you hear a familiar voice coming from above.
        """
        c "Aryanna! [Player.sheet.name]!"
        c "Are you there?"
        "Above, not far away, you manage to catch a glimpse of Ciry's familiar face through the dust cloud raised by the explosion."
        ary "Big sis! Yeah, we're here!"
        c "Oh Ary! Thanks the Blessed Eve!"
        c "Are you alright?!"
        ary "Yeah we're fine big sis..."
        p "Almost... at least"
        ary "Big bro defeated that bad monster with a magic sword!"
        c "What?"
        c "Anyway... You might be able to climb those rocks!"    
        jump chapter_3

    label pull_sword:
        if not pull_attempted:
            $ pull_attempted = True
            "As you touch the hilt of that old sword, a warmth unfolds within you. This sensation of calm and pure"
            "happiness reminds you of something."
            play music ascendingthevale fadein 4.0 volume 0.2
            "Yes, that dream."
            window hide
            show 00008-3630713263 with annoytheuser:
                blur 75
            $ renpy.pause()
            "You feel exactly as you did upon waking from that strange dream, where the image of that beautiful woman with"
            "white hair had appeared to you."
            hide 00008-3630713263 with annoytheuser
            play music cheezeecave fadein 2.0 volume 0.5
        $ roll = Player.roll_ability("strength")
        "ROLL: [roll.result]"
        if roll.result >= 15:
            "SUCCESS"
            "The sword seems like moving a very little bit, but the you feel a strange vibration coming from the sword."
            "It stops moving."
        else:
            "FAILED"
            "You try to pull out the sword, but it resists strongly, not budging an inch."
        return

    label drop_sword:
        "You try to let go of the sword, but strangely your hands do not respond."
        if not drop_attempted:
            $ drop_attempted = True
            "Your grip is still firm on the hilt."
            p "{i}(What happens? Am I paralyzed with fear?){/i}"
            p "{i}(No, this is something different... I just... can't open my hands!){/i}"
        return

    label cave_to_academy:
        # Scene transition from the cave
        # scene bg_cave_exit with fade
        # play music "music/epic_aftermath.ogg" fadein 2.0

        "The return to the surface was a blur of exhaustion and adrenaline. With Aryanna safe, and Ciry supporting her as the three of you climbed out of the cavern, the weight of the battle still lingered heavily in your mind."
        "The sword, now just a rusty, unremarkable blade, hangs at your side. But you can feel something within it, or perhaps within yourself—something has changed."

        c "You did it. You saved her. I—"
        "Ciry’s voice breaks as she glances at Aryanna, then back to you. Her expression is a mixture of gratitude and awe."
        c "I don’t even know what to say. Just… thank you."
        ary "Big bro was so cool! That glowing sword, the explosion—everything!"
        "You offer Aryanna a small smile, but her words make you uneasy. The memory of the light and the sudden power of the sword lingers in your mind, unanswered questions swirling like a storm."

        # scene bg_academy_gate with dissolve
        "By the time you make it back to the Academy gates, night has fallen. The familiar sight of the towers and courtyards is both comforting and surreal, as if you’re seeing it all for the first time."

        c "We’ll take Aryanna to the infirmary. They’ll check her over, just to be safe."
        ary "I’m fine, really! Big bro already took care of everything."
        "Despite her protests, Ciry insists, leading Aryanna toward the infirmary building."
        c "We’ll talk later, alright? I want to hear everything."
        "Her gaze lingers on you for a moment before she disappears into the building with her sister."

        # Player reflects on the events
        # scene bg_player_room_night with fade
        "That night, alone in your dormitory, you find yourself staring at the sword. It sits on the desk, its dull surface betraying none of the brilliance it displayed in the cavern."
        "You think back to the battle, to the surge of power, and to the strange, overwhelming presence you felt in that moment. The Silent Goddess. Was it really her? And why did she choose you?"

        menu:
            "Examine the sword":
                "You pick up the sword, turning it over in your hands. Despite its ordinary appearance, it feels… alive. Or maybe it’s you that feels different."
                p "(What exactly happened down there? And why me?)"
                "You spend hours turning the questions over in your mind, but no answers come."
            "Decide to let it go for now":
                "You leave the sword where it is, running a hand through your hair. The events of the day were too much, and you’re not sure you have the energy to confront them tonight."
                p "(Whatever happened, I’ll figure it out. Just… not now.)"
                "Sleep eventually claims you, though your dreams are restless and filled with flashes of light and the sound of Aryanna’s voice."

        # Transition back to normal life
        # scene bg_academy_courtyard with dissolve
        "The days that follow are a return to routine—or at least, they should be."
        "Despite attending lessons and continuing your training under Professor Tris, the events in the cavern weigh heavily on your mind. Ciry notices, of course. She always does."

        # scene bg_academy_classroom with dissolve
        tri "Focus."
        "Professor Tris’s voice snaps you out of your thoughts. She’s standing across the room, arms crossed, watching you carefully."
        tri "Whatever is distracting you, leave it at the door. A distracted rogue is a dead rogue."
        "You nod, muttering an apology, but her words stick with you. You know she’s right."

        # Conversation with Ciry
        # scene bg_academy_courtyard with dissolve
        "Later, during a rare free afternoon, you find yourself sitting with Ciry in the Academy courtyard. She’s flipping through a thick tome on magical theory, but her eyes keep darting toward you."
        c "You’ve been quiet lately."
        p "Just… thinking about everything that happened. The sword, the light. It’s hard to shake."
        c "I figured. Aryanna hasn’t stopped talking about it. 'Big bro’s magic sword,' she calls it."
        "She smiles, but there’s concern behind it."
        c "You know, if you want to talk about it, I’m here. Or if you’d rather not, that’s fine too. Just… don’t carry it alone, okay?"

        "Her kindness softens the tension in your chest, and you can’t help but smile a little."
        c "Actually, I was thinking… we haven’t had much time to just relax since everything happened. What do you say we hang out after lessons tomorrow?"
        p "Hang out? Like, just the two of us?"
        c "Yeah! I mean, unless you’d rather train or brood over the mysteries of glowing swords. I hear brooding is very 'rogue.'"
        "Her teasing tone makes you laugh despite yourself."
        p "Alright, alright. After lessons, then."
        c "It’s a date! Uh, I mean—not a date-date, obviously, unless… you know what, never mind. Tomorrow, courtyard, don’t forget!"
        "She grins and gathers her book, giving you a little wave as she heads back toward the dorms."

        # scene bg_player_room_night with dissolve
        "You return to your room, feeling a strange sense of normalcy for the first time since the cavern. Maybe things really are starting to settle down—or maybe this is just the calm before the next storm."

    
label chapter_3:
    # Discovery of the Statue of the Silent Goddess within the school and the book that Ciry gradually translates.
    # First encounter with Hooded-Woman
    # Meeting Theo and preparation for the school tournament
    label academy_intro_rogue:
        # scene bg_academy_classroom with fade
        # play music "music/academy_theme.ogg" fadein 2.0

        "The first months at the Academy have been intense—a mix of emotions and hard work. Each day begins early with one-on-one lessons focused on your role as a rogue."
        "You are the only student in the class of Professor Tris. Tris is a fascinating and enigmatic woman, always dressed in dark clothing, her steps so light she seems more shadow than person. Her voice is calm but carries an undeniable authority, and every word she speaks feels carefully measured."

        # scene bg_training_ground with dissolve
        tri "A rogue is not just some opportunist."
        tri "You are the eyes and hands of your party. The first to spot danger. The first to neutralize it."
        "Her gaze is unwavering as she walks ahead of you through the training grounds, her movements precise and silent."
        tri "Quieter."
        "You freeze mid-step, realizing your foot had grazed a loose stone."
        tri "Still too noisy. Try again."
        "Practical lessons with Tris are grueling. She has you navigating obstacle courses, disappearing into shadows, and disarming traps. Every mistake is met with a calm correction, every success with a faint nod of approval."

        # scene bg_library with dissolve
        "Afternoons are often spent in the library, surrounded by ancient tomes and intricate diagrams of traps."
        tri "This one."
        "She places a finger on a yellowed page, pointing to an elaborate mechanism."
        tri "Designed to ensnare an entire party of adventurers. But a clever rogue would know how to bypass it."
        "You lean closer, captivated by the detailed illustration. The more Tris explains, the more her vast knowledge becomes apparent."
        p "How do you know so much about these traps?"
        tri "Experience."
        tri "You’re not the first student I’ve trained. Nor, I hope, will you be the last."

        # scene bg_academy_courtyard with dissolve
        "Despite the intensity of your lessons, Tris ensures you have moments of reprieve. Often, you find yourselves in the Academy courtyard, her leaning casually against a tree while quizzing you."
        tri "If you found a room with three chests and only one disarm kit, which would you choose? And why?"
        "Her tone is teasing, but her sharp eyes study your reaction."
        menu:
            "Answer confidently":
                p "The middle chest. It’s often the most heavily guarded, which means it likely contains the best treasure."
                tri "Interesting. And if you’re wrong?"
                p "Then I learn something for next time."
                tri "(smiling faintly) A good answer. Calculated risk is key."
            "Answer hesitantly":
                p "The chest closest to the exit... it’s probably a decoy, but it’s the safest choice."
                tri "Safety is important, but hesitation can cost lives. A rogue must learn to trust their instincts."
            "Admit uncertainty":
                p "I’m not sure. Maybe I’d wait and see if there were clues nearby?"
                tri "Clever. Observation is often more important than action. Use the environment to your advantage."

        # scene bg_dormitory_night with dissolve
        "Evenings in the dormitory are solitary, but occasionally, Tris visits, bringing a small chest filled with training tools."
        tri "Show me how you’d open this."
        "She places the chest on your desk, leaning against the window as moonlight filters into the room."
        "No matter how tired you are, her presence is motivating, and you find yourself focusing intently on the task. The faint click of the lock finally breaking earns you a rare smile from her."
        tri "Good. You’re improving."

        # scene bg_academy_classroom with dissolve
        "As the weeks pass, Tris becomes more than just your teacher. She’s a guide, a mentor, and at times, a puzzle you’re eager to unravel."
        tri "One day, outside these walls, you’ll find yourself in situations where no one can guide you."
        tri "But if you remember what you’ve learned here, you’ll survive any challenge."
        "Her words stay with you, a mix of comfort and weight. Each lesson feels like a step into the unknown, but with her guidance, you begin to see your potential—not just as a rogue, but as someone destined for something greater."


    label orc_vs_mage_conflict:
        # Scene setup
        # scene courtyard_day with fade
        # play music "tense_argument.mp3"
        "As you walk through the academy courtyard, the sounds of a heated argument catch your attention. A crowd of students has gathered, forming a loose circle around the commotion."
        "Pushing through the crowd, you see her—an imposing, muscular half-orc girl, her expression furious, towering over a smaller, sharply dressed boy. It's the same girl you noticed in the cafeteria a few days ago."
        # show orc_girl_angry at left
        # show mage_boy_arrogant at right
        "The boy, his robes finely embroidered with arcane symbols, sneers at the half-orc girl with open disdain. His tone is dripping with contempt."        
        dan "Listen here, you filthy *Half-Blood*. Know your place before you embarrass yourself further."        
        "The half-orc girl clenches her fists, her muscles tensing. Her voice booms with fury as she steps closer to him."
        the "Ye wanna say that 'gain, eh? Ye lil' worm? Say it, an' I’ll knock yer teeth down yer throat!"        
        dan "Oh, I will. Your kind doesn't belong here, let alone in the academy. Barbaric brute!"
        "The crowd murmurs in anticipation, and you notice several larger boys standing behind the mage, smirking and cracking their knuckles. It's clear they're his lackeys, ready to back him up."
        # show orc_girl_tense at left
        "The half-orc girl glances around, her defiant expression faltering just slightly as she realizes she's outnumbered. Still, she doesn't back down."
        the "Oh, ye think I’m scared o’ yer lot? Bring it! I’ll bash yer skulls in, one by one!"
        "The tension in the air is palpable, and you feel the weight of the moment pressing down on you. You can't just stand by."
        
        menu:
            "Side with the Half-Orc Barbarian Girl":
                $ alliance = "the"
                jump side_with_orc
            "Side with the Noble Mage Boy":
                $ alliance = "dan"
                jump side_with_mage
            "Stay neutral and walk away":
                $ alliance = "neutral"
                jump stay_neutral

    label side_with_orc:
        $ Player.achievements.append("Side with Theo")
        $ Theo.approval += 10
        "You step forward, placing yourself between the half-orc girl and the mage boy, your heart racing."        
        p "That's enough! Leave her alone. She hasn't done anything to deserve this."        
        # show mage_boy_shocked at right
        "The mage looks at you in disbelief, his smirk replaced by annoyance."
        dan "You're siding with *her*? Figures. Another fool to join the brutes."
        # show orc_girl_surprised at left
        "The half-orc girl looks at you with a mixture of surprise and gratitude. For a moment, her furious expression softens."
        the "Eh, ye got guts, I’ll give ye that. Thanks fer steppin’ in."
        "The mage boy scoffs, signaling to his lackeys."
        dan "Fine. Let's see if your little alliance can handle what's coming next. Let's go, boys."
        "He storms off, his lackeys following closely behind, though their glares linger on you."
        "The crowd begins to disperse, and the half-orc girl turns to you with a nod of appreciation."
        the "Name’s Theo. Ye ain’t half bad, y’know. Not many folk’d do what ye just did."
        p "It was the right thing to do."
        "You sense that you've made an ally today. One whose strength and courage might come in handy in the future."
        "(Theo's approval: +10)"
        jump after_conflict

    label side_with_mage:
        $ Player.achievements.append("Side with Dante")
        "You step forward, aligning yourself with the mage boy and his lackeys. The half-orc girl narrows her eyes at you, betrayal flickering across her face."

        p "Maybe you should learn to control your temper. This academy isn't the place for threats and violence."
        
        # show orc_girl_hurt at left
        "The half-orc girl glares at you, her anger briefly replaced by a hint of hurt."

        the "Figures. Just another coward siding with the bullies."

        # show mage_boy_smirk at right
        "The mage boy chuckles, his arrogance growing."

        dan "Smart choice. At least someone here understands how things work."

        "The crowd begins to disperse as the half-orc girl storms off, her shoulders tense with barely contained fury."

        dan "I'll remember this. Maybe you're not as hopeless as the rest of them."

        "You've clearly made an impression on the mage boy and his circle, though you can't help but wonder if siding with him was the right decision."
        jump after_conflict

    label stay_neutral:
        "You hesitate, unsure of how to act. The tension is thick, but ultimately, you decide not to get involved."
        "The half-orc girl and the mage boy exchange a few more heated words before the crowd begins to disperse."
        "You walk away, leaving the conflict unresolved. Whether it was the right choice or not, you'll never know."
        jump after_conflict

    label after_conflict:
        "With the confrontation behind you, you reflect on what just happened. The choices you made today might shape your future relationships at the academy."

    label ch3_choices_1:
    menu:
        "Date with Ciry":
            label date_with_ciry:
                # Scene Setup
                # scene bg_academy_garden with fade
                "After rescuing Aryanna, you and Ciry decide to take a quiet walk in the academy gardens. The evening is calm, the moon casting a gentle glow over the carefully tended plants and pathways."
                "Ciry walks beside you, her usual confident demeanor softened by relief and gratitude."

                c "Thank you, [Player.sheet.name]. For everything. Aryanna means the world to me, and... I don't even want to think about what could've happened if you hadn't been there."

                p "You don't have to thank me, Ciry. I couldn't just stand by and do nothing."
                c "Still... it means a lot to me. And to her. I think she'll be talking about her 'big hero' for weeks."
                "Ciry smiles warmly, but her eyes betray a hint of curiosity. You can tell she's still thinking about the events in the cavern."

                menu:
                    "Ask about the magic sword and the Silent Goddess":
                        $ Player.achievements.append("Ciry knows")
                        p "Ciry, I need to ask you something. That sword I used in the cavern... and that light. It wasn’t normal, was it?"
                        c "No, it definitely wasn’t. I've seen magic weapons before, but that was... different. And Aryanna mentioned you saying something about a goddess?"
                        p "Yeah. The Silent Goddess. I felt... something. Like she was guiding me. But I don't understand why or how."
                        "Ciry looks thoughtful, her brow furrowed in concentration."
                        c "The Silent Goddess... As I was telling you that day, she’s more of a myth than anything, but some ancient texts mention her as a protector of lost souls and outcasts.
                        If you’re connected to her somehow, it might explain why that sword reacted to you."
                        p "Do you think we can find more about her? Or the sword?"
                        c "Absolutely. If you’re willing, we can look through the academy archives together. They’re extensive—maybe we’ll find something useful."
                        "Her determination is contagious, and you feel a surge of hope. With Ciry by your side, the mystery of the Silent Goddess doesn’t seem so insurmountable."
                        c "And hey, you’re not alone in this. Whatever this connection is, we’ll figure it out. Together."
                        "You can’t help but smile at her words, grateful for her unwavering support."

                    "Be vague and dismiss Aryanna's words":
                        p "Aryanna probably just imagined things. She was scared—it’s not surprising that her mind would play tricks on her."
                        "Ciry raises an eyebrow, clearly unconvinced, but she doesn’t press the issue."
                        c "Maybe. But that light... it wasn’t exactly subtle, [Player.sheet.name]. Whatever happened down there was powerful. I just hope you’re okay."
                        p "I’m fine, really. And maybe it’s better if we just leave it at that for now."
                        "She nods slowly, though her eyes linger on you, searching for something you’re not ready to share."
                        c "Alright. But if you ever want to talk about it, I’m here. No secrets, okay?"
                        "Her words make you feel a pang of guilt, but you nod, grateful that she’s willing to let it go for now."

                # Continue the date
                "The conversation shifts to lighter topics as the two of you continue your walk through the gardens. Fireflies dart through the air, their soft glow adding to the serene atmosphere."
                "After a while, you find yourselves sitting on a bench under a sprawling willow tree."
                c "You know, [Player.sheet.name], you’re full of surprises. First, you save my sister, and now... well, let’s just say I’m glad you’re on my side."

                menu:
                    "Flirt with Ciry (geeky approach)":
                        p "What can I say? I aim to impress. But honestly, I think the real surprise is how you manage to look so... captivating while talking about magical theory for hours."
                        "Ciry freezes for a moment, her cheeks turning pink as she processes your words."
                        c "C-Captivating? You’re just saying that because I went on that rant about planar binding last week."
                        p "Not at all. I mean, who else can make complex arcane equations sound so fascinating? You’re like a walking magical encyclopedia... except way more charming."
                        "She lets out a laugh, clearly flustered but also pleased."
                        c "You’re such a dork. But, uh... thanks. I think."

                    "Keep it friendly":
                        p "I’m just glad everything worked out. Aryanna’s safe, and that’s what matters."
                        "Ciry smiles warmly, her usual confident demeanor replaced by something softer."
                        c "Yeah. It does. And I owe you for that."

                "The evening stretches on, the two of you sharing stories, laughter, and a newfound closeness."

            jump ch3_choices_1

        "Date with Gwen" if "First date with Gwen" in Player.achievements and "Second date with Gwen" not in Player.achievements:
            $ Player.achievements.append("Second date with Gwen")
            label gwen_second_date:
                show gwen_student at topleft with dissolve
                # scene bg academy_path_night with fade
                "The two walk back towards the Academy under the glow of moonlight, their conversation easy and relaxed."                
                gwe "You're not bad company for a quiet guy, you know that?
                Tell you what—why don't you come back to my place for a bit? I've got something to show you."                
                menu:
                    "Agree to go with her":
                        p "Alright, sure. Lead the way."
                        jump gwen_house

                    "Politely decline":
                        p "Thanks, but I should probably head back. It's getting late."
                        gwe "(smirking) Fair enough, new boy. Maybe next time."
                        hide gwen_student with dissolve
                        jump ch3_choices_1

            label gwen_house:
                # scene bg gwen_house_interior with fade
                "Gwen leads [Player.sheet.name] to a small but cozy house nestled on the outskirts of the Academy grounds. Inside, it's filled with curiosities: strange books, glimmering crystals, and faintly glowing runes etched into the walls."                
                gwe "Make yourself at home. I'll be right back."                
                "She disappears into another room, leaving [Player.sheet.name] to nervously take in his surroundings. Something about the place feels... different, though he can't quite put his finger on it."                
                # scene bg gwen_house_dark with dissolve
                "When Gwen returns, her demeanor has shifted. The playful grin remains, but her eyes glow faintly, and the air around her seems charged with an unfamiliar energy."                
                gwe"You're a sweet guy, [Player.sheet.name]. I like that about you. But there's something you should know about me..."
                hide gwen_student with dissolve
                """
                "Her form begins to change subtly. Her eyes burn brighter, small horns appear on her head, and a tail flicks into view behind her."
                When Gwen reveals her true succubus form, the transformation is as breathtaking as it is unsettling.
                The youthful charm of her academy disguise—a petite teenage girl with bright, mischievous eyes and a playful smile—is completely shed.
                In its place stands a vision of mature, otherworldly beauty that exudes power and centuries of practiced seduction.
                Gwen's stature shifts dramatically. She now stands taller, her posture commanding and poised, with a natural grace that makes every movement seem deliberate and alluring.
                Her body is no longer girlish but fully matured, with a perfect balance of athleticism and voluptuousness. Her curves are emphasized in a way that feels almost supernatural—designed to draw the eye and capture attention.
                Her previously soft, pale skin takes on a slight iridescent glow, like moonlight shimmering on a darkened sea. There's a faint hint of crimson along her shoulders and arms, a subtle reminder of her infernal nature.
                Small runic patterns etched in faint gold appear across her skin, pulsating faintly as if alive with magic.
                Gwen's eyes, once bright and playful, now blaze with an intense, glowing crimson hue, framed by thick, dark lashes.
                They seem to pierce directly into the soul, conveying a depth of knowledge and an unspoken promise of ecstasy—and danger.
                Her short, playful haircut elongates into flowing locks of deep, jet-black hair streaked with hints of crimson. Her hair seems almost alive, swaying gently as if caught in an unseen breeze, adding to her otherworldly allure.
                Two sleek, curved horns spiral elegantly from her temples, glossy black with subtle red veins that pulse with heat. They give her an air of regal dominance, as if she's a queen of her infernal realm.
                From her back sprout enormous bat-like wings, their leathery surface marked with faint, glowing runes similar to those on her skin. The wings fold and unfurl gracefully, their movements hypnotic and predatory.
                Her tail, long and sinuous, moves with a mind of its own. It is tipped with a spade-like shape that glimmers faintly, catching the light in a way that seems both playful and threatening.
                Her academy uniform dissolves into a flowing, form-fitting gown of deep black and crimson. The fabric shimmers like liquid obsidian, clinging to her curves while leaving parts of her shoulders, back, and legs daringly exposed.
                The edges of the gown are embroidered with intricate golden patterns resembling infernal script.
                A choker of dark metal adorned with a single ruby rests around her neck, glowing faintly like a heartbeat. Her fingers are adorned with ornate rings, their gemstones pulsating with a faint inner light.
                Gwen's voice, once playful and teasing, becomes richer and more resonant, dripping with confidence and seduction. It's the kind of voice that wraps around you, drawing you closer even when every instinct tells you to run.
                The air around her seems to ripple with heat, not uncomfortable but disorienting, like standing too close to a fire. Her presence is almost magnetic, impossible to ignore, as if every movement and gesture is calculated to ensnare attention.
                A faint, intoxicating aroma follows her, a mix of jasmine, dark spices, and something ineffable that stirs primal instincts.
                """
                show gwen_succubus at top with dissolve
                
                menu:
                    "Roll a D20 on Nature":
                        $ roll = Player.roll_skill("nature")
                "ROLL: [roll.result]"
                if roll.result >= 10:
                    p "(shocked) Y-you're... a Succubus?"
                else:
                    p "(shocked) What... What are you?"
                    gwe "(smiling warmly) Never heard about Succubus, dear?"                
                gwe "(softly) Guilty as charged. Don't worry, I'm not here to hurt you. I just... wanted to see if you'd trust me. And you did."
                
                menu:
                    "React with fear":
                        p "I-I need to go. I'm sorry, Gwen."
                        gwe "(sighing) I understand. Just remember, I never meant to scare you."

                    "React with curiosity":
                        p "Why reveal this to me? Why take the risk?"
                        gwe "Because I'm tired of hiding. And maybe, just maybe, I thought you'd understand."

                    "React with acceptance":
                        p "(smiling nervously) Well... you're still Gwen, right? I guess that doesn't change anything."
                        gwe "(smiling warmly) You're something else, [Player.sheet.name]. I think I like you even more now."

            label gwen_confession:
                # scene bg gwen_house_dark with fade
                "Your breath catches as Gwen steps closer, her glowing eyes locked onto yours. The air around her feels heavier, almost suffocating, but her voice remains soft and alluring."                
                gwe "You see, [Player.sheet.name], there's a little more to me than just being a mischievous girl at the Academy."                
                "She tilts her head, her horns catching the faint light of the runes on the walls. Her tail flicks lazily behind her as she gazes at him with a mix of amusement and something deeper—something darker."
                gwe "I have a habit, you might say. A... special arrangement with the students I bring home."
                p "(uneasy) W-what kind of arrangement?"                
                gwe "I make them feel things they've never felt before. Pleasure beyond their wildest imagination. I take them to heights they didn't even know existed. And they love it, [Player.sheet.name]. Every second of it."
                "Her smile sharpens, a glimmer of something predatory in her expression."
                gwe "But, of course, such ecstasy comes at a price. Nothing in this world is truly free, after all."
                p "(nervously) The price...? What are you saying?"
                gwe "(leaning in) Their souls, [Player.sheet.name]. I take their souls. It's what sustains me. Keeps me alive, keeps me... powerful."
                "You stumble back slightly, your pulse racing as her words sink in. Your gaze darts to the strange runes on the walls, to the faint, otherworldly glow in her eyes."
                gwe "(softly) Don't look so scared, darling. It's not as bad as it sounds. Most of them didn't even care—they were too lost in the moment to notice what they'd given up."                
                "She takes another step closer, her voice dropping to a sultry whisper."                
                gwe "But you're different, aren't you? So sweet, so nervous... I couldn't resist you. And now, here you are, in my home, all to yourself."
                
                menu:
                    "Confront her with fear and anger":
                        p "(shouting) So this is what you do? You lure people in just to destroy them? That's... that's monstrous!"
                        gwe "(smirking) Oh, [Player.sheet.name], don't be so dramatic. I never force anyone—they all agree in the end. Even the ones who protest at first."
                        "You back away, heart pounding, desperately scanning for an escape route."

                    "Challenge her with courage":
                        p "(firmly) If you think I'm going to just let you take my soul, you've got another thing coming. I'm not like the others."
                        gwe "(laughing softly) Oh, darling, that's what they all say. But we'll see, won't we?"

                    "Appeal to her humanity":
                        p "(gently) Gwen... if you really liked me, why would you do this? There has to be another way."
                        gwe "(pausing) Another way...? You think you can change me, [Player.sheet.name]? Save me from what I am?"
                        "For a brief moment, her expression softens, but it's quickly replaced by a knowing smirk."
                        gwe "You're adorable. But I wonder—are you willing to bet your soul on it?"

                menu:
                    "Try to escape":
                        jump escape_gwen
                    "Accept her offer":
                        jump accept_gwen_offer 

            label escape_gwen:
                "Your mind races. Every fiber of your being screams for you to get out, to leave this dangerous and enchanting creature behind."                
                p "(thinking) I can't stay here. I need to find a way out before it's too late."
                "As Gwen steps closer, her glowing eyes pinning you in place, he spots the faint outline of the door behind her."                
                gwe "What's the matter, darling? Second thoughts? You're not thinking of leaving, are you?"
                
                menu:
                    "Attempt to distract her":
                        menu:
                            "Roll a D20 on Performance":
                                $ roll = Player.roll_skill("performance")
                        "ROLL: [roll.result]"
                        if roll.result >= 10:
                            p "(nervously) No, I just... I need some time to think about all this. It's a lot to take in."
                            gwe "(smirking) Oh, [Player.sheet.name], you're adorable when you're scared. But alright, I'll give you some space. Just don't run—I'd hate to have to chase you."                        
                            "As she steps back, [Player.sheet.name] bolts for the door, adrenaline propelling him forward. Gwen's laughter echoes behind him as he throws the door open and runs into the night."                        
                            "The Academy grounds blur past him as he sprints back to the safety of the dorms, his chest heaving and heart pounding. He doesn't look back, but her voice lingers in his mind, a soft, sultry promise."                        
                            gwe "(off-screen) You can run, [Player.sheet.name], but you'll be back. They always come back..."   
                            jump ch3_choices_1
                        else:
                            "You try to distract her, but she cannot be fooled so easily..."

                    "Try to overpower her":
                        menu:
                            "Roll a D20 on Athletics":
                                $ roll = Player.roll_skill("athletics")
                        "ROLL: [roll.result]"
                        if roll.result >= 10:
                            "You clench your fists, your fear replaced by a surge of defiance. You grab a nearby chair and hurl it in Gwen's direction."                        
                            gwe "(laughing) Really? You think that's going to stop me?"                        
                            "The distraction works just long enough for you to dart past her. You fell her claws graze your shoulder as you dive through the door, slamming it shut behind you."                        
                            "You don't stop running until you're far from her house, your breaths ragged and heart pounding. Safe for now, but her parting words haunt you."                        
                            gwe "(off-screen) You're fun, [Player.sheet.name]. I hope we get to play again soon..."
                            jump ch3_choices_1
                        else:
                            "You lunge forward, trying to shove Gwen aside with all your strength. But to your shock, her hand shoots out, grabbing your wrist effortlessly."
                            "Her grip is firm, almost unyielding, as if you've run into an unmovable force."                            
                            gwe "Tsk, tsk. Such impatience."
                            "She steps closer, her other hand brushing against your shoulder to steady you—or perhaps to remind you of how firmly she's in control."                            
                            "You struggle against her hold, but her strength is far beyond what you expected. The faint scent of her perfume fills the air as her face draws nearer to yours."                            
                            gwe "I told you, there's no running from me. Not until I allow it."
                            "Her tone softens, almost playful, but there's a dangerous edge to her words. Her eyes bore into yours, daring you to try again."
                            "Your body tenses as she pushes you backward, pinning you lightly against the nearby wall. It's not painful, but her dominance is unmistakable."                            
                            gwe "You're strong... but not strong enough."
                            "Her breath brushes against your cheek as her fingers linger on your wrist, a subtle reminder of her power over you."

                            menu:
                                "Keep resisting":
                                    "You thrash, trying to break free, but it's like fighting against a storm. Gwen's grip tightens just enough to still your movements."
                                    gwe "Shhh... Relax. You'll only hurt yourself like this."
                                    "Her voice is laced with a strange mixture of authority and gentleness. Despite yourself, you begin to feel your strength ebb away."
                                    jump surrender_to_gwen
                                "Stop struggling":
                                    "Realizing that resistance is futile, you let your body relax under her hold. She notices your surrender with a smirk."
                                    gwe "Good. Much better."
                                    jump surrender_to_gwen

                label surrender_to_gwen:
                    "Gwen releases you, though her presence still feels like an invisible chain keeping you rooted to the spot."
                    gwe "See? That wasn't so hard, was it?"
                    "Her fingers trail along your arm as she steps back, a gesture as much about control as it is about mockery."                    
                    "You take a deep breath, unsure whether to feel anger, fear, or something else entirely."
                    gwe "(smiling softly) Let me take care of you. Just relax."                            
                    "Gwen guides you gently, her power overwhelming yet strangely comforting. You feel yourself slipping, but her warmth keeps you grounded until the very end."                            
                    "As you open your eyes, you know something is different. Gwen stands before you, her expression unreadable."                            
                    gwe"You're stronger than most, [Player.sheet.name]. Perhaps you'll even survive this... for a while."                            
                    "You don't know what she means, but for now, you choose to believe her. The bond between them is undeniable, even if it came at a cost you can't fully comprehend."
                    jump soul_anchor

                label accept_gwen_offer:
                    "Your fear battles with a strange, unshakable curiosity. You meets Gwen's glowing eyes and take a shaky breath."            
                    p "(hesitant) If this is what you are... then I guess I'm willing to take the risk."                    
                    gwe "(surprised) Oh? You're full of surprises, [Player.sheet.name]. I didn't expect you to give in so easily. Or maybe I underestimated you."                    
                    "She steps closer, her presence overwhelming, but her smile holds a warmth that feels oddly genuine despite the danger."                    
                    gwe "(softly) I'll admit, I've grown fond of you. So I'll make this special for you. No tricks, no games. Just... bliss. Are you ready?"                    
                    p "I'm ready. Just... go easy on me."
                    gwe "(laughing) Oh, [Player.sheet.name], I'll make it worth your while. Trust me."                    
                    "Gwen reaches for you, her touch igniting a cascade of sensations that defy explanation. For a fleeting moment, all your fears dissolve, replaced by a euphoria that consumes you entirely."
                    "But deep in the back of your mind, you feel something slipping away—a piece of yourself you might never recover."
                    "When it's over, you're left breathless, the glow in Gwen's eyes dimming slightly as she gazes at you with a mix of satisfaction and regret."                    
                    gwe "You were... extraordinary, [Player.sheet.name]. I'll never forget you."                    
                    "He sinks into the chair, his soul now hers, but a part of him doesn't care. The experience was worth it—or so he convinces himself."
                            
            label soul_anchor:
                "You sit up slowly, your head spinning from the overwhelming sensations you just endured. Your body feels... intact, but there's an unfamiliar warmth in your chest, like something ancient and powerful is stirring within you."
                "Gwen watches you, her confident smirk faltering for the first time. Her glowing eyes narrow as if trying to pierce through a veil she's never encountered before."                
                gwe "This... this doesn't make sense."                
                p "(groggily) What are you talking about? I thought... you said you'd take my soul."                
                "She steps back, her tail flicking agitatedly as she studies you like a puzzle she can't solve."
                gwe "(muttering) I did. Or at least, I tried. I've never failed before—not in centuries. But you... you're still here."
                "[Player.sheet.name] blinks, confusion mingling with the faint remnants of fear. He places a hand on his chest, feeling the steady thrum of his heartbeat."
                p "I'm... alive?"                
                gwe "(narrowing eyes) Barely. Something is keeping your soul anchored to your body, something strong. Stronger than anything I've ever encountered."
                "She paces, her claws clicking against the stone floor as she mutters to herself."
                gwe "It's like... there's a shield around it. No, not a shield—more like chains. Bound tightly to something I can't touch. What in the Nine Hells are you?"
                
                menu:
                    "Deny knowing anything about it":
                        p "I have no idea what you're talking about! I'm just... me. Nothing special."                        
                        gwe "(sharply) No one who's ‘just them' survives me, [Player.sheet.name]. You're hiding something, even if you don't know it."                        
                        "She leans in, her glowing eyes boring into his, her voice low and dangerous."                        
                        gwe"I'm going to find out what makes you so different, and when I do, you'd better hope it doesn't make you more valuable to me."
                        
                    "Tell her about the sword":                        
                        gwe "(intrigued) Interesting. You're not lying, are you? No, you don't even know what you're hiding."                        
                        "Her smile returns, though this time it's less predatory and more curious, almost amused."                        
                        gwe"Well, aren't you the most fascinating little mystery? Maybe keeping you around will be more entertaining than I thought."                       
            
            jump ch3_choices_1

        "Date with Theo" if "Side with Theo" in Player.achievements:            
            label date_with_theo:
                # scene park_evening with fade
                # play music "gentle_evening_theme.mp3"

                "You and Theo decide to spend some time together in the academy’s beautiful park. The sun is setting, painting the sky with hues of orange and pink."

                # show theo_happy at left
                the "Well, ain’t this a fine evenin’, eh? This place be lookin' like somethin’ outta one o’ them bard tales. All shiny-like an’ calm."

                "Theo stretches her muscular arms and takes a deep breath of the fresh evening air."
                the "So, whatcha wanna do, eh? We could mess about, or jus’ sit an’ chat. Yer call."

                menu:
                    "Go for a walk together":
                        $ affection += 5
                        "You suggest taking a walk around the park, enjoying the scenery together."
                        the "Aye, a walk’s soundin’ nice. Let’s stretch them legs an’ see what we find."
                        jump date_walk

                    "Sit by the lake and talk":
                        $ affection += 10
                        "You suggest sitting by the lake to relax and chat."
                        the "Eh, a quiet sit-down don’t sound too bad. Guess I can handle not punchin’ somethin’ fer a while."
                        jump date_lake

                    "Challenge her to an arm-wrestling match":
                        $ affection += 15
                        "You playfully challenge Theo to an arm-wrestling match."
                        the "Ha! Ye sure 'bout that, mate? Me strength ain’t fer show, y’know!"
                        jump date_armwrestle

            label date_walk:
                # scene park_path with fade
                "You and Theo stroll along the park's winding paths, surrounded by trees and flowers."

                the "This place be all quiet-like, huh? Don’t get me wrong, I like bashin’ heads, but sometimes, a bit o’ peace is nice too."
                "Theo glances at you with a grin."
                the "Ye ever think 'bout how small we is, standin' in all this big world? Makes ye wonder, don’t it?"

                menu:
                    "Agree with her sentiment":
                        $ affection += 5
                        "You nod, agreeing that the world feels vast and awe-inspiring."
                        the "Aye, glad ye see it too. Life’s a big ol’ mystery, an’ we just tryin’ to make sense of it."

                    "Tease her for being philosophical":
                        "You joke about her sudden philosophical side."
                        the "Oi, don’t go thinkin’ I’m all brawn an’ no brains! Even a barbarian’s got thoughts, y’know!"

                "As you continue walking, Theo’s tone turns more serious."
                the "Ye know, I weren’t always wanderin' about like this. When I was little, I... weren’t treated too kind. Got sold as a slave, y’see. Some right nasty folk bought me, wanted me fer... fightin’, mostly."
                "She clenches her fists, her cheerful demeanor briefly fading."
                the "But then, one day, a group o’ paladins stormed in. Proper shiny folk, with big ol’ swords and hearts bigger than mountains. They saved me, they did."
                the "Ever since, I been dreamin’ o’ bein’ like 'em. But this academy... they said I ain’t got the 'references.' Fancy word fer sayin’ I ain’t noble enough, I reckon."
                the "So here I am, swingin’ axes instead. Ain’t a bad life, but... someday, I’ll show 'em. I’ll be a paladin, just like them who saved me."
                "You walk in silence for a while, letting her words sink in."
                jump date_end

            label date_lake:
                # scene lake_evening with fade
                "The two of you find a quiet spot by the lake, the water shimmering in the fading light."

                the "This here’s nice. Don’t reckon I’ve spent much time jus’ sittin’ by a lake afore."
                "Theo skips a stone across the water, her strength sending it skipping farther than you expected."
                the "What 'bout you, mate? What’s yer idea of a good time? Punchin’ goblins? Climbin’ mountains? Or somethin' else?"

                menu:
                    "Say you enjoy adventuring":
                        "You tell Theo you love the thrill of adventuring, just like she does."
                        the "Ha! Knew we was alike. Ain’t nothin’ better than a good fight an’ a stiff drink after!"

                    "Say you enjoy quiet moments like this":
                        $ affection += 5
                        "You tell her you enjoy moments of peace and quiet, like this one."
                        the "Aye, I guess there’s somethin’ special 'bout it. Sittin' here with ye makes it even better."

                "Theo looks at the lake for a moment, her expression softening."
                the "Ye know, this calm... it’s rare fer me. When I was a wee lass, there weren’t no calm. Got sold off like a piece o’ meat. Life as a slave ain’t no life at all."
                the "But then, some paladins came. They cut through them bastards like butter an’ freed me. Saved me life, they did. I been dreamin’ o’ bein’ like 'em ever since."
                the "This academy, though... They don’t think I’m paladin material. So they shoved me in the barbarian class. But I’ll prove ‘em wrong. One day, I’ll make 'em see."
                "You feel a new sense of respect for Theo as she opens up about her past."
                jump date_end

            label date_armwrestle:
                # scene park_table with fade
                "You and Theo find a sturdy table, and she eagerly sets her arm on it, ready for the challenge."

                the "Alright, mate, give it yer best shot! But don’t go cryin’ when I wipe the floor with ye!"
                "You grip Theo’s hand, her calloused palm strong and steady. The two of you lock eyes as the match begins."

                menu:
                    "Try to win with all your strength":
                        "You put everything you have into the match, straining against Theo’s strength."
                        "She grins as she easily overpowers you, slamming your arm down."
                        the "Ha! Told ye I’m the strongest! But good on ye fer tryin’, mate."

                    "Pretend to struggle but let her win":
                        $ affection += 10
                        "You put up a show of resistance but ultimately let Theo win."
                        the "Hah! I knew I’d win! Yer tough, but I’m tougher! Still, good match, eh?"

                    "Use a clever trick to distract her and win":
                        "You feint a distraction, causing Theo to briefly lose focus. Taking the chance, you slam her arm down."
                        the "Oi! That weren’t fair! But I gotta hand it to ye—yer clever, I’ll give ye that."

                "Theo laughs heartily, but as the laughter fades, she grows thoughtful."
                the "Ye know, strength’s always been me thing. Had to be, growin’ up. Weren’t no one there to protect me but meself—at least until them paladins showed up."
                the "They saved me from the worst, and I swore I’d be like ‘em one day. But this academy thinks I’m naught but a brute. Bah, I’ll show 'em what I’m made of."
                "Her determination is palpable, and you can’t help but admire her resolve."
                jump date_end

            label date_end:
                scene park_night with fade
                "As the evening comes to an end, you and Theo make your way back to the academy, the bond between you stronger than ever."

                the "That was a good time, mate. Yer alright fer someone who ain’t swingin’ a big ol’ axe. Let’s do this again sometime, eh?"
        
            jump ch3_choices_1

        "Skip (continue with your life at the Academy)":
            jump chapter_4

    # label assassin_encounter_cloak:
    #     # Scene setup
    #     # scene bedroom_night with fade
    #     # play music "suspense_theme.mp3"
        
    #     "The stillness of the night is broken by the faint creak of a floorboard. You wake up, heart pounding, as the realization hits you: someone is inside your home."
    #     "Reaching for your dagger, you barely have time to prepare when the door creaks open. A shadowy figure steps inside, their blade gleaming ominously in the faint moonlight."
        
    #     "Before you can act, a voice whispers in your ear, low and calm, though no one is there."
        
    #     hooded_woman "{i}Stay quiet and don't panic. I can help you.{/i}"
        
    #     "You flinch, your eyes darting around the room. Out of the corner of your vision, you spot a hooded figure materializing in the shadows. Her golden eyes seem to glow, locking onto yours."
        
    #     menu:
    #         "Trust her and listen":
    #             "You stay silent, nodding slightly, unsure of who this woman is but desperate for help."
                
    #         "Demand answers":
    #             p "Who are you?! What's going on?!"
                
    #             hooded_woman "{i}No time for questions. If you want to live, follow my lead.{/i}"
    #             "Her tone brooks no argument, and you reluctantly nod."
        
    #     "The assassin steps closer, their gaze scanning the room. The hooded woman tosses something to you—a shimmering cloak that feels impossibly light in your hands."
        
    #     hooded_woman "{i}Put it on. This will render you invisible to them, but it won't last long.{/i}"
        
    #     menu:
    #         "Put on the cloak":
    #             "You throw the cloak around your shoulders, feeling a strange tingle as it settles over you. The assassin's gaze passes over you without reaction, as though you've disappeared."
                
    #         "Hesitate":
    #             "You hesitate, unsure if you can trust her, but the assassin's approach leaves you no choice. You throw the cloak around your shoulders just in time, vanishing from sight."
        
    #     "The hooded woman's voice whispers again, soft and urgent."
        
    #     hooded_woman "{i}Now, use your skills. You've trained for moments like this. Stay quiet, stay sharp, and take them down.{/i}"
        
    #     menu:
    #         "Sneak behind the assassin":
    #             "You move silently across the room, your footsteps barely a whisper on the wooden floor. The cloak conceals you completely, and the assassin seems oblivious to your presence."
                
    #             "When you're close enough, you reach out, your dagger poised. With a swift, calculated motion, you disarm the assassin, their blade clattering to the floor."
                
    #         "Set a trap using the surroundings":
    #             "You scan the room quickly, noticing a loose curtain cord dangling nearby. Silently, you tie it into a makeshift tripwire."
                
    #             "Then, with a deliberate noise, you draw the assassin's attention. As they lunge, they trip over the cord, falling heavily to the floor."
        
    #     "The assassin struggles, but you seize the opportunity, pinning them down and pressing your dagger to their throat."
        
    #     "The hooded woman steps forward, her presence commanding."
        
    #     hooded_woman "{i}Enough.{/i}"
        
    #     "The assassin freezes, their eyes wide with fear as they glance at her. Without another word, the assassin scrambles to their feet and flees, disappearing into the night."
        
    #     stop music fadeout 2.0
    #     # play music "mystery_theme.mp3"
        
    #     "You turn to the hooded woman, your breath heavy. She nods approvingly, her golden eyes glowing faintly."
        
    #     hooded_woman "{i}You did well. But this was only the beginning.{/i}"
        
    #     menu:
    #         "Ask who she is":
    #             p "Who are you? And why did you help me?"
                
    #             hooded_woman "{i}That's a story for another time. For now, let's just say I have an interest in seeing you survive.{/i}"
                
    #         "Thank her nervously":
    #             p "T-Thank you. I don't know how I could have done that without you."
                
    #             hooded_woman "{i}Perhaps. But you're stronger than you think. Remember that.{/i}"
        
    #     "Before you can say anything else, she vanishes into the shadows as quickly as she appeared, leaving you alone in the stillness of the night."




label chapter_4:
    # School tournament
    # Theoric test
    # Simulated dungeon with mechanical goblins, traps, and the Lake of the Spirit Trial
    # The "Cursed Dawn" goddess, evil sister of the Blessed Eve, will interfere in the spirit trial with a much darker test of her own
    # 1v1 Final battle against Geralt Dune

    label cursed_dawn_offer:
        # scene bg_academy_evening with fade
        # play music "mysterious_theme.ogg" fadein 2.0

        "The academy corridors are eerily silent as the sun dips below the horizon. Shadows stretch long and dark, flickering as faint torches light the hall."
        "Your teammates are elsewhere, preparing for the tournament, but you've found yourself alone, wandering the quiet halls lost in thought."
        "As you pass by the library entrance, you feel a strange sensation—a chill, as though the air itself has grown heavier."
        "A faint whisper brushes against your ear, and you turn sharply."

        # scene bg_library_door_dark with dissolve
        "There, standing in the shadows near the library door, is a hooded figure cloaked in deep, flowing black robes."
        "Her presence seems to warp the air around her, as if reality itself resists her existence."

        hwm "You're quite determined, aren't you, little thief?"
        "Her voice is smooth and cold, laced with a subtle power that makes your skin crawl."
        p "Who are you? What do you want?"
        hwm "Oh, just a concerned... observer. Someone who sees potential in you—potential that is being squandered."

        "The figure steps closer, and as she moves, the shadows cling to her like living tendrils. Despite the darkness obscuring her face, you feel her gaze pierce straight through you."

        hwm "The tournament is no mere game, you know. It's a proving ground. A chance to rise above the rest, to show them all who truly deserves to stand at the top."
        p "I don’t need your help. I can handle it on my own."
        hwm "Of course you can." 
        "Her tone drips with condescension, a mocking smile audible in her words."
        hwm "But why struggle? Why risk failure when I can offer you... an edge?"

        "With a slow, deliberate motion, she reaches beneath her cloak and pulls out a shimmering, ethereal garment—a cloak that seems to ripple and shimmer like liquid darkness."

        hwm "This is no ordinary cloak. Its magic can make you unseen, untouchable, untraceable. With it, you can slip past any obstacle, unseen by even the sharpest eyes."
        hwm "Imagine the possibilities, dear thief. During the trials, you could gain the upper hand with ease—an advantage no one could ever trace back to you."
        p "(A cloak of invisibility...)"
        "The idea is tempting. You can already imagine the countless ways it could help—not just during the tournament, but beyond."

        label hwm_questions:
            menu:
                "Ask about the cloak":
                    p "What’s the catch? Magic like this doesn’t come without a price."
                    hwm "Smart boy. You're right—everything has a cost. But this? This is... a gift. Call it an investment."
                    hwm "All I ask is that you use it well. Show me the cunning and ambition I know you possess."
                    jump hwm_questions

                "Ask about her identity":
                    p "Why would you help me? Who are you, really?"
                    "The woman chuckles softly, a sound both alluring and unnerving."
                    hwm "A friend. A guide, perhaps. Someone who understands what it takes to win in this cruel world."
                    hwm "My name is irrelevant for now. Call me... an ally in the shadows."
                    jump hwm_questions

                "Refuse the cloak":
                    p "I don’t need your help. Keep your cloak and your games."
                    "The figure tilts her head slightly, as if amused by your defiance."
                    hwm "Pride is a dangerous thing, little thief. Don’t let it blind you to opportunity."
                    hwm "But... I respect your decision. For now."
                    "With a wave of her hand, the cloak vanishes, and the figure melts back into the shadows."

                "Accept the cloak":
                    $ player_accepted_cloak = True
                    "You reach out, your hand trembling slightly as your fingers brush against the fabric of the cloak."
                    "It feels weightless, cold to the touch yet oddly comforting."
                    p "What do you want in return?"
                    hwm "Oh, nothing too burdensome. Consider it a token of trust—a gift for someone who will do great things."
                    hwm "But remember this: gifts always come with... expectations."
                    "She hands you the cloak, her voice dropping to a whisper."
                    hwm "Use it wisely. You’ll find it invaluable—not just for the trials, but for the secrets this academy hides."
                    p "(Secrets?)"
                    hwm "Oh yes. This academy holds many secrets, and I suspect you’re clever enough to uncover them. This cloak will help you slip where others cannot tread."


    label tournament_intro:
        # scene academy_arena with fade
        # play music "epic_tournament.mp3"

        "The grand arena of the academy buzzes with excitement as the students gather for the annual end-of-year tournament. The tournament is a showcase of skill, intellect, and teamwork—a final challenge before the academy break."
        "Your team is assembled: Ciry, your ever-reliable companion, and [alliance], the person you chose to ally with earlier in the year."

        if alliance == "Theo":
            show theo_confident at left
            "Theo, the towering half-orc barbarian, cracks her knuckles, a wide grin on her face."
            theo "Ha! We’ll crush 'em. Ain’t no team out there better than us!"
        elif alliance == "Dante":
            show dante_calculating at left
            "Dante, the noble mage, adjusts his robes with a smirk, confidence radiating from him."
            dante "Victory is assured. I’ve already calculated every possibility."

        show ciry_ready at center
        "Ciry gives you a reassuring nod, her focus unshakable."
        ciry "We’ve got this. Just stick together, and we’ll win."

        "The announcer’s voice echoes through the arena, silencing the crowd."
        announcer "Ladies and gentlemen, welcome to the annual End-of-Year Tournament! Today, our teams will face three trials. Only the strongest, smartest, and bravest will emerge victorious!"
        "The crowd erupts into cheers as the announcer continues."

        announcer "The first trial: a test of knowledge. The second trial: a simulated dungeon. And finally, the third trial: a one-on-one duel! Let the tournament begin!"
        jump trial_one

    label trial_one:
        scene classroom_theory with fade
        "The first trial takes place in a grand lecture hall, with each team seated at desks. A professor stands at the front, ready to administer the test."

        if alliance == "Theo":
            theo "Bah, tests. This ain’t what I signed up for. I’m better at bashin’ than thinkin’."
            ciry "Don’t worry, Theo. We’ll carry this one. Just try your best!"
        elif alliance == "Dante":
            dante "A theory test? Excellent. This is where we shine. Let’s focus and ace it."
            ciry "Don’t get too cocky, Dante. We still need to work as a team."

        "The professor clears his throat and begins reading out questions related to the *Player’s Handbook* of *Dungeons & Dragons 5th Edition*."

        menu:
            "Answer the question about spell slots.":
                "You confidently explain how spell slots work, earning points for your team."
                $ team_score += 10
            "Answer the question about saving throws.":
                "You explain the mechanics of saving throws, impressing the judges."
                $ team_score += 10
            "Pass the question to your teammates.":
                if alliance == "Theo":
                    "Theo fumbles the answer, but Ciry steps in to save the day."
                    $ team_score += 5
                elif alliance == "Dante":
                    "Dante smugly answers the question with ease."
                    $ team_score += 10

        "The theory test concludes, and your team’s score is announced."
        if team_score >= 20:
            "Your team scores high marks, placing you among the top teams!"
            $ team_rank = 1
        else:
            "Your team scores average marks, leaving you in the middle of the rankings."
            $ team_rank = 2

        jump trial_two

    label trial_two:
        scene dungeon_simulation with fade
        "The second trial takes place in a magically simulated dungeon. The environment is filled with traps, mechanical goblins, and other challenges."

        if alliance == "Theo":
            theo "Now this is what I’m talkin’ about! Lemme at 'em!"
            ciry "Stay sharp, Theo. We need to stick together."
        elif alliance == "Dante":
            dante "A simulated dungeon? Child’s play. Let’s move carefully and efficiently."
            ciry "Let’s not underestimate the challenge, Dante."

        "The first challenge is a swarm of mechanical goblins blocking your path."
        menu:
            "Charge in with Theo/Dante leading the way.":
                if alliance == "Theo":
                    "Theo barrels through the goblins, smashing them with her strength."
                    $ team_score += 10
                elif alliance == "Dante":
                    "Dante casts a powerful fireball, incinerating most of the goblins."
                    $ team_score += 10
            "Coordinate a careful strategy with Ciry.":
                "Ciry expertly guides the team, allowing you to take out the goblins with precision."
                $ team_score += 15

        "Next, your team faces a powerful mechanical boss. It towers over you, gears whirring and weapons ready."

        menu:
            "Distract the boss while your teammates attack.":
                "You draw the boss’s attention, giving your teammates an opening to strike."
                $ team_score += 10
            "Lead a coordinated attack with Ciry and Theo/Dante.":
                "Together, you and your team bring down the boss with a well-coordinated assault."
                $ team_score += 15

        "The final challenge is a magical lake that reveals and animates your deepest fears."
        "One by one, your team members face their fears and work together to overcome them."
        
    label cursed_dawn:
        # Background: Trial Arena
        scene bg_trial_arena with fade
        play music "music/ominous_theme.ogg" fadein 2.0

        "The final trial begins, a test of spirit, where competitors are to face their deepest fears in a constructed illusionary space."
        "The judges signal the start, and a faint, ethereal mist fills the arena as your mind begins to drift."
        
        # Conditional branching
        if accepted_hooded_woman:
            "But something feels... wrong."
            "The mist, which should have been silvery and calming, suddenly turns darker, tinged with a crimson hue."
            "A chilling wind sweeps through the arena, sending shivers down your spine."

            # Introduction of the Cursed Dawn
            scene bg_dark_void with fade
            play sound "sound/dark_whisper.ogg"

            "The surroundings dissolve into darkness. All sound fades, replaced by a low, echoing voice that seems to come from everywhere and nowhere at once."
            cd "So you accepted her help, did you? How... predictable."
            "The voice is sharp, cold, and filled with a sinister amusement. A figure materializes from the shadows—a woman cloaked in black, her presence radiating malevolence."
            cd "You sought power, and power always comes with a price. Did you truly think the Blessed Eve would protect you from me?"

            menu:
                "Who are you?":
                    p "Who... who are you?"                    
                "Stay silent.":
                    p "(Stay calm. Don’t give her the satisfaction of fear.)"
                    cd "Oh, silent bravery? How charming. But bravery won't save you here."
            cd "You don't recognize me? Perhaps your little gnome companion failed to mention me during her lesson on deities. I am the Cursed Dawn, sister of her precious Blessed Eve."
            cd "Yes, I've been watching you for a while... I was wondering why the Silent Goddes is so much interested in having you as her pet."
            cd "(snickering provocatively) She whispers her little riddles into your dreams and calls it guidance, doesn't she?. It’s laughable."
            cd "Let me show you the true depths of your spirit—your failures, your fears, and the lies you tell yourself to keep moving forward."

            # The Dark Test begins
            # scene bg_fear_hall with dissolve
            "The darkness shifts, and you find yourself standing in a warped reflection of the Academy courtyard."
            "The buildings are cracked and crumbling, the sky above a blood-red hue. Shadows writhe at the edges of your vision, and ghostly whispers fill the air."
            cd "Face the truth, mortal. Or be consumed by it."
            # Player encounters their fears
            "Suddenly, familiar figures emerge from the shadows. It's your companions—Ciry, Theo or Dante, and Aryanna—but their faces are twisted in anger and hatred."
            c "You think you're a hero? You're nothing but a coward who hides behind others."
            the "You're weak. You couldn’t save anyone without someone else's power."
            dan "Pathetic. You’ve always relied on others to fight your battles."
            "Their words pierce through you, each one cutting deeper than the last. You try to speak, but the weight of their accusations keeps you silent."

            # Player's choices
            menu:
                "Stand your ground":
                    p "No... This isn't real. You're not real."
                    "You steady yourself, focusing on the truth. These are illusions, crafted to break you, and you won’t let them win."
                    "The figures waver, their forms flickering as your resolve strengthens."
                    cd "Impressive. But resolve alone won't save you."
                "Doubt yourself":
                    p "(Maybe... maybe they're right. I have relied on others too much.)"
                    "The shadows close in as doubt clouds your mind. The figures grow stronger, their accusations louder."
                    cd "Good. Accept it. Sink into the truth of your insignificance."

            # The conclusion of the Dark Test
            scene bg_dark_void with dissolve
            "The vision dissolves, and you find yourself back in the dark void with the Cursed Dawn."
            cd "You’re stronger than I expected. Perhaps there’s something worth breaking in you after all."
            cd "But remember this, mortal. You carry my mark now, the shadow of the Cursed Dawn. And this is because I have plans for you."
            "A searing pain burns on your arm, and when you glance down, a faint black sigil in the shape of a crescent moon glows ominously on your skin."
            cd "I offer you true power, should you ever seek it."
            cd "I offer you to not be the puppet of that Silent Goddess... such a joke of a deity. What kind of ‘savior’ can’t even speak for herself?"
            cd "Go, little pawn. Win your tournament. But know that I am watching."

            # scene bg_trial_arena with fade
            "With a final, mocking laugh, the darkness fades, and you’re back in the arena."
            "The mist clears, and you collapse to your knees, gasping for breath. The other competitors look just as shaken, but none of them seem to have experienced the same... interference."

            c "Hey! Are you okay?"
            "Ciry rushes over, concern etched on her face. You nod weakly, hiding your arm from her view."
            p "(The mark... so this was real?)"

        else:
            # Normal trial continues
            "The mist envelops you, and visions of your deepest fears emerge. But there’s nothing out of the ordinary—just the standard test of spirit."

        if alliance == "Theo":
            the "A lake messin’ with my head? Bah, I’ll bash it jus’ like everything else!"
            "Theo’s confidence helps the team push through the illusions."
            $ team_score += 10
        elif alliance == "Dante":
            dant "Illusions? Mere tricks. Focus your mind, and they’ll shatter."
            "Dante’s logical approach guides the team to success."
            $ team_score += 15

        "Your team emerges from the dungeon, tired but victorious."
        if team_score >= 40:
            "You place in the top two teams and advance to the final trial!"
            $ team_rank = 1
        else:
            "Your team performs well but doesn’t make it to the top two."
            $ team_rank = 2

        # jump trial_three if team_rank == 1 else after_tournament

    label trial_three:
        scene arena_duel with fade
        "The final trial is a one-on-one duel between the strongest members of the two top teams."

        if alliance == "Theo":
            theo "Guess it’s my turn, eh? Time to show ‘em what I’m made of!"
        elif alliance == "Dante":
            dante "This is it. Let me show them the true power of a mage."

        "Your teammate steps into the arena, facing off against a formidable opponent. The duel is intense, and both fighters give it their all."

        menu:
            "Encourage your teammate to go all out.":
                "Your encouragement gives your teammate the boost they need to win the duel!"
                $ team_score += 20
            "Suggest a cautious strategy.":
                "Your teammate fights carefully, but the opponent gains the upper hand."
                $ team_score -= 10

        "The duel concludes, and the final winner is announced."
        if team_score >= 50:
            "Your team wins the tournament, earning glory and recognition across the academy!"
        else:
            "Your team places second, but you’ve gained valuable experience and camaraderie."

        jump after_tournament

    label after_tournament:
        "The tournament comes to an end, and you reflect on the trials you faced and the bonds you forged."

        $ choice = ""
        $ rewards_list = [
            "Shield of Justice",
            "Critical Ring",
            "Gloves of Gargantuan",
            "Amulet of Mana"
        ]
        menu:
            "Choose your reward"

            "[rewards_list[0]]":
                python:
                    Player.inventory.append(rewards_list[0])
                    choice = rewards_list[0]
                    Player.ac_bonus += 3

            "[rewards_list[1]]":
                python:
                    Player.inventory.append(rewards_list[1])
                    choice = rewards_list[1]
                    Player.dmg_critical_threshold -= 2

            "[rewards_list[2]]":
                python:
                    Player.inventory.append(rewards_list[2])
                    choice = rewards_list[2]
                    Player.sheet.strength += 2

            "[rewards_list[3]]":
                python:
                    Player.inventory.append(rewards_list[3])
                    choice = rewards_list[3]



    
label chapter_5:
    # Changing class (if player wants) and accelerated summer course for the new class
    # Dark teachings from Hooded-Woman, during summer, if player accepts
    label gwen_returns:
        "You've done your best to put the encounter behind you, burying the memory of Gwen's true form under the routine of academy life. But no matter how hard you try, it lingers—her glowing crimson eyes, the brush of her claws, the unsettling mix of fear and fascination."
        "Then one day, she returns."
        "You're sitting in the academy courtyard, trying to focus on a particularly dense passage in one of your magical theory books. The chatter of students fills the air, a comforting background noise—until you hear a familiar voice behind you."

        gwen "Miss me?"
        "Your heart stops. You turn, and there she is—Gwen, back in her playful, mischievous academy disguise. She's dressed in the same student uniform, her hair cropped short again, her bright eyes gleaming with amusement. She looks harmless, normal even, but you know better now."

        gwen "You're still alive. I have to admit, I'm impressed. I thought you might've run off to some temple by now, begging a cleric to ward me away."

        p "What are you doing here, Gwen?"
        "You shift uncomfortably, the memory of her true form flashing in your mind."
        gwen "You, of course. I told you, didn't I? There's something about you, something... deliciously unique."

        "Her words send a shiver down your spine."
        p "I thought you already got what you wanted."
        "You try to keep your voice steady, but the memory of her glowing eyes makes it difficult."

        gwen "Oh, I tried. Believe me, I tried. But whatever is anchoring your soul to your body? It's powerful. Too powerful for even me to break through. I need to figure out what it is."

        "You swallow hard, unsure whether to feel relieved or terrified."
        p "And why does that matter to you?"
        "Gwen's playful smirk fades, replaced by something more serious."
        gwen "Because your soul, my dear, was the most delicious thing I've ever tasted. Centuries of seduction, centuries of taking what I want, and nothing has ever come close to the sweetness of you. And I couldn't even finish the meal."
        "Her words hang in the air, and you feel a cold sweat forming on your brow."
        gwen "But don't worry. I'm not here to hurt you. Yet. I just... need to figure you out. For now, you're safe. Think of me as... a friend."
        p "A friend?"
        "You repeat the word, incredulous."
        gwen "Why not? Who else knows your secret? Who else can help you understand what's going on with that soul of yours?"
        "Her words have a strange logic to them, even if every instinct tells you to stay as far away from her as possible."
        gwen "So, what do you say? Want to figure this out together?"
        "Her voice drops to a low, honeyed tone, and you hesitate. The memory of her glowing eyes and infernal wings looms large, but there's something else too—a curiosity, a faint pull that you can't entirely resist."

        menu:
            "I don't trust you, Gwen. Stay away from me.":
                p "I don't trust you, Gwen. Stay away from me."

                gwen "(smirking) Oh, you wound me. But that’s okay. I’ll keep my distance—for now. I can be patient."

                "She stands, her smirk lingering as she disappears into the crowd. Even as she leaves, you feel her presence, like a shadow that won’t let you go."

                jump after_gwen_returns

            "Fine. But I'm keeping my guard up.":
                p "Fine. But I'm keeping my guard up."

                gwen "(chuckling) Of course you are. I wouldn’t expect anything less. Just don’t let that guard of yours get too heavy to carry."

                "She leans back, resting her hands on the bench, her smirk softening into something almost genuine."

                jump after_gwen_returns

            "If you're offering answers, I'm in.":
                p "If you're offering answers, I'm in."

                gwen "(grinning) I knew you'd see reason. You and I, we’re going to make an excellent team. Just you wait."

                "Her eyes gleam with something between excitement and hunger, and you can’t quite tell if you’ve made the right choice—or the worst one."

        "The encounter with Gwen leaves you unsettled, no matter your choice. Her presence lingers in your mind, a constant reminder of the mysteries—and dangers—surrounding her."
        "But one thing is certain: your path is now inexorably tied to hers, for better or worse."


    label gwen_connection_scene:
        "Days turn into weeks, and Gwen’s presence becomes an inescapable part of your life. Whether in the academy courtyard, during classes, or even in your dreams, she lingers—watching, waiting, her motives unclear but her fascination with you undeniable."

        "One night, as you sit in your dorm room pouring over a tome on magical anomalies, there’s a knock at your door. Before you can answer, it creaks open, and Gwen steps inside, her usual playful smirk replaced by something more serious."

        gwen "We need to talk."

        "You close the book and sit up, your heart racing. Gwen rarely shows this kind of intensity, and it puts you on edge."

        p "What’s this about, Gwen? Another cryptic comment about my soul?"

        gwen "(shaking her head) No. This is different. I've been... looking into things. About you. About us."

        "The way she says 'us' sends a shiver down your spine. She steps closer, her crimson eyes flickering with an unusual softness."

        gwen "I’ve learned something. Something important."

        p "I’m listening."

        gwen "There’s a way to understand what’s anchoring your soul. A ritual, ancient and forbidden. It’s dangerous, but if it works... we’ll finally have answers. For both of us."

        "You stare at her, trying to gauge her sincerity. For once, there’s no trace of her usual playfulness—only determination."

        p "And what’s in it for you, Gwen? Why are you so invested in this?"

        gwen "(hesitant) I told you before... your soul is unlike anything I’ve encountered. It’s not just curiosity. There’s a part of me that... craves it. But it’s more than that now. I need to know why I can’t break you. Why I feel... bound to you."

        p "(suspicious) Bound? What does that mean?"

        gwen "(softly) I don’t know. That’s what I want to find out."

        menu:
            "Agree to the ritual":
                p "Fine. If it gets me answers, I’ll do it."

                gwen "(relieved) Good. I knew you’d see reason. But I have to warn you—it won’t be easy. This ritual will lay your soul bare. There’s no hiding from it."

                "Her words send a chill through you, but you nod, determination outweighing your fear."

                jump gwen_ritual_preparation

            "Refuse the ritual":
                p "No. I don’t trust you enough to do this."

                gwen "(smirking, but with a hint of sadness) I figured you’d say that. But I’ll be here when you change your mind. Because you will, eventually."

                "She steps back, her crimson eyes lingering on you before she leaves the room. Even as the door closes, you feel her presence, like a shadow clinging to your soul."

                "The days that follow are restless. Gwen keeps her distance, but her gaze always seems to find you in the crowd. The weight of her proposal hangs heavy in your mind, no matter how much you try to bury it."


    label gwen_ritual_preparation:
        "Over the next few days, Gwen becomes unusually focused, helping you prepare for the ritual. She shares ancient texts, teaches you incantations, and warns you of the risks involved."

        gwen "This isn’t just about answers, you know. It’s about trust. If we do this, we’ll be bound together in ways neither of us fully understands."

        "Her words linger as the night of the ritual approaches. Despite your doubts, you can’t shake the feeling that this is the path you were meant to take."




label chapter_6:
    # The beginning of the rituals to meet the past chosen of the Silent Goddess at Mushroom House
    # From this moment on, lessons, school events and rituals alternate:
        # The ritual with Trent
        # Class lessons and study play choice
        # The ritual with Deva
        # The meeting with Geralt Dune            
        # School excursion to Dune's manor house

    label deva_ritual:
        # Scene setup
        # scene meditation_room with fade
        # play music "meditation_theme.mp3"

        "You sit cross-legged, the familiar calm of meditation washing over you. The air around you seems to grow heavy with an unspoken power."
        "As you focus, your mind drifts, and the faint hum of divine energy fills the room, pulling you deeper into the ritual."
        
        "Suddenly, a vision appears before you—a fierce warrior woman, her form illuminated by a faint, otherworldly glow."
        # show deva_image
        
        "Her piercing gaze locks onto yours, and though she doesn't speak, her presence commands your full attention. You feel her name in your soul: {i}Deva.{/i}"
        "The Silent Goddess's power flows through the vision, and Deva's story begins to unfold before your eyes…"

        # scene deva_childhood with dissolve
        # play music "haunting_theme.mp3"
        
        "Deva is but a child in a nomadic barbarian village in the far north, nestled near the snowy mountains. One day, while playing, she hears a strange hum."
        "Drawn by the sound, she follows it to a hidden cave where she discovers an ancient sword, glowing faintly with divine energy. Playfully, she picks it up and swings it around."        
        "The sword delays her return home, and when she finally heads back, she sees a nightmare unfolding. Frost Giants are attacking her village."
        "She watches in horror as the giants destroy her home and devour her family and neighbors. Frozen with fear and despair, Deva eventually flees."        
        "The vision shifts, showing Deva surviving alone in the wilderness. The sword, her only companion, offers her warmth on frigid nights and warns her of lurking dangers."
        "It guides her in finding food and keeps her safe from predators. The bond between Deva and the sword grows stronger with each passing day."

        # scene deva_meets_villagers with dissolve
        # play music "soft_theme.mp3"
        
        "Years later, Deva stumbles upon a new settlement by a great river. There, she meets an elderly couple who show her kindness."
        "Though she lives a wild, solitary life, she grows fond of them. They leave her food on cold nights, and the woman teaches her to read."        
        "One night, as Deva sleeps by her small fire, the sword vibrates with urgency, glowing brighter than ever before. It leads her to the couple's house."
        "In the shadows, she senses two predatory presences—Dire Wolves, monstrous and bloodthirsty. The couple cries for help, their voices trembling with fear."

        # scene deva_wolf_battle with dissolve
        # play music "battle_theme.mp3"

        "Deva refuses to flee this time. With fierce determination, she faces the wolves. The sword vibrates intensely, its glow nearly blinding the beasts."
        "Though injured in the battle, Deva's newfound resolve and the sword's divine power help her slay both wolves. The elderly couple is saved."
        "The vision fades momentarily, but you feel a deep sense of awe. Deva's story continues to unfold."

        # scene deva_frost_giants with dissolve
        # play music "epic_theme.mp3"
        
        "Now an experienced warrior, Deva becomes a protector of the region, helping villages threatened by monsters and evil forces."
        "One day, she hears of Frost Giants attacking a familiar settlement—the very one that once took her in."        
        "Overcoming her childhood fears, Deva confronts the giants, slaying many with the sword's divine power. A black dragon leading the giants attacks next, but Deva's holy fury fuels her strength."
        "In a climactic battle, she scales the dragon and pierces its skull with the sword, ending its reign of terror."

        # scene deva_genocide_with dissolve
        # play music "dark_theme.mp3"
        
        "But the vision turns darker. Deva, in her Sacred Rage, follows the retreating giants to their village, killing warriors and innocents alike."
        "As she is about to strike down a pregnant giantess and her child, the sword grows unbearably heavy. It refuses to obey her will, resonating with a sense of sorrow and warning."
        "Deva regains her senses, grateful to the sword for stopping her from committing an atrocity. This moment shapes her deeply, and she vows to wield her power with greater wisdom."
        "The vision fades, and Deva looks at you once more, her expression a mixture of strength and pain."

        # hide deva_image with dissolve
        # play music "mystical_theme.mp3"
        
        "As the vision ends, the Silent Goddess's presence lingers in the air. Deva's story echoes in your heart, a tale of strength, loss, and redemption."
        "You feel a newfound connection to the Silent Goddess and her Chosen, as though their trials are now entwined with your own."



    label private_ritual:
        scene ritual_room with fade
        """
        The chamber is dimly lit, the air thick with the scent of burning incense and old magic. Strange runes etched into the stone walls shimmer faintly as the ritual reaches its climax.
        Gwen stands before you, her infernal wings partially unfurled, her glowing crimson eyes fixed on you with an intensity that makes it hard to breathe.
        """    
        gwe "Are you ready? This ritual... it will lay everything bare. Your soul, my essence... nothing will remain hidden."
        
        menu:
            "Nod silently":
                "You nod, unable to speak, your heart pounding in your chest."
                
            "Express doubt":
                p "I'm not sure about this, Gwen. What if something goes wrong?"                
                gwe "Something always goes wrong. That's half the fun, isn't it?"
                "She smirks, but there's a flicker of something genuine in her eyes. Concern? No, surely not."

        "Gwen steps closer, her clawed hand brushing your cheek. Her touch is cold, sending a shiver down your spine."
        gwe "Just relax. This might sting a little."
        "She places her other hand on your chest, right above your heart. A dark energy begins to swirl around her, tendrils of shadow curling like smoke. You feel an unnatural pull, like your very essence is being drawn to the surface."
        
        # scene ritual_glow with dissolve
        
        "But then, something unexpected happens."
        "A blinding light erupts from within you, golden and pure, cutting through the shadows like a blade. The runes on the walls flicker and shift, their infernal glow replaced by a soft, holy radiance."        
        gwe "(startled) What... what is this?"
        
        "She stumbles back, shielding her eyes from the light. Her wings twitch, and for the first time, you see fear on her face."        
        p "I don't know... Ehm isn't... this supposed to happen?"        
        """
        The light intensifies, filling the room with a radiant, almost otherworldly glow. You feel a gentle warmth spreading across your body.
        Then, something unexpected happens. A strange, soothing presence envelops your mind. It’s not just in you—it’s everywhere, as if the air itself is alive with meaning.
        Your thoughts... they begin to shift. You realize that your mind has somehow connected with Gwen's. You sense her presence, her emotions, her fears—and they echo through you like whispers of an ancient melody.
        She glances at you, her usual guarded demeanor softening in the glowing light. You can see the confusion, the vulnerability in her eyes.
        There’s no voice in the room, but meanings—pure, unspoken truths—begin to appear in both your mind and Gwen's. They’re not words but something deeper, primal and raw, yet profoundly calming.
        You can feel the presence as if it’s something ancient, wise, and benevolent. It’s not trying to control or force you. Instead, it simply exists, weaving a tapestry of understanding between you and Gwen.
        """        
        dea "Gwenethra, daughter of shadow, bound by infernal chains. You have touched the root of a soul under my protection. In doing so, you have invited me into this place."        
        gwe "(whispering) The... Silent Goddess?"        
        "Words and meanings continue to appear, unyielding yet gentle."        
        dea "You have lived in darkness, consumed by your instincts. But I offer you a choice: Redemption. Not to walk the path of light, but to sever the chains that bind you to the infernal plane. To be free."
        
        menu:
            "Encourage Gwen to accept":
                $ Player.achievements.append("Redeemed Gwen")
                p "Gwen, this is your chance. You don't have to be a slave to your nature anymore."                
                gwe "(hesitant) Free... I don't even know what that means anymore."                
                dea "Freedom means choice. To act, not as your instincts demand, but as your will decides."                
                "Gwen stares at the light, her expression conflicted. Finally, she steps forward, reaching out tentatively."                
                gwe "I... I accept."                
                "The light envelops her, and for a moment, her form dissolves into pure radiance. When it fades, she stands before you, her wings smaller, her eyes no longer glowing but a deep, soulful violet."                
                gwe "I feel... lighter. But also... hollow."                
                dea "That is the weight of freedom. You will learn to carry it."
                "Gwen stands silently for a moment, her new form radiating a subtle, serene aura. Her deep violet eyes meet yours, and you sense a storm of emotions swirling within her."
                gwe "I... I don’t know what to make of this. I’ve spent so long being driven by my instincts, by my power. Now, it feels like... like a part of me is missing."
                
                menu:
                    "Reassure her":
                        p "You’re not missing anything, Gwen. You’re free now, free to choose your own path. That’s all you need."
                        gwe "(softly) Freedom... It’s strange. Exciting, but terrifying. I don’t know who I am without that part of me."

                    "Challenge her doubts":
                        p "Or maybe you’re just afraid of what freedom means. It’s easier to follow instincts than to decide for yourself, isn’t it?"
                        gwe "(frowning) Afraid? Maybe I am. But don’t think for a moment that I’ll back down from this. I’ll figure it out, one way or another."

                    "Lighten the mood":
                        p "Well, you’re still Gwen, and I doubt anything can take away your sharp tongue and flair for drama."
                        gwe "(smirking faintly) Hah. Trust you to make a joke at a time like this. Maybe I need that, though. Thanks."

                "She steps away, wrapping her arms around herself as though shielding against an unseen chill. Her voice trembles slightly, but it carries a determination you’ve never heard from her before."
                gwe "I need time. Time to figure out what this change means for me, for us. I’m not ready to dive headfirst into whatever lies ahead—not yet."

                menu:
                    "Encourage her":
                        p "Take all the time you need, Gwen. I’ll be here when you’re ready."
                        "She looks at you, a faint smile forming on her lips. It’s not her usual smirk, but something softer, more vulnerable."
                        gwe "Thank you. For giving me this chance, for... believing in me."

                    "Ask about your bond":
                        p "What happens to our connection, then? Are we still bound in some way?"
                        gwe "Our bond remains, mortal. I’m still your patron, guiding you. That part of me will always be with you, whether I’m at your side or not."

                    "Push for more":
                        p "You’ve changed, but that doesn’t mean you should walk away from everything. Don’t you want to see where this could take us?"
                        gwe "(sighing) I do, but not yet. I need to understand who I am now before I can stand beside you again. Give me time."

                "Gwen takes a deep breath, her composure returning as she straightens and places a hand on your shoulder."
                gwe "But don’t think I’m abandoning you, mortal. I’ll still be your patron, guiding you from the shadows, as I always have. My power will remain at your disposal, though it may take a different form now."
                "Her fingers brush lightly against your shoulder before she steps back, her gaze steady and resolute."
                gwe "And who knows? Perhaps one day, when I’ve figured all this out, I’ll join you in your adventures. You’ll need someone to keep you out of trouble, after all."
                "She winks, her playful tone returning for just a moment, a glimpse of the Gwen you’ve come to know."
                gwe "Until then, don’t do anything reckless without me. I’d hate to have to clean up your messes from afar."
                "Gwen begins to fade into the shadows, her presence lingering for just a moment longer before disappearing entirely. You’re left standing alone in the quiet, a faint sense of her power still coursing through you."

                                
            "Remain silent":                
                "You say nothing, watching as Gwen wrestles with the choice before her."                
                gwe "I... I don't know if I can. What am I without my instincts? Without my power?"                
                dea "You are what you choose to become."                
                "Gwen hesitates, then shakes her head, stepping back."                
                gwe "No. I can't. I've been this way too long."                
                dea "So be it. The choice remains, should you seek it again."                
                "The light fades, and the room grows dark once more. Gwen turns to you, her crimson eyes filled with a mix of regret and defiance."                
                gwe "Let's finish what we started. No more interruptions."
                "The room falls into an almost sacred silence, the remnants of the calming light fading, leaving behind an atmosphere thick with raw, electric energy."
                "Gwen turns toward you, her crimson eyes burning with an intense mixture of desire and determination. She approaches slowly, her every step deliberate, her form glowing faintly with the remnants of the ritual's power."
                gwe "No more interruptions. This is our moment, yours and mine. Let me show you the depths of what we can become together."
                """
                She places her hands on your chest, and a strange warmth courses through your body.
                Gwen begins to chant in a language you don't recognize, her voice low and sultry, carrying a power that seems to resonate with the very essence of your being.
                Her hands begin to glow faintly as demonic runes appear in the air around you both, their intricate patterns dancing in unison with her words. The connection between you grows deeper, your mind and hers intertwining.
                Every thought, every emotion she feels is laid bare before you, and in turn, she experiences every part of you.The bond is intoxicating, overwhelming, and for a moment, it feels as though the two of you are one.
                An indescribable sensation fills you, a pleasure beyond anything you could have imagined. It's not just physical—it’s spiritual, an ecstasy that touches the deepest parts of your soul.
                Gwen’s touch, her presence, becomes the center of your world, and you feel yourself drawn deeper into her embrace.
                She gasps, her head tilting back as the ritual reaches its peak. Her voice trembles, filled with a mixture of triumph and bliss.
                """
                gwe "This... this is perfection. Together, we are unstoppable. Your soul... your essence... it’s unlike anything I’ve ever known."
                "The glowing runes flare brightly before fading into your skin, leaving behind faint marks that pulse with a soft, dark energy. Gwen collapses against you, breathing heavily, her body trembling from the intensity of the experience."
                gwe "It’s done. The bond is complete. You and I... we’re connected now, in ways neither of us could have imagined."
                "She looks up at you, her eyes softer now, her usual cocky smirk replaced with something more genuine, almost reverent."
                gwe "You’ve given me something I’ve never had before... satisfaction, completeness. For that, I swear to you—I am bound to you, now and forever. A part of my power will live within you, always."
                "You feel a faint spark deep within you, a fragment of Gwen’s dark energy embedding itself into your very being. It’s both foreign and familiar, a shadow that you know will always be a part of you."
                "Gwen leans closer, her lips brushing against your ear as she whispers softly."
                gwe "You’ve changed me. And together, we’ll change everything."
                "Her words linger in the air as she pulls back, her expression one of complete devotion. Whatever the future holds, you know that this bond, this connection, will shape everything that comes next."
                $ Player.achievements.append("Demonic Bond")
                "Added Feat: 'Demonic Bond'"
                $ Player.sheet.charisma += 2                
                "[Player.sheet.name]'s Charisma: +2"

            

label chapter_7:
    # The ritual with Brandan Dune (Dune story is explained)
    # The ritual with Yorin, part 1
    # History lesson with the story of the City-dungeon and the story of the Academy
    # Ritual with Yorin (and Trent), part 2

        

label demo_end:
    stop music fadeout 2.0
    scene bg room
    "Thank you for playing this game!"
    "This demo game has now ended, but it's still work in progress."
    "If you enjoyed it, please stay updated. You'll be able to download the next version and continue right from you last game save."
    call gameover from _call_gameover_1



label study_plan_1:
    "Choose the course to follow for the current term:"
    menu:

        "Survival in the woods" if "survival" not in Player.courses_taken: # Ranger teacher
            "This course will improve your Constitution (+1) and will grant you a proficiency in the Survival skill."
            menu:
                "Take the course":
                    $ Player.sheet.constitution += 1
                    $ Player.sheet.skills_wisdom["survival"] = True
                    $ Player.courses_taken.append("survival")
                "Go back":
                    call study_plan_1 from _call_study_plan_1_1

        "Basics of dungeoneering" if "dungeon" not in Player.courses_taken: # Rogue teacher
            "This course will improve your Dexterity (+1) and will grant you a proficiency in the Perception skill."
            menu:
                "Take the course":
                    $ Player.sheet.dexterity += 1
                    $ Player.sheet.skills_wisdom["perception"] = True
                    $ Player.courses_taken.append("dungeon")
                "Go back":
                    call study_plan_1 from _call_study_plan_1_2

        "History of Magic" if "arcana" not in Player.courses_taken: # Wizard teacher
            "This course will improve your Intelligence (+1) and will grant you a proficiency in the Arcana skill."
            menu:
                "Take the course":
                    $ Player.sheet.intelligence += 1
                    $ Player.sheet.skills_intelligence["arcana"] = True
                    $ Player.courses_taken.append("arcana")
                "Go back":
                    call study_plan_1 from _call_study_plan_1_3

        "Persuasion Techniques" if "persuasion" not in Player.courses_taken: # Bard teacher
            "This course will improve your Charisma (+1) and will grant you a proficiency in the Persuasion skill."
            menu:
                "Take the course":
                    $ Player.sheet.charisma += 1
                    $ Player.sheet.skills_charisma["persuasion"] = True
                    $ Player.courses_taken.append("persuasion")
                "Go back":
                    call study_plan_1 from _call_study_plan_1_5

        "Principles of the faithful" if "religion" not in Player.courses_taken: # Cleric teacher
            "This course will improve your Wisdom (+1) and will grant you a proficiency in the Religion skill."
            menu:
                "Take the course":
                    $ Player.sheet.wisdom += 1
                    $ Player.sheet.skills_intelligence["religion"] = True
                    $ Player.courses_taken.append("religion")
                "Go back":
                    call study_plan_1 from _call_study_plan_1_6

        "Basics of combat and martial arts" if "combat" not in Player.courses_taken: # Figther teacher
            "This course will improve your Strength (+1) and will grant you a proficiency in the Athletics skill."
            menu:
                "Take the course":
                    $ Player.sheet.strength += 1
                    $ Player.sheet.skills_strength["athletics"] = True
                    $ Player.courses_taken.append("combat")
                "Go back":
                    call study_plan_1 from _call_study_plan_1_8
        
    $ Player.save_json()
    return


label study_plan_2:
    "Choose the course to follow for the current term:"
    menu:

        "Fighting wild animals" if "animals" not in Player.courses_taken: # Barbarian teacher
            "This course will improve your Strength (+1) and will grant you a proficiency in the Animal-Handling skill."
            menu:
                "Take the course":
                    $ Player.sheet.strength += 1
                    $ Player.sheet.skills_wisdom["animal-handling"] = True
                    $ Player.courses_taken.append("animals")
                "Go back":
                    call study_plan_2 from _call_study_plan_2

        "Recognize evil in the world" if "evil" not in Player.courses_taken: # Paladin teacher
            "This course will improve your Wisdom and Constitution Abilities."
            menu:
                "Take the course":
                    $ Player.sheet.strength += 1
                    $ Player.sheet.wisdom += 1
                    $ Player.courses_taken.append("evil")
                "Go back":
                    call study_plan_2 from _call_study_plan_2_1

        "The dangers of magic" if "magic" not in Player.courses_taken: # Sorcerer teacher
            "This course will improve your Charisma and Constitution Abilities."
            menu:
                "Take the course":
                    $ Player.sheet.charisma += 1
                    $ Player.sheet.constitution += 1
                    $ Player.courses_taken.append("magic")
                "Go back":
                    call study_plan_2 from _call_study_plan_2_2

        "Tales of extraplanar entities" if "extraplanar" not in Player.courses_taken: # Figther teacher
            "This course will improve your Charisma and Wisdom Abilities."
            menu:
                "Take the course":
                    $ Player.sheet.charisma += 1
                    $ Player.sheet.intelligence += 1
                    $ Player.courses_taken.append("extraplanar")
                "Go back":
                    call study_plan_2 from _call_study_plan_2_3

        "The armony with nature" if "nature" not in Player.courses_taken: # Druid teacher
            "This course will improve your Wisdom (+1) and will grant you a proficiency in the Nature skill"
            menu:
                "Take the course":
                    $ Player.sheet.wisdom += 1
                    $ Player.sheet.skills_intelligence["nature"] = True
                    $ Player.courses_taken.append("nature")
                "Go back":
                    call study_plan_2 from _call_study_plan_2_4

    $ Player.save_json()
    return


label gameover:
    scene gameover
    play music mandown fadein 1.0
    "GAME OVER"
    $ renpy.full_restart()

