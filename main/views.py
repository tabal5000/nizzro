from django.shortcuts import render
from django.db import IntegrityError
from django.db.models import Q
from django.shortcuts import redirect 
from django.http import HttpResponse, HttpResponseRedirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .forms_config.forms import ComputerForm
from .models  import Computer
# Create your views here.
"""

"""
def MainPage(request):
    form_create_computer = ComputerForm()
	
    query = request.GET.get('search')
    if query == "" or query == None:
        computers = Computer.objects.all()
        return render(request, 'main.html', {'form_create' : form_create_computer, 'computers' : computers})

    filtered_computers = set() # Te racunalnike bom na koncu vrnil
    computers = set() # Zacasna mnozica 
    splitan_query = query.split(",")
	# Najprej naredim eno množico v katero dodam vse racunalnike, ki ustrezajo prvemu kriteriju
    for comp in Computer.objects.filter(description__contains=splitan_query[0].strip()):
        filtered_computers.add(comp)
	
	# Potem pa za vsak kriterij naredim presek racunalnikov, ki she vedno ustrezajo
    for query in splitan_query[1:]:
        for comp in Computer.objects.filter(description__contains=query.strip()):
            computers.add(comp)	
        filtered_computers = filtered_computers & computers # Naredim presek z "novimi" racunalniki	
    return render(request, 'main.html', {'form_create' : form_create_computer, 'computers' : filtered_computers})

    

def Edit_Computer(request,pk):
    computer = Computer.objects.get(id=pk)
    if request.method == 'GET':
        form_edit_computer = ComputerForm(instance=computer)
        return render(request, 'edit.html', {'form' : form_edit_computer})
    elif request.method == 'POST':
        form = ComputerForm(request.POST,instance=computer)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(request.path_info)  
        else:
            print('form invalid!')
            return HttpResponseRedirect(request.path_info)  
    return HttpResponseRedirect(request.path_info)  
    
def Create(request):
    form = ComputerForm(request.POST)
    if form.is_valid():
        data = form.cleaned_data
        try:
            computer = Computer(**data)
            computer.save()
        except IntegrityError as e:
            print("Error: ",e)
        return redirect('main')
    else:
        print('Form invalid.')
        return redirect('main')

def Delete(request,pk):
    Computer.objects.get(id=pk).delete()
    return HttpResponse(status=200)
	

    
	
	
	
	
	
""" @login_required
@user_passes_test(is_osebje)
def StudentList(request):
    user_list = Vpis.objects.filter().all().order_by('student__last_name')
    user_filter = Student_list_filter(request.GET,queryset=user_list)
    filter_form = user_filter.form
    paginator = Paginator(user_filter.qs, 10)
    page = request.GET.get('page')

    try:
        response_data = paginator.page(page)
    except PageNotAnInteger:
        response_data = paginator.page(1)
    except EmptyPage:
        response_data = paginator.page(paginator.num_pages)
    # Dodaj form fields za uvoz študentov
    form_uvoz = UploadFileForm()
    form_zeton = ZetonForm()
    if request.method == 'GET':
        return render(request, 'student_list.html', {'students': response_data,
                 'form' : filter_form, 'form_uvoz' : form_uvoz, 'form_zeton' : form_zeton})

    elif request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                st_dodanih = handle_uploaded_file(request.FILES['datoteka'])
                print(st_dodanih)
                return redirect(reverse('student_added') + '?added=' + str(st_dodanih))
            except Exception as e:
                print(str(e))
                error = "Pri uvozu datoteke je prišlo do napake. Poskusite znova. "
                return render(request, 'student_list.html', {'students': response_data,
                            'form' : filter_form, 'form_uvoz' : form_uvoz, 'error' : error, 'form_zeton' : form_zeton}) """

