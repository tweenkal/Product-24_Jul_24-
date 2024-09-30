from django.db import models
from django.utils.safestring import mark_safe

# Create your models here.


rlist=[
    ('1','1'),
    ('2','2'),
    ('3','3'),
    ('4','4'),
    ('5','5'),
]

class category(models.Model):
    cat_name = models.CharField(max_length=30)
    cat_desc = models.TextField()

    def __str__(self):
        return self.cat_name

class seller_table(models.Model):
    s_name = models.CharField(max_length=30)
    s_dp = models.ImageField(upload_to='photos')
    s_proof = models.ImageField(upload_to='photos')
    s_email = models.EmailField()
    s_phone = models.BigIntegerField()
    s_dob = models.DateField()



    def admin_photo(self):
        return mark_safe('<img src="{}" width="100"/>'.format(self.s_dp.url))

    admin_photo.allow_tags = True

    def proof_photo(self):
        return mark_safe('<img src="{}" width="100"/>'.format(self.s_proof.url))

    proof_photo.allow_tags = True

    def __str__(self):
        return self.s_name

class brand_table(models.Model):
    b_name = models.CharField(max_length=30)
    b_logo = models.ImageField(upload_to='photos')
    b_desc = models.TextField()

    def b_photo(self):
        return mark_safe('<img src="{}" width="100"/>'.format(self.b_logo.url))

    b_photo.allow_tags = True

    def __str__(self):
        return self.b_name

class product_table(models.Model):
    p_name = models.CharField(max_length=30)
    p_brand = models.ForeignKey(brand_table,on_delete=models.CASCADE)
    p_seller = models.ForeignKey(seller_table,on_delete=models.CASCADE)
    p_category = models.ForeignKey(category,on_delete=models.CASCADE)
    p_price = models.FloatField()
    p_Quantity = models.FloatField()
    p_image = models.ImageField(upload_to='photos')

    def product_photo(self):
        return mark_safe('<img src="{}" width="100"/>'.format(self.p_image.url))

    product_photo.allow_tags = True

    def __str__(self):
        return  self.p_name

class order_table(models.Model):
    s_id = models.ForeignKey(seller_table,on_delete=models.CASCADE)
    p_id = models.ForeignKey(product_table,on_delete=models.CASCADE)
    purchase_Qty = models.FloatField()
    Order_datetime = models.DateTimeField()

class feedback(models.Model):
    s_id = models.ForeignKey(seller_table,on_delete=models.CASCADE)
    rating = models.CharField(max_length=30,choices=rlist)
    review = models.TextField()
