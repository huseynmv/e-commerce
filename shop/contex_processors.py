from .models import Product, ProductCategory,Color
def global_product_category(request):
    product_category = ProductCategory.objects.all()
    colors = list(Color.objects.all().values_list('id', flat=True))
    # print(colors)
       
    context={
        'product_category':product_category,
        'color':colors,
        
    }
    return context

