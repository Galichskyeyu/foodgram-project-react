from django.contrib import admin
from recipes.models import (FavoriteRecipe, Ingredient, Recipe,
                            RecipeIngredient, ShoppingCart, Subscribe, Tag)


class RecipeIngredientAdmin(admin.StackedInline):
    model = RecipeIngredient
    autocomplete_fields = ('ingredient',)


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'get_author', 'name',
        'get_tags', 'get_favorite_count',
    )
    search_fields = ('name',)
    list_filter = ('author__username', 'name', 'tags__name',)
    inlines = (RecipeIngredientAdmin,)
    empty_value_display = '-пусто-'

    @admin.display(description='Автор')
    def get_author(self, obj):
        return obj.author.username

    @admin.display(description='Теги')
    def get_tags(self, obj):
        list_ = [_.name for _ in obj.tags.all()]
        return ', '.join(list_)

    @admin.display(description='В избранном')
    def get_favorite_count(self, obj):
        return obj.favorite_recipe.count()


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'name', 'color', 'slug',
    )
    search_fields = ('name', 'slug',)
    empty_value_display = '-пусто-'


@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'name', 'measurement_unit',
    )
    search_fields = ('name',)
    list_filter = ('name',)
    empty_value_display = '-пусто-'


@admin.register(Subscribe)
class SubscribeAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'user', 'author', 'created',
    )
    search_fields = (
        'user__email', 'author__email',
    )
    empty_value_display = '-пусто-'


@admin.register(FavoriteRecipe)
class FavoriteRecipeAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'user', 'get_recipe', 'get_count',
    )
    empty_value_display = '-пусто-'

    @admin.display(description='Рецепты')
    def get_recipe(self, obj):
        return [
            f'{item["name"]} ' for item in obj.recipe.values('name')[:5]]

    @admin.display(description='В избранном')
    def get_count(self, obj):
        return obj.recipe.count()


@admin.register(ShoppingCart)
class ShoppingCartAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'user', 'get_recipe', 'get_count',
    )
    empty_value_display = '-пусто-'

    @admin.display(description='Рецепты')
    def get_recipe(self, obj):
        return [
            f'{item["name"]} ' for item in obj.recipe.values('name')[:5]
        ]

    @admin.display(description='В списке покупок')
    def get_count(self, obj):
        return obj.recipe.count()
