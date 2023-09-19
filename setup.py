from setuptools import find_packages, setup

setup(
    name="GreyCat",
    version="0.0.0",
    author="DataThings S.A.",
    author_email="contact@datathings.com",
    license="https://www.apache.org/licenses/LICENSE-2.0.html",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    python_requires=">=3.8",
    extras_require={
        "numpy": ["numpy"],
        "pandas": ["numpy", "pandas"],
    },
)
