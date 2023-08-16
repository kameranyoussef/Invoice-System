from django.shortcuts import render, HttpResponse
from django.views.generic import CreateView, UpdateView, ListView
from .models import Company, Customer, Invoice, Product
from .forms import CompanyForm, CustomerForm, InvoiceForm, CProInlines, UProInlines


class CompanyListView(ListView):
    paginate_by = 10
    model: type[Company] = Company
    ordering: list[str] = ["-created_at"]
    template_name = "inc/lcom.html"


class CompanyCreateView(CreateView):
    model: type[Company] = Company
    form_class: type[CompanyForm] = CompanyForm
    template_name = "inc/create_update.html"
    success_url = "/list_company"


class CompanyUpdateView(UpdateView):
    model: type[Company] = Company
    form_class: type[CompanyForm] = CompanyForm
    template_name = "inc/create_update.html"
    success_url = "/list_company"


# ------------------------------------------------------------------------------------------------------------
class CustomerListView(ListView):
    paginate_by = 10
    model: type[Customer] = Customer
    ordering: list[str] = ["-created_at"]
    template_name = "inc/lcus.html"


class CustomerCreateView(CreateView):
    model: type[Customer] = Customer
    form_class: type[CustomerForm] = CustomerForm
    template_name = "inc/create_update.html"
    success_url = "/list_customer"


class CustomerUpdateView(UpdateView):
    model: type[Customer] = Customer
    form_class: type[CustomerForm] = CustomerForm
    template_name = "inc/create_update.html"
    success_url = "/list_customer"


# ------------------------------------------------------------------------------------------------------------
class InvoiceListView(ListView):
    model = Invoice
    paginate_by = 10
    ordering = ["-created_at"]
    template_name = "inc/linv.html"


def InvoiceCreateView(request) -> HttpResponse:
    if request.method == "POST":
        form: InvoiceForm = InvoiceForm(request.POST)
        if form.is_valid():
            p: any = form.save()
            formset = CProInlines(request.POST, instance=p)
            if formset.is_valid():
                formset.save()
                return HttpResponse("<h1>Invoice Created</h1>")
    else:
        objInvoice: Invoice = Invoice()
        form = InvoiceForm()
        formset = CProInlines(instance=objInvoice)

    context: dict[str, any] = {
        "form": form,
        "formset": formset,
    }
    return render(request, "inc/create_inv.html", context=context)


def InvoiceUpdateView(request, pk) -> HttpResponse:
    objInvoice: Invoice = Invoice.objects.get(id=pk)
    if request.method == "POST":
        formset = UProInlines(request.POST, instance=objInvoice)
        if formset.is_valid():
            formset.save()
            return HttpResponse("<h1>Invoice Update</h1>")
    else:
        formset = UProInlines(instance=objInvoice)

    context: dict[str, any] = {
        "formset": formset,
    }
    return render(request, "inc/create_update.html", context=context)


# ------------------------------------------------------------------------------------------------------------
def SerachView(request) -> HttpResponse:
    searchKey: any = request.GET.get("search")
    if searchKey != "":
        CompanyObj = Company.objects.filter(name__contains=searchKey)
        CustomerObj = Customer.objects.filter(name__contains=searchKey)

        context = {
            "searchKey": searchKey,
            "CompanyObj": CompanyObj,
            "CustomerObj": CustomerObj,
        }
        return render(request, "inc/search.html", context=context)
    return render(request, "inc/home.html")


def InvoiceExportView(request, pk) -> HttpResponse:
    # get objs
    objInvoice: Invoice = Invoice.objects.get(id=pk)
    ObjProducts: Product = Product.objects.filter(invoice=pk)

    # Calculate
    GesSum, UstSum, EndSum = 0, 0, 0
    for pro in ObjProducts:
        GesSum = GesSum + (pro.price * pro.count)
        UstSum = UstSum + ((pro.price * pro.count) * pro.vat / 100)
    EndSum: any | int = GesSum + UstSum

    # context
    context: dict[str, any] = {
        "objInvoice": objInvoice,
        "ObjProducts": ObjProducts,
        "GesSum": GesSum,
        "UstSum": UstSum,
        "EndSum": EndSum,
    }
    return render(request, "inc/export.html", context=context)
