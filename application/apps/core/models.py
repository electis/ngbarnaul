from pytils import translit
from django.db import models


def get_image_path(self, filename):
    return translit.translify(filename)


class Setting(models.Model):
    title = models.CharField(max_length=128, verbose_name="Title", blank=True, default='')
    keywords = models.CharField(max_length=255, verbose_name="keywords", blank=True, default='')
    description = models.CharField(max_length=255, verbose_name="description", blank=True, default='')
    logo = models.ImageField(upload_to=get_image_path, null=True, blank=True)
    logo2x = models.ImageField(upload_to=get_image_path, null=True, blank=True)


class Navbar(models.Model):
    title = models.CharField(max_length=128, blank=True, default='')
    url = models.CharField(max_length=32, blank=True, default='')
    position = models.SmallIntegerField(default=10, help_text="<0 is buttons")


class Banner(models.Model):
    logo = models.CharField(max_length=128, verbose_name="Logo IMG", blank=True, default='')
    logo2x = models.CharField(max_length=128, verbose_name="Logo2x IMG", blank=True, default='')
    text_big = models.CharField(max_length=255, verbose_name="Text big", blank=True, default='')
    text_small = models.CharField(max_length=255, verbose_name="Text small", blank=True, default='')
    position = models.SmallIntegerField(default=10)


class Counter(models.Model):
    text_big = models.CharField(max_length=255, verbose_name="Text big", blank=True, default='')
    text_small = models.CharField(max_length=255, verbose_name="Text small", blank=True, default='')
    button_title = models.CharField(max_length=128, blank=True, default='')
    button_url = models.CharField(max_length=32, blank=True, default='')
    background = models.CharField(max_length=255, verbose_name="Background", blank=True, default='')


class Card(models.Model):
    background = models.CharField(max_length=255, verbose_name="Background", blank=True, default='')
    text_top = models.CharField(max_length=255, blank=True, default='')
    text_middle = models.TextField(help_text="list", blank=True, default='[]')
    text_bottom = models.CharField(max_length=255, blank=True, default='')
    # button_title = models.CharField(max_length=128, blank=True, default='')
    button_url = models.CharField(max_length=32, blank=True, default='')
    position = models.SmallIntegerField(default=10)


class Review(models.Model):
    video1_url = models.CharField(max_length=64, blank=True, default='')
    video2_url = models.CharField(max_length=64, blank=True, default='')
    position = models.SmallIntegerField(default=10)


class Team(models.Model):
    text_big = models.CharField(max_length=255, blank=True, default='')
    text_small = models.TextField(blank=True, default='')
    image = models.CharField(max_length=128, blank=True, default='')
    image2x = models.CharField(max_length=128, blank=True, default='')
    services_title = models.CharField(max_length=128, blank=True, default='')


class Minister(models.Model):
    name = models.CharField(max_length=255, blank=True, default='')
    function = models.CharField(max_length=255, blank=True, default='')
    image = models.ImageField(upload_to=get_image_path, blank=True, null=True)
    image2x = models.ImageField(upload_to=get_image_path, blank=True, null=True)
    about = models.TextField(blank=True, default='')
    phone = models.CharField(max_length=32, blank=True, default='')
    short_name = models.CharField(max_length=64, blank=True, default='')
    social_page = models.CharField(max_length=64, blank=True, default='')
    social_vk = models.CharField(max_length=64, blank=True, default='')
    social_fb = models.CharField(max_length=64, blank=True, default='')
    social_ok = models.CharField(max_length=64, blank=True, default='')
    social_inst = models.CharField(max_length=64, blank=True, default='')
    social_youtube = models.CharField(max_length=64, blank=True, default='')
    position = models.SmallIntegerField(default=10)

    def __str__(self):
        return f'{self.position} - {self.name}'


class Contact(models.Model):
    title = models.CharField(max_length=128, blank=True, default='')
    text = models.CharField(max_length=255, blank=True, default='')
    address = models.CharField(max_length=128, blank=True, default='')
    phone = models.CharField(max_length=128, blank=True, default='')
