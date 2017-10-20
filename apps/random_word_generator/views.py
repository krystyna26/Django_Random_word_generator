from django.shortcuts import render, HttpResponse, redirect
from django.utils.crypto import get_random_string
unique_id = get_random_string(length=14)
unique_id
u'rRXVe68NO7m3mHoBS488KdHaqQPD6Ofv'

# the index function is called when root is visited
def nothing(request):
    return redirect('/random_word')


def index(request):
    context = {
        "number" : get_random_string(length=14),
    }
    # count attempt
    if 'count' in request.session:
        request.session['count'] += 1 # session[key] = value
    else:
        request.session['count'] = 1
    return render(request, "random_word_generator/index.html", context, request.session['count'])


def generateRand(request):
    if request.method == "POST":
        context = {
            "number" : get_random_string(length=14),
        }
    return redirect("/random_word")


def reset(request):
    if 'count' in request.session:
        request.session['count'] = 0
    else:
        request.session['count'] = request.session['count']
    return redirect('/random_word')