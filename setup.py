import codecs
import os
from setuptools import setup, find_packages
from setuptools import setup, find_packages

# these things are needed for the README.md show on pypi (if you dont need delete it)
here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()


VERSION = '1.1.2'
DESCRIPTION = ' A computer vision library that supports Win, packaged with patches for visual libraries such as \
                Opencv, matplotlib, and image. In the future, Pytorch will also be supported, all of which are IPCS team \
                engineering code experience. '
LONG_DESCRIPTION = 'Ipcsvision is a computer vision library that supports Win'

setup(
    name="Ipcsvision",
    version=VERSION,
    author="IPCS",
    author_email='',
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
    license='MIT',
    install_requires=[
        'requests',
        'tqdm',
        'matplotlib',
        'scikit-image',
        'torch',
        'opencv-python',
        'tqdm',
        'torchvision',
        'torchsummary'
    ],
    keywords=['python', 'computer vision', 'Ipcsvision','windows'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Microsoft :: Windows",
    ]
)
