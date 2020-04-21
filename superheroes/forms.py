from django.forms import ModelForm

from superheroes.models import Hero


class HeroForm(ModelForm):
    class Meta:
        model = Hero
        fields = '__all__'
