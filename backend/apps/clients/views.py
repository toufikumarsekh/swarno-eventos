from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

from apps.companies.models import Company, Membership
from .models import Client
from .forms import ClientForm


def get_company(company_slug, user):
    membership = get_object_or_404(
        Membership.objects.select_related("company"),
        company__slug=company_slug,
        company__is_active=True,
        user=user,
        is_active=True,
    )
    return membership.company


@login_required
def client_list(request, company_slug):
    company = get_company(company_slug, request.user)
    clients = Client.objects.filter(company=company)

    query = request.GET.get("q", "").strip()
    if query:
        clients = clients.filter(name__icontains=query) | clients.filter(
            phone__icontains=query
        )

    return render(request, "clients/list.html", {
        "company": company,
        "clients": clients.distinct(),
        "query": query,
    })


@login_required
def client_create(request, company_slug):
    company = get_company(company_slug, request.user)
    form = ClientForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        client = form.save(commit=False)
        client.company = company
        client.created_by = request.user
        client.save()
        return redirect("companies:clients:detail", company_slug=company.slug, pk=client.pk)

    return render(request, "clients/form.html", {
        "company": company, "form": form, "page_title": "Add Client",
    })


@login_required
def client_detail(request, company_slug, pk):
    company = get_company(company_slug, request.user)
    client = get_object_or_404(Client, pk=pk, company=company)
    return render(request, "clients/detail.html", {
        "company": company, "client": client,
    })


@login_required
def client_edit(request, company_slug, pk):
    company = get_company(company_slug, request.user)
    client = get_object_or_404(Client, pk=pk, company=company)
    form = ClientForm(request.POST or None, instance=client)

    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("companies:clients:detail", company_slug=company.slug, pk=client.pk)

    return render(request, "clients/form.html", {
        "company": company, "form": form, "page_title": "Edit Client",
    })
