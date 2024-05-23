# we can use a package with its setup.py file

# this setuptools package help us to install other package 
from setuptools import setup


def pre_install():
    #f = open("readme.md" , "r")
    text = "picopy package" #f.read()
    return text

setup(name="picopy" ,
      version="1.0.1", 
      author="kiki js" , 
      description="convert image to watercolor", 
      long_description=pre_install() , # its like readme
      requires= [] ,
      author_email="k.jhnshid@gmail.com",
      packages=["picopy"]
      )


