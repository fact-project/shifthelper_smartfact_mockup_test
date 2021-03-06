from setuptools import setup

setup(
    name='shifthelper_smartfact_mockup_test',
    version='0.2.0',
    description='shifthelper_smartfact_mockup_test',
    url='https://github.com/fact-project/shifthelper_smartfact_mockup_test',
    author='Dominik Neise',
    author_email='neised@phys.ethz.ch',
    license='GPL3',
    packages=[
        'smartfact_mockup',
    ],
    # package_data={},
    # tests_require=['pytest>=3.0.0'],
    # setup_requires=['pytest-runner'],
    install_requires=[
        'numpy',
    ],
    zip_safe=False,
    entry_points={
        'console_scripts': [
            'SH_test_one_by_one = smartfact_mockup.one_by_one:main',
        ],
    }
)
