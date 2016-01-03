from setuptools import setup

setup(
    name='anybox-nose-selenium',
    version='0.0.1',
    description='anybox-nose-selenium is a plugin for nose that provides '
                'support to launch selenium tests.',
    long_description=open('README.rst').read(),
    author='Pierre Verkest',
    author_email='pverkest@anybox.fr',
    url='https://github.com/petrus-v/anybox-nose-selenium',
    packages=[
        'anybox'
        'anybox.nose_selenium',
        'anybox.nose_selenium.plugins',
    ],
    install_requires=[
        'nose',
        'selenium-extra-api',
    ],
    dependency_links=[
        'git+https://github.com/petrus-v/selenium-extra-api.git@master#'
        'egg=selenium-extra-api',
    ],
    entry_points={
        'nose.plugins.0.10': [
            'selenium = anybox.nose_selenium.plugins.selenium:Selenium'
        ]
    },
    license='Mozilla Public License 2.0 (MPL 2.0)',
    keywords='nose selenium CI',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Mozilla Public License 2.0 (MPL 2.0)',
        'Operating System :: POSIX',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: MacOS :: MacOS X',
        'Topic :: Software Development :: Quality Assurance',
        'Topic :: Software Development :: Testing',
        'Topic :: Utilities',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7']
)
