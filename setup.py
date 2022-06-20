import setuptools
from distutils.util import convert_path

with open("README.md", "r", encoding='utf-8') as fh:
    long_description = fh.read()

main_ns = {}
ver_path = convert_path('backtrader_bokeh/version.py')
with open(ver_path, encoding='utf-8') as ver_file:
    exec(ver_file.read(), main_ns)

setuptools.setup(
    name='backtrader_bokeh',
    version=main_ns['__version__'],
    description='Plotting package for Backtrader (Bokeh)',
    python_requires='>=3.6',
    author='Metaer',
    author_email='metaer.sol@gmail.com',
    long_description=long_description,
    long_description_content_type="text/markdown",
    license='GPLv3+',
    url="https://github.com/iniself/backtrader_bokeh_basic",
    project_urls={
        "Bug Tracker": "https://github.com/iniself/backtrader_bokeh_basic/issues",
        "Documentation": "https://github.com/iniself/backtrader_bokeh_basic/wiki",
        "Source Code": "https://github.com/iniself/backtrader_bokeh_basic",
        "Demos": "https://github.com/iniself/backtrader_bokeh_basic/tree/gh-pages",
    },

    # What does your project relate to?
    keywords=['trading', 'development', 'plotting', 'backtrader', 'Bokeh'],

    packages=setuptools.find_packages(),
    package_data={'backtrader_bokeh': ['templates/*.j2', 'templates/js/*.js']},

    install_requires=[
        'backtrader',
        'bokeh',
        'jinja2',
        'pandas',
        'matplotlib~=3.2.2',
    ],
)
