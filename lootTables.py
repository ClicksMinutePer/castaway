import random

scavenging = {
    "peritem": {
        "div": 2,
        "min": 2,
        "max": 10
    },
    "types": {
        0: 5,
        1: 4,
        2: 3,
        3: 3
    }
}

fishing = {
    "peritem": {
        "div": 1,
        "min": 0,
        "max": 2
    },
    "types": {
        40: 1
    }
}

mining = {
    "peritem": {
        "div": 1,
        "min": 0,
        "max": 1
    },
    "types": {
        10: 15,
        11: 1,
        12: 3,
        13: 10
    }
}

farming = {
    "peritem": {
        "div": 1,
        "min": 0,
        "max": 2
    },
    "types": {
        41: 5,
        42: 5,
        43: 1,
        44: 4,
        45: 5,
        46: 2,
        47: 4,
        48: 4,
        49: 5
    }
}

exploring = {
    "peritem": {
        "div": 10,
        "min": 1,
        "max": 2
    },
    "types": {
        "fishing_spots": 3,
        "mines": 1,
        "undiscovered_land": 2,
        "farms": 3
    }
}


class LootTable:
    def __init__(self, minutes, level=1, hunger=10, water=10):
        self.minutes = minutes
        self.level = level
        self.food = hunger
        self.water = water

    def getTable(self):
        levelMult = (1.5 * self.level**2) + 13
        return ((levelMult*self.minutes)/(.1*self.minutes+10))*((min(self.food, 5)+5)/10)*(self.water/10)

    def table(self, amount, table):
        rewards = []
        for _ in range(round(amount/table["peritem"]["div"])):
            chance = random.randint(table["peritem"]["min"], table["peritem"]["max"])
            rewards += random.choices(
                population=list(table["types"].keys()),
                weights=list(table["types"].values()),
                k=chance
            )
        return rewards
