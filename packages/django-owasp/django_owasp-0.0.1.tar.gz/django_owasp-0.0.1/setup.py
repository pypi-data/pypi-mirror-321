from setuptools import setup, find_packages


setup(
    name="django-owasp",
    version="0.0.1",
    description="Placeholder for django-owasp package",
    author="Tyrone Software",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[],
    classifiers=[
        "Framework :: Django",
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
)