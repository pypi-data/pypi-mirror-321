from setuptools import setup, find_packages
with open("README.md", "r", encoding="utf-8") as fh: 
    long_description = fh.read()
setup(
    name='topsispackage3280',
    version='0.3',
    packages=find_packages(),
    install_requires=[
        'numpy',
        'pandas',
    ],
    author='Bhumika Tandon',
    author_email='bhumii2114@gmail.com',
    description='A TOPSIS implementation package',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/bhumiii2114/topsis_package',
)
