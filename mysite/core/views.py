from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView, CreateView
from django.core.files.storage import FileSystemStorage
from django.urls import reverse_lazy


from .forms import FilForm
from .models import Fil

class Home(TemplateView):
    template_name = 'home.html'



def upload(request):
    context = {}
    if request.method == 'POST':
        uploaded_file = request.FILES['document']
        fs = FileSystemStorage()
        name = fs.save(uploaded_file.name, uploaded_file)
        context['url'] = fs.url(name)
    return render(request, 'upload.html', context)

def fil_list(request):
    books = Fil.objects.all()
    return render(request, 'book_list.html', {
        'fil': Fil
    })


#def upload_fil(request):
    if request.method == 'POST':
        form = FilForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = FilForm()
    return render(request, 'upload_book.html', {
        'form': form
    })


#def delete_fil(request, pk):
    if request.method == 'POST':
        book = Fil.objects.get(pk=pk)
        book.delete()
    return redirect('book_list')


#class FilListView(ListView):
    model = Fil
    template_name = 'class_book_list.html'
    context_object_name = 'books'


#class UploadFilView(CreateView):
    model = Fil
    form_class = FilForm
    success_url = reverse_lazy('class_book_list')
    template_name = 'upload_book.html'
