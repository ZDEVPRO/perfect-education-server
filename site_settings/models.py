from django.db import models
from django.utils.safestring import mark_safe


class HomeScreen(models.Model):
    subtitle = models.CharField(max_length=600)
    title = models.CharField(max_length=600)
    image = models.ImageField(upload_to='images/site_settings/')
    description = models.TextField()

    button1_name = models.CharField(max_length=300)
    button1_link = models.CharField(max_length=1000)

    button2_name = models.CharField(max_length=300)
    button2_link = models.CharField(max_length=1000)

    def __str__(self):
        return self.title

    def image_tag(self):
        return mark_safe('<img src="{}" height="50">'.format(self.image.url))

    class Meta:
        verbose_name = 'Home Screen'
        verbose_name_plural = 'Home Screen'

    # BIZ BILAN MUKAMMALIK SARI ERISHING!
    # PERFECT EDUCATION
    # O'quv Markazimiz o‘z faoliyatini yo‘lga qo‘ygan ondayoq oldiga ulkan maqsad qo‘ygan:
    # Yuqori muvaffaqiyat cho‘qqilarini egallashni istagan yoshlar uchun eng zarur bilimlarni yuqori sifatda professional tarzda yetkazish.

    # BUTTON1 = KURSLARIMIZ
    # BUTTON2 = BIZ BILAN ALOQA


class About(models.Model):
    subtitle = models.CharField(max_length=600)
    title = models.CharField(max_length=600)
    image = models.ImageField(upload_to='images/site_settings/')
    description = models.TextField()

    button1_name = models.CharField(max_length=300)
    button1_link = models.CharField(max_length=1000)

    button2_name = models.CharField(max_length=300)
    button2_link = models.CharField(max_length=1000)

    def __str__(self):
        return self.title

    def image_tag(self):
        return mark_safe('<img src="{}" height="50">'.format(self.image.url))

    class Meta:
        verbose_name = 'Biz haqimizda'
        verbose_name_plural = 'Biz haqimizda'

    # BIZ BILAN MUKAMMALIK SARI ERISHING!
    # Biz haqimizda
    # PERFECT EDUCATION o‘quv markazi 2018-yildan o‘z faoliyatini boshlagan. Ushbu qisqa vaqt mobaynida 1000 nafardan
    # ziyod abituriyentlarni Oliy o‘quv yutlariga tayyorlagan. Bizning bitiruvchilarimiz O‘zbekistonning eng nufuzli Oliy o‘quv yurtlarining
    # talabalari bo‘lib kelmoqda. O‘quv markazi tashkil etilishidan maqsad abituriyentlarni qisqa muddatda (10 oyda) talabalik baxtiga muyassar etish.


class BotAndChatIdContact(models.Model):
    title = models.CharField(max_length=600, default='Bot Token And Chat ID')
    bot_token = models.CharField(max_length=1000)
    chat_id = models.CharField(max_length=1000)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Telegram Bot Data Contact'
        verbose_name_plural = 'Telegram Bot Data Contact'


class BotAndChatIdCourse(models.Model):
    title = models.CharField(max_length=600, default='Bot Token And Chat ID')
    bot_token = models.CharField(max_length=1000)
    chat_id = models.CharField(max_length=1000)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Telegram Bot Data Course'
        verbose_name_plural = 'Telegram Bot Data Course'


class ContactData(models.Model):
    address = models.TextField(max_length=600)
    email = models.CharField(max_length=600)
    phone = models.CharField(max_length=600)

    def __str__(self):
        return self.address

    class Meta:
        verbose_name = 'Aloqa Malumotlari'
        verbose_name_plural = 'Aloqa Malumotlari'
