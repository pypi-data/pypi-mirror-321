from setuptools import setup, find_packages

setup(
    name='fx_shared_models',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'Django>=3.0',
        'django-environ>=0.10.0',
    ],
    python_requires='>=3.8',
    author='FX Backend',
    author_email='fxbackend@gmail.com',
    description='Shared models for FX Backend',
    long_description='Shared models package containing Customer and System Settings models for FX Backend',
    url='https://github.com/fxbackend/fx_shared_models',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Framework :: Django',
    ],
) 