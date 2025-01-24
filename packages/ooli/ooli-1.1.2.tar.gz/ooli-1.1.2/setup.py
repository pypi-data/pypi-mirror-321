from setuptools import setup, find_packages

setup(
    name="ooli",
    version="1.1.2",
    author="Jina",
    description="A tool for scanning APK Smali files for keywords.",
    packages=find_packages(),
    python_requires=">=3.6",
    entry_points={
        "console_scripts": [
            "ooli=ooli.ooli:main",
        ],
    },
)
