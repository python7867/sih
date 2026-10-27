
from collections import deque

acts = {
    "pickup key": {
        "pre": ["at robot rooma", "keyat rooma"],
        "add": ["has key"],
        "remove": ["keyat rooma"]
    },
    "unlock door": {
        "pre": ["at robot rooma", "has key", "locked door"],
        "add": ["unlocked door"],
        "remove": ["locked door"]
    },
    "open door": {
        "pre": ["at robot rooma", "unlocked door"],
        "add": ["open door"],
        "remove": []
    },
    "move ab": {
        "pre": ["at robot rooma", "open door"],
        "add": ["at robot roomb"],
        "remove": ["at robot rooma"]
    }
}

start = {"at robot rooma", "keyat rooma", "locked door"}
goal = {"at robot roomb"}
