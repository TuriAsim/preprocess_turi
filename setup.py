import setuptools

with open('README.md','r') as file:
	long_description= file.read()


setuptools.setup(
	name='preprocess_turi',   # this should be unqiue
	version='0.0.1',
	author='Asim Abbas Turi',
	author_email='asim.abbas2011@gmail.com',
	description='This is the preprocessing package for nlp',
	Long_descripion = long_description,
    Long_descripion_content_type = 'text/markdown',
    packages = setuptools.find_packegs(),
    classifiers = [
    'programming language'::Python :: 3,
    'License :: OSI Approved :: MIT License',
    'Operating System :: OS Independent']
    python_requires = '>=3.5'
	)