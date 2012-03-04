from django.core.management.base import BaseCommand

class Command(BaseCommand):
	
	def handle(self,*args,**options):
		import argparse
		parser = argparse.ArgumentParser(description='Create A Django Application')
		parser.add_argument('-n','--app_name',help='Please Add App Name')
		parser.parse_args(args)