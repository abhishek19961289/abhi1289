from django.http import HttpResponse
from django.shortcuts import render
from django.core.paginator import Paginator
from django.core.paginator import EmptyPage,PageNotAnInteger


def home(request):
    return HttpResponse("Hello, Django!")

def index1(request):  
    my_dicts = {f"key_{i}": f"value_{i}" for i in range(100)}
    context = {'my_dictionary': my_dicts}
    return render(request, 'hi.html', context)

def my_view(request):
    my_dictionary = {f"key_{i}": f"value_{i}" for i in range(100)}
    context = {'my_dictionary': my_dictionary}
    return render(request, 'dict.html', context)

def index(request):
    ServiceData = {f"key_{i}": f"value_{i}" for i in range(100)}  # Example dictionary data
   #paginator = Paginator(list(items_list.items()), 10)
    paginator = Paginator(ServiceData, 10)
      # Convert dict_items to list and paginate
    
    
    page_obj = paginator.get_page(2)
    serviceDatafinal = paginator.get_page(page_obj)
    paginator = Paginator(ServiceData)
    
    context = {'my_dictionary': page_obj}
    
    # context = {
    #     'page_obj': page_obj,
    # }
    return render(request, 'index.html', context)




def index3(request):
    data = range(1, 101)  # Your data list

    paginator = Paginator(data, 10)  # Create a Paginator object with desired page size
    page_number = request.GET.get('page')  # Get the current page number from the request

    page_obj = paginator.get_page(page_number)  # Get the desired page object

    return render(request, 'my_template.html', {'page_obj': page_obj})

def dynamic_image_view(request):
    image_url_param = request.GET.get('image_url_param', '')
    dynamic_image_url = None

    if image_url_param:
        dynamic_image_url = image_url_param

    return render(request, 'dynamic_image_url.html', {'dynamic_image_url': dynamic_image_url})

def dynamic_image_view1(request):
    # Get the image URL from wherever you're retrieving it (e.g., a database or API)
    image_url = "https://th.bing.com/th/id/R.13820971a962ffbeb63a8fef36185b16?rik=vZ3lu%2blbhy6jxw&riu=http%3a%2f%2fwallup.net%2fwp-content%2fuploads%2f2016%2f03%2f10%2f319576-photography-landscape-nature-water-grass-trees-plants-sunrise-lake.jpg&ehk=6WS2p9KknQa9F%2bgAH16n44NReuUyS2rzXah2zy7kiAw%3d&risl=&pid=ImgRaw&r=0"
    
    return render(request, 'dynamic_image.html', {'image_url': image_url})

from django.http import JsonResponse

def my_view2(request):
    print('@')
    if request.method == 'POST':
        field1 = request.POST.get('field1')
        field2 = request.POST.get('field2')
        
        # Process the data as needed
        
        print(field1)

        response_data = {
            'message': 'Data received successfully',
            'field1': field1,
            'field2': field2
        }
        
        return JsonResponse(response_data)
    
def my_page(request):
    return render(request, 'ftob.html')
