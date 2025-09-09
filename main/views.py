from django.shortcuts import render

# Create your views here.

def show_main(request):
    context = {
        'name': 'Chris Darren',
        'npm': '2406396956',
        'store_name' : 'Lil Champs'
    }


    return render(request, "main.html", context)