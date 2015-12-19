from setuptools import setup

setup(
    name='GephiStreamer',
 
    version="2.0.0",
 
    packages=['gephistreamer'],
 
    author="Matthieu Totet (@totetmatt)",

    author_email="matthieu.totet@gmail.com",
 
    description="Tools to stream data to gephi",

    long_description=open('README.md').read(),
 
    include_package_data=True,

    url='https://github.com/totetmatt/GephiStreamer',
    
    install_requires=[
          'requests',
      ],

    classifiers=[
        "Programming Language :: Python",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.4",
        "Topic :: Communications",
    ],
)