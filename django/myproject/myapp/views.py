##### .../myapp/views.py #####

from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.db import connection
from django.views.generic import TemplateView
from django.template import Context, RequestContext, Template
# Import custom Django DB model.
from myapp.models import Person, Shirt
# Import custom form.
from myapp.forms import NameForm, ShirtForm, ExpenseFormSimple, ExpenseFormFancy


"""
    Render custom 'Home' page.
"""
def home(request):
    form = NameForm()
    form_shirt = ShirtForm()
    form_expense = ExpenseFormSimple()
    #form_expense = ExpenseFormFancy()

    # Special Django variable 'context' used to make available data to html file.
    context = {
                'form': form,
                'form_shirt':form_shirt,
                'form_expense':form_expense
    }
    return render(request, 'myapp/home.html', context)

"""
    Render custom 'Form' page.
"""
def form_page(request):
    form = NameForm()

    # Special Django variable 'context' used to make available data to html file.
    context = {
                'form': form
    }
    return render(request, 'myapp/form.html', context)

"""
    Render custom 'Thanks' page.
"""
def thanks(request):
    form = NameForm()

    return render(request, 'myapp/thanks.html')

"""
    Process form submission - 'NameForm'.
"""
def submit_name(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        f = NameForm(request.POST)
        # check whether it's valid:
        if f.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            f_name = f.cleaned_data['first_name']
            l_name = f.cleaned_data['last_name']
            try:
                print("DB-ADD - START...")
                db_addNames(f_name=f_name, l_name=l_name)
            except:
                print("ERROR - New submitted names not added to database.")
                return HttpResponse("ERROR - New submitted names not added to database.")
            finally:
                print("DB-ADD - DONE.")
            # Redirect to a new URL:
            #* Redirect using function name.
            return redirect(home)

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()

    #return render(request, 'name.html', {'form': form})
    return redirect(home)

"""
    Process form submission - 'ShirtForm'.
"""
def submit_shirt(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        f = ShirtForm(request.POST)
        # check whether it's valid:
        if f.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            name = f.cleaned_data['name']
            shirt_size = f.cleaned_data['shirt_size']
            try:
                print("DB-ADD - START...")
                db_shirt(name=name, shirt_size=shirt_size)
            except:
                print("ERROR - New submitted shirt not added to database.")
                return HttpResponse("ERROR - New submitted shirt not added to database.")
            finally:
                print("DB-ADD - DONE.")
            # Redirect to a new URL:
            #* Redirect using function name.
            return redirect(home)

    # if a GET (or any other method) we'll create a blank form
    else:
        form = ShirtForm()

    #return render(request, 'name.html', {'form': form})
    return redirect(home)

"""
    TO-DO!
    Process form submission - 'ExpenseForm'.
"""
def submit_expense(request):
    pass

"""
    Render custom 'DB' page.
"""
def db_page(request):
    persons = Person.objects.all()

    # Special Django variable 'context' used to make available data to html file.
    context = {
                'persons': persons,
    }
    return render(request, 'myapp/db.html', context)

"""
    Render custom IP page.
    - Display IP Address.
    - Using 'RequestContext' instead 'Context' object.
"""
def client_ip_view(request):
    template = Template('{{ title }}: {{ ip_address }}')
    context = RequestContext(request, {
        'title': 'Your IP Address',
    }, [ip_address_processor])
    return HttpResponse(template.render(context))



####################
# HELPER FUNCTIONS.
####################
"""
    Using raw SQL, get table data from database.
"""
# Helper function.
def my_custom_sql(tablename):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM %s" %tablename)
        #cursor.execute("SELECT foo FROM bar WHERE id = %s", [self.id])
        #row = cursor.fetchone()
        row = cursor.fetchall()
    return row

"""
    Add 'new' name to database.
"""
def db_addNames(f_name, l_name):
    newP = Person(first_name=f_name, last_name=l_name)
    newP.save()

"""
    Add 'new' shirt to database.
"""
def db_shirt(name, shirt_size):
    newS = Shirt(name=name, shirt_size=shirt_size)
    newS.save()


"""
    Get IP address.
"""
def ip_address_processor(request):
    return {'ip_address': request.META['REMOTE_ADDR']}



####################
# EXPERIMENT CODE.
####################
"""
    Test endpoint.
    - [OPTION-01]: Display simple "Hello World" message.
    - [OPTION-02]: Display database table data.
"""
def test_simple(request):
    # OPTION-01.
    return HttpResponse("TEST MESSAGE - Hello, world.")
    # OPTION-02.
#    data_list = my_custom_sql(tablename="fruits")
#    return HttpResponse("TEST MESSAGE - %s" %data_list[1][1])

"""
    Render custom 'testpage' page.
"""
def test_page(request):
    db_tb_name="fruits"
    data_list = my_custom_sql(tablename=db_tb_name)
    persons = Person.objects.all()
    db_tb_name_aa = Person._meta.db_table
    form = NameForm()

    # Special Django variable 'context' used to make available data to html file.
    context = {
                'data': data_list,
                'db_tb_name': db_tb_name,
                'persons': persons,
                'db_tb_name_aa': db_tb_name_aa,
                'form': form
    }
    return render(request, 'myapp/testpage.html', context)

"""
    Process "test" form page submissions.
"""
def test_form_submit_name(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # Create a form instance and populate it with data from the request:
        f = NameForm(request.POST)
        # check whether it's valid:
        if f.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # Redirect to a new URL:
            #* M-01: Redirect using function name.
            #** NOTE: The 'redirect' (which will ultimately return a 'HttpResponseRedirect') can accept a model, view, or URL as passed in argument.
            return redirect(form_page)
            #* M-02: Redirect using URL.
            #return redirect('/form/')
            #* M-03: Redirect using 'HttpResponseRedirect' where passed in argument can only be URL.
            #return HttpResponseRedirect('/form/')
            #return HttpResponseRedirect('/form/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()

    #return render(request, 'name.html', {'form': form})
    return redirect(form_page)



#class HomePageView(TemplateView):
#    template_name = "home.html"
