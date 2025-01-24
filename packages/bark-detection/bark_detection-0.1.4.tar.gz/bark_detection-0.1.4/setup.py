from setuptools import setup, find_packages

VERSION = '0.1.4'
DESCRIPTION = 'Package for bark detection in audio file'

# Setting up
setup(
    name="bark_detection",
    version=VERSION,
    author="jgab",
    #author_email="<mail@neuralnine.com>",
    description=DESCRIPTION,
    packages=find_packages(),
    package_data={'bark_detection': ['model/wdog_trained.h5']},
    install_requires=['numpy==1.24.3','pandas==2.0.3','tensorflow==2.13.0','librosa==0.10.2.post1','matplotlib==3.7.3','pillow==10.1.0'], # 'tensorflow-io-gcs-filesystem==0.34.0'
    keywords=['python', 'ML', 'bark', 'detection'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Programming Language :: Python :: 3",
    ]
)