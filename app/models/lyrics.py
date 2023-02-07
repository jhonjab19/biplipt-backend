from django.db import models

from app.models.admins import Admin
from app.models.albums import Album
from app.models.artists import Artist
from app.models.genres import Genre
from app.models.system import VisibilityOptions
from app.models.users import User


class Lyric(models.Model):
   'Modelo de las letras'
   id = models.BigAutoField(primary_key=True)
   dns = models.CharField(max_length=255, db_index=True, unique=True)
   visibility = models.CharField(max_length=10, choices=VisibilityOptions.choices, default=VisibilityOptions.Public)
   verify = models.BooleanField(default=False)
   tags = models.CharField(max_length=255, db_index=True)
   name = models.CharField(max_length=80)
   nativeName = models.CharField(max_length=80)
   track = models.PositiveSmallIntegerField(null=True, default=None)
   duraction = models.PositiveIntegerField(null=True, default=None)
   country = models.CharField(max_length=2)
   language = models.CharField(max_length=20)
   year = models.PositiveSmallIntegerField(null=True, default=None)
   composers = models.CharField(max_length=255, null=True, default=None)
   writers = models.CharField(max_length=255, null=True, default=None)
   copyright = models.CharField(max_length=400, null=True, default=None)
   lyric = models.TextField()
   nativeLyric = models.TextField(null=True, default=None)
   appleMusicID = models.CharField(max_length=255, null=True, default=None)
   deezerID = models.CharField(max_length=255, null=True, default=None)
   spotifyID = models.CharField(max_length=255, null=True, default=None)
   youTubeID = models.CharField(max_length=255, null=True, default=None)
   youTubeMusicID = models.CharField(max_length=255, null=True, default=None)
   views = models.BigIntegerField(default=0)
   addedAt = models.DateTimeField(auto_now_add=True)
   updatedAt = models.DateTimeField(auto_now=True)
   artistId = models.ForeignKey(Artist, on_delete=models.CASCADE, db_column="artistId")
   albumId = models.ForeignKey(Album, on_delete=models.CASCADE, db_column="albumId")
   genresGroup = models.ManyToManyField(Genre, related_name="genresGroup")
   approvedBy = models.ForeignKey(Admin, on_delete=models.SET_NULL, null=True, db_column="approvedBy")
   sentBy = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, default=None, db_column="sentBy")
   
   class Meta:
      db_table = "app_lyrics"
      verbose_name = "lyric"
      verbose_name_plural = "lyrics"
   
   def __str__(self):
      return self.name


class LyricFT(models.Model):
   'Modelo de Feacturing de las letras y de las versiones'
   lyricId = models.ForeignKey(Lyric, on_delete=models.CASCADE, db_column="lyricId")
   name = models.CharField(max_length=80)
   nativeName = models.CharField(max_length=80)
   dns = models.CharField(max_length=255)
   
   class Meta:
      db_table = "app_lyric_ft"
      verbose_name = "lyric featuring"
      verbose_name_plural = "lyrics featuring"
   
   def __str__(self):
      return self.name


class LyricModifications(models.Model):
   'Modelos de registro de modificaciones de las letras'
   lyricId = models.ForeignKey(Lyric, on_delete=models.CASCADE, db_column="lyricId")
   modifiedBy = models.ForeignKey(Admin, on_delete=models.SET_NULL, null=True, db_column="modifiedBy")
   sentBy = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, default=None, db_column="sentBy")
   times = models.PositiveSmallIntegerField(default=1)
   addedAt = models.DateTimeField(auto_now_add=True)
   updatedAt = models.DateTimeField(auto_now=True)

   class Meta:
      db_table = 'app_lyric_modifications'
      verbose_name = "lyric modifications"
      verbose_name_plural = "lyrics modifications"
   
   def __str__(self):
      return f"lyric modified: {self.lyricId}"

   
class LyricLikes(models.Model):
   'Likes de las letras'
   userId = models.ForeignKey(User, on_delete=models.CASCADE, db_column="userId")
   lyricId = models.ForeignKey(Lyric, on_delete=models.CASCADE, db_column="lyricId")
   at = models.DateTimeField(auto_now_add=True)
   
   class Meta:
      db_table = "app_lyric_likes"
      verbose_name = "lyric likes"
      verbose_name_plural = "lyric likes"
   
   def __str__(self):
      return f"like to: {self.lyricId}"
