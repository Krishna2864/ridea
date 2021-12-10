from django.forms import  ModelForm

class Userform(ModelForm):
    class META:
        form = Username
        field = '__all__'