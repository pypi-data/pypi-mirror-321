from setuptools import find_packages, setup


extras_test = [
    "hypothesis",
    "ruff",
    "pyproj",
    "pytest",
    "pytest-cov",
    "pytest-asyncio",
    "tox",
    "build",
]


setup(
    name="ton_message_body_decoder",
    keywords=[
        "cryptocurrency",
        "ton",
    ],
    use_scm_version=True,
    description="ton_message_body_decoder",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    packages=find_packages(exclude=("tests", "scripts", "examples", "docs")),
    package_data={
        "ton_message_body_decoder": ["py.typed"],
    },
    setup_requires=[
        "setuptools_scm",
    ],
    install_requires=[
        "pytoniq_core",
    ],
    extras_require={
        "test": extras_test,
    },
    url="https://github.com/Grommash9/ton_message_body_decoder",
    project_urls={
        "Documentation": "https://grommash9.github.io/ton_message_body_decoder/",
        "Source": "https://github.com/Grommash9/ton_message_body_decoder",
    },
    author="Oleksandr Prudnikov",
    author_email="prudnikov21@icloud.com",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
    ],
)
