
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

def find_plan(start, goal):
    q = deque([(start, [])])
    vis = [start]

    while q:
        st, plan = q.popleft()

        if goal <= st:
            return plan

        for name, act in acts.items():
            if set(act["pre"]) <= st:
                new = (st - set(act["remove"])) | set(act["add"])

                if new not in vis:
                    vis.append(new)
                    q.append((new, plan + [name]))

    return None

plan = find_plan(start, goal)

if plan:
    for i, action in enumerate(plan, 1):
        print(i, action)
else:
    print("no plan")
