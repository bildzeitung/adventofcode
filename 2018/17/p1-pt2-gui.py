#!/usr/bin/env python
"""
    Day 17

    Interactive app. Just because.

"""
import sys
from pathlib import Path
from prompt_toolkit import Application
from prompt_toolkit.layout.containers import Window, HSplit
from prompt_toolkit.layout.controls import FormattedTextControl
from prompt_toolkit.widgets import HorizontalLine
from prompt_toolkit.layout.layout import Layout
from prompt_toolkit.key_binding import KeyBindings


SPRING = (500, 0)
coords = {}


def display():
    """ Match the output from puzzle description
    """
    min_x = min(i[0] for i in coords)
    max_x = max(i[0] for i in coords)
    min_y = min(i[1] for i in coords)
    max_y = max(i[1] for i in coords)

    lines = []

    for y in range(min_y, max_y + 1):
        row = ""
        for x in range(min_x, max_x + 1):
            if (x, y) in coords:
                row += coords[(x, y)]
            else:
                row += "."
        lines.append(row)
    return "\n".join(lines)


# start from spring
oset = [SPRING]
finished = set()

status = FormattedTextControl()


def drip():
    max_y = max(i[1] for i in coords)
    #
    # Victory condition; display results in status bar
    #
    if not oset:
        min_y = min(k[1] for k, i in coords.items() if i == "#")
        # count all water characters
        total_water = sum(v in ("~", "|") for c, v in coords.items() if c[1] >= min_y)
        # just count the settled water
        drained = sum(v == "~" for c, v in coords.items() if c[1] >= min_y)
        status.text = f"TOTAL: {total_water} {drained}"
        return

    # treat water as a stack
    active = oset.pop()
    status.text = f"({active[0]}, {active[1]}) "

    # By default, I want to go down
    down = (active[0], active[1] + 1)

    # Am I part of a drip? If so, I'm done
    if down in coords and coords[down] == "|":
        status.text += "I am a drip"
        return

    # Bounds check to stop flowing down
    if down[1] > max_y:
        status.text += "is outflow"
        return

    # Proceed down until out of range or hit something
    while down[1] <= max_y and down not in coords:
        coords[down] = "|"
        oset.append(active)  # for later
        oset.append(down)
        status.text += "dripped"
        return

    # walk left and right until a boundary is hit
    left = (active[0] - 1, active[1])
    down = (left[0], left[1] + 1)
    while (
        (left not in coords or coords[left] == "|")
        and down in coords
        and coords[down] != "|"
    ):
        coords[left] = "|"
        left = (left[0] - 1, left[1])
        down = (left[0], left[1] + 1)

    right = (active[0] + 1, active[1])
    down = (right[0], right[1] + 1)
    while (
        (right not in coords or coords[right] == "|")
        and down in coords
        and coords[down] != "|"
    ):
        coords[right] = "|"
        right = (right[0] + 1, right[1])
        down = (right[0], right[1] + 1)

    # contained? If so, then the row is still water
    if (
        left in coords
        and right in coords
        and coords[left] == "#"
        and coords[right] == "#"
    ):
        for i in range(left[0] + 1, right[0]):
            coords[(i, active[1])] = "~"
        status.text += "settled"

    if left not in coords:
        coords[left] = "|"
        oset.append(left)
        status.text += "open left"

    if right not in coords:
        oset.append(right)
        status.text += "open right"


kb = KeyBindings()
ftc = FormattedTextControl()


@kb.add("c")
def render(event):
    drip()
    ftc.text = display()


@kb.add("q")
def exit_(event):
    event.app.exit()


@kb.add("g")
def go(event):
    while oset:
        drip()
    ftc.text = display()
    drip()


@kb.add("s")
def save(event):
    with open("output.txt", "w") as f:
        f.write(display())


def main():
    with Path(sys.argv[1]).open() as f:
        # eg. x=495, y=2..7
        for line in f:
            c1, c2 = [x.strip() for x in line.split(",")]
            const_coord, value = c1.split("=")
            value = int(value)
            var_coord, val_range = c2.split("=")
            val_range = [int(x) for x in val_range.split("..")]
            for i in range(val_range[0], val_range[1] + 1):
                if const_coord == "x":
                    coords[(value, i)] = "#"
                else:
                    coords[(i, value)] = "#"

    # add water spring
    coords[SPRING] = "+"

    ftc.text = display()
    root = HSplit(
        [Window(content=ftc), HorizontalLine(), Window(content=status, height=1)]
    )
    layout = Layout(root)

    app = Application(layout=layout, key_bindings=kb, full_screen=True)
    app.run()

    # drip(coords)


if __name__ == "__main__":
    main()
