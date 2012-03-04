from django.core.management.base import BaseCommand, CommandError
from django.conf import settings
from DynaWebKit import utils

params = ('app_name','db_user','admin_email',)

class Command(BaseCommand):
	
	def handle(self, *args, **options):
		kwargs = utils.args_util.process_args(args=args)
		utils.args_util.check_params(kwargs,params)
		print 'good to create db'
		
		
		
		
		
		
		
		
					