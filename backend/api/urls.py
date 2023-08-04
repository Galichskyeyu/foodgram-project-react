from api.views import (AddAndDeleteFavoriteRecipe, AddAndDeleteShoppingCart,
                       AddAndDeleteSubscribe, AuthToken, DownloadCart,
                       IngredientsViewSet, RecipesViewSet, SubscribeViewSet,
                       TagsViewSet, UsersViewSet, set_password)
from django.urls import include, path
from rest_framework.routers import DefaultRouter

app_name = 'api'

router = DefaultRouter()
router.register('users', UsersViewSet)
router.register('tags', TagsViewSet)
router.register('ingredients', IngredientsViewSet)
router.register('recipes', RecipesViewSet)


urlpatterns = [
    path(
        'auth/token/login/',
        AuthToken.as_view(),
        name='login'
    ),
    path(
        'users/set_password/',
        set_password,
        name='set_password'
    ),
    path(
        'users/<int:user_id>/subscribe/',
        AddAndDeleteSubscribe.as_view(
            {'post': 'create', 'delete': 'perform_destroy'}
        ),
        name='subscribe'
    ),
    path(
        'recipes/<int:recipe_id>/favorite/',
        AddAndDeleteFavoriteRecipe.as_view(),
        name='favorite_recipe'
    ),
    path(
        'recipes/<int:recipe_id>/shopping_cart/',
        AddAndDeleteShoppingCart.as_view(),
        name='shopping_cart'
    ),
    path(
        'recipes/download_shopping_cart/',
        DownloadCart.as_view({'get': 'download_shopping_cart'}),
        name='download_shopping_cart'
    ),
    path(
        'users/subscriptions/',
        SubscribeViewSet.as_view({'get': 'subscriptions'}),
        name='subscriptions'
    ),
    path('', include(router.urls)),
    path('', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
]
