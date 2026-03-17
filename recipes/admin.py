from django.contrib import admin
from .models import Category, Recipe

# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    ... # Configurações para o modelo Category


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    ... # Configurações para o modelo Recipe



admin.site.register(Category, CategoryAdmin)