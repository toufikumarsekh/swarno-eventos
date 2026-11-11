from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render

from apps.companies.models import Company, Membership
from .models import Quotation
from .forms import QuotationForm, QuotationItemFormSet


def get_company_or_404(request, company_slug):
    company = get_object_or_404(Company, slug=company_slug, is_active=True)
    get_object_or_404(
        Membership, company=company, user=request.user, is_active=True
    )
    return company


@login_required
def quotation_list(request, company_slug):
    company = get_company_or_404(request, company_slug)
    quotations = Quotation.objects.filter(company=company).select_related("client", "event")

    query = request.GET.get("q", "").strip()
    status = request.GET.get("status", "").strip()

    if query:
        quotations = quotations.filter(
            Q(number__icontains=query)
            | Q(title__icontains=query)
            | Q(client__name__icontains=query)
        )
    if status:
        quotations = quotations.filter(status=status)

    return render(request, "quotations/list.html", {
        "company": company,
        "quotations": quotations,
        "query": query,
        "selected_status": status,
        "statuses": Quotation.Status.choices,
    })


@login_required
def quotation_create(request, company_slug):
    company = get_company_or_404(request, company_slug)

    if request.method == "POST":
        form = QuotationForm(request.POST, company=company)
        quotation = Quotation(company=company, created_by=request.user)
        formset = QuotationItemFormSet(request.POST, instance=quotation)

        if form.is_valid() and formset.is_valid():
            with transaction.atomic():
                quotation = form.save(commit=False)
                quotation.company = company
                quotation.created_by = request.user
                quotation.save()
                formset.instance = quotation
                formset.save()
            messages.success(request, "Quotation created successfully.")
            return redirect(
                "companies:quotations:detail",
                company_slug=company.slug,
                pk=quotation.pk,
            )
    else:
        form = QuotationForm(company=company)
        formset = QuotationItemFormSet(instance=Quotation(company=company))

    return render(request, "quotations/form.html", {
        "company": company,
        "form": form,
        "formset": formset,
        "page_title": "Create Quotation",
    })


@login_required
def quotation_detail(request, company_slug, pk):
    company = get_company_or_404(request, company_slug)
    quotation = get_object_or_404(
        Quotation.objects.select_related("client", "event").prefetch_related("items"),
        company=company,
        pk=pk,
    )
    return render(request, "quotations/detail.html", {
        "company": company,
        "quotation": quotation,
    })


@login_required
def quotation_edit(request, company_slug, pk):
    company = get_company_or_404(request, company_slug)
    quotation = get_object_or_404(
        Quotation, company=company, pk=pk
    )

    if quotation.status != Quotation.Status.DRAFT:
        messages.error(
            request,
            "Only draft quotations can be edited. Create a revision for an issued quotation.",
        )
        return redirect(
            "companies:quotations:detail",
            company_slug=company.slug,
            pk=quotation.pk,
        )

    if request.method == "POST":
        form = QuotationForm(request.POST, instance=quotation, company=company)
        formset = QuotationItemFormSet(request.POST, instance=quotation)
        if form.is_valid() and formset.is_valid():
            with transaction.atomic():
                form.save()
                formset.save()
            messages.success(request, "Quotation updated successfully.")
            return redirect(
                "companies:quotations:detail",
                company_slug=company.slug,
                pk=quotation.pk,
            )
    else:
        form = QuotationForm(instance=quotation, company=company)
        formset = QuotationItemFormSet(instance=quotation)

    return render(request, "quotations/form.html", {
        "company": company,
        "form": form,
        "formset": formset,
        "page_title": "Edit Quotation",
        "quotation": quotation,
    })
