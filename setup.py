from setuptools import setup

setup(
    name='bride-of-frankensystem-usask',
    version='1.0',
    packages=['', 'BOFS', 'BOFS.admin', 'BOFS.default'],
    package_data={
        'BOFS': [
            'admin/templates/*.*',
            'static/*.*',
            'static/img/*.*',
            'static/js/*.*',
            'templates/*.*'
        ]
    },
    url='https://github.com/colbyj/bride-of-frankensystem/',
    license='LGPL-3.0',
    author='Colby Johanson',
    author_email='colby.johanson@usask.ca',
    description='A framework that allows for the development of custom online experiments and surveys.',
    install_requires=[
        "future",
        "flask",
        "eventlet",
        "flask-socketio",
        "sqlalchemy",
        "flask-sqlalchemy",
        "flask-sessionstore",
    ]

)
