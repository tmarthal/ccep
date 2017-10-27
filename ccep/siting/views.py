from django.shortcuts import get_object_or_404, render


from siting.models import County, SitingModel, ModelLayer

def index(request):
    counties = County.objects.filter(active=True).order_by('name')
    # View code here...
    return render(request, 'siting/index.html', {
        'counties': counties,
    }, content_type='text/html')



def detail(request, county_id):
    county = get_object_or_404(County, pk=county_id)
    counties = County.objects.filter(active=True).order_by('name')

    # get default or
    sitingModels = SitingModel.objects.filter(active=True, county=county).order_by('model_date')
    sitingModelId = request.GET.get('sitingModelId')
    sitingModel = None
    if sitingModelId:
        sitingModel = sitingModels.get(id=sitingModelId)


    if not sitingModel:
        try:
            sitingModel = sitingModels.get(default=True)
        except SitingModel.DoesNotExist:
            sitingModel = None

    print("found siting model ", sitingModel)
    layers = ModelLayer.objects.filter(sitingModel=sitingModel)

    return render(request, 'siting/detail.html', {
            'county': county, 'border': county.mpoly.json, 'counties': counties,
            'sitingModels':sitingModels, 'model': sitingModel,
            'layers': layers
        }
    )




