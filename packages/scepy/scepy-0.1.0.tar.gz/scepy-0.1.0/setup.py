from setuptools import setup, find_packages

setup(
    name="scepy",
    use_scm_version=True,
    author="Ahsan Khodami",
    author_email="ahsan.khodami@gmail.com",
    description="Your package description here",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/AhsanKhodami/scepy",
    project_urls={
        "Bug Tracker": "https://github.com/AhsanKhodami/scepy/issues",
    },
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
    install_requires=[
        # Add your dependencies here
    ],
)
