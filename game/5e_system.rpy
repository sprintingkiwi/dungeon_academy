init python:
    import sheet_5e as sheet_5e
    from sheet_5e.monsters import SRD_monsters
    from sheet_5e.equipment import SRD_equipment
    from sheet_5e.spellcasting import SRD_spells
    import json
    import random
    from random import randint
    import textwrap


    def nar(text):
        lines = textwrap.wrap(text, 108)
        for line in lines:
            narrator(line)


    def restore_party(party):
        for hero in party:
            hero.restore()


    def find_item(obj, key):
        if key in obj: return obj[key]
        for k, v in obj.items():
            if isinstance(v, dict):
                item = find_item(v, key)
                if item != None:
                    return item            


    # def roll_dice(dice_string):
    class Roll(object):
        def __init__(self, dice_string, multiplier=1):
            self.dice_str = dice_string.split("d")
            self.number_dice = int(self.dice_str[0]) * multiplier
            facesstr = self.dice_str[1]
            self.faces = 0
            self.natural_result = 0
            self.result = 0
            self.addition = 0
            if "+" in facesstr:
                splitting = facesstr.split("+")
                self.addition = int(splitting[1])
                self.faces = int(splitting[0])
            else:
                self.faces = int(facesstr)            
            for d in range(self.number_dice):
                self.natural_result += randint(1, self.faces)
            self.result = self.natural_result + self.addition


    def hit_roll(user, target, stat):        
        atk_bonus = user.get_attack_bonus(stat)
        roll = user.roll("1d20+"+str(atk_bonus))
        narrator(f"ATTACK ROLL: {roll.natural_result} + {atk_bonus}(attack bonus) = {roll.result}")        
        ac = int(target.get_armor_class())
        narrator(f"Comparing attack roll with target Armor Class ({ac})... ")
        if roll.result >= ac:
            return (True, roll)
        else:
            return (False, roll)


    ### ACTIONS ###
    class Action(object):
        def __init__(self, user):
            self.name = ""
            self.is_spell = False
            self.scope = "Enemy" # or Ally or Allies or Enemies or Self
            self.user = user
            self.target = None

        def requirements(self):
            return True

        def effect(self, target):
            self.target = target
            # narrator(f"Processing action {self.name}")

    class Spell(Action):
        def __init__(self, user):
            super().__init__(user)
            self.sheet = None
            self.used_slot_level = 0

        def requirements(self):            
            if self.used_slot_level == 0:
                return True
            elif self.user.get_spell_slots(self.used_slot_level) - self.user.used_spell_slots[self.used_slot_level] >= 1:
                self.user.used_spell_slots[self.used_slot_level] += 1
                return True
            else:
                return False

        def effect(self, target):
            super().effect(target)
            narrator("Choose slot level", interact=False)
            spell_slot_choices = []
            for i in range(9):
                if self.user.get_spell_slots(i+1) > 0:
                    spell_slot_choices.append((str(i+1), i+1))
            self.used_slot_level = renpy.display_menu(spell_slot_choices)


    class DefaultAttack(Action):
        def __init__(self, user):
            super().__init__(user)
            self.name = "Attack"

        def effect(self, target):
            super().effect(target)
            narrator(self.user.get_name() + " attacks " + self.target.get_name())
            ## TO DO: Calculations for finesse weapons here ##
            hit_roll_result = hit_roll(self.user, self.target, "strength")
            hit = hit_roll_result[0]
            roll = hit_roll_result[1]
            if hit:
                narrator("Hit!")
                damage = self.user.roll_default_damage(roll).result
                narrator(f"{self.target.get_name()} takes {damage} points of damage")
                self.target.take_damage(damage)
            else:
                narrator("Miss...")

    class CureWounds(Spell):
        def __init__(self, user):
            super().__init__(user)
            self.name = "Cure Wounds"
            self.scope = "Ally"
            self.sheet = SRD_spells["cure-wounds"]

        def effect(self, target):
            super().effect(target)
            roll = self.user.roll("1d8", mod=self.user.get_spellcasting_ability()).result
            # narrator("Roll for healing (wisdom): " + str(roll))
            self.target.take_damage(-roll)
            narrator(self.target.get_name() + " recovers " + str(roll) + " hit points.")
    
    class BurningHands(Spell):
        def __init__(self, user):
            super().__init__(user)
            self.name = "Burning Hands"
            self.scope = "Enemies"
            self.sheet = SRD_spells["burning-hands"]

        def effect(self, target):
            super().effect(target)
            narrator(f"{self.user.get_name()} produces a blaze that invests all enemies!")
            damage_dice = self.sheet["damage"]["damage_at_slot_level"][str(self.used_slot_level)]
            for target in self.target:
                narrator(f"Rolling {damage_dice} fire damages for {target.get_name()}...")
                roll = self.user.roll(damage_dice).result
                if target.roll_saving_throw("dexterity", self.user.get_spell_DC()):                    
                    roll = int(roll / 2)
                narrator(target.get_name() + " takes " + str(roll) + " points of damage" )
                target.take_damage(roll)
        
    ### ### ###


    class RPG_Entity(object):
        def __init__(self, sheet):
            self.sheet = sheet
            self.character = None
            self.actions = [DefaultAttack]
            self.image = None
            self.initiative = 0
            self.dmg_critical_threshold = 20
            self.dmg_critical_multiplier = 2
            self.ac_bonus = 0

        def get_name(self):
            return self.sheet["name"]

        def save_json(self):
            with open(self.get_name()+".json", 'w') as outfile:
                outfile.write(json.dumps(dict(self.sheet), indent = 4))
                outfile.close()

        def get_hp(self):
            raise NotImplementedError()
        def get_attack_bonus(self):
            raise NotImplementedError()
        def roll_default_damage(self):
            raise NotImplementedError()        
        def get_armor_class(self):
            raise NotImplementedError()
        def get_proficiency_bonus(self):
            raise NotImplementedError()
        def take_damage(self, damage):
            raise NotImplementedError()
        def restore(self):
            raise NotImplementedError()
        def get_spellcasting_ability(self):
            raise NotImplementedError()

        def get_modifier(self, ability):
            return sheet_5e.Character.getModifier(self.sheet[ability])

        def get_spell_DC(self):
            return 8 + self.get_proficiency_bonus() + self.get_modifier(self.get_spellcasting_ability())
        
        def roll(self, dice_string, mod=None, advantage=False, critical=False):
            modifier = 0
            if mod != None:
                modifier = self.get_modifier(mod)
            multiplier = 1 # For damage rolls
            if critical:
                multiplier = self.dmg_critical_multiplier
                renpy.with_statement(vpunch)
                narrator("CRITICAL HIT!")
            roll = Roll(dice_string, multiplier)
            if roll.faces == 20: # For d20 rolls
                if roll.natural_result == 20:
                    renpy.with_statement(vpunch)
                    narrator("CRITICAL SUCCESS!")
                elif roll.natural_result == 1:
                    renpy.with_statement(hpunch)
                    narrator("CRITICAL FAILURE!")
            if advantage:
                second_roll = Roll(dice_string, multiplier)
                if second_roll.result > roll.result:
                    roll = second_roll
            roll.result += modifier
            if mod != None:
                narrator(f"({self.get_name()}) ROLL: {roll.natural_result} + {modifier}({mod}) = {roll.result}")
            else:
                narrator(f"({self.get_name()}) ROLL: {roll.result}")
            return roll

        def roll_ability(self, ability, advantage=False):
            return self.roll("1d20", ability, advantage)

        def roll_saving_throw(self, save, DC):
            narrator(self.get_name() + " rolls a saving throw on " + save)
            roll = self.roll_ability(save)
            if "saving_throws" in self.sheet:
                if save in self.sheet["saving_throws"]:
                    roll.result += self.get_proficiency_bonus()
            if roll.result < DC:
                narrator(f"{str(roll.result)} vs DC {DC}: Failed!")
                return False
            else:
                narrator(f"{str(roll.result)} vs DC {DC}: Successful!")
                return True
        
        def choose_action(self):
            action = random.choice(self.actions)(self)
            return action

        def select_target(self, enemy_group):
            if self.current_target == None or self.current_target.get_hp() <= 0:
                self.current_target = random.choice(enemy_group)
            return self.current_target

        def prebattle(self):
            if self.image != None:
                renpy.show(self.image, at_list=[topright])
        
        def postbattle(self):
            if self.image != None:
                renpy.hide(self.image)


    class Adventurer(RPG_Entity):
        def __init__(self, sheet):
            super().__init__(sheet)
            self.race = "Human"
            self.weapon = None
            self.armor = None

        def get_hp(self):
            return self.sheet.hp

        def get_proficiency_bonus(self):
            return self.sheet["prof_bonus"]

        def get_attack_bonus(self, stat):
            prof_bonus = self.sheet["prof_bonus"]
            ability_bonus = self.get_modifier(stat)
            return prof_bonus + ability_bonus

        def set_ability(self, ability, value):
            if ability == "Strength":
                Player.sheet.strength = value
            elif ability == "Dexterity":
                Player.sheet.dexterity = value
            elif ability == "Constitution":
                Player.sheet.constitution = value
            elif ability == "Intelligence":
                Player.sheet.intelligence = value
            elif ability == "Wisdom":
                Player.sheet.wisdom = value
            elif ability == "Charisma":
                Player.sheet.charisma = value

        def roll_default_damage(self, hit_roll): # TO DO: Must differentiate between types of weapons
            crit = hit_roll.natural_result >= self.dmg_critical_threshold         
            return self.roll(self.weapon["damage"]["damage_dice"], mod="strength", critical=crit)

        def get_armor_class(self):
            return self.sheet.armour_class + self.ac_bonus

        def get_spellcasting_ability(self):
            ability = self.sheet.spellcasting_stat
            if ability == "int":
                return "intelligence"
            elif ability == "wis":
                return "wisdom"
            elif ability == "cha":
                return "charisma"

        def take_damage(self, damage):
            self.sheet.hp -= damage

        def restore(self):
            self.sheet.hp = self.sheet.max_hp

        def roll_skill(self, skillname, advantage=False):
            roll = self.roll("1d20", advantage=advantage)
            proficient = False
            dsheet = dict(self.sheet)
            skills_abilities = ["strength", "dexterity", "intelligence", "charisma", "wisdom"]
            for skill in skills_abilities:
                key = "skills_" + skill
                if skillname in dsheet[key]:
                    proficient = dsheet[key][skillname]
            if proficient:
                roll.result += self.sheet["prof_bonus"]
            return roll

        def equip_weapon(self, weapon):
            self.sheet.giveItem(weapon)
            self.weapon = weapon

        def equip_armor(self, armor):
            self.sheet.giveItem(armor)
            self.armor = armor

    
    class PlayableAdventurer(Adventurer):
        def __init__(self, sheet):
            super().__init__(sheet)
            self.character = None
            self.courses_taken = []
            self.inventory = ["Potion"]
            self.used_spell_slots = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0] # to spell level 9
            self.approval = 0

        def choose_action(self):
            choices = []
            for action in self.actions:
                a = action(user=self)
                if a.requirements():
                    choices.append((a.name, a))
            choice = renpy.display_menu(choices)
            return choice

        def select_target(self, enemy_group):
            options = []
            for enemy in enemy_group:
                options.append((enemy.get_name(), enemy))
            choice = renpy.display_menu(options)
            return choice

        def prebattle(self):
            if self.image != None:
                renpy.show(self.image, at_list=[topleft])
        
        def postbattle(self):
            if self.image != None:
                renpy.hide(self.image)

        def get_spell_slots(self, spell_level):
            slots = self.sheet.class_spellcasting["spell_slots_level_" + str(spell_level)]
            # narrator(f"{slots}")
            return slots
            # return 1 # to do

    
    class PlayerAdventurer(PlayableAdventurer):
        def __init__(self, sheet):
            super().__init__(sheet)            
            self.locations = {}
            self.current_location = ""
            self.achievements = []

        def roll(self, dice, mod=None, advantage=False, critical=False):
            parts = dice.split("d")
            d = parts[1]
            if "+" in d:
                d = d.split("+")[0]
            prompt = "Roll " + parts[0] + " D" + d
            if advantage:
                prompt += " (ADVANTAGE!)"
            renpy.display_menu([ (prompt, "")])
            return super().roll(dice, mod)


    class Monster(RPG_Entity):
        def __init__(self, sheet):
            super().__init__(sheet)
            self.current_target = None
            self.max_hp = self.sheet["hit_points"]

        def get_hp(self):
            return self.sheet["hit_points"]

        def get_attack_bonus(self, stat=None):
            return int(self.sheet["actions"][0]["attack_bonus"])

        def roll_default_damage(self, hit_roll):
            crit = hit_roll.natural_result >= self.dmg_critical_threshold
            return self.roll(self.sheet["actions"][0]["damage"][0]["damage_dice"], critical=crit)

        def get_armor_class(self):
            return self.sheet["armor_class"] + self.ac_bonus

        def get_proficiency_bonus(self):
            return math.floor(max(0, self.sheet["challenge_rating"] - 1) / 4) + 2

        def get_spellcasting_ability(self):
            return 0

        def restore(self):
            self.sheet["hit_points"] = self.max_hp

        def take_damage(self, damage):
            self.sheet["hit_points"] -= damage


    
    def battle(party, enemy_group, can_lose=False): # enemy_group is list of Monsters or Adventurers
        active_party = []
        active_enemies = []
        for member in party:
            if member.get_hp() > 0:
                active_party.append(member)
        for enemy in enemy_group:
            active_enemies.append(enemy)
        battlers = active_party + active_enemies
        narrator("Battle start!")
        narrator("Roll for initiative!")
        for battler in battlers:
            battler.initiative = battler.roll_ability("dexterity").result
        battlers.sort(key=lambda x: x.initiative, reverse=True)
        initlog = "Turn order based on initiative rolls: "
        for battler in battlers:
            initlog += battler.get_name() + "(" + str(battler.initiative) + "), "
        narrator(initlog)
        while len(active_party) > 0 and len(active_enemies) > 0:
            battlers = active_party + active_enemies
            battlers.sort(key=lambda x: x.initiative, reverse=True)
            for battler in battlers:
                if battler.get_hp() <= 0:
                    continue
                battler.prebattle()
                turnlog = battler.get_name() + "'s turn"
                if battler in party:
                    turnlog += "\nHP: " + str(battler.get_hp())
                narrator(turnlog)
                action = battler.choose_action()
                scope = action.scope
                target = None
                if scope == "Enemy":
                    if battler in party:
                        target = battler.select_target(active_enemies)
                    elif battler in enemy_group:
                        target = battler.select_target(active_party)
                elif scope == "Ally":
                    if battler in party:
                        target = battler.select_target(active_party)
                    elif battler in enemy_group:
                        target = battler.select_target(active_enemies)
                elif scope == "Enemies":
                    if battler in party:
                        target = active_enemies
                    elif battler in enemy_group:
                        target = active_party
                elif scope == "Allies":
                    if battler in party:
                        target = active_party
                    elif battler in enemy_group:
                        target = enemy_group
                else:
                    narrator("WRONG SCOPE")
                action.effect(target)
                battler.postbattle()
                # Check death
                for battler in battlers:
                    if battler.get_hp() <= 0:
                        narrator(f"{battler.get_name()} is knocked out!")
                        if battler in active_party:
                            active_party.remove(battler)
                        elif battler in active_enemies:
                            active_enemies.remove(battler)
                        battlers.remove(battler)
                    if len(active_party) <= 0:
                        narrator("YOU LOSE")
                        if not can_lose:
                            renpy.call("gameover")
                        return "Lose"
                    elif len(active_enemies) <= 0:
                        narrator("YOU WIN")
                        return "Win"
