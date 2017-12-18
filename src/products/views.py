from django.shortcuts import render, Http404,get_object_or_404
from django.views.generic import ListView,DetailView
from .models import Product

class ProductListView(ListView):
    template_name = 'products/list.html'

    def get_queryset(self, *args, **kwargs):
        request = self.request
        return Product.objects.all()

class ProductDetailView(DetailView):
    queryset = Product.objects.all()
    template_name = 'products/detail.html'

    def get_object(self, *args, **kwargs):
        request = self.request
        slug = self.kwargs.get('slug')
        # instance = get_object_or_404(Product, slug=slug, active=True)
        try:
            instance = Product.objects.get(slug=slug, active=True)
        except Product.DoesNotExist:
            raise Http404("Not found")
        except Product.MultipleObjectsReturned:
            queryset = Product.objects.filter(slug=slug, active=True)
            instance = queryset.first()
        except:
            raise Http404('Unknown error')

        return instance



class ProductFeaturedListView(ListView):
    template_name = 'products/list.html'

    def get_queryset(self, *args, **kwargs):
        request = self.request
        return Product.objects.all().featured()

class ProductFeaturedDetailView(DetailView):
    template_name = 'products/featured-detail.html'
    queryset = Product.objects.featured()
