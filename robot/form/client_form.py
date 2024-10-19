from django.forms import ModelForm

from robot.models import Client


class ClientForm(ModelForm):
    class Meta:
        model = Client
        fields = [
            "name",
            "cases",
        ]
