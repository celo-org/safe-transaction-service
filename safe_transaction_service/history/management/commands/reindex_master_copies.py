from django.core.management.base import BaseCommand

from ...services import IndexServiceProvider


class Command(BaseCommand):
    help = 'Force reindexing of Safe events/traces (depending on the running mode)'

    def add_arguments(self, parser):
        parser.add_argument('--addresses', nargs='+', help='Safe addresses. If not provided all will be reindexed')
        parser.add_argument('--block-process-limit', type=int, help='Number of blocks to query each time',
                            default=1000)
        parser.add_argument('--from-block-number', type=int, help='Which block to start reindexing from', required=True)

    def handle(self, *args, **options):
        block_process_limit = options['block_process_limit']
        from_block_number = options['from_block_number']
        self.stdout.write(self.style.SUCCESS(f'Setting block-process-limit to {block_process_limit}'))
        self.stdout.write(self.style.SUCCESS(f'Setting from-block-number to {from_block_number}'))

        IndexServiceProvider().reindex_master_copies(
            from_block_number,
            block_process_limit=block_process_limit,
            addresses=options['addresses']
        )
