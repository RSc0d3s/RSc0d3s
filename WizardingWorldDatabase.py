# RSCodes Python dictionary
# 01/18/2022
# This is a dictionary which allows use to key in a spell from The Wizarding World of Harry POtter
# and find out what the spell or charm does or what they are used for.
# Note to self: better to use "key":"value" if key with phrases use dict() key="value" if single digit/word key

name = input("What is your name? ")
print("Hello, " + name.title() + ". \nWelcome to the Wizarding World's database.")
PotterDict = {"aberto":"opens locked doors.",
                "accio":"summon objects.",
                "aguamenti":"summons water.",
                "alohomora":"unlocks objects.",
                "anapneo":"clears someone's airway.",
                "aparecium":"reveals secret, written messages.",
                "apparate":"transportation spell that allows a witch or wizard to instantly travel on the spot.",
                "avis":"conjures a small flock of birds.",
                "avada kedavra":"is the killing curse.",
                "bat bogey bex":"turns the target's boogers into bats.",
                "bombardo":"creates an explosion.",
                "brackium emendo":"heals broken bones.",
                "capacious extremis":"is known as the Extension Charm.",
                "confundo":"is the confundus charm. Causes confusion to target.",
                "conjunctivitis curse":"affects the eyes and sight of a target.",
                "crinus muto":"changes hair color and style.",
                "crucio":"is one of three Unforgivable Curses, it causes unbearable pain in the target.",
                "diffindo":"is used to precisely cut an object.",
                "disillusionment charm":"causes the target to take on the appearance of its surroundings.",
                "disapparate":"a non-verbal transportation spell (apparate is the opposite).",
                "engorgio":"causes rapid growth in the targeted object.",
                "episkey":"heals minor injuries.",
                "expecto patronum":"a powerful projection of hope and happiness that drives away Dementors.",
                "erecto":"allows a witch or wizard to build a structure, like a tent.",
                "evanesco":"vanishes objects.",
                "expelliarmus":"forces an opponent to drop whatever's in their possession.",
                "ferula":"is a healing charm that conjures wraps and bandages for wounds.",
                "fidelius charm":"is a complex charm that conceals a secret into the soul of a chosen 'Secret Keeper'.",
                "fiendfyre curse":"conjures destructive, enormous enchanted flames.",
                "finite incantatem":"is a general counter-spell that's used to reverse or counter already cast charms.",
                "furnunculus curse":"is a jinx that causes a breakout of boils or pimples.",
                "geminio":"duplicates objects.",
                "glisseo":"transforms a staircase into a slide.",
                "iomenum revelio":"reveals the presence of another person.",
                "iomonculus charm":"detects anyone's true identity and location on a piece of parchment.",
                "immobulus":"immobilises living targets.",
                "impedimenta":"is a temporary jinx that slows the movement of the target.",
                "incarcerous":"conjures ropes.",
                "imperio":"places the target under the complete control of the caster.",
                "impervius":"makes an object waterproof.",
                "incendio":"conjures flames.",
                "langlock":"causes the target's tongue to stick to the roof of their mouth.",
                "legilimens":"invades or navigates another person's mind.",
                "levicorpus":"levitates the target by their ankle.",
                "locomotor mortis":"the Leg-Locker curse bounds the target's legs.",
                "lumos":"illuminates the caster's wand.",
                "morsmordre":"conjures and projects Lord Voldemort's Dark Mark.",
                "mucus ad nauseam":"inflicts an extreme runny nose or cold.",
                "muffliato":"creates a buzzing sound in the target's ears to prevent eavesdropping.",
                "nox":"reverses the lumos charm, extinguishing a wand's light.",
                "obliviate":"erases the target's memory.",
                "obscuro":"conjures a blindfold.",
                "oculus reparo":"repairs eyeglasses.",
                "oppugno":"directs an object or person to attack a victim.",
                "petrificus totalus":"Temporarily freezes or petrifies the body of the target.",
                "periculum":"conjures flares/red sparks.",
                "piertotum locomotor":"is used to bring to life inanimate objects and artifacts.",
                "protean charm":"link objects together for better communication.",
                "protego":"casts an invisible shield around the caster, protecting against spells and objects.",
                "reducto":"reduces the target to pieces.",
                "reducio":"shrinks an enlarged object to its regular size.",
                "renneverate":"awakens or revives the target.",
                "reparifors":"heals magical ailments like poisoning or paralysis.",
                "reparo":"fixes broken objects.",
                "rictusempra":"is a charm that disarms an opponent by tickling them.",
                "riddikulus":"is used to defeat a Boggart,the charm allows the scary creature to assume a comedic form.",
                "scourgify":"cleans objects.",
                "sectumsempra":"inflicts severe lacerations and hemorrhaging on the target.",
                "serpensortia":"conjures a live snake.",
                "silencio":"silences the target.",
                "sonorus":"amplifies the witch or wizard's voice.",
                "spongify":"aoftens the target.",
                "stupefy":"is the Stunning spell freezes objects and renders living targets unconscious.",
                "tarantallegra":"is aimed at the legs, causes uncontrollable dancing movement.",
                "unbreakable vow":"is a magically binding contract that results in the death of whoever breaks it.",
                "wingardium_leviosa":"causes an object to levitate.",}

key = input("Type in the spell or charm to see what it does: ").lower()
if key in PotterDict:
    print ("This spell or charm", PotterDict[key])
    while True:
        key = input("Type in the spell or charm to see what it does: ").lower()
        try:
            print("This spell or charm", PotterDict[key])
        except KeyError:
            print("Spell not found. A report has been sent to the Ministry of Magic.")
else:
    print ("Spell not found. A report has been sent to the Ministry of Magic.")
    endProgram()





