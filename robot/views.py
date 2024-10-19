from django.shortcuts import render
from django.views.decorators.http import require_POST

from robot.form.robot_form import ConstructForm


def index(request):
    return render(request, "pages/index.html")


@require_POST
def create(request):
    form = ConstructForm(request.POST)
    if form.is_valid():
        outinput(request.POST)
        form.save()
    return render(request, "pages/index.html", {"form": form})


def outinput(data):
    start_x, start_y = int(data["start_column"]), int(data["start_row"])
    original_step = [start_x, start_y]
    position = data["position"]

    def compare(x, y):
        on_going = original_step[0] + x, original_step[1] + y
        while on_going == [start_x, start_y]:
            on_going = original_step[0] + x, original_step[1] + y
        return on_going

    for items in position:
        if items.upper() == "N":
            original_step = compare(0, -1)
        elif items.upper() == "W":
            original_step = compare(-1, 0)
        elif items.upper() == "S":
            original_step = compare(0, 1)
        elif items.upper() == "E":
            original_step = compare(1, 0)

    return f"Case #{i}{original_step[0]} {original_step[1]}"
