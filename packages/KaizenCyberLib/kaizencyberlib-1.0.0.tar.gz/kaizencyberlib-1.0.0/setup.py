from setuptools import setup, find_packages

setup(
    name="KaizenCyberLib",  # Nom de votre package
    version="1.0.0",  # Numéro de version
    description="Une bibliothèque Python pour la cybersécurité et les tests éthiques.",
    long_description=open("README.md", "r", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    author="Votre Nom",
    author_email="votre.email@example.com",
    url="https://github.com/votre_github/KaizenCyberLib",  # URL du repo GitHub
    license="MIT",
    packages=find_packages(),
    install_requires=[
        "requests",
        "scapy",
        "pytest",
        "pytest-mock","whois"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Security",
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
    ],
    python_requires=">=3.7",
)
