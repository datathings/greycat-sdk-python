from setuptools import find_packages, setup

setup(
    name="GreyCat",
    version="0.0.0",
    author="DataThings S.A.",
    author_email="contact@datathings.com",
    license="https://www.apache.org/licenses/LICENSE-2.0.html",
    package_dir={"": "."},
    packages=find_packages(where="."),
    python_requires=">=3.8",
    install_requires=["numpy>=1.24,<2.0"],
    extras_require={
        "pandas": ["pandas"],
        "tensorflow": ["tensorflow"],
        "torch": ["torch"],
    },
)
