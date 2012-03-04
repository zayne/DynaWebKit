from django.conf import settings
import utils

invalid_args_error = 'Please Enter All Arguments as key=value.  e.g. %(key)s=%(value)s'

invalid_key_error = 'Please make sure to enter the following argument %(key)s'

missing_arg_value = 'The following argument %(key)s is missing a value'

def process_args(args=None):
	kwargs = dict()
	if not args:
		return kwargs
	for i in args:
		try:
			k,v = i.split('=')
			kwargs[k] = v
		except ValueError, ve:
			utils.exceptions.raise_exception(
				invalid_args_error % dict(
					key   = 'user',
					value = 'admin'
					),
				settings.DYNA_EXCEPTIONS['management_command_exception']
				)
	return kwargs

def check_param(args,param):
	if not args.has_key(param):
		utils.exceptions.raise_exception(
			invalid_key_error % dict(
				key = param 
			),
			settings.DYNA_EXCEPTIONS['management_command_exception']
		)
	else:
		if args[param] is None or args[param] == '':
			utils.exceptions.raise_exception(
				missing_arg_value % dict(
					key = param 
				),
			settings.DYNA_EXCEPTIONS['management_command_exception']
		)

def check_params(args,params):
	if args is None or not isinstance(args,dict):
		utils.exceptions.raise_exception(
			invalid_args_error % dict(
				key   = 'arg',
				value = 'some_value'
			),
			settings.DYNA_EXCEPTIONS['management_command_exception']
		)
	if params is None or not isinstance(params,tuple):
		utils.exceptions.raise_app_exception(
			settings.DYNA_APP_ERROR
		)
	for param in params:
		check_param(args,param)
		
	
	
	