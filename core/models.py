from django.db        import models

from authtools.models import AbstractEmailUser

class User(AbstractEmailUser):
    full_name = models.CharField("full name", max_length=255, blank=True)
    preferred_name = models.CharField("preferred name", max_length=255, blank=True)

    def get_full_name(self):
        return self.full_name

    def get_short_name(self):
        return self.preferred_name

class Artist(models.Model):
    name = models.CharField("name", max_length=255, blank=False)
    themes = models.ManyToManyField('Theme',related_name='artists')

    def get_artist_name(self):
        return self.name

    def get_artist_themes(self):
        return self.themes


class Theme(models.Model):
    name = models.CharField("name", max_length=50, blank=False)

    def get_theme_name(self):
        return self.name

    def get_theme_artists(self):
        return self.artists
