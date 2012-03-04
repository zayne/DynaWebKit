
def dynamic_import(module,cls):
	try:
		module = __import__(module, globals(), locals(), [cls])
		return module.__dict__[cls]
	except ImportError, e:
		utils.raise_app_exception(e.message)