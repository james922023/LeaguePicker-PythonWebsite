from django.db import models

# Create your models here.

class LeagueItem(models.Model):
    
    name = models.CharField(max_length=100, unique=True)
    url = models.CharField(max_length=100, unique = True)
    
    def __str__(self) ->str:
        """
        Function to print out, data on object when .all() function is calleed
        """
        return (f'{self.name}-{self.url}')


class LeagueChamp(models.Model):
    
    name = models.CharField(max_length=100, unique=True)
    url = models.CharField(max_length=100, unique=True)
    
    def __str__(self)->str:
        """
        Function to print out, data on object when .all() function is calleed
        """
        return (f'{self.name}-{self.url}')
    
class LeagueRune(models.Model):
    
    name = models.CharField(max_length=100, unique=True)
    url = models.CharField(max_length=100, unique=True)
    
    def __str__(self)->str:
        """
        Function to print out, data on object when .all() function is calleed
        """
        return (f'{self.name}-{self.url}')
    
class TopBuilds(models.Model):
    
    champion = models.CharField(max_length=100)
    items = models.JSONField()
    runes = models.JSONField()
    ability_order = models.JSONField()
    
    def __str__(self)->str:
        """
        Function to print out, data on object when .all() function is calleed
        """
        return (f'{self.champion}-{self.items}-{self.runes}-{self.ability_order}')