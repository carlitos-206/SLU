#Basic Django Packages/Libs
from django.contrib import messages
from django.http.response import HttpResponseRedirect
from django.shortcuts import render, HttpResponse, redirect
from .models import *

#Creates Plain Message box in python for validation instead of JS
from tkinter import *
from tkinter import messagebox


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
            messages.error(request, "No Spaces Allowed")
            messages.error(request, "Case Sensitive")
            return redirect("/")
        this_team = teams.objects.filter(name=request.POST['teamName'])
        request.session['user_id'] = this_team[0].id
    return redirect("/dashboard")

#Dashboard + Query function ( Send Off )
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
    #QUERY BY SECTION
        
        if result_searched== "ALL":
            everything = kitchenItems.objects.all()
            context = {
                        'teams' : this_team[0],
                        'something': everything
                    }
            return render(request, "result.html", context)
        # Querying for all departments
        if result_dept == "all":
            
            # language query variable ( these are local to this If statement )
            english_result = kitchenItems.objects.filter(item__contains=result_searched)
            french_result = kitchenItems.objects.filter(item_french__contains=result_searched)
            spanish_result = kitchenItems.objects.filter(item_spanish__contains=result_searched)
            
            #Item not in this section
            if len(english_result) + len(french_result) + len(spanish_result) == 0:
                messages.error(request, f' "{result_searched}" not in this section "{result_dept}" for "{result_language}" ')
                return render(request, "result.html")
            
            #query ALL:
            
            #Empty Query in all Sections
            if result_searched == "":
                messages.error(request, "Please enter a search term")
                return render(request, "result.html")
            
            #Check if item in english
            if len(english_result) >=1:
                
                #English to English Query in all Sections
                if result_language == "english":
                    context = {
                        'teams' : this_team[0],
                        'something': english_result
                    }
                    return render(request, "result.html", context)
                
                #Englisht to French Query in all Sections
                if result_language == "french":
                    context = {
                        'teams' : this_team[0],
                        'something': english_result
                    }
                    return render(request, "result_french.html", context)
                
                #English to Spanish Query in all Sections
                if result_language == "spanish":
                    print("spanish 3")
                    context = {
                        'teams' : this_team[0],
                        'something': english_result
                        }
                    return render(request, "result_spanish.html", context)
            
            #Check if the item is in spanish
            if len(spanish_result) >=1:
                
                #Spanish to English Query in all Sections
                if result_language == "english":
                    context = {
                        'teams' : this_team[0],
                        'something': spanish_result
                    }
                    return render(request, "result.html", context)
                
                #Spanish to French Query in all Sections
                if result_language == "french":
                    context = {
                        'teams' : this_team[0],
                        'something': spanish_result
                    }
                    return render(request, "result_french.html", context)
                
                #Spanish to Spanish Query in all Sections
                if result_language == "spanish":
                    context = {
                        'teams' : this_team[0],
                        'something': spanish_result
                    }
                    return render(request, "result_spanish.html", context)
            
            #Check if the item is in french
            if len(french_result) >=1:
                #French to English Query in all Sections
                if result_language == "english":
                    context = {
                        'teams' : this_team[0],
                        'something': french_result
                    }
                    return render(request, "result.html", context)
                
                #French to French Query in all Sections
                if result_language == "french":
                    context = {
                        'teams' : this_team[0],
                        'something': french_result
                    }
                    return render(request, "result_french.html", context)
                
                #French to Spanish Query in all Sections
                if result_language == "spanish":
                    context = {
                        'teams' : this_team[0],
                        'something': french_result
                    }
                    return render(request, "result_spanish.html", context)
    #Querying by BOH Section
        if result_dept == "boh":
            # language query variable ( these are local to this If statement )
            english_result = kitchenItems.objects.filter(section=sections.objects.get(name="BOH"), item__contains=result_searched)
            french_result = kitchenItems.objects.filter(section=sections.objects.get(name="BOH"), item_french__contains=result_searched)
            spanish_result = kitchenItems.objects.filter(section=sections.objects.get(name="BOH"), item_spanish__contains=result_searched)
            
            #Item not in this section
            if len(english_result) + len(french_result) + len(spanish_result) == 0:
                messages.error(request, f' "{result_searched}" not in this section "{result_dept}" for "{result_language}" ')                
                return render(request, "result.html")
            #Empty Query for BOH
            if result_searched == "":
                messages.error(request, "Please enter a search term")
                return render(request, "result.html")
            
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
            
            #Check if item in english
            if len(english_result) >=1:
                
                #English to English Query in all Sections
                if result_language == "english":
                    context = {
                        'teams' : this_team[0],
                        'something': english_result
                    }
                    return render(request, "result.html", context)
                
                #Englisht to French Query in all Sections
                if result_language == "french":
                    context = {
                        'teams' : this_team[0],
                        'something': english_result
                    }
                    return render(request, "result_french.html", context)
                
                #English to Spanish Query in all Sections
                if result_language == "spanish":
                    print("spanish 3")
                    context = {
                        'teams' : this_team[0],
                        'something': english_result
                        }
                    return render(request, "result_spanish.html", context)
            
            #Check if the item is in spanish
            if len(spanish_result) >=1:
                
                #Spanish to English Query in all Sections
                if result_language == "english":
                    context = {
                        'teams' : this_team[0],
                        'something': spanish_result
                    }
                    return render(request, "result.html", context)
                
                #Spanish to French Query in all Sections
                if result_language == "french":
                    context = {
                        'teams' : this_team[0],
                        'something': spanish_result
                    }
                    return render(request, "result_french.html", context)
                
                #Spanish to Spanish Query in all Sections
                if result_language == "spanish":
                    context = {
                        'teams' : this_team[0],
                        'something': spanish_result
                    }
                    return render(request, "result_spanish.html", context)
                
            #Check if the item is in french
            if len(french_result) >=1:
                #French to English Query in all Sections
                if result_language == "english":
                    context = {
                        'teams' : this_team[0],
                        'something': french_result
                    }
                    return render(request, "result.html", context)
                
                #French to French Query in all Sections
                if result_language == "french":
                    context = {
                        'teams' : this_team[0],
                        'something': french_result
                    }
                    return render(request, "result_french.html", context)
                
                #French to Spanish Query in all Sections
                if result_language == "spanish":
                    context = {
                        'teams' : this_team[0],
                        'something': french_result
                    }
                    return render(request, "result_spanish.html", context)
        
        #Query by FOH Section
        if result_dept == "foh":
            # language query variable ( these are local to this If statement )
            english_result = kitchenItems.objects.filter(section=sections.objects.get(name="FOH"), item__contains=result_searched)
            french_result = kitchenItems.objects.filter(section=sections.objects.get(name="FOH"), item_french__contains=result_searched)
            spanish_result = kitchenItems.objects.filter(section=sections.objects.get(name="FOH"), item_spanish__contains=result_searched)
            
            #Item not in this section
            if len(english_result) + len(french_result) + len(spanish_result) == 0:
                messages.error(request, f' "{result_searched}" not in this section "{result_dept}" for "{result_language}" ')
                return render(request, "result.html")
            #Empty Query
            if result_searched == "":
                messages.error(request, "Please enter a search term")
                return render(request, "result.html")
            
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
            
            #Check if item in english
            if len(english_result) >=1:
                
                #English to English Query in all Sections
                if result_language == "english":
                    context = {
                        'teams' : this_team[0],
                        'something': english_result
                    }
                    return render(request, "result.html", context)
                
                #Englisht to French Query in all Sections
                if result_language == "french":
                    context = {
                        'teams' : this_team[0],
                        'something': english_result
                    }
                    return render(request, "result_french.html", context)
                
                #English to Spanish Query in all Sections
                if result_language == "spanish":
                    print("spanish 3")
                    context = {
                        'teams' : this_team[0],
                        'something': english_result
                        }
                    return render(request, "result_spanish.html", context)
            
            #Check if the item is in spanish
            if len(spanish_result) >=1:
                
                #Spanish to English Query in all Sections
                if result_language == "english":
                    context = {
                        'teams' : this_team[0],
                        'something': spanish_result
                    }
                    return render(request, "result.html", context)
                
                #Spanish to French Query in all Sections
                if result_language == "french":
                    context = {
                        'teams' : this_team[0],
                        'something': spanish_result
                    }
                    return render(request, "result_french.html", context)
                
                #Spanish to Spanish Query in all Sections
                if result_language == "spanish":
                    context = {
                        'teams' : this_team[0],
                        'something': spanish_result
                    }
                    return render(request, "result_spanish.html", context)

            #Check if the item is in french
            if len(french_result) >=1:
                #French to English Query in all Sections
                if result_language == "english":
                    context = {
                        'teams' : this_team[0],
                        'something': french_result
                    }
                    return render(request, "result.html", context)
                
                #French to French Query in all Sections
                if result_language == "french":
                    context = {
                        'teams' : this_team[0],
                        'something': french_result
                    }
                    return render(request, "result_french.html", context)
                
                #French to Spanish Query in all Sections
                if result_language == "spanish":
                    context = {
                        'teams' : this_team[0],
                        'something': french_result
                    }
                    return render(request, "result_spanish.html", context)
        
        #Query by DMO Section
        if result_dept == "dmo":
            
            # language query variable ( these are local to this If statement )
            english_result = kitchenItems.objects.filter(section=sections.objects.get(name="DMO"), item__contains=result_searched)
            french_result = kitchenItems.objects.filter(section=sections.objects.get(name="DMO"), item_french__contains=result_searched)
            spanish_result = kitchenItems.objects.filter(section=sections.objects.get(name="DMO"), item_spanish__contains=result_searched)
            
            #Item not in this section
            if len(english_result) + len(french_result) + len(spanish_result) == 0:
                messages.error(request, f' "{result_searched}" not in this section "{result_dept}" for "{result_language}" ')
                return render(request, "result.html")
            #Empty Query
            if result_searched == "":
                messages.error(request, "Please enter a search term")
                return render(request, "result.html")
            
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
            
            #Check if item in english
            if len(english_result) >=1:
                
                #English to English Query in all Sections
                if result_language == "english":
                    context = {
                        'teams' : this_team[0],
                        'something': english_result
                    }
                    return render(request, "result.html", context)
                
                #Englisht to French Query in all Sections
                if result_language == "french":
                    context = {
                        'teams' : this_team[0],
                        'something': english_result
                    }
                    return render(request, "result_french.html", context)
                
                #English to Spanish Query in all Sections
                if result_language == "spanish":
                    print("spanish 3")
                    context = {
                        'teams' : this_team[0],
                        'something': english_result
                        }
                    return render(request, "result_spanish.html", context)
            
            #Check if the item is in spanish
            if len(spanish_result) >=1:
                #Spanish to English Query in all Sections
                if result_language == "english":
                    context = {
                        'teams' : this_team[0],
                        'something': spanish_result
                    }
                    return render(request, "result.html", context)
                
                #Spanish to French Query in all Sections
                if result_language == "french":
                    context = {
                        'teams' : this_team[0],
                        'something': spanish_result
                    }
                    return render(request, "result_french.html", context)
                
                #Spanish to Spanish Query in all Sections
                if result_language == "spanish":
                    context = {
                        'teams' : this_team[0],
                        'something': spanish_result
                    }
                    return render(request, "result_spanish.html", context)
            
            #Check if the item is in french
            if len(french_result) >=1:
                #French to English Query in all Sections
                if result_language == "english":
                    context = {
                        'teams' : this_team[0],
                        'something': french_result
                    }
                    return render(request, "result.html", context)
                
                #French to French Query in all Sections
                if result_language == "french":
                    context = {
                        'teams' : this_team[0],
                        'something': french_result
                    }
                    return render(request, "result_french.html", context)
                
                #French to Spanish Query in all Sections
                if result_language == "spanish":
                    context = {
                        'teams' : this_team[0],
                        'something': french_result
                    }
                    return render(request, "result_spanish.html", context)
        
    #Wrongful Query 
    else:
        messages.error(request, f'No results found for:  "{result_searched}" in {result_language} ')
        return render(request, "result.html", context)


#Contact Card ( supervisor call list ) 
def contact(request):
    if 'user_id' in request.session:
        return render(request, "contact.html")
    else:
        return redirect("/")

#Schedule Page Display only cafe in session
def schedule(request):
    if 'user_id' in request.session:
        this_team = teams.objects.filter(id=request.session['user_id'])
        #Verifies what cafe is in session and displays the schedule for that cafe only
        if this_team[0].name == "Bluebill":
            return render(request, "bluebill_schedule.html")
        if this_team[0].name == "Nuage":
            return render(request, "nuage_schedule.html")
        if this_team[0].name == "Union":
            return render(request, "union_schedule.html")
        if this_team[0].name == "Root":
            return render(request, "root_schedule.html")
    else:
        return redirect("/")

#Safety Page
def safety(request):
    if 'user_id' in request.session:
        return render(request, "safety.html")
    else:
        return redirect("/")

# Log Out
def exit(request):
    request.session.clear()
    return redirect("/")