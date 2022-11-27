from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

# Create your views here.
from gifts.models import Gifts
from gifts.forms import CreateGift


@login_required(login_url='')
def home(request):
    return render(request, 'home.html')


@login_required(login_url='all_gifts')
def gifts(request):

    gifts_data = Gifts.objects.all()

    return render(request, 'gifts.html', {'gift': gifts_data})


@login_required(login_url='new_gift')
def new_gift(request):
    author = User.objects.get(id=request.user.id)

    if request.method == 'POST':
        form = CreateGift(request.POST)
        if form.is_valid():
            gift = form.save(commit=False)
            gift.author_id = author
            gift.save()
            return redirect('all_gifts')

    formset = CreateGift()
    for i in formset:
        print(i)
    context = {'form': formset}

    return render(request, 'add_gift.html', context)

