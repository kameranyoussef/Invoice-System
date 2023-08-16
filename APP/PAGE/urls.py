from django.contrib.auth import views as auth_views
from django.views.generic.base import TemplateView
from django.urls import path
from . import views


urlpatterns = [
    path("", TemplateView.as_view(template_name="base.html"), name="home"),
    path(
        "login/",
        auth_views.LoginView.as_view(template_name="auth/login.html", success_url="/"),
        name="login",
    ),
    path(
        "logout/",
        auth_views.LogoutView.as_view(template_name="auth/logout.html"),
        name="logout",
    ),
]

htmxpatterns = [
    path("search/", views.SerachView, name="search"),
    path("export/<int:pk>", views.InvoiceExportView, name="export"),
    path("list_company/", views.CompanyListView.as_view(), name="list_company"),
    path("create_company/", views.CompanyCreateView.as_view(), name="create_company"),
    path(
        "update_company/<int:pk>",
        views.CompanyUpdateView.as_view(),
        name="update_company",
    ),
    path("list_customer/", views.CustomerListView.as_view(), name="list_customer"),
    path(
        "create_customer/", views.CustomerCreateView.as_view(), name="create_customer"
    ),
    path(
        "update_customer/<int:pk>",
        views.CustomerUpdateView.as_view(),
        name="update_customer",
    ),
    path("list_invoice/", views.InvoiceListView.as_view(), name="list_invoice"),
    path("create_invoice/", views.InvoiceCreateView, name="create_invoice"),
    path("update_invoice/<int:pk>", views.InvoiceUpdateView, name="update_invoice"),
]

urlpatterns += htmxpatterns
