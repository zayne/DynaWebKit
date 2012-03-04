from django.core.management.base import CommandError
import utils

def get_module(class_name):
	m = class_name.split('.')[:1]
	module = __import__(modulename, globals(), locals(), [name])
	
def raise_app_exception(error_msg):
	raise Exception(error_msg)
	
def raise_command_error(error_msg):
	raise CommandError(error_msg)

def raise_exception(error_msg,cls):
	if cls is None or cls == '':
		raise_app_exception('Improper Use of Exception Module')
	module, cls_name = utils.string_util.get_module_and_class(cls)
	exception = utils.import_util.dynamic_import(module,cls_name)
	if isinstance(exception(),CommandError):
		raise_command_error(error_msg)
	raise_app_exception(error_msg)