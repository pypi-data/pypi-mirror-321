from setuptools import setup, find_packages

setup(
    name='django-errformer',
    version='0.1.1',
    description='Send errors and logs to Telegram chat.',
    long_description=open('Readme.md').read(),
    long_description_content_type='text/markdown',
    author='Oleg Tarasov',
    author_email='tolegu@ya.ru',
    url='https://github.com/breduin/django-errformer',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Django>=4.0',
    ],
    classifiers=[
        'Framework :: Django',
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
    ],
)
