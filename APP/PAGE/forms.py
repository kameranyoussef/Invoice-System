from django.forms.models import inlineformset_factory
from django.forms import ModelForm, TextInput, NumberInput, EmailInput
from .models import Company, Customer, Invoice, Product


class CompanyForm(ModelForm):
    def __init__(self, *args, **kwargs) -> None:
        super(CompanyForm, self).__init__(*args, **kwargs)
        self.fields["name"].label = ""
        self.fields["address"].label = ""
        self.fields["plz"].label = ""
        self.fields["ort"].label = ""
        self.fields["land"].label = ""
        self.fields["tel"].label = ""
        self.fields["email"].label = ""
        self.fields["contact"].label = ""

    class Meta:
        model: type[Company] = Company
        fields: str = "__all__"
        widgets: dict[str, any] = {
            "name": TextInput(attrs={"placeholder": "Company name"}),
            "address": TextInput(attrs={"placeholder": "Address: eg. Road St.10"}),
            "plz": NumberInput(attrs={"placeholder": "Plz: eg. 1121"}),
            "ort": TextInput(attrs={"placeholder": "Ort: eg. Berlin"}),
            "land": TextInput(attrs={"placeholder": "Land: eg. Deutschland"}),
            "tel": NumberInput(attrs={"placeholder": "Tel: eg. 4922233344455"}),
            "email": EmailInput(attrs={"placeholder": "Email: eg. email@email.com"}),
            "contact": TextInput(attrs={"placeholder": "Contact name: eg. John Smith"}),
        }


class CustomerForm(ModelForm):
    def __init__(self, *args, **kwargs) -> None:
        super(CustomerForm, self).__init__(*args, **kwargs)
        self.fields["name"].label = ""
        self.fields["address"].label = ""
        self.fields["plz"].label = ""
        self.fields["ort"].label = ""
        self.fields["land"].label = ""
        self.fields["tel"].label = ""
        self.fields["email"].label = ""

    class Meta:
        model: type[Company] = Customer
        fields: str = "__all__"
        widgets: dict[str, any] = {
            "name": TextInput(attrs={"placeholder": "Customer name"}),
            "address": TextInput(attrs={"placeholder": "Address: eg. Road St.10"}),
            "plz": NumberInput(attrs={"placeholder": "Plz: eg. 1121"}),
            "ort": TextInput(attrs={"placeholder": "Ort: eg. Berlin"}),
            "land": TextInput(attrs={"placeholder": "Land: eg. Deutschland"}),
            "tel": NumberInput(attrs={"placeholder": "Tel: eg. 4922233344455"}),
            "email": EmailInput(attrs={"placeholder": "Email: eg. email@email.com"}),
        }


class InvoiceForm(ModelForm):
    def __init__(self, *args, **kwargs) -> None:
        super(InvoiceForm, self).__init__(*args, **kwargs)
        self.fields["customer"].label = ""
        self.fields["company"].label = ""

    class Meta:
        model: type[Invoice] = Invoice
        fields: str = "__all__"


class ProductForm(ModelForm):
    def __init__(self, *args, **kwargs) -> None:
        super(ProductForm, self).__init__(*args, **kwargs)
        self.fields["product"].label = ""
        self.fields["unit"].label = ""
        self.fields["price"].label = ""
        self.fields["count"].label = ""
        self.fields["vat"].label = ""

    class Meta:
        model: type[Product] = Product
        fields: str = "__all__"
        widgets: dict[str, any] = {
            "product": TextInput(attrs={"placeholder": "Product Name"}),
            "unit": TextInput(attrs={"placeholder": "Unit Type"}),
            "price": NumberInput(attrs={"placeholder": "Price: eg 1.53"}),
            "count": NumberInput(attrs={"placeholder": "Count eg 55"}),
            "vat": NumberInput(attrs={"placeholder": "VAT: eg 7.5"}),
        }


CProInlines: type[inlineformset_factory] = inlineformset_factory(
    Invoice,
    Product,
    form=ProductForm,
    extra=0,
    can_delete=False,
)
UProInlines: type[inlineformset_factory] = inlineformset_factory(
    Invoice,
    Product,
    form=ProductForm,
    extra=0,
    can_delete=False,
)
