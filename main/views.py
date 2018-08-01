from django.shortcuts import render
from django.db import IntegrityError
from django.shortcuts import redirect 
from django.http import HttpResponse
from .forms_config.forms import CreateComputerForm
from .models  import *
# Create your views here.
def MainPage(request):
    form_create_computer = CreateComputerForm()
    computers = Computer.objects.all()
    print()
    return render(request, 'main.html', {'form_create' : form_create_computer, 'computers' : computers})
    
def Create(request):
    form_create_computer = CreateComputerForm()
    form = CreateComputerForm(request.POST)
    if form.is_valid():
        data = form.cleaned_data
        try:
            computer = Computer(**data)
            computer.save()
        except IntegrityError as e:
            print("Error: ",e)
        return redirect('main')
    else:
        print('poop')
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

