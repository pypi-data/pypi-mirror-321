from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="k9crypt",
    version="0.1.0",
    author="K9Crypt",
    author_email="hi@k9crypt.xyz",
    description="A special encryption algorithm created for K9Crypt.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/k9crypt/k9crypt-python",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Security :: Cryptography",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    python_requires=">=3.7",
    install_requires=[
        "cryptography>=41.0.7",
        "brotli>=1.1.0",
    ],
)