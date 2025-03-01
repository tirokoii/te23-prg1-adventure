ROBOSQUIRRELS = [

    {
        "id": 1,
        "title": "Welcome to the Squirrel Regime",
        "text": "In a world where squirrels control everything through their massive robotech suits, humanity has lost its freedom. The brutality these squirrels exert on their citizens feels like a distant dream for most—far from the harsh reality. Now, you stand at a crossroads. Who are you in this dystopian world?",
        "loot": [],
        "options": [
            {"text": "I am a rebel, fighting for freedom.", "next_id": 2},
            {"text": "I am a squirrel, one of the oppressive leaders.", "next_id": 3},
            {"text": "I am a neutral observer, just trying to survive.", "next_id": 4}
        ]
    },

    {
        "id": 2,
        "title": "The Rebel's Path",
        "text": "As a rebel, you’ve participated in many actions against the squirrels' regime. Your latest actions have made you a primary target of the squirrels. You know you need to find a place to hide or perhaps ally with other resistance groups to stand a chance.",
        "loot": ["Rebel Medkit", "Tarnished Spoon", "Squirrel Credits"],
        "options": [
            {"text": "Seek shelter with another rebel cell.", "next_id": 5},
            {"text": "Go off on your own to avoid detection.", "next_id": 6},
            {"text": "Use the Rebel Medkit to heal your wounds.", "next_id": 27, "item_required": "Rebel Medkit"},
            {"text": "Use the Tarnished Spoon to craft a makeshift weapon.", "next_id": 32, "item_required": "Tarnished Spoon"}
        ]
    },

    {
        "id": 3,
        "title": "The Squirrel Regime",
        "text": "As one of the squirrels in power, you were raised in a world where control, discipline, and absolute obedience are everything. You control one of the largest robotech suits, and you’ve recently been given a new mission: to find and eliminate any resistance groups threatening your vision for the future.",
        "loot": ["Stealth Cloak", "Squirrel Credits", "Armor Plating"],
        "options": [
            {"text": "Start a large-scale hunt for the rebels.", "next_id": 7},
            {"text": "Doubt the regime's methods and seek a different path.", "next_id": 8},
            {"text": "Use the Stealth Cloak to blend in and gather information.", "next_id": 28, "item_required": "Stealth Cloak"},
            {"text": "Use the Squirrel Credits to bribe a guard for information.", "next_id": 33, "item_required": "Squirrel Credits"},
            {"text": "Use Armor Plating to upgrade your robotech suit.", "next_id": 40, "item_required": "Armor Plating"}
        ]
    },

    {
        "id": 4,
        "title": "The Path of Neutrality",
        "text": "As a neutral observer, you try to stay out of the conflicts between the rebels and squirrels. Your goal is to survive in this new world. But how long can you stay on the sidelines when both sides are watching you?",
        "loot": ["Squirrel Tech Device", "Survival Seeds", "Rebel Knife", "Power Cell"],
        "options": [
            {"text": "Try to sneak through the squirrels' territorial borders to reach a safe place.", "next_id": 9},
            {"text": "Go to the resistance group to possibly find allies who can help you.", "next_id": 10},
            {"text": "Use the Squirrel Tech Device to hack into their surveillance system.", "next_id": 29, "item_required": "Squirrel Tech Device"},
            {"text": "Use the Survival Seeds to barter for safe passage.", "next_id": 34, "item_required": "Survival Seeds"},
            {"text": "Use the Rebel Knife to defend yourself against an incoming attack.", "next_id": 35, "item_required": "Rebel Knife"},
            {"text": "Use the Power Cell to charge a nearby transport vehicle.", "next_id": 41, "item_required": "Power Cell"}
        ]
    },

    {
        "id": 5,
        "title": "A Dangerous Alliance",
        "text": "You find a small group of rebels willing to help you. But to gain their trust, you must carry out a dangerous mission—to sabotage a key squirrel factory producing new robotech suits.",
        "loot": ["Rebel Medkit", "Stealth Cloak", "Tarnished Spoon", "Squirrel Tech Device"],
        "options": [
            {"text": "Accept the mission and go sabotage the factory.", "next_id": 11},
            {"text": "Refuse the mission, it's too risky.", "next_id": 12},
            {"text": "Use the Stealth Cloak to infiltrate the factory unnoticed.", "next_id": 30, "item_required": "Stealth Cloak"},
            {"text": "Use the Tarnished Spoon to disable the factory’s machinery.", "next_id": 36, "item_required": "Tarnished Spoon"},
            {"text": "Use the Squirrel Tech Device to disable the security system.", "next_id": 42, "item_required": "Squirrel Tech Device"}
        ]
    },

    {
        "id": 6,
        "title": "Alone on the Run",
        "text": "You move through dark alleys, trying to keep a low profile, but suddenly, you hear the sound of large robotech suits approaching. The squirrels have caught wind of your location. You must make a quick decision to survive.",
        "loot": ["Rebel Medkit", "Squirrel Credits", "Power Cell"],
        "options": [
            {"text": "Seek shelter in an abandoned building.", "next_id": 13},
            {"text": "Stand and confront them, hoping to escape at the last moment.", "next_id": 14},
            {"text": "Use the Rebel Medkit to heal yourself before the confrontation.", "next_id": 31, "item_required": "Rebel Medkit"},
            {"text": "Use the Squirrel Credits to bribe a passerby for directions.", "next_id": 37, "item_required": "Squirrel Credits"},
            {"text": "Use the Power Cell to power up a nearby transport for a quick escape.", "next_id": 43, "item_required": "Power Cell"}
        ]
    },

    {
        "id": 7,
        "title": "The Hunt Begins",
        "text": "You mobilize a full-scale operation against the rebels. Your robotech suit is a formidable weapon, and with your team of elite squirrel soldiers, you track down their hideouts one by one. However, the deeper you get into the hunt, the more you start to question if this is the right path.",
        "loot": [],
        "options": [
            {"text": "Push forward, complete the mission for the regime.", "next_id": 15},
            {"text": "Begin to question the ethics of the hunt and seek a different path.", "next_id": 16}
        ]
    },

    {
        "id": 8,
        "title": "A Doubtful Leader",
        "text": "You begin to have doubts about the regime's methods. The violent oppression weighs heavily on your conscience. Could there be another way, one that doesn't involve destruction and control? Perhaps there are other squirrels who share your doubts.",
        "loot": ["Squirrel Tech Device", "Squirrel Armor", "Rebel Knife"],
        "options": [
            {"text": "Seek out other squirrels who might be sympathetic to your cause.", "next_id": 17},
            {"text": "Dismiss your doubts and continue following orders.", "next_id": 18},
            {"text": "Use the Squirrel Tech Device to contact other sympathetic squirrels.", "next_id": 44, "item_required": "Squirrel Tech Device"}
        ]
    },

    {
        "id": 9,
        "title": "Crossing Enemy Lines",
        "text": "You manage to sneak through the borders of the squirrel-controlled zones. However, the further you travel, the more you realize that you are getting closer to a major resistance hideout. There is a high chance you might be discovered, but also an opportunity to find allies.",
        "loot": [],
        "options": [
            {"text": "Continue moving forward, hoping to make contact with the resistance.", "next_id": 19},
            {"text": "Turn back and find another route to escape detection.", "next_id": 20}
        ]
    },

    {
        "id": 10,
        "title": "The Resistance's Offer",
        "text": "You meet with the resistance group, and after a tense discussion, they offer you an opportunity to join their cause. However, they need you to prove your loyalty by taking part in a high-risk mission to destroy one of the squirrels' largest weapon caches.",
        "loot": ["Rebel Knife", "Rebel Medkit", "Squirrel Tech Device"],
        "options": [
            {"text": "Agree to take the mission and prove your loyalty.", "next_id": 21},
            {"text": "Refuse the mission, unsure if you can trust the resistance.", "next_id": 22},
            {"text": "Use the Rebel Knife to cut through security fencing.", "next_id": 45, "item_required": "Rebel Knife"}
        ]
    },

    {
        "id": 27,
        "title": "Healing the Wounds",
        "text": "You use the Rebel Medkit to patch up your injuries. The pain eases, but the tension remains. You feel slightly better but know you’re not fully safe yet.",
        "loot": [],
        "options": [
            {"text": "Seek shelter with another rebel cell.", "next_id": 5},
            {"text": "Go off on your own to avoid detection.", "next_id": 6}
        ]
    },

    {
        "id": 28,
        "title": "Blending In",
        "text": "You activate the Stealth Cloak, making yourself nearly invisible to the squirrels around you. You move quietly, gathering information, but must be careful not to draw attention.",
        "loot": [],
        "options": [
            {"text": "Use the information you gathered to plan your next move.", "next_id": 7},
            {"text": "Move deeper into enemy territory to gather more intel.", "next_id": 8}
        ]
    },

    {
        "id": 29,
        "title": "Hacking the Surveillance",
        "text": "You use the Squirrel Tech Device to hack into their surveillance system. The cameras in the area go dark, allowing you to move undetected. However, you only have a limited amount of time before the system resets.",
        "loot": [],
        "options": [
            {"text": "Move quickly through the blind spots to escape.", "next_id": 9},
            {"text": "Use the time to gather crucial intel about their operations.", "next_id": 10}
        ]
    },

    {
        "id": 30,
        "title": "Infiltration",
        "text": "You use the Stealth Cloak to sneak into the squirrel factory. You move undetected through the halls, but you know time is running out. You need to act quickly.",
        "loot": [],
        "options": [
            {"text": "Sabotage the equipment and plant explosives.", "next_id": 11},
            {"text": "Explore the factory further to find more valuable targets.", "next_id": 12}
        ]
    },

    {
        "id": 31,
        "title": "Prepping for the Confrontation",
        "text": "You heal yourself with the Rebel Medkit, but you're still not at your best. With the robotech suits closing in, you must decide how to face them.",
        "loot": [],
        "options": [
            {"text": "Seek shelter in an abandoned building.", "next_id": 13},
            {"text": "Stand and confront them, hoping to escape at the last moment.", "next_id": 14}
        ]
    },

    {
        "id": 32,
        "title": "Improvised Weapon",
        "text": "You use the Tarnished Spoon to fashion a crude weapon. It's not ideal, but it might help you in close combat if necessary.",
        "loot": [],
        "options": [
            {"text": "Use the makeshift weapon to confront an incoming guard.", "next_id": 38},
            {"text": "Keep the weapon hidden and move stealthily.", "next_id": 39}
        ]
    },

    {
        "id": 33,
        "title": "Bribe for Information",
        "text": "You offer your Squirrel Credits to the guard, and after some hesitation, they give you valuable information about the enemy’s movements.",
        "loot": [],
        "options": [
            {"text": "Use the information to avoid a trap and escape.", "next_id": 7},
            {"text": "Plan your next move based on the new intel.", "next_id": 8}
        ]
    },

    {
        "id": 34,
        "title": "Barter for Safe Passage",
        "text": "You offer the Survival Seeds to a local merchant who agrees to let you pass through safely. The seeds might have been worth more in another place, but here they are of value to the right person.",
        "loot": [],
        "options": [
            {"text": "Continue traveling with your new knowledge.", "next_id": 9},
            {"text": "Try to find out more about the merchant's connections.", "next_id": 10}
        ]
    },

    {
        "id": 45,
        "title": "Cutting the Fence",
        "text": "You quietly cut through the security fencing around the weapon cache. The resistance members follow you, and after some tense moments, you manage to infiltrate the facility. The mission is more dangerous than you expected.",
        "loot": ["Weapons Cache", "Squirrel Armor", "Gold Coins"],
        "options": [
            {"text": "Take the loot and leave the facility quickly.", "next_id": 46},
            {"text": "Plant explosives to destroy the weapons cache.", "next_id": 47}
        ]
    },

    {
        "id": 46,
        "title": "A Rich Escape",
        "text": "With the loot secured, you exit the facility just before the guards arrive. You've made it out with some valuable items—Weapons Cache, Squirrel Armor, and Gold Coins. The resistance will be pleased with your contribution.",
        "loot": ["Weapons Cache", "Squirrel Armor", "Gold Coins"],
        "options": [
            {"text": "Return to the resistance to deliver the goods.", "next_id": 48},
            {"text": "Go rogue and use the loot for your own benefit.", "next_id": 49}
        ]
    },

    {
        "id": 48,
        "title": "A Hero's Reward",
        "text": "You return to the resistance with the loot. Your actions have secured their trust, and they begin to plan a major assault against the squirrels' regime. The balance is starting to shift in favor of the oppressed.",
        "loot": [],
        "options": [
            {"text": "Join the final assault against the squirrels.", "next_id": 50},
            {"text": "Use your newfound power to establish a new government.", "next_id": 51}
        ]
    },

    {
        "id": 50,
        "title": "Victory Over Tyranny",
        "text": "With the resistance's full support, you lead a final assault against the squirrels' regime. The oppressive robotech suits are dismantled, and the squirrels' reign comes to an end. The world begins to heal, and you are hailed as a hero.",
        "loot": [],
        "options": [
            {"text": "Lead the rebuilding efforts in a free world.", "next_id": 52},
            {"text": "Retire and leave the world to the next generation.", "next_id": 53}
        ]
    },

    {
        "id": 52,
        "title": "Rebuilding the World",
        "text": "As the new leader, you help rebuild the world from the ashes. With your vision and determination, you create a society where no one will ever be oppressed again. Peace reigns.",
        "loot": [],
        "options": [
            {"text": "Continue leading as the world flourishes.", "next_id": 54},
            {"text": "Step down and let the world continue without you.", "next_id": 55}
        ]
    },
    
    {
        "id": 54,
        "title": "The Eternal Leader",
        "text": "Your leadership is timeless. Generations remember your sacrifices, and the world prospers under your guidance. You have truly changed the course of history for the better.",
        "loot": [],
        "options": []
    }
]
