from django.contrib import admin
from site_settings.models import HomeScreen, About, BotAndChatIdContact, BotAndChatIdCourse, ContactData


class HomeScreenAdmin(admin.ModelAdmin):
    list_display = ['title', 'image_tag']


class AboutAdmin(admin.ModelAdmin):
    list_display = ['title', 'image_tag']


admin.site.register(ContactData)
admin.site.register(HomeScreen, HomeScreenAdmin)
admin.site.register(About, AboutAdmin)
admin.site.register(BotAndChatIdContact)
admin.site.register(BotAndChatIdCourse)
