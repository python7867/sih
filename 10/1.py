
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
