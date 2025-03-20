from setuptools import find_packages, setup

setup(
    name="GreyCat",
    version="0.0.0",
    author="DataThings S.A.",
    author_email="contact@datathings.com",
    license="https://www.apache.org/licenses/LICENSE-2.0.html",
    package_dir={"": "."},
    packages=find_packages(where="."),
    python_requires=">=3.9",
    install_requires=["numpy>=2.1"],
    extras_require={
        "pandas": ["pandas>=2.0,<3"],
        "tensorflow": ["tensorflow>=2.13.1,<3"],
        "torch": ["torch>=2.1,<3"],
    },
)
