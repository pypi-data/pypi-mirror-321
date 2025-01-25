from setuptools import setup, find_packages

setup(
    name="multi-process-manager",
    version="1.5.0",
    description="Gestionnaire de processus pour python",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Younity MC",
    author_email="contact@younity-mc.fr",
    url="https://github.com/Younity-MC/python-process-manager",
    packages=find_packages(),
    install_requires=[],
    classifiers=[
        "License :: OSI Approved :: MIT License",
    ],
    python_requires='>=3.11',
)
