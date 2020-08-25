import setuptools

setuptools.setup(
    name="MTGNN",
    version="0.1",
    author="Anonymous",
    author_email="author@example.com",
    description="MTGNN package",
    long_description="Some long description",
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    install_requires = [
        "matplotlib",
        "numpy",
        "pandas",
        "scipy",
        "torch",
        "scikit_learn"
    ]
)