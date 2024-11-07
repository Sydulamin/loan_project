from django.db.models import Q
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Wing_One, Project
from .forms import Wing_One_Form
from .decorators import admin_only, allowerd_users


@login_required(login_url='login')
@admin_only
def dashboard(request):
    wing = User.objects.all().exclude(username='admin')
    qs = Wing_One.objects.all()

    name_of_proj_query = request.GET.get('name_of_proj')
    wing_query = request.GET.get('wing')
    amount_per_currency = request.GET.get('amount_per_currency')
    amount_in_million = request.GET.get('amount_in_million')

    if name_of_proj_query != '' and name_of_proj_query is not None:
        qs = qs.filter(name__icontains=name_of_proj_query).distinct()
    elif amount_per_currency != '' and amount_per_currency is not None:
        qs = qs.filter(amount_as_per_agreement_currency__icontains=amount_per_currency).distinct()
    elif amount_in_million != '' and amount_in_million is not None:
        qs = qs.filter(amount_in_equivalent_million_us__icontains=amount_in_million).distinct()

    context = {
        'queryset': qs,
        'wing': wing,
    }
    return render(request, 'dashboard.html', context)


@login_required(login_url='login')
@allowerd_users(allowed_roles='wings')
def index(request):
    user = request.user
    queryset = Wing_One.objects.filter(wing=user)
    form = Wing_One_Form()
    form.wing = user
    if request.method == 'POST':
        # Extract data from the POST request
        project_name = request.POST.get('name')
        project_support = 'project_support' in request.POST
        budget_support = 'budget_support' in request.POST
        loan_or_grant = request.POST.get('loan_or_grant')
        amount_as_per_agreement_currency = request.POST.get('amount_as_per_agreement_currency')
        loan_amount = request.POST.get('loan_amount')
        loan_duration = request.POST.get('loan_duration')
        loan_terms = request.POST.get('loan_terms')
        grant_amount = request.POST.get('grant_amount')
        grant_terms = request.POST.get('grant_terms')
        status = request.POST.get('status')

        # Convert the amount and other numerical fields to the correct type
        try:
            amount_as_per_agreement_currency = float(amount_as_per_agreement_currency)
            loan_amount = float(loan_amount) if loan_amount else None
            loan_duration = int(loan_duration) if loan_duration else None
            grant_amount = float(grant_amount) if grant_amount else None
        except ValueError:
            return HttpResponse("Invalid data entered.", status=400)

        # Create the Project object
        project = Project(
            name=project_name,
            project_support=project_support,
            budget_support=budget_support,
            loan_or_grant=loan_or_grant,
            amount_as_per_agreement_currency=amount_as_per_agreement_currency,
            loan_amount=loan_amount,
            loan_duration=loan_duration,
            loan_terms=loan_terms,
            grant_amount=grant_amount,
            grant_terms=grant_terms,
            status=status
        )

        # Save the project to the database
        project.save()
        return redirect('home')

    return render(request, 'index.html', context)


@allowerd_users(allowed_roles='wings')
def update_wing(request, pk):
    wing = Wing_One.objects.get(id=pk)
    form = Wing_One_Form(instance=wing)
    if request.method == "POST":
        form = Wing_One_Form(request.POST, instance=wing)
        if form.is_valid():
            form.instance.wing = request.user
            form.save()
            return redirect('home')
    context = {
        'form': form
    }
    return render(request, 'wing_create.html', context)


@login_required(login_url='login')
@admin_only
def wing_page(request, pk):
    user = User.objects.get(id=pk)
    qs = Wing_One.objects.filter(wing=user)
    wing = User.objects.all().exclude(username='admin')

    name_of_proj_query = request.GET.get('name_of_proj')
    wing_query = request.GET.get('wing')
    amount_per_currency = request.GET.get('amount_per_currency')
    amount_in_million = request.GET.get('amount_in_million')

    if name_of_proj_query != '' and name_of_proj_query is not None:
        qs = qs.filter(name__icontains=name_of_proj_query).distinct()
    elif amount_per_currency != '' and amount_per_currency is not None:
        qs = qs.filter(amount_as_per_agreement_currency__icontains=amount_per_currency).distinct()
    elif amount_in_million != '' and amount_in_million is not None:
        qs = qs.filter(amount_in_equivalent_million_us__icontains=amount_in_million).distinct()

    context = {
        'queryset': qs,
        'wing': wing,
        'user': user,

    }
    return render(request, 'wing.html', context)
