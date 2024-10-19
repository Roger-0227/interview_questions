from django.forms import ModelForm

from robot.models import Construct


class ConstructForm(ModelForm):
    class Meta:
        model = Construct
        fields = [
            "instructions",
            "rows",
            "columns",
            "start_row",
            "start_column",
            "position",
        ]
