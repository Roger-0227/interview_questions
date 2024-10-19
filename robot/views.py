from django.shortcuts import render
from django.views.decorators.http import require_POST

from robot.form.construct_form import ConstructForm
from robot.form.client_form import ClientForm
from robot.models import Client, Construct


def index(request):
    return render(request, "pages/index.html")


@require_POST
def client(request):
    client_form = ClientForm(request.POST)
    client_form.save()
    content = {
        "form": client_form,
        "number": 1,
        "name": request.POST.get("name"),
        "cases": request.POST.get("cases"),
    }
    return render(request, "pages/create.html", content)


@require_POST
def create(request):
    form = ConstructForm(request.POST)
    cases = request.POST.get("cases")
    name = request.POST.get("name")
    number = request.POST.get("number")
    result_list = Construct.objects.filter(name__name=name)
    breakpoint()
    if int(number) <= int(cases):
        if form.is_valid():
            form = form.save(commit=False)
            form.name = Client.objects.filter(name=name).first()
            form.cases = Client.objects.filter(cases=cases).first()
            form.result_case = output(request.POST, number)
            form.save()
            number = int(number) + 1
            content = {
                "form": form,
                "name": name,
                "number": number,
                "cases": cases,
            }

            return render(request, "pages/create.html", content)
    return render(
        request,
        "pages/result.html",
        {
            "name": name,
            "result_list": result_list,
        },
    )


def output(data, number):
    # robot = Construct.objects.filter()
    start_x, start_y = int(data["start_column"]), int(data["start_row"])
    original_step = (start_x, start_y)
    position = data["position"]
    route = [original_step]
    explore = [original_step]

    def compare(x, y):
        on_going = original_step[0] + x, original_step[1] + y
        if on_going in route:
            while on_going in route:
                on_going = on_going[0] + x, on_going[1] + y
            explore.append(on_going)
        route.append(on_going)
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

    return f"Case #{number}: {original_step[1]} {original_step[0]}"


# def result(request, id):
#     pass
