from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db.backends.utils import logger
from django.shortcuts import render, redirect
from django.http import HttpResponse

import random
import itertools

from gifts.models import Gift, Shaker, Invitation, Pairs
from gifts.forms import CreateGift, CreateInvitation, DeleteInvitation, \
    DeleteGift, CreateShaker, AddPersonToShaker


@login_required(login_url='')
def home(request):
    return render(request, 'home.html')


@login_required(login_url='all_gifts')
def gifts(request):
    gifts_data = Gift.objects.filter(author_id=request.user.id)

    return render(request, 'gifts.html', {'gift': gifts_data})


@login_required(login_url='delete_gift')
def delete_gift(request, pk):
    gift = Gift.objects.get(id=pk)
    form = DeleteGift(instance=gift)

    if request.method == 'POST':
        gift.delete()
        return redirect('all_gifts')

    context = {'form': form}
    return render(request, 'delete_gift.html', context)


@login_required(login_url='update_gift')
def update_gift(request, pk):
    gift = Gift.objects.get(id=pk)
    form = CreateGift(instance=gift)

    if request.method == 'POST':
        form = CreateGift(request.POST, instance=gift)

        if form.is_valid():
            form.save()
            return redirect('all_gifts')

    context = {'form': form}
    return render(request, 'update_gift.html', context)


@login_required(login_url='new_gift')
def create_gift(request):
    author = User.objects.get(id=request.user.id)

    if request.method == 'POST':
        form = CreateGift(request.POST)

        if form.is_valid():
            gift = form.save(commit=False)
            gift.author_id = author
            gift.save()
            return redirect('all_gifts')

    formset = CreateGift()
    context = {'form': formset}

    return render(request, 'add_gift.html', context)


@login_required(login_url='invite')
def create_invitation(request):
    owner = User.objects.get(id=request.user.id)

    if request.method == 'POST':
        form = CreateInvitation(request.POST)

        if form.is_valid():
            invitation = form.save(commit=False)
            invitation.owner = owner
            invitation.save()
            return redirect('all_invitations')

    formset = CreateInvitation()
    context = {'form': formset}

    return render(request, 'invite.html', context)


@login_required(login_url='all_invitations')
def invitations(request):
    invitations_data = Invitation.objects.filter(owner=request.user.id)

    return render(request, 'invitations.html', {'invitations': invitations_data})


@login_required(login_url='gifts/all_invitations/invitation/delete')
def delete_invitation(request, pk):
    invitation = Invitation.objects.get(id=pk)
    form = DeleteInvitation(instance=invitation)

    if request.method == 'POST':
        invitation.delete()
        return redirect('all_invitations')

    context = {'form': form}

    return render(request, 'delete_invitation.html', context)


@login_required(login_url='all_shakers')
def shakers(request):
    shakers_data = Shaker.objects.filter(user_in_shake=request.user.id).values()

    return render(request, 'shakers.html', {'shakers': shakers_data})


@login_required(login_url='new_shaker')
def create_shaker(request):
    owner = User.objects.get(id=request.user.id)

    if request.method == 'POST':
        form = CreateShaker(request.POST)
        if form.is_valid():
            shaker = form.save()
            shaker.owner = request.user.id
            shaker.save()
            shaker.user_in_shake.add(owner)

            return redirect('all_shakers')

    formset = CreateShaker()

    return render(request, 'new_shaker.html', {'form': formset})


@login_required(login_url='add_person')
def add_person_to_shaker(request, pk):
    form = AddPersonToShaker()
    shaker = Shaker.objects.get(id=pk)

    if request.method == 'POST':
        person = User.objects.get(username=request.POST.get('username'))
        shaker.user_in_shake.add(person)

    users = shaker.user_in_shake.all()
    context = {'form': form, 'users': users}

    return render(request, 'invite_into_shaker.html', context)


@login_required(login_url='shake')
def shake(request, pk):
    checked = {}
    shaker = Shaker.objects.get(id=pk)
    users = list(shaker.user_in_shake.all())
    random.shuffle(users)

    while len(checked.keys()) < len(users):
        permutation = list(itertools.permutations(users, 2))
        random.shuffle(permutation)

        for i in permutation:
            if i[1] not in checked.values():
                checked.update(dict([i]))

    for i in checked:
        pair = Pairs(user_1=i, user_2=checked[i], shaker=shaker)

        try:
            pair.save()
        except Exception as e:
            logger.error(e.__str__())
            return HttpResponse('Shaker ju?? wymieszany')

    return render(request, 'shakers.html')


@login_required(login_url='gifts_of_shaked_users')
def gifts_of_shaked_users(request, pk):
    shaked_user = Pairs.objects.filter(user_1=request.user.id).filter(shaker=pk)
    gifts_data = Gift.objects.filter(author_id=shaked_user[0].user_2)

    return render(request, 'gifts_of_shaked_user.html', {'gift': gifts_data})
