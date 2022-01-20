from setuptools import setup


extra = {}
setup(
    name="html2bbcode3",
    version="3.0.0",
    packages=["html2bbcode3"],
    url="https://github.com/issaccv/html2bbcode3",
    license="BSD",
    author="issaccv",
    author_email="8qllyhy@gmail.com",
    description="HTML to BBCode converter for Python 3",
    package_data={"html2bbcode": ["data/defaults.conf"]},
    classifiers=[
        "Topic :: Utilities",
        "Topic :: Text Processing :: Markup :: HTML",
        "License :: OSI Approved :: BSD License",
        "Programming Language :: Python :: 3",
    ],
    **extra,
)
