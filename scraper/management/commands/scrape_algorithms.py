from django.core.management.base import BaseCommand
from scraper.scrape import scrape_algorithms

class Command(BaseCommand):
    help = 'Scrape algorithms from Mayo Clinic Labs'

    def handle(self, *args, **kwargs):
        scrape_algorithms()
        self.stdout.write(self.style.SUCCESS('Successfully scraped and saved algorithms'))
