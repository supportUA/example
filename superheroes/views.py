from django.core.paginator import PageNotAnInteger, EmptyPage, Paginator
from django.shortcuts import get_object_or_404, redirect

from superheroes.forms import HeroForm
from superheroes.models import Hero

from django.shortcuts import render



def index(request):
    object_list = Hero.objects.filter(status='published')
    page = request.GET.get('page', 1)
    paginator = Paginator(object_list, 5)  # 5 на каждой странице
    try:
        heroes = paginator.page(page)
    except PageNotAnInteger:
        heroes = paginator.page(1)
    except EmptyPage:
        heroes = paginator.page(paginator.num_pages)
    return render(request, 'superheroes/index.html',
                  {'page': page, 'heroes': heroes})


def hero_detail(request, hero_id):
    # Страница одного героя
    hero = get_object_or_404(Hero, pk=hero_id)
    return render(request, 'superheroes/single.html', {'hero': hero})


def create_hero(request):
    # Функция создать героя
    form = HeroForm()
    if request.method == 'POST':
        form = HeroForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form': form}
    return render(request, 'superheroes/forms/create.html', context)


def update_hero(request, pk):
    # Функция обновить героя
    hero = Hero.objects.get(id=pk)
    form = HeroForm(instance=hero)
    if request.method == 'POST':
        form = HeroForm(request.POST, request.FILES, instance=hero)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {"form": form, 'hero': hero}
    return render(request, 'superheroes/forms/save.html', context)


def delete_hero(request, pk):
    # Функция удалить героя
    hero = Hero.objects.get(id=pk)
    if request.method == 'POST':
        hero.delete()
        return redirect('/')
    context = {'item': hero}
    return render(request, 'superheroes/forms/delete_hero.html', context)

