from django.shortcuts import render
from django.db import IntegrityError
from django.shortcuts import redirect
from django.http import HttpResponse, HttpResponseRedirect
from .filters import *
from .models import *
from .forms_config.forms import ListElementForm, ProcessorForm
# Create your views here.
"""

"""
def MainPageView(request):
    if request.method == 'GET':
        processor_form = ProcessorForm()
        return render(request,'main.html', {'processor_form' : processor_form })

def SystemListsView(request):

    if request.method == 'GET':
        request_copy = request.GET.copy()
        if not request.GET:
            request_copy['syslist_id'] = '1'
        list_element_form = ListElementForm()

        list_element_filter = ListElementsFilter(request_copy,queryset=ListElements.objects.all())
        filter_form = list_element_filter.form
        list_elements = list_element_filter.qs
        return render(request,'system_lists.html',{'list_elements' : list_elements,
                            'filter_form':filter_form, 'add_list_element_form' : list_element_form})

    if request.method == 'POST':
        form = ListElementForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            try:
                list_element = ListElements(**data).save()
            except IntegrityError as e:
                print('Error',e)
            return redirect('syslists_view')
        else:
            print('Form invalid.')
            return redirect('syslists_view')

def ListElementsDetailView(request,pk):
    if request.method == 'DELETE':
        ListElements.objects.get(id=pk).delete()
        return HttpResponse(status=204)

def ProcessorView(request):
    if request.method == 'POST':
        form = ProcessorForm(request.POST,request.FILES)
        if form.is_valid():
            data = form.cleaned_data
            try:
                processor = Processor(**data).save()
            except IntegrityError as e:
                print('Error',e)
            return redirect('main_view')
        else:
            print('Form invalid.')
            return redirect('main_view')

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

