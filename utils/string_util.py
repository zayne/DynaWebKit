import utils

def get_module_and_class(full_class_name):
	try:
		module = full_class_name[:full_class_name.rindex('.')]
		cls_name = full_class_name[full_class_name.rindex('.')+1:len(full_class_name)]
		return module, cls_name
	except ValueError, e:
		utils.exceptions.raise_app_exception(e.message)
		