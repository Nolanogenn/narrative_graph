from setuptools import find_packages, setup

setup(
        name="narrative_lib",
        packages=find_packages(include=['narrative_lib','rdflib']),
        version='0.0.1',
        description='library to build and edit narrative graphs',
        author='gnolano',
        install_requires=[],
        setup_requires=['pytest_runner'],
        tests_require=['pytest==4.4.1'],
        test_suite='test'
        )
