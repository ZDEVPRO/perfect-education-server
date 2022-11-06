from django.shortcuts import render, redirect
from home.models import Contact, Teacher, Course, TopCourse, Result, EnrollCourse
from site_settings.models import BotAndChatIdContact, BotAndChatIdCourse
from django.contrib import messages
import requests
from django.core.paginator import Paginator


def index(request):
    coursess = TopCourse.objects.all().order_by('-id')[:3]

    context = {
        'coursess': coursess
    }
    return render(request, 'pages/index.html', context)


def about(request):
    return render(request, 'pages/about.html')


def courses(request):
    coursess = Course.objects.all().order_by('-id')

    p = Paginator(coursess, 9)
    page_number = request.GET.get('page')
    page_obj = p.get_page(page_number)

    context = {
        'courses': coursess,
        'page_obj': page_obj
    }
    return render(request, 'pages/courses.html', context)


def course_detail(request, id):
    course = Course.objects.get(id=id)
    other_courses = TopCourse.objects.all().order_by('?')[:3]

    context = {
        'course': course,
        'other': other_courses
    }
    return render(request, 'pages/course_detail.html', context)


def results(request):
    result_all = Result.objects.all().order_by('-id')

    context = {
        'results': result_all
    }
    return render(request, 'pages/results.html', context)


def get_client_ip(request):
    x = request.META.get('HTTP_X_FORWARDED_FOR')
    if x:
        ip = x.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


def contact(request):
    if request.method == 'POST':
        bot_data = BotAndChatIdContact.objects.last()

        data = Contact()
        data.fullname = request.POST.get('fullname')
        data.phone = request.POST.get('phone')
        data.message = request.POST.get('message')
        data.ip = get_client_ip(request)
        data.save()
        messages.success(request,
                         'Xabaringiz muvoffaqiyatli yetkazildi. Siz bilan qisqa vaqt ichida aloqaga chiqamiz. Raxmat!')

        text = f'🇺🇿 YANGI XABAR KELDI! 🇺🇿 \n' \
               f'\n 👨  FISH: {data.fullname}' \
               f'\n 📲  Telefon raqam: {data.phone}' \
               f'\n 🌐  IP RAQAM: {data.ip}' \
               f'\n 🕒  VAQT: {data.create_time.strftime("%H:%M")}' \
               f'\n 📆  SANA: {data.create_date.strftime("%d-%m-%Y")}' \
               f'\n 📩  XABAR: {data.message}'
        text1 = "".join(text)

        bot_token = f'{bot_data.bot_token}'
        bot_chatID = f'{bot_data.chat_id}'

        url = f'https://api.telegram.org/bot{bot_token}/sendMessage?chat_id={bot_chatID}&parse_mode=Markdown&text={text1}'

        response = requests.get(url)

    return render(request, 'pages/contact.html')


def teachers(request):
    teachers_all = Teacher.objects.all().order_by('-id')
    result_all = Result.objects.all().order_by('-id')

    context = {
        'teachers': teachers_all,
        'results': result_all,
    }

    return render(request, 'pages/teachers.html', context)


def teacher_detail(request, id):
    teacher = Teacher.objects.get(id=id)
    teacher_courses = Course.objects.filter(teacher=teacher)

    context = {
        'teacher': teacher,
        'teacher_courses': teacher_courses
    }
    return render(request, 'pages/teacher_detail.html', context)


def enroll_course(request, id):
    if request.method == 'POST':
        bot_data = BotAndChatIdCourse.objects.last()
        data = EnrollCourse()
        data.course_type = request.POST.get('course_type')
        data.full_name = request.POST.get('full_name')
        data.phone = request.POST.get('phone')
        data.ip = get_client_ip(request)
        data.save()
        messages.success(request, 'Kursga muvoffaqiyatli yozildingiz. Qisqa vaqt ichida siz bilan bog`lanamiz. Raxmat!')

        text = f"🇺🇿 YANGI O'QUVCHI! 🇺🇿 \n" \
               f'\n 📗  KURS: {data.course_type}' \
               f'\n 👨  FISH: {data.full_name}' \
               f'\n 📲  Telefon raqam: {data.phone}' \
               f'\n 🌐  IP RAQAM: {data.ip}' \
               f'\n 🕒  VAQT: {data.create_time.strftime("%H:%M")}' \
               f'\n 📆  SANA: {data.create_date.strftime("%d-%m-%Y")}'
        text1 = "".join(text)

        bot_token = f'{bot_data.bot_token}'
        bot_chatID = f'{bot_data.chat_id}'

        url = f'https://api.telegram.org/bot{bot_token}/sendMessage?chat_id={bot_chatID}&parse_mode=Markdown&text={text1}'

        response = requests.get(url)
    try:
        course = Course.objects.get(id=id)
    except Exception as e:
        print(e)
        course1 = TopCourse.objects.get(id=id)
        course = course1.courses

    context = {
        'course': course
    }
    return render(request, 'pages/enroll_course.html', context)
