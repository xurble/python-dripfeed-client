import setuptools

with open('README.md', encoding='utf-8') as f:
    long_description = f.read()

setuptools.setup(
    name='dripfeed-client',
    version='0.1.3',
    description='A client for the dripfeed RSS proxy service.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Gareth Simpson',
    author_email='g@xurble.org',
    url='https://github.com/xurble/python-dripfeed-client',
    license='MIT',
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Intended Audience :: Developers",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    install_requires=[
        'requests',
        # Add more dependencies if required
    ],
    include_package_data=True,
)
