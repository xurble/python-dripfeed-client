import setuptools


with open('readme.md', encoding='utf-8') as f:
    long_description = f.read()


setuptools.setup(
    name='dripfeed-client',
    version='0.0.2',
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
    ],
    install_requires=[
        'requests',
    ],
    include_package_data=True,
)
