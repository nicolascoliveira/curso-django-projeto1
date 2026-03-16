from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=65) # Texto curto
    created_at = models.DateTimeField(auto_now_add=True) # Data e hora de criação
    updated_at = models.DateTimeField(auto_now=True) # Data e hora de atualização


class Recipe(models.Model):
    title = models.CharField(max_length=65), # Texto curto
    description = models.CharField(max_length=165), # Texto curto
    slug = models.SlugField(), # Texto curto, sem espaços, usado para URLs
    preparation_time = models.IntegerField(), # Número inteiro
    preparation_time_unit = models.CharField(max_length=65), # Texto curto
    servings = models.IntegerField(), # Número inteiro
    servings_unit = models.CharField(max_length=65), # Texto curto
    preparation_steps = models.TextField() # Texto longo
    preparation_steps_is_html = models.BooleanField(default=False) # Verdadeiro ou falso
    created_at = models.DateTimeField(auto_now_add=True) # Data e hora de criação
    updated_at = models.DateTimeField(auto_now=True) # Data e hora de atualização
    is_published = models.BooleanField(default=False) # Verdadeiro ou falso
    cover = models.ImageField(upload_to='recipes/covers/%Y/%m/%d/') # Imagem
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True) # Chave estrangeira para a categoria
    author = models.ForeignKey('auth.User', on_delete=models.SET_NULL, null=True) # Chave estrangeira para o autor
