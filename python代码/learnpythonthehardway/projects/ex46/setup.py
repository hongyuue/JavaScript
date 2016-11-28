try:
	from setuptools import setup
except ImportError:
	from distutils.core import setup

config= {
	'description':'My project',
	'author':'yuue',
	'url':'URL to get it at.',
	'download_url':'hongyuue@163.com',
	'version':'0.1',
	'install_requires':['nose'],
	'packages':['ex46'],
	'scripts':[],
	'name':'projectname'
}

setup(**config)