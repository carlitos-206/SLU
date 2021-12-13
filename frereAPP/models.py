from django.db import models


#------- THIS IS DB FOR TEAMS ----------------
class teamManager(models.Manager):
    def team_validator(self, teamName):
        team_exist = teams.objects.filter(name=teamName)
        if team_exist:
            team_exist[0] == teamName
            return True
        else:
            return False
class teams(models.Model):
    name = models.CharField(max_length=250)
    objects = teamManager()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    
#----------------END---------------------------



#---------THIS IS DB FOR KITCHEN SECTIONS-------------
class sections(models.Model):
    name = models.CharField(max_length=250)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
#-----------END-------------------------------



#------------THIS IS DB FOR KITCHENWARE------

class kitchenItems(models.Model):
    section = models.ForeignKey(sections, related_name="sections", on_delete=models.CASCADE)
    html_tag=models.TextField()
    item = models.CharField(max_length=250)
    item_french = models.CharField(max_length=250 , default="")
    item_spanish = models.CharField(max_length=250 , default="")
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

#-----------END--------------------------------


