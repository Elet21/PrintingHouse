from .models import SubCategory



def search(search_query):
    return SubCategory.objects.filter(name__icontains=search_query)


