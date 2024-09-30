from django.contrib import admin
from .models import category,seller_table,brand_table,product_table,order_table,feedback

# Register your models here.

class showcategory(admin.ModelAdmin):
    list_display = ["cat_name","cat_desc"]

admin.site.register(category,showcategory)

class showseller_table(admin.ModelAdmin):
    list_display = ["s_name","s_dp","s_proof","s_email","s_phone","s_dob","s_dob","admin_photo","proof_photo"]

admin.site.register(seller_table,showseller_table)

class showbrand_table(admin.ModelAdmin):
    list_display = ["b_name","b_logo","b_desc","b_photo"]

admin.site.register(brand_table,showbrand_table)

class showproduct_table(admin.ModelAdmin):
    list_display = ["p_name","p_brand","p_seller","p_category","p_Quantity","product_photo","p_price"]

admin.site.register(product_table,showproduct_table)

class showorder_table(admin.ModelAdmin):
    list_display = ["s_id","p_id","purchase_Qty","Order_datetime"]

admin.site.register(order_table,showorder_table)

class showfeedback(admin.ModelAdmin):
    list_display = ["s_id","rating","review"]

admin.site.register(feedback,showfeedback)
