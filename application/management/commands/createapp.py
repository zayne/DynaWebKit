from django.core.management.base import BaseCommand, CommandError
from django.conf import settings
from DynaWebKit import utils

dyna_root = settings.NEW_APPLICATION_PATH

params = ('app_name',)

class Command(BaseCommand):
	
	def create_or_fail(self,result,app_name):
		if not bool(result['permitted']):
			if result.has_key('username') and result.has_key('groupname'):
				error = 'App user doesn\'t have permission to create the app. '\
					'Permissions belong to group %(groupname)s and user %(username)s' % dict(
						groupname = result['groupname'],
						username  = result['username']
				)
				utils.exceptions.raise_exception(
					error,
					settings.DYNA_EXCEPTIONS['management_command_exception']
				)
			else:
				utils.exceptions.raise_app_exception(settings.DYNA_APP_ERROR)
		else:
			utils.shell_util.create_django_project(dyna_root,app_name)
			
	def check_exception(self,result):
		if result.has_key('exception'):
			error = 'Please make sure to create the DynaWebKit root directory at %(app_root)s '\
				% dict(app_root = dyna_root)
			utils.exceptions.raise_exception(
				error,
				settings.DYNA_EXCEPTIONS['management_command_exception']
			)
	
	def create_app(self,app_name):
		result = utils.shell_util.check_permission(path=dyna_root)
		if result.has_key('permitted'):
			self.create_or_fail(result,app_name)
			print '%(app_name)s has been successfully initialized' % dict(
				app_name = app_name
			)
			return True
		else:
			self.check_exception(result)
		utils.exceptions.raise_app_exception(settings.DYNA_APP_ERROR)
			
		
	
	def handle(self, *args, **options):
		kwargs = utils.args_util.process_args(args=args)
		utils.args_util.check_params(kwargs,params)
		self.create_app(kwargs.get('app_name',None))