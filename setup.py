from setuptools import setup, find_packages

version = '0.1'

setup(
    name='ckanext-cmap',
    version=version,
    description="CKAN extension for CMAP Data Sharing Hub",
    long_description="""\
    """,
    classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
    keywords='',
    author='',
    author_email='',
    url='',
    license='',
    packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
    namespace_packages=['ckanext', 'ckanext.cmap'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        # -*- Extra requirements: -*-
    ],
    entry_points=\
    """
    [ckan.plugins]
    # Add plugins here, eg
    cmap_routing=ckanext.cmap.routing:CMAPRoutingPlugin
    cmap_configurer=ckanext.cmap.configurer:CMAPConfigurerPlugin
    cmap_organization_form=ckanext.cmap.forms:CMAPOrganizationForm
    cmap_dataset_form=ckanext.cmap.forms:CMAPDatasetForm
    """,
)
