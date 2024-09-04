from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'npm' : '2306213136',
        'name': 'Daanish Inayat Rahman',
        'class': 'PBP A'
    }

    return render(request, "main.html", context)