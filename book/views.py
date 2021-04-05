from django.http.response import HttpResponseNotFound,HttpResponseRedirect,Http404,JsonResponse
from django.shortcuts import get_object_or_404,render,HttpResponse,redirect
from django.urls import reverse_lazy
from .forms import BookForm,CategoryForm
from .models import *
from django.views.generic import ListView,CreateView,UpdateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import  LoginRequiredMixin
from django.core.serializers.json import DjangoJSONEncoder
import json

# Create your views here.
# @login_required
# def home(request):
#     context={}
#     context['data']=Book.objects.filter(user=request.user)
#     return render(request,'book/book/home.html',context)

class BookListView(LoginRequiredMixin,ListView):
    model = Book
    template_name = "book/book/home.html"
    context_object_name='data'
    paginate_by=5
    # queryset = Book.objects.all().order_by('created_on').select_related('category')

    def get_queryset(self):
        return super().get_queryset().filter(user=self.request.user).order_by('created_on').select_related('category')

# def create_book(request):
#     if request.method == 'GET':
#         context={}
#         context['form']=BookForm()
#         return render(request,'book/book/create.html',context)
#     elif request.method == 'POST':
#         form = BookForm(request.POST)
#         if form.is_valid():
#            book = form.save(commit=False)
#            book.user =request.user
#            book.save()
#            return redirect('book_home')
#         else:
#             context={}
#             context['form']=BookForm()
#             return render(request,'book/book/create.html',context)  

def book_list_api(request):
    books = Book.objects.all().values()
    json_data = json.dumps(list(books),cls=DjangoJSONEncoder)
    return HttpResponse(json_data,content_type='application/json')

class BookCreateView(LoginRequiredMixin,CreateView):
    model = Book
    form_class=BookForm
    template_name = "book/book/create.html"
    success_url=reverse_lazy('book_home')

    def form_valid(self,form):
        book=form.save(commit=False)
        book.user=self.request.user
        book.save()
        return redirect(self.success_url)

# def update_book(request,id):
#     # try:
#         #      book=Book.objects.get(id=id)
#         # except Book.DoesNotExist:
#         #     return HttpResponseNotFound()
#     book = get_object_or_404(Book,id=id ,user=request.user)
#     if request.method == 'GET':
        
#         context={}
#         context['form']=BookForm(instance=book)
#         return render(request,'book/book/create.html',context)
#     elif request.method == 'POST':
#         form = BookForm(data=request.POST,instance=book)
#         if form.is_valid():
#             form.save()
#             return redirect('book_home')
#         else:
#             context={}
#             context['form']=BookForm()
#             return render(request,'book/book/create.html',context)  

class BookUpdateView(LoginRequiredMixin,UpdateView):
    model = Book
    form_class=BookForm
    template_name = "book/book/create.html"
    success_url=reverse_lazy('book_home')
    pk_url_kwarg = 'id'

    def get_object(self):
        pk=self.kwargs.get('id')
        if pk is None:
            raise Http404()
        b= Book.objects.filter(pk=pk,user=self.request.user).first()
        if b is None:
            raise Http404()
        else:
            return b        


@login_required
def delete_book(request,  id):
    book=get_object_or_404(Book, id=id,user=request.user)
    book.delete()
    return redirect('book_home')

#category
#-------------------------------------

class CategoryListView(LoginRequiredMixin,ListView):
    model = Category
    template_name = "book/category/home.html"
    context_object_name='data'

class CategoryCreateView(LoginRequiredMixin,CreateView):
    model = Category
    form_class=CategoryForm
    template_name = "book/category/create.html"
    success_url=reverse_lazy('category_home')

class CategoryUpdateView(LoginRequiredMixin,UpdateView):
    model = Category
    form_class=CategoryForm
    template_name = "book/category/create.html"
    success_url=reverse_lazy('category_home')
    pk_url_kwarg = 'id'

@login_required
def delete_category(request,  id):
    category=get_object_or_404(Category, id=id)
    category.delete()
    return redirect('category_home')

