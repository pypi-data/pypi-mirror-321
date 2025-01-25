from setuptools import setup, find_packages

setup(
    name="lu77U-SHA256",
    version="1.2.1",
    author="Sam MG Harish (lu77_u)",
    author_email="sammgharish@gmail.com",
    url = "https://github.com/sam-mg/Python-SHA-256-Implementation",
    license="Apache Software License 2.0",
    description="An Fully Manual SHA-256 Hasher",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
    install_requires=["click"],
    entry_points={
        "console_scripts": [
            "lu77U-SHA256 = lu77U_SHA256.Main:main"
        ]
    }
)