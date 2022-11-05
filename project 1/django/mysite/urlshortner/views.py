from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .models import ShortUrls

from datetime import datetime
from random import choice, randint
import string


def generate_short_id(num_of_chars: int):
    return ''.join(choice(string.ascii_letters+string.digits) for _ in range(num_of_chars))

@csrf_exempt
def index(request):
    if request.method == 'POST':
        url = request.POST['url']

        # redirect to index page if url is empty
        if not url:
            return render(request, 'index.html')

        short_id = generate_short_id(8)

        # save url and short_id to database
        new_link = ShortUrls(original_url=url, short_id=short_id, created_at=datetime.now())
        new_link.save()
        short_url = request.build_absolute_uri() + short_id

        return render(request, 'index.html', {'short_url': short_url})

    return render(request, 'index.html')
    # return HttpResponse("Hello, world. You're at the polls index.")

def redirect_url(request, short_id):
    link = ShortUrls.objects.get(short_id=short_id)
    if link:
        return redirect(link.original_url)
    else:
        return render(request, 'index.html')

def random(request):
    link = ShortUrls.objects.all()
    if link:
        return redirect(link[randint(0,len(link)-1)].original_url)
    else:
        return render(request, 'index.html')


