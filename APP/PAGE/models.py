from django.db import models


class Timestamped(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract: bool = True


class Company(Timestamped):
    name = models.CharField(max_length=100)
    contact = models.CharField(max_length=100)
    tel = models.DecimalField(max_digits=16, decimal_places=0)
    email = models.EmailField(max_length=100)
    address = models.CharField(max_length=100)
    plz = models.IntegerField()
    ort = models.CharField(max_length=100)
    land = models.CharField(max_length=100)

    class Meta:
        default_related_name: str = "Company"
        verbose_name: str = "Company"
        verbose_name_plural: str = "Companies"

    def __str__(self) -> str:
        return f"100-{self.id}, Company: {self.name}"


class Customer(Timestamped):
    name = models.CharField(max_length=100)
    tel = models.DecimalField(max_digits=16, decimal_places=0)
    email = models.EmailField(max_length=100)
    address = models.CharField(max_length=100)
    plz = models.IntegerField()
    ort = models.CharField(max_length=100)
    land = models.CharField(max_length=100)

    class Meta:
        default_related_name: str = "Customer"
        verbose_name: str = "Customer"
        verbose_name_plural: str = "Customers"

    def __str__(self) -> str:
        return f"100-{self.id}, Customer: {self.name}"


class Invoice(Timestamped):
    customer = models.ForeignKey(
        Customer, on_delete=models.SET_NULL, null=True, blank=False
    )
    company = models.ForeignKey(
        Company, on_delete=models.SET_NULL, null=True, blank=False
    )

    class Meta:
        default_related_name: str = "Invoice"
        verbose_name: str = "Invoice"
        verbose_name_plural: str = "Invoices"

    def __str__(self) -> str:
        return f"100-{self.id}"


class Product(Timestamped):
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE)
    product = models.CharField(max_length=100)
    unit = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    count = models.IntegerField()
    vat = models.DecimalField(max_digits=5, decimal_places=2)

    class Meta:
        default_related_name: str = "Product"
        verbose_name: str = "Product"
        verbose_name_plural: str = "Products"

    def __str__(self) -> str:
        return f"100-{self.id}, Product:{self.product}, Invoice:{self.invoice}"

    @property
    def cal_Ges(self) -> float:
        return self.count * self.price

    @property
    def cal_Ust(self) -> float:
        x = self.count * self.price
        return x * self.vat / 100
