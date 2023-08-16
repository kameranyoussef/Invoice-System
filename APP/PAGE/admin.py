from django.contrib import admin
from .models import Company, Customer, Product, Invoice

    

admin.site.site_header = "Admin Dashboard"


class CompanyAdmin(admin.ModelAdmin):
    list_display = ("name", "address", "plz", "ort", "land", "tel", "email", "contact")


admin.site.register(Company, CompanyAdmin)


class CustomerAdmin(admin.ModelAdmin):
    list_display = ("name", "address", "plz", "ort", "land", "tel", "email")


admin.site.register(Customer, CustomerAdmin)


class ProductInline(admin.TabularInline):
    model = Product
    extra = 0


class InvoiceAdmin(admin.ModelAdmin):
    inlines = [ProductInline]


admin.site.register(Invoice, InvoiceAdmin)


class ProductAdmin(admin.ModelAdmin):
    list_display = ("invoice", "product", "unit", "price", "count", "vat")


admin.site.register(Product, ProductAdmin)
