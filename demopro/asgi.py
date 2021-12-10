# save the form
def home(request):
    if request.method = 'POST':
        Username = UserForm(request.POST)
        if Username.is_valid():
            Username.save()

