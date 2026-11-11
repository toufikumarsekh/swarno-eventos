from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.shortcuts import render, redirect, get_object_or_404

from .forms import CompanyRegistrationForm
from .models import Company, Membership


@login_required
def company_list(request):
    memberships = Membership.objects.filter(
        user=request.user,
        is_active=True,
        company__is_active=True,
    ).select_related("company")

    return render(request, "companies/list.html", {
        "memberships": memberships,
    })


@login_required
def register_company(request):
    if request.method == "POST":
        form = CompanyRegistrationForm(request.POST)
        if form.is_valid():
            with transaction.atomic():
                company = form.save(commit=False)
                company.created_by = request.user
                company.save()

                Membership.objects.create(
                    company=company,
                    user=request.user,
                    role=Membership.Role.OWNER,
                )

            return redirect("companies:dashboard", slug=company.slug)
    else:
        form = CompanyRegistrationForm()

    return render(request, "companies/register.html", {"form": form})


@login_required
def registration_success(request):
    return render(request, "companies/success.html")


@login_required
def company_dashboard(request, slug):
    membership = get_object_or_404(
        Membership.objects.select_related("company", "user"),
        company__slug=slug,
        company__is_active=True,
        user=request.user,
        is_active=True,
    )

    company = membership.company
    memberships = Membership.objects.filter(
        company=company,
        is_active=True,
    ).select_related("user")

    user_companies = Membership.objects.filter(
        user=request.user,
        is_active=True,
        company__is_active=True,
    ).select_related("company")

    return render(request, "companies/dashboard.html", {
        "company": company,
        "membership": membership,
        "memberships": memberships,
        "member_count": memberships.count(),
        "user_companies": user_companies,
    })
