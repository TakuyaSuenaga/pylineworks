from setuptools import setup, find_packages

setup(
    name="pylineworks",
    description="Lineworks API client library",
    url="https://github.com/TakuyaSuenaga/pylineworks",
    author="Takuya Suenaga",
    author_email="takuya.suenaga.dev@gmail.com",
    license="MIT",
    include_package_data=True,
    use_scm_version=True,
    setup_requires=["setuptools_scm", "setuptools_rust"],
    packages=find_packages(exclude=["tests", "tests.*"]),
    install_requires=[
        "requests>=2.20.0,<3.0",
        "PyJWT==2.6.0",
        "cryptography==40.0.2",
    ],
    zip_safe=False,
    keywords=["lineworks"],
    classifiers=[
        "Intended Audience :: Developers",
        "Development Status :: 3 - Alpha",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
)
