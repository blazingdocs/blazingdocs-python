from setuptools.depends import get_module_constant
from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="blazingdocs",
    packages=find_packages(exclude=["examples"]),
    version=get_module_constant("blazingdocs", "__version__"),
    description="BlazingDocs Python client",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Mentalstack",
    author_email="hello@blazingdocs.com",
    url="https://blazingdocs.com",
    download_url="https://github.com/blazingdocs/blazingdocs-python",
    keywords=["doc", "docx", "pdf", "odt", "report", "document", "template", "office", "openoffice", "merge", "xml", "json", "csv"],
    install_requires=["requests>=2.26.0"],
    python_requires=">=3.4",
    project_urls={
        "Bug Tracker": "https://github.com/blazingdocs/blazingdocs-python/issues",
        "Documentation": "https://docs.blazingdocs.com",
        "Source Code": "https://github.com/blazingdocs/blazingdocs-python",
    },
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Topic :: Software Development :: Libraries :: Python Modules", ],
    license="MIT"
)
