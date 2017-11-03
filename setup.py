from setuptools import setup


setup(
	name='classification',
	version='0.1.0',
	install_rquires=['numpy', 'scipy', 'metaploit', 'scikit_learn'],
	packages=['classification'],
	include_package_data=True,
	package_data={
		'' : ['iris.py'],
	},
	entry_points={
		'console_scripts': [
			"classify = classification.plot_iris_dataset:main"
		]
	}
)