from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

from apps.companies.models import Membership
from apps.clients.models import Client
from .models import Enquiry, FollowUp
from .forms import EnquiryForm, FollowUpForm


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
def enquiry_list(request, company_slug):
    company = get_company(company_slug, request.user)
    enquiries = Enquiry.objects.filter(company=company).select_related("client")

    status = request.GET.get("status", "")
    if status:
        enquiries = enquiries.filter(status=status)

    return render(request, "enquiries/list.html", {
        "company": company,
        "enquiries": enquiries,
        "statuses": Enquiry.Status.choices,
        "selected_status": status,
    })


@login_required
def enquiry_create(request, company_slug):
    company = get_company(company_slug, request.user)
    form = EnquiryForm(request.POST or None, company=company)

    if request.method == "POST" and form.is_valid():
        enquiry = form.save(commit=False)
        enquiry.company = company
        enquiry.created_by = request.user
        enquiry.save()
        return redirect(
            "companies:enquiries:detail",
            company_slug=company.slug,
            pk=enquiry.pk,
        )

    return render(request, "enquiries/form.html", {
        "company": company, "form": form, "page_title": "New Enquiry",
    })


@login_required
def enquiry_detail(request, company_slug, pk):
    company = get_company(company_slug, request.user)
    enquiry = get_object_or_404(
        Enquiry.objects.select_related("client"),
        pk=pk,
        company=company,
    )
    followups = FollowUp.objects.filter(
        enquiry=enquiry,
        company=company,
    )
    return render(request, "enquiries/detail.html", {
        "company": company,
        "enquiry": enquiry,
        "followups": followups,
    })


@login_required
def enquiry_edit(request, company_slug, pk):
    company = get_company(company_slug, request.user)
    enquiry = get_object_or_404(Enquiry, pk=pk, company=company)
    form = EnquiryForm(
        request.POST or None,
        instance=enquiry,
        company=company,
    )

    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect(
            "companies:enquiries:detail",
            company_slug=company.slug,
            pk=enquiry.pk,
        )

    return render(request, "enquiries/form.html", {
        "company": company, "form": form, "page_title": "Edit Enquiry",
    })


@login_required
def followup_create(request, company_slug, pk):
    company = get_company(company_slug, request.user)
    enquiry = get_object_or_404(Enquiry, pk=pk, company=company)
    form = FollowUpForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        followup = form.save(commit=False)
        followup.company = company
        followup.enquiry = enquiry
        followup.created_by = request.user
        followup.save()
        return redirect(
            "companies:enquiries:detail",
            company_slug=company.slug,
            pk=enquiry.pk,
        )

    return render(request, "enquiries/followup_form.html", {
        "company": company,
        "enquiry": enquiry,
        "form": form,
    })
