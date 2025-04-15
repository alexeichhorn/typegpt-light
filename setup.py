import setuptools

with open("README.md", "r") as f:
    long_description = f.read()

setuptools.setup(
    name="typegpt_light",
    version="0.0.4",
    author="Alexander Eichhorn",
    author_email="",
    description="TypeGPT Light is a reduced version of TypeGPT that uses OpenAI's built-in strucutred output, but keeps some nice architecture features of TypeGPT.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/alexeichhorn/typegpt",
    install_requires=[
        "typing_extensions>=4.1.0",
        "openai>=1.40.0",
    ],
    packages=setuptools.find_packages(),
    classifiers=["Programming Language :: Python :: 3", "License :: OSI Approved :: MIT License", "Operating System :: OS Independent"],
    python_requires=">=3.10",
)
