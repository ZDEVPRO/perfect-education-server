from django.db import models
from django.utils.safestring import mark_safe
from ckeditor.fields import RichTextField


class Logo(models.Model):
    title = models.CharField(default='PERFECT EDUCATION LOGO', max_length=300)
    image = models.ImageField(upload_to='images/logo/')
    favicon = models.ImageField(upload_to='images/favicon/')

    def __str__(self):
        return self.title

    def image_tag(self):
        return mark_safe('<img src="{}" height="50">'.format(self.image.url))

    def favicon_tag(self):
        return mark_safe('<img src="{}" height="50">'.format(self.favicon.url))

    class Meta:
        verbose_name = 'Site Logo'
        verbose_name_plural = 'Site Logo'


class Contact(models.Model):
    fullname = models.CharField('ISM FAMILIYA', max_length=600)
    phone = models.CharField('TELEFON', max_length=600)
    message = models.TextField('XABAR')
    ip = models.CharField('IP ADDRESS', max_length=400)
    create_time = models.TimeField(auto_now_add=True)
    create_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.fullname

    class Meta:
        verbose_name = 'Aloqa Bo`limi'
        verbose_name_plural = 'Aloqa Bo`limi'


class Teacher(models.Model):
    full_name = models.CharField(max_length=600)
    image = models.ImageField(upload_to='images/teacher/')
    category = models.CharField(max_length=600)
    phone = models.CharField(max_length=600)
    about_me = RichTextField()

    def __str__(self):
        return self.full_name

    def image_tag(self):
        return mark_safe('<img src="{}" height="50">'.format(self.image.url))

    class Meta:
        verbose_name = 'Ustozlar'
        verbose_name_plural = 'Ustozlar'


class Course(models.Model):
    title = models.CharField(max_length=600)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name='teacher')
    image = models.ImageField(upload_to='images/courses/')
    price = models.IntegerField(default=0)
    about = RichTextField()

    def __str__(self):
        return self.title

    def price_intcomma(self):
        return f"{self.price:,}"

    def image_tag(self):
        return mark_safe('<img src="{}" height="50">'.format(self.image.url))

    def teacher_name(self):
        return self.teacher.full_name

    class Meta:
        verbose_name = 'Kurslar'
        verbose_name_plural = 'Kurslar'


class TopCourse(models.Model):
    courses = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='mycourses')

    def __str__(self):
        return self.courses.title

    class Meta:
        verbose_name = 'Top Kurslar'
        verbose_name_plural = 'Top Kurslar'


class Result(models.Model):
    full_name = models.CharField(max_length=600)
    image = models.ImageField(upload_to='images/results/')
    university = models.CharField(max_length=600)

    def __str__(self):
        return self.full_name

    def image_tag(self):
        return mark_safe('<img src="{}" height="50">'.format(self.image.url))

    class Meta:
        verbose_name = 'Natijalar'
        verbose_name_plural = 'Natijalar'


class EnrollCourse(models.Model):
    course_type = models.CharField(max_length=600)
    full_name = models.CharField(max_length=600)
    phone = models.CharField(max_length=100)
    ip = models.CharField(max_length=200)
    create_time = models.TimeField(auto_now_add=True)
    create_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = 'Kurs Uchun Qabul'
        verbose_name_plural = 'Kurs Uchun Qabul'
