from setuptools import setup, find_packages

setup(
    name="stack_builder",
    version="0.1.0",
    description="A tool to generate project foundations like Dockerfile, composefile, setup database, ... using Docker",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    author="informatiako groups",
    author_email="ankoayfeno@gmail.com",
    url="https://gitlab.com/internship4450447/informatiako",
    packages=find_packages(),  # Trouve tous les sous-packages
    include_package_data=True,
    install_requires=[
        "click",
        "jinja2",
        "pyyaml",
    ],
    entry_points={
        "console_scripts": [
            "stack_builder=source_code.stack_builder:generate_project",  # Point d'entrée CLI
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
)
