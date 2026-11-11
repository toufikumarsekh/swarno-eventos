from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render
from apps.companies.models import Company, Membership
from .models import Event
from .forms import EventForm


def get_company_or_404(request, company_slug):
    company = get_object_or_404(Company, slug=company_slug, is_active=True)
    get_object_or_404(
        Membership,
        company=company,
        user=request.user,
        is_active=True,
    )
    return company


@login_required
def event_list(request, company_slug):
    company = get_company_or_404(request, company_slug)
    events = Event.objects.filter(company=company).select_related(
        "client", "enquiry"
    )

    query = request.GET.get("q", "").strip()
    status = request.GET.get("status", "").strip()

    if query:
        events = events.filter(
            Q(title__icontains=query)
            | Q(client__name__icontains=query)
            | Q(venue__icontains=query)
        )

    if status:
        events = events.filter(status=status)

    return render(request, "events/list.html", {
        "company": company,
        "events": events,
        "query": query,
        "selected_status": status,
        "statuses": Event.Status.choices,
    })


@login_required
def event_create(request, company_slug):
    company = get_company_or_404(request, company_slug)

    if request.method == "POST":
        form = EventForm(request.POST, company=company)
        if form.is_valid():
            event = form.save(commit=False)
            event.company = company
            event.created_by = request.user
            event.save()
            return redirect(
                "companies:events:detail",
                company_slug=company.slug,
                pk=event.pk,
            )
    else:
        form = EventForm(company=company)

    return render(request, "events/form.html", {
        "company": company,
        "form": form,
        "page_title": "Create Event",
    })


@login_required
def event_detail(request, company_slug, pk):
    company = get_company_or_404(request, company_slug)
    event = get_object_or_404(
        Event.objects.select_related("client", "enquiry"),
        company=company,
        pk=pk,
    )
    return render(request, "events/detail.html", {
        "company": company,
        "event": event,
    })


@login_required
def event_edit(request, company_slug, pk):
    company = get_company_or_404(request, company_slug)
    event = get_object_or_404(Event, company=company, pk=pk)

    if request.method == "POST":
        form = EventForm(request.POST, instance=event, company=company)
        if form.is_valid():
            form.save()
            return redirect(
                "companies:events:detail",
                company_slug=company.slug,
                pk=event.pk,
            )
    else:
        form = EventForm(instance=event, company=company)

    return render(request, "events/form.html", {
        "company": company,
        "form": form,
        "page_title": "Edit Event",
        "event": event,
    })
