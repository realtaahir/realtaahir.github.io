from django.shortcuts import render

# Create your views here.

def index(request):
    # section_data = Section.objects.all()
    # context = {
    #     'section_data': section_data  # Pass the section_data to the template
    # }
    return render(request, 'landing/index.html' )


