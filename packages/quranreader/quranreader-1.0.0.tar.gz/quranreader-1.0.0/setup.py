from setuptools import setup, find_packages

# Lire le README.md pour la description longue
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()
required = [
    "requests==2.32.3",
]

setup(
    name='quranreader',
    version='1.0.0',
    packages=find_packages(),
    install_requires=required,
    description='QuranReader: Package pour gérer les sourates et le coran',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="personne monsieur",
    author_email="monsieurnobody01@gmail.com",
    url='https://gitlab.com/misternobody01/package_muslimdeen.git',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
    include_package_data=True
)
