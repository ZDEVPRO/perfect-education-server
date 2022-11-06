from django.contrib import admin
from home.models import Contact, Logo, Teacher, Course, TopCourse, Result, EnrollCourse

admin.site.index_title = 'АДМИНИСТРАЦИЯ САЙТА'
admin.site.site_header = 'PERFECT EDUCATION - Панель управления'
admin.site.site_title = 'Панель управления'


class ContactAdmin(admin.ModelAdmin):
    list_display = ['fullname', 'phone', 'create_time', 'create_date', 'ip']
    readonly_fields = ['fullname', 'phone', 'ip', 'create_time', 'create_date', 'ip']


class LogoAdmin(admin.ModelAdmin):
    list_display = ['title', 'image_tag', 'favicon_tag']


class TeacherAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'category', 'phone', 'image_tag']


class CourseAdmin(admin.ModelAdmin):
    list_display = ['title', 'teacher', 'image_tag']


class ResultAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'image_tag']


class EnrollCourseAdmin(admin.ModelAdmin):
    list_display = ['course_type', 'full_name', 'phone', 'ip']
    readonly_fields = ['course_type', 'full_name', 'phone', 'create_time', 'create_date', 'ip']


admin.site.register(Logo, LogoAdmin)
admin.site.register(Teacher, TeacherAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(TopCourse)
admin.site.register(Result, ResultAdmin)
admin.site.register(EnrollCourse, EnrollCourseAdmin)
admin.site.register(Contact, ContactAdmin)
