from django.shortcuts import render, redirect
from orders.models import Order
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse


def sign_up(request):
    if request.method == 'GET':
        return render(request, 'accounts/signup.html', context={
            'title': 'Реєстрація',
        })
    elif request.method == 'POST':
        # 1 - Зчитування данних іх форми
        login_x = request.POST.get('login')
        pass1_x = request.POST.get('pass1')
        email_x = request.POST.get('email')

        # 2 - Додавання користувача у базу
        user = User.objects.create_user(login_x, email_x, pass1_x)
        user.save()

        # 3 - Формування звіту:
        color = 'red'
        report = 'В реєстрації відмовлено!'
        if user is not None:
            color = '#43F727'
            report = 'Реєстрація успішно завершена!'

        # 4 - Завантаження сторінки звіту
        return render(request, 'accounts/reports.html', context={
            'title': 'Звіт про Реєстрацію',
            'color': color,
            'report': report,
            'app': 'reports',
        })


def sign_in(request):
    if request.method == 'GET':
        return render(request, 'accounts/signin.html', context={
            'title': 'Авторизація',
        })
    elif request.method == 'POST':
        # 1 - Зчитування данних іх форми
        login_x = request.POST.get('login')
        pass1_x = request.POST.get('pass1')

        # 2 - Перевірка пари "Логин\Пароль"
        user = authenticate(request, username=login_x, password=pass1_x)

        # 3 - Формування звіту:
        color = 'red'
        report = 'Користувач не знайдений!'
        if user is not None:
            color = '#43F727'
            report = 'Авторизація успішно завершена!'
            login(request, user)

        # 4 - Завантаження сторінки звіту
        return render(request, 'accounts/reports.html', context={
            'title': 'Звіт про Авторизацію',
            'color': color,
            'report': report,
            'app': 'reports',
        })


def sign_out(request):
    logout(request)
    return redirect('/')


def profile(request):
    return render(request, 'accounts/profile.html', context={
        'title': 'Профіль користувача',
        'app': 'Profile',
    })


def ajax_reg(request):
    response = dict()
    login = request.GET.get('login')
    email = request.GET.get('email')
    try:
        User.objects.get(username=login)
        response['login_message'] = 'зайнятий'
    except User.DoesNotExist:
        response['login_message'] = 'вільний'

    try:
        User.objects.get(email=email)
        response['email_message'] = 'зайнятий'
    except User.DoesNotExist:
        response['email_message'] = 'вільний'

    return JsonResponse(response)