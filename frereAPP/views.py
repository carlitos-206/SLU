from django.contrib import messages
from django.shortcuts import render, HttpResponse, redirect
from django.utils import translation
from .models import *

#Landing Page
def index(request):
    return render(request, 'index.html')

#Team Confirmation ( Log In )
def team(request):
    if request.method == 'GET':    
        return redirect('/')
    if request.method == 'POST':
        if not teams.objects.team_validator(request.POST['teamName']):
            messages.error(request, "Team Not Found")
            return redirect("/")
        this_team = teams.objects.filter(name=request.POST['teamName'])
        request.session['user_id'] = this_team[0].id
    return redirect("/dashboard")

#Dashboard + Query function ( Send Off)
def dashboard(request):
    if 'user_id' not in request.session:
        return redirect("/")
    this_team = teams.objects.filter(id = request.session['user_id'])
    context = {
        'teams' : this_team[0]
    }
    return render(request, 'dashboard.html', context)


#Query Results Landing Page + Query function to search for results
def result(request):
    #Ensure visitor is logged in ( Has a session )
    if 'user_id' not in request.session:
        return redirect("/")
    this_team = teams.objects.filter(id = request.session['user_id'])
    context = {
        'teams' : this_team[0]
    }
    if request.method == "POST":
        # creating variables for the query
        result_searched = request.POST["search"]
        result_language = request.POST["language"]
        result_dept = request.POST["dept"]
        print(result_searched, result_language, result_dept)
        
        # language query variable
        english_result = kitchenItems.objects.filter(item__contains=result_searched)
        french_result = kitchenItems.objects.filter(item_french__contains=result_searched)
        spanish_result = kitchenItems.objects.filter(item_spanish__contains=result_searched)
        
    #QUERY BY SECTION
        
        # Querying for all departments
        if result_dept == "all":
            # language query variable
            english_result = kitchenItems.objects.filter(item__contains=result_searched)
            french_result = kitchenItems.objects.filter(item_french__contains=result_searched)
            spanish_result = kitchenItems.objects.filter(item_spanish__contains=result_searched)
            #query ALL:
            if result_searched== "ALL":
                everything = kitchenItems.objects.all()
                context = {
                        'teams' : this_team[0],
                        'something': everything
                    }
                return render(request, "result.html", context)
            #Empty Query in all Sections
            if result_searched == "":
                messages.error(request, "Please enter a search term")
                return render(request, "result.html")
            
            #Wrongful Query
            # if result_searched not in list_result:
            #     messages.error(request, f"No results found for:  {result_searched} ")
            #     return render(request, "result.html")
            
            #English Query in all Sections
            if result_language == "english":
                context = {
                    'teams' : this_team[0],
                    'something': english_result
                }
                return render(request, "result.html", context)
            #French Query in all Sections
            if result_language == "french":
                context = {
                    'teams' : this_team[0],
                    'something': french_result
                }
                return render(request, "result_french.html", context)
            
            #Spanish Query in all Sections
            if result_language == "spanish":
                print("spanish start")
                #Spanish to English Query
                if result_searched == english_result:
                    print("spanish 1 ")
                    context = {
                    'teams' : this_team[0],
                    'something': english_result
                    }
                    return render(request, "result.html", context)
                
                #Spanish to French Query
                if result_searched == french_result:
                    print("spanish 2")
                    context = {
                    'teams' : this_team[0],
                    'something': french_result
                    }
                    return render(request, "result_french.html", context)
                    
                else:
                    print("spanish 3")
                    context = {
                    'teams' : this_team[0],
                    'something': spanish_result
                    }
                    return render(request, "result_spanish.html", context)
                
                
                # context = {
                #     'teams' : this_team[0],
                #     'something': spanish_result
                # }
                # return render(request, "result_spanish.html", context)
        
        
    #Querying by BOH Section
        if result_dept == "boh":
            # language query variable
            english_result = kitchenItems.objects.filter(section=sections.objects.get(name="BOH"), item__contains=result_searched)
            french_result = kitchenItems.objects.filter(section=sections.objects.get(name="BOH"), item_french__contains=result_searched)
            spanish_result = kitchenItems.objects.filter(section=sections.objects.get(name="BOH"), item_spanish__contains=result_searched)
            
            #Empty Query for BOH
            if result_searched == "":
                messages.error(request, "Please enter a search term")
                return render(request, "result.html")
            
            #Wrongful Query
            # if result_searched not in list_result:
            #     messages.error(request, f"No results found for:  {result_searched} ")
            #     return render(request, "result.html")
            
            #English Query for BOH
            if result_language == "english":
                context = {
                    'teams' : this_team[0],
                    'something': english_result
                }
                return render(request, "result.html", context)
            
            #French Query for BOH
            if result_language == "french":
                context = {
                    'teams' : this_team[0],
                    'something': french_result
                }
                return render(request, "result_french.html", context)
            
            #Spanish Query for BOH
            if result_language == "spanish":
                context = {
                    'teams' : this_team[0],
                    'something': spanish_result
                }
                return render(request, "result_spanish.html", context)
        
        #Query by FOH Section
        if result_dept == "foh":
            #language query variable
            english_result = kitchenItems.objects.filter(section=sections.objects.get(name="FOH"), item__contains=result_searched)
            french_result = kitchenItems.objects.filter(section=sections.objects.get(name="FOH"), item_french__contains=result_searched)
            spanish_result = kitchenItems.objects.filter(section=sections.objects.get(name="FOH"), item_spanish__contains=result_searched)
            
            #Empty Query
            if result_searched == "":
                messages.error(request, "Please enter a search term")
                return render(request, "result.html")
            
            #Wrongful Query
            # if result_searched not in list_result:
            #     messages.error(request, f"No results found for:  {result_searched} ")
            #     return render(request, "result.html")
            
            #English Query for FOH
            if result_language == "english":
                context = {
                    'teams' : this_team[0],
                    'something': english_result
                }
                return render(request, "result.html", context)
            
            #French Query for FOH
            if result_language == "french":
                context = {
                    'teams' : this_team[0],
                    'something': french_result
                }
                return render(request, "result_french.html", context)
            
            #spanish Query for FOH
            if result_language == "spanish":
                context = {
                    'teams' : this_team[0],
                    'something': spanish_result
                }
                return render(request, "result_spanish.html", context)
        
        
        #Query by DMO Section
        if result_dept == "dmo":
            
            #language query variable
            english_result = kitchenItems.objects.filter(section=sections.objects.get(name="DMO"), item__contains=result_searched)
            french_result = kitchenItems.objects.filter(section=sections.objects.get(name="DMO"), item_french__contains=result_searched)
            spanish_result = kitchenItems.objects.filter(section=sections.objects.get(name="DMO"), item_spanish__contains=result_searched)
            #Empty Query
            if result_searched == "":
                messages.error(request, "Please enter a search term")
                return render(request, "result.html")
            
            #Wrongful Query
            # if result_searched not in list_result:
            #     messages.error(request, f"No results found for:  {result_searched} ")
            #     return render(request, "result.html")
            
            #English Query for DMO Section
            if result_language == "english":
                context = {
                    'teams' : this_team[0],
                    'something': english_result
                }
                return render(request, "result.html", context)
            
            #French Query for DMO Section
            if result_language == "french":
                context = {
                    'teams' : this_team[0],
                    'something': french_result
                }
                return render(request, "result.html", context)
            
            #Spanish Query for DMO Section
            if result_language == "spanish":
                context = {
                    'teams' : this_team[0],
                    'something': spanish_result
                }
                return render(request, "result.html", context)
        else:
            messages.error(request, "No results found ")
            return render(request, "result.html", context)
    # return redirect("/dashboard")



# #Landing page + translation Query from English to X
# def english2X(request):
#     if 'user_id' not in request.session:
#         return redirect("/")
#     this_team = teams.objects.filter(id = request.session['user_id'])
#     context = {
#         'teams' : this_team[0]
#     }
#     if request.method == "POST":
#         # creating variables for the query
#         result_searched = request.POST["search"]
#         result_language = request.POST["language"]
#         result_dept = request.POST["dept"]
#         print(result_searched, result_language, result_dept)
        
#         # language query variable
#         english_result = kitchenItems.objects.filter(item__contains=result_searched)
#         french_result = kitchenItems.objects.filter(item_french__contains=result_searched)
#         spanish_result = kitchenItems.objects.filter(item_spanish__contains=result_searched)
#     #Query English to spanish
#         if result_language == "spanish":
#             english = kitchenItems.objects.filter(item__contains=result_searched)
#             context = {
#                     'teams' : this_team[0],
#                     'something': english,
#                 }
#             return render(request, "result_spanish.html", context)
#     return render(request, "result.html", context)

#contact supervisors
def contact(request):
    return render(request, "contact.html")

def exit(request):
    request.session.clear()
    return redirect("/")