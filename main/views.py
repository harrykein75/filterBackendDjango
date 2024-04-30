from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, JsonResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views import generic
from django.db.models import Q

from .models import Point

# def index(request):
#     points = Point.objects.all()
#     return render(request, 'main/index.html', {'points':points})

# def detail(request, points_id):
#     point = get_object_or_404(Point, pk=points_id)
#     return render(request, 'main/detail.html', {'point': point})

class PointListView(generic.ListView):
    template_name = 'main/index.html'
    context_object_name = 'points'

    def get_queryset(self):
        return Point.objects.all()

class PointDetailView(generic.DetailView):
    model = Point
    template_name = "main/detail.html"

def search_view(request):
    print(request)
    if request.method == 'GET' and request.is_ajax():
        query = request.GET.get('query', '')
        # Perform search using Django ORM
        results = Point.objects.filter(Q(location__icontains=query) | Q(address__icontains=query))
        # Serialize the results into JSON
        data = [{'name': result.address} for result in results]
        return JsonResponse(data, safe=False)
    else:
        # Return error response if not an AJAX GET request
        return JsonResponse({'error': 'Invalid request'}, status=400)

def order_data(request):
    # Retrieve data from the database and order it alphabetically by the 'name' field
    queryset = Point.objects.all().order_by('location')

    # Serialize the data into JSON format
    data = [{'name': item.location} for item in queryset]

    return JsonResponse(data, safe=False)

def get_data1(request):
    # Retrieve all data from the database
    queryset = Point.objects.all()

    # Paginate the queryset
    paginator = Paginator(queryset, 2)  # 10 items per page
    page_number = request.GET.get('page')

    try:
        page_obj = paginator.page(page_number)
    except PageNotAnInteger:
        page_obj = paginator.page(1)
    except EmptyPage:
        page_obj = paginator.page(paginator.num_pages)
    
    # Serialize the data into JSON format
    data = {
        #'results': list(page_obj),
        'results': [{'location': item.location, 'address': item.address, 'latitude': item.latitude, 'longitude': item.longitude} for item in page_obj.object_list],
        'total_pages': paginator.num_pages
    }

    return JsonResponse(data, safe=False)

def get_data(request):
    # Retrieve all data from the database
    queryset = Point.objects.all()

    # Apply search filter
    search_query = request.GET.get('search')
    if search_query:
        queryset = queryset.filter(Q(location__icontains=search_query) | Q(address__icontains=search_query))

    # Apply ordering
    ordering = request.GET.get('ordering')

    if ordering:
        queryset = queryset.order_by(ordering)

    # Paginate the queryset
    paginator = Paginator(queryset, 10)  # 10 items per page
    page_number = request.GET.get('page')

    try:
        page_obj = paginator.page(page_number)
    except PageNotAnInteger:
        page_obj = paginator.page(1)
    except EmptyPage:
        page_obj = paginator.page(paginator.num_pages)
    
    # Serialize the data into JSON format
    data = {
        'results': [{'location': item.location, 'address': item.address, 'latitude': item.latitude, 'longitude': item.longitude, 'user': item.user.username if item.user else 'N/A', 'visible': item.visible, 'date': item.date} for item in page_obj.object_list],  # Convert queryset to list of dictionaries
        'total_pages': paginator.num_pages
    }
    return JsonResponse(data)

    
