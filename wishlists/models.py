from django.db import models

# Create your models here.
class Wishlist(models.Model):
  list_name = models.CharField(max_length=200)
  pub_date = models.DateTimeField('date published')

class WishlistItem(models.Model):
  wish_list = models.ForeignKey(Wishlist)
  item_name = models.CharField(max_length=200)
  item_description=models.CharField(max_length=1024)
  item_price = models.DecimalField(max_digits=32, decimal_places=2)
  item_url = models.URLField(max_length=200)
  item_image = models.ImageField(upload_to=None)
