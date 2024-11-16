rpy monologue single

init python:
    config.tts_voice = "David"

# Talking characters
define p = Character("You", who_color="#86f1ff")
define c = Character("Ciry", who_color="#ffff80")
define d = Character("Dante", who_color="#ff9500")
define t = Character("Theo", who_color="#7cff75")
define tol = Character("Tolomeus", who_color="#ff0000")
define rob = Character("Robin", who_color="#faa2fa")
define dra = Character("Dragon", who_color="#00f549")
define tri = Character("Tris", who_color="#b3ffca")
define rec = Character("Rector", who_color="#f4f4f4")
define bel = Character("Bella", who_color="#ffc4e4")
define dya = Character("Dyana", who_color="#a79aff")
define ary = Character("Aryanna", who_color="#ff0062")
define hob = Character("", who_color="#007d11")
define dea = Character("", who_color="#ffffff")
define uk = Character("???", who_color="#d5d5d5")
define gwe = Character("Gwen", color="#FF69B4")

# Cutscene stuff
define annoytheuser = Dissolve(3.0)

# Stored variables
default PARTY = []
default Player = None
default Ciry = None
default Theo = None
default Dante = None
default ABILITIES = ("Strength", "Dexterity", "Constitution", "Intelligence", "Wisdom", "Charisma")



# The game starts here.
label start:

    python:

        if renpy.mobile:
            quick_menu = True

        if config.developer:
            quick_menu = True
            config.rollback_enabled = True

        # ADVENTURERS
        Ciry = PlayableAdventurer(sheet_5e.Character(
            name="Ciry",
            age="16",
            level=1,
            gender="Female",
            classs=sheet_5e.CLASSES["cleric"],
            strength=14,
            dexterity=12,
            constitution=14,
            wisdom=15,
            intelligence=10,
            charisma=10
        ))
        Ciry.race = "Gnome"
        Ciry.character = c
        Ciry.image = "ciry"
        Ciry.actions = [DefaultAttack, CureWounds]
        Ciry.equip_weapon(SRD_equipment['morningstar'])        
        # Ciry.equip_armor(SRD_equipment['leather-armor'])
        # testimg = renpy.image("Ciry", "images/Characters/ciry.png")

        Dante = PlayableAdventurer(sheet_5e.Character(
            name="Dante",
            age="15",
            level=1,
            gender="Male",
            classs=sheet_5e.CLASSES["wizard"],
            strength=9,
            dexterity=15,
            constitution=13,
            wisdom=11,
            intelligence=16,
            charisma=14
        ))
        Dante.race = "Human"
        Dante.character = d
        Dante.image = "dante"
        Dante.actions = [DefaultAttack, BurningHands, CureWounds]
        Dante.equip_weapon(SRD_equipment['quarterstaff'])
        Dante.sheet.experience += Dante.sheet.experience.to_next_level
        Dante.sheet.experience += Dante.sheet.experience.to_next_level
        Dante.sheet.experience += Dante.sheet.experience.to_next_level
        Dante.sheet.experience += Dante.sheet.experience.to_next_level

        Theo = PlayableAdventurer(sheet_5e.Character(
            name="Theo",
            age="17",
            level=1,
            gender="Female",
            classs=sheet_5e.CLASSES["barbarian"],
            strength=17,
            dexterity=12,
            constitution=15,
            wisdom=10,
            intelligence=8,
            charisma=13
        ))
        Theo.race = "Half-Orc"
        Theo.character = t
        Theo.image = "theo"
        Theo.actions = [DefaultAttack]
        Theo.equip_weapon(SRD_equipment['club'])

        Player = PlayerAdventurer(sheet_5e.Character(
            name="Ale",
            age="16",
            level=1,
            gender="Male",
            classs=sheet_5e.CLASSES["rogue"],
            strength=8,
            dexterity=8,
            constitution=8,
            wisdom=8,
            intelligence=8,
            charisma=8
        ))
        Player.character = p
        Player.actions = [DefaultAttack]
        Player.equip_weapon(SRD_equipment['dagger'])
        Player.courses_taken = []

        Ciry.save_json()
        Dante.save_json()
        Theo.save_json()
        Player.save_json()

        # PARTY
        PARTY = [Player, Ciry, Dante, Theo]

        # MONSTERS
        Goblin = Monster(SRD_monsters["goblin"])
        Goblin.image = "goblin_m"
        Zombie = Monster(SRD_monsters["zombie"])
        Zombie.image = "zombie_f"
        GiantRat = Monster(SRD_monsters["giant-rat"])
        GiantRat.image = "giant-rat"
        Hobgoblin = Monster(SRD_monsters["orc"])
        Hobgoblin.sheet["name"] = "Hobgoblin"
        Hobgoblin.image = "hobgoblin"

        test_enemies = [Goblin, Zombie]
        # test_enemies = [GiantRat]

        Goblin.save_json()
        Zombie.save_json()
        Hobgoblin.save_json()
        GiantRat.save_json()

        # EQUIPMENT
        weapon = SRD_equipment['shortbow']
        open('weapon.json', 'w').write(json.dumps(weapon, indent = 4)) 

        # SPELLS
        open('spell.json', 'w').write(json.dumps(SRD_spells["burning-hands"], indent = 4))

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    # call gameover

    scene dice academy1
    #DEBUG:
    # $ narrator(str(Ciry.get_name()))
    # $ narrator(str(Ciry.get_modifier("wisdom")))
    # $ narrator(str(Ciry.roll_ability("strength")))
    # $ renpy.show("ciry")
    menu:
        "Battle test":
            play music stoneworldbattle
            $ battle(PARTY, test_enemies)
            $ restore_party(PARTY)
            call gameover from _call_gameover

        "Begin story":
            $ restore_party(PARTY)
            play music onmyway fadein 2.0
            "Welcome to Dungeon Academy!"
            jump chapter_1

        "Dungeon Crawler":
            "Starting dungeon crawler mode..."
            jump dungeon_crawler

        "Debug Jump":
            jump debug  



# This ends the game.
return
