from setuptools import setup, find_packages

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="recommendation-engine",
    version="1.0.0",
    description="A full-stack recommendation engine built with FastAPI, React, and PostgreSQL",
    packages=find_packages(),
    install_requires=requirements,
    python_requires=">=3.9",
)
