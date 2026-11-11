from decimal import Decimal

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.db.models import Sum
from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone
from django.views.decorators.http import require_POST

from apps.companies.models import Company
from apps.quotations.models import Quotation

from .forms import PaymentForm, ExpenseForm, VoidReasonForm
from .models import Payment, Expense


def get_company_or_404(user, company_slug):
    return get_object_or_404(
        Company,
        slug=company_slug,
        is_active=True,
        memberships__user=user,
        memberships__is_active=True,
    )


@login_required
def finance_dashboard(request, company_slug):
    company = get_company_or_404(request.user, company_slug)

    payments = Payment.objects.filter(
        company=company,
        status=Payment.Status.POSTED,
    )
    expenses = Expense.objects.filter(
        company=company,
        status=Expense.Status.POSTED,
    )

    total_income = payments.aggregate(total=Sum("amount"))["total"] or Decimal("0.00")
    total_expenses = expenses.aggregate(total=Sum("amount"))["total"] or Decimal("0.00")

    accepted_quotations = Quotation.objects.filter(
        company=company,
        status=Quotation.Status.ACCEPTED,
    ).prefetch_related("items")

    paid_by_quotation = {
        row["quotation_id"]: row["total"]
        for row in payments.filter(quotation__isnull=False)
        .values("quotation_id")
        .annotate(total=Sum("amount"))
    }

    outstanding = sum(
        (
            max(
                quotation.grand_total - paid_by_quotation.get(
                    quotation.pk, Decimal("0.00")
                ),
                Decimal("0.00"),
            )
            for quotation in accepted_quotations
        ),
        Decimal("0.00"),
    )

    context = {
        "company": company,
        "total_income": total_income,
        "total_expenses": total_expenses,
        "net_cash": total_income - total_expenses,
        "outstanding": outstanding,
        "recent_payments": payments.select_related("client")[:5],
        "recent_expenses": expenses.select_related("event")[:5],
    }
    return render(request, "finance/dashboard.html", context)


@login_required
def payment_list(request, company_slug):
    company = get_company_or_404(request.user, company_slug)
    payments = Payment.objects.filter(company=company).select_related(
        "client", "event", "quotation"
    )

    return render(request, "finance/payment_list.html", {
        "company": company,
        "payments": payments,
    })


@login_required
def payment_create(request, company_slug):
    company = get_company_or_404(request.user, company_slug)

    if request.method == "POST":
        form = PaymentForm(request.POST, company=company)
        if form.is_valid():
            payment = form.save(commit=False)
            payment.company = company
            payment.created_by = request.user
            payment.status = Payment.Status.POSTED
            payment.posted_at = timezone.now()
            payment.full_clean()
            payment.save()

            messages.success(request, "Payment recorded successfully.")
            return redirect(
                "companies:finance:payment_detail",
                company_slug=company.slug,
                pk=payment.pk,
            )
    else:
        form = PaymentForm(company=company)

    return render(request, "finance/payment_form.html", {
        "company": company,
        "form": form,
    })


@login_required
def payment_detail(request, company_slug, pk):
    company = get_company_or_404(request.user, company_slug)
    payment = get_object_or_404(
        Payment.objects.select_related("client", "event", "quotation", "created_by"),
        company=company,
        pk=pk,
    )

    return render(request, "finance/payment_detail.html", {
        "company": company,
        "payment": payment,
        "void_form": VoidReasonForm(),
    })


@login_required
@require_POST
def payment_void(request, company_slug, pk):
    company = get_company_or_404(request.user, company_slug)
    form = VoidReasonForm(request.POST)

    if not form.is_valid():
        messages.error(request, "Please provide a valid reason of at least 5 characters.")
        return redirect(
            "companies:finance:payment_detail",
            company_slug=company.slug,
            pk=pk,
        )

    with transaction.atomic():
        payment = get_object_or_404(
            Payment.objects.select_for_update(),
            company=company,
            pk=pk,
        )

        if payment.status != Payment.Status.POSTED:
            messages.warning(request, "Only posted payments can be voided.")
        else:
            payment.status = Payment.Status.VOID
            payment.void_reason = form.cleaned_data["reason"]
            payment.voided_at = timezone.now()
            payment.full_clean()
            payment.save(update_fields=[
                "status", "void_reason", "voided_at", "updated_at"
            ])
            messages.success(request, "Payment has been voided. Its record is preserved.")

    return redirect(
        "companies:finance:payment_detail",
        company_slug=company.slug,
        pk=pk,
    )


@login_required
def expense_list(request, company_slug):
    company = get_company_or_404(request.user, company_slug)
    expenses = Expense.objects.filter(company=company).select_related("event")

    return render(request, "finance/expense_list.html", {
        "company": company,
        "expenses": expenses,
    })


@login_required
def expense_create(request, company_slug):
    company = get_company_or_404(request.user, company_slug)

    if request.method == "POST":
        form = ExpenseForm(request.POST, company=company)
        if form.is_valid():
            expense = form.save(commit=False)
            expense.company = company
            expense.created_by = request.user
            expense.status = Expense.Status.POSTED
            expense.posted_at = timezone.now()
            expense.full_clean()
            expense.save()

            messages.success(request, "Expense recorded successfully.")
            return redirect(
                "companies:finance:expense_detail",
                company_slug=company.slug,
                pk=expense.pk,
            )
    else:
        form = ExpenseForm(company=company)

    return render(request, "finance/expense_form.html", {
        "company": company,
        "form": form,
    })


@login_required
def expense_detail(request, company_slug, pk):
    company = get_company_or_404(request.user, company_slug)
    expense = get_object_or_404(
        Expense.objects.select_related("event", "created_by"),
        company=company,
        pk=pk,
    )

    return render(request, "finance/expense_detail.html", {
        "company": company,
        "expense": expense,
        "void_form": VoidReasonForm(),
    })


@login_required
@require_POST
def expense_void(request, company_slug, pk):
    company = get_company_or_404(request.user, company_slug)
    form = VoidReasonForm(request.POST)

    if not form.is_valid():
        messages.error(request, "Please provide a valid reason of at least 5 characters.")
        return redirect(
            "companies:finance:expense_detail",
            company_slug=company.slug,
            pk=pk,
        )

    with transaction.atomic():
        expense = get_object_or_404(
            Expense.objects.select_for_update(),
            company=company,
            pk=pk,
        )

        if expense.status != Expense.Status.POSTED:
            messages.warning(request, "Only posted expenses can be voided.")
        else:
            expense.status = Expense.Status.VOID
            expense.void_reason = form.cleaned_data["reason"]
            expense.voided_at = timezone.now()
            expense.full_clean()
            expense.save(update_fields=[
                "status", "void_reason", "voided_at", "updated_at"
            ])
            messages.success(request, "Expense has been voided. Its record is preserved.")

    return redirect(
        "companies:finance:expense_detail",
        company_slug=company.slug,
        pk=pk,
    )
