from django.db import models

# Create your models here.
class Customer(models.Model):
    nama = models.CharField(max_length=200, blank= True, null = True)
    no_hp = models.CharField(max_length=200, blank= True, null = True)
    email = models.CharField(max_length=200, blank= True, null = True)
    date_created = models.DateTimeField(auto_now_add = True, null = True)

    def __str__(self):
        return self.nama

class Tag(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True)
    def __str__(self):
        return self.name

class Product(models.Model):
    CATEGORY=(
        ('Indoor', 'Indoor'),
        ('Out Door', 'Out Door'),
    )
    name = models.CharField(max_length=200, blank=True, null=True)
    price = models.IntegerField(blank=True, null=True)
    category = models.CharField(max_length=200, blank=True, null=True, choices=CATEGORY)
    description = models.CharField(max_length=200, blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add = True, null = True)
    tag = models.ManyToManyField(Tag)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = "Product"
    # yang atas ini (class Meta)digunakan ketika ingin di admin nya tidak ada 's'

class Order(models.Model):
    STATUS=(
        ('Pending', 'Pending'),
        ('Out for delifery', 'Out for delifery'),
        ('Delifered', 'Delifered'),
    )
    customer  = models.ForeignKey(Customer, null=True, on_delete=models.SET_NULL)
    product  = models.ForeignKey(Product, null=True, on_delete=models.SET_NULL)
    date_created = models.DateTimeField(auto_now_add = True, null = True)
    status = models.CharField(max_length=200, null=True, choices=STATUS)

    def __str__(self):
        return '%s,%s' % (self.status, self.customer)