import os
from django.db.transaction import atomic
from optparse import make_option
from django.core.management import BaseCommand
from ...item import get_item_type_from_path
from ...models import Item


class Command(BaseCommand):
    args = 'item'
    option_list = BaseCommand.option_list + (
        make_option(
            '-r', '--recursive', action='store_true', default=False,
            help='find items from specified directory recursively'
        ),
    )

    def handle(self, *args, **kwargs):
        for path in args:
            path = os.path.abspath(path)

            if os.path.isfile(path):
                item_type = get_item_type_from_path(path)
                if item_type:
                    self._import_file(path, item_type)

            elif os.path.isdir(path):
                self._import_files_from_directory(path, kwargs['recursive'])

    def _import_file(self, path, item_type):
        item, is_created = Item.objects.get_or_create(path=path, type=item_type)
        if is_created:
            self.stdout.write('importing {}'.format(path))

    @atomic
    def _import_files_from_directory(self, path, recursive):
        for file_path in self._enumerate_files(path, recursive):
            item_type = get_item_type_from_path(file_path)
            if item_type:
                self._import_file(file_path, item_type)

    def _enumerate_files(self, path, recursive):
        if recursive:
            for root, dirs, files in os.walk(path):
                for file_name in files:
                    yield os.path.join(root, file_name)

        else:
            for file_name in os.listdir(path):
                file_path = os.path.join(path, file_name)
                if os.path.isfile(file_path):
                    yield file_path
