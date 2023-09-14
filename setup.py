from setuptools import find_packages, setup

setup(
    name="greycat",
    version="0.0.0",
    author="DataThings S.A.",
    author_email="contact@datathings.com",
    license="https://creativecommons.org/licenses/by-nd/4.0/",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    python_requires=">=3.8",
    extras_require={
      "numpy": ["numpy"],
      "pandas": ["numpy", "pandas"],
    },
)
