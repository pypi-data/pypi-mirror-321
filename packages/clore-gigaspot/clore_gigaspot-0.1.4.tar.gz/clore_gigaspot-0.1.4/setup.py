from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='clore_gigaspot',
    version='0.1.4',
    packages=find_packages(),
    package_dir={"clore_gigaspot": "clore_gigaspot"},
    install_requires=[
        "requests==2.32.3",
        "aiohttp==3.11.11"
    ],
    author='CLORE.AI',
    author_email='marketing@clore.ai',
    description='GigaSPOT managment library',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',  # License type
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.9',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://gitlab.com/cloreai-public/gigaspot-python-sdk'
)