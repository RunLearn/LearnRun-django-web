from django.forms import ModelForm

from profileapp.models import Profile

app_name = 'profileapp'

class ProfileCreationForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['image', 'nickname', 'message']