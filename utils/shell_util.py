import os, stat, pwd, grp
from django.conf import settings
from fabric.api import local


def create_django_project(dyna_root,app_name):
	cd = 'cd %(app_root)s' % dict(
		app_root = dyna_root
		)
	create_project = 'django-admin.py startproject %(app_name)s' % dict(
		app_name = app_name
		)
	local('%(cd)s;%(create_project)s' % dict(
		cd             = cd,
		create_project = create_project)
	)	

def path_exists(path=None):
	return os.path.exists(path)
	
def create_dir(path=None,deep=False):
	if not deep:
		os.mkdir(path)
	else:
		os.makedirs(path)

def check_permission(path=None):
	result = dict()
	uid = settings.DYNA_KIT_UID
	gid = settings.DYNA_KIT_GID
	try:
		st = os.stat(path)
	except OSError, e:
		result['exception'] = e.message
		return result
	result['permitted'] = bool(st.st_uid==uid) & bool(st.st_gid==gid)
	result['username'] = pwd.getpwuid(st.st_uid)[0]
	result['groupname'] = grp.getgrgid(st.st_gid)[0]
	return result

def run(command=None,output=False):
	local(command,capture=output)