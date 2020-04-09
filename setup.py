from setuptools import setup,find_packages

setup(name='pt_tool',
	packages=find_packages(),
	install_requires=["django","django-crispy-forms==1.9.0"])
