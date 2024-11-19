from setuptools import setup

setup(
    name='recommendation',
    version='1.0.0',
    install_requires=[
        'Django>=4.0',

    ],
    packages=['recommendations', 'recommendations.migrations', 'music_recommendation_project'],
    url='',
    license='',
    author='Ngabirano Derrick',
    author_email='derrric65@gmail.com',
    description='This is a recommendation library that can be used in all django apps for recommending',
    classifiers=[
        'Programming Language :: Python :: 3',
        'Framework :: Django',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
