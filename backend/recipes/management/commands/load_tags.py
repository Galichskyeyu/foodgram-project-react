from django.core.management import BaseCommand
from recipes.models import Tag


class Command(BaseCommand):
    help = 'Загрузка тегов'

    def handle(self, *args, **kwargs):
        data = [
            {'name': 'Завтрак', 'color': '#00FF00', 'slug': 'breakfast'},
            {'name': 'Обед', 'color': '#FF0000', 'slug': 'dinner'},
            {'name': 'Ужин', 'color': '#0000FF', 'slug': 'supper'}
        ]
        Tag.objects.bulk_create(Tag(**tag) for tag in data)
        self.stdout.write(self.style.SUCCESS('Теги загружены.'))
