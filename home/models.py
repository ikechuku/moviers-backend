from django.db import models
from django.contrib.auth.models import User

class Playlist(models.Model):
    title = models.CharField(max_length=100)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.self.title

    # def get_absolute_url(self):
    #     return reverse("Playlist_detail", kwargs={"pk": self.pk})

class Genre(models.Model):
    tile = models.CharField( max_length=50)
    def __str__(self):
        return self.title

 # def get_absolute_url(self):
    #     return reverse("Genre_detail", kwargs={"pk": self.pk})
    

class Movie (models.Model):
    tile = models.CharField( max_length=50)
    
    def __str__(self):
        return self.name

    # def get_absolute_url(self):
        # return reverse("Movie _detail", kwargs={"pk": self.pk})



class Favorite(models.Model):
    movie = models.ForeignKey("home.Movie", on_delete=models.CASCADE)
    
    def __str__(self):
        return self.movie

    # def get_absolute_url(self):
    #         return reverse("FavoriteF_detail", kwargs={"pk": self.pk})
