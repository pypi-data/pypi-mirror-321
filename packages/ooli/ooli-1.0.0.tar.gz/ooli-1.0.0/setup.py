from setuptools import setup

setup(
    name="ooli",
    version="1.0.0",
    author="Jina",
    description="A tool for scanning APK Smali files for keywords.",
    py_modules=["ooli"],
    entry_points={
        "console_scripts": [
            "ooli=ooli:main",
        ],
    },
    python_requires=">=3.6",
)
