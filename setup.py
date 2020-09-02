import setuptools

with open('README.md', 'r') as file:
	long_description = file.read()


setuptools.setup(
	name = 'preprocess_turi',   # this should be unqiue
	version = '0.0.2',
	author = 'Asim Abbas Turi',
	author_email = 'asim.abbas2011@gmail.com',
	description = 'This is the preprocessing package for nlp',
	Long_descripion = long_description,
    Long_descripion_content_type = 'text/markdown',
    packages = setuptools.find_packages(),
    classifiers = [
    'Programming Language :: Python :: 3',
    'License :: OSI Aproved :: MIT License',
    "Operating System :: OS Independent"],
    python_requires = '>=3.5'
	)
	