from django.http import JsonResponse

from api.models import Product, Category


def show_all_products(request):
    products = Product.objects.all()
    products_json = [product.to_json() for product in products]
    return JsonResponse(products_json, safe=False)


def get_one_product(request, product_id):
    return JsonResponse(Product.objects.get(id=product_id).to_json(), safe=False)


def show_all_categories(request):
    categories = Category.objects.all()
    categories_json = [category.to_json() for category in categories]
    return JsonResponse(categories_json, safe=False)


def get_one_category(request, category_id):
    return JsonResponse(Category.objects.get(id=category_id).to_json(), safe=False)


def get_products_by_category(request, category_id):
    products = Product.objects.filter(category_id=category_id)
    products_json = [product.to_json() for product in products]
    return JsonResponse(products_json, safe=False)