from .models import ProductCategory
def global_product_category(request):
    product_category = ProductCategory.objects.all()
    context={
        'product_category':product_category,
    }
    return context