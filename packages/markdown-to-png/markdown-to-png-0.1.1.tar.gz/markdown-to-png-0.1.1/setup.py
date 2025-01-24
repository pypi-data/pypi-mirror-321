from setuptools import setup, find_packages


setup (
    name="markdown-to-png",
    version="0.1.1",
    description="Convert Markdown files to styled PNG images.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Richie",
    author_email="mohammadpagard.dev@gmail.com",
    url="https://github.com/mohammadpagard/markdown-to-png",
    packages=find_packages(),
    include_package_data=True,
    install_required=["markdown", "imgkit"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
