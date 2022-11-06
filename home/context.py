from datetime import date
from home.models import Logo, Teacher
from site_settings.models import HomeScreen, About, ContactData


def site_logo(request):
    logo_site = Logo.objects.last()
    context = {
        'logo_site': logo_site
    }
    return context


def teacher_view(request):
    my_teacher = Teacher.objects.all()

    context = {
        'my_teacher': my_teacher
    }
    return context


def current_date(request):
    now = date.today()
    now_year = now.strftime("%Y")
    context = {
        'now_year': now_year
    }
    return context


def home_screen_view(request):
    home_screen = HomeScreen.objects.last()

    context = {
        'home_screen': home_screen
    }
    return context


def about_view(request):
    about = About.objects.last()

    context = {
        'about': about
    }
    return context


def contact_data_view(request):
    contact_data = ContactData.objects.last()

    context = {
        'contact_data': contact_data
    }
    return context
