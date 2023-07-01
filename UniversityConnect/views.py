from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.models import User, AnonymousUser
from googletrans import Translator
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .models import Curso
from django.shortcuts import get_object_or_404

def homepage(request):
    PAGE_NAME = 'Home'
    user = request.user
    if isinstance(user, AnonymousUser):
        return render(request, 'UniversityConnect/html/pt/index.html', {
            'request': request,
            })
    else:
        social_account = user.socialaccount_set.first()
        if social_account:
            user_social = social_account.user
            user_social.username = user_social.username.title()
            return render(request, 'UniversityConnect/html/pt/index.html', {
            'request': request,
            'user': user_social,
            })
        else:
            return render(request, 'UniversityConnect/html/pt/index.html', {
            'request': request,
            })

@csrf_protect
def cursos(request):
    PAGE_NAME = 'Cursos'
    if request.method == 'POST':
        novo_titulo = request.POST.get('novo_titulo')
        primeiro_curso = Curso.objects.first()

        if novo_titulo and primeiro_curso:
            primeiro_curso.titulo = novo_titulo
            primeiro_curso.save()

    curso = Curso.objects.all()
    for curso in curso:
        trans = Translator()
        titulo_en = trans.translate(curso.titulo, dest='en').text
        curso.tittle_en = titulo_en
        description_en = trans.translate(curso.titulo, dest='en').text
        curso.description_en = description_en
        curso.save()

    categoria_selecionada = request.GET.get('categoria', '')
    if categoria_selecionada == '':
        curso = Curso.objects.all()
    else:
        curso = Curso.objects.filter(categoria=categoria_selecionada)
    context = {'request': request, 'curso': curso, 'page_name': 'Cursos', 'page_name': PAGE_NAME,}
    return render(request, 'UniversityConnect/html/pt/cursos.html', context=context)



def cursos_detail(request, id):
    curso = get_object_or_404(
        Curso,
        id=id,
    )

    PAGE_NAME = f'{curso.titulo}'
    context = {'request': request, 'curso': curso, 'page_name': 'Cursos', 'page_name': PAGE_NAME,}
    return render(request, 'UniversityConnect/html/pt/cursos_detail.html', context=context)




@login_required(login_url='/accounts/login/')
def profile(request):
    PAGE_NAME = 'Cursos'
    context = {'request': request, 'page_name': 'Perfil','page_name': PAGE_NAME,}

    return render(request, 'UniversityConnect/html/pt/profile.html', context=context)



