from django.shortcuts import render, redirect
from .models import Store, Product
from .forms import StoreForm, ProductForm

# Create your views here.
def index(request):
    stores = Store.objects.all()
    context = {
        'stores': stores,
    }
    return render(request, 'stores/index.html', context)

def detail(request, store_pk):
    store = Store.objects.get(pk=store_pk)
    product_form = ProductForm()
    products = Product.objects.filter(store=store)
    context = {
        'store': store,
        'product_form': product_form,
        'products': products,
    }
    return render(request, 'stores/detail.html', context)

def create(request):
    if request.method == 'POST':
        form = StoreForm(request.POST)
        if form.is_valid():
            store = form.save()
            return redirect('stores:detail', store.pk)
    else:
        form = StoreForm()
    context = {
        'form': form,
    }
    return render(request, 'stores/create.html', context)

def create_product(request, store_pk):
    store = Store.objects.get(pk=store_pk)
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            product = form.save(commit=False)
            product.user = request.user
            product.store = store
            product.save()
            return redirect('stores:detail', store_pk)
        
def delete_product(request, store_pk, product_pk):
    product = Product.objects.get(pk=product_pk)
    product.delete()
    return redirect('stores:detail', store_pk)