from django.shortcuts import render

def show_main(request):
    context = {
        'npm' : '2406435881',
        'name': 'Rheina Adinda Morani Sinurat',
        'class': 'PBP E'
    }

    return render(request, "main.html", context)
# Create your views here.
