from django.forms import ModelForm

from projectapp.models import Project


class ProjectCreationView(ModelForm):
    class Meta:
        model = Project
        fields = ['name','description','image']