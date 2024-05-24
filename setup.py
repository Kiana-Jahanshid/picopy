# we can use a package with its setup.py file

# this setuptools package help us to install other package 
from setuptools import setup
from pathlib import Path


def pre_install():
    #f = open("README.md" , "r")
    #text = f.read()
    this_directory = Path(__file__).parent
    long_description = (this_directory / "README.md").read_text()    
    return long_description

with open('./requirements.txt') as f:
    install_requires = f.read().splitlines()


setup(name="picopy" ,
    version="1.0.11", 
    author="kiki js" , 
    description="convert an image to a watercolor image 🎨", 
    long_description=pre_install() ,
    requires= [] ,
    author_email="k.jhnshid@gmail.com",
    packages=["picopy"] ,
    long_description_content_type='text/markdown' ,
    install_requires= install_requires ,
    url="https://github.com/Kiana-Jahanshid/picopy" ,
    entry_points={"console_scripts": ["picopy=picopy.picopy:convert_image_to_watercolor"]},
    include_package_data=True
    )


