from django.http import JsonResponse
from town.views import get_towns
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def get(request):
    dsl_query = request.body
    if request.method == "POST":
        response = get_towns(dsl_query)
    return JsonResponse({"countItem": len(response), "towns": response})


# def get_towns(request):
#     with connection.cursor() as cursor:
#         cursor.execute("SELECT * FROM town_town")
#         row = cursor.fetchall()
#         print(row)
#     return JsonResponse({'countItem': len(row), 'row': row})
