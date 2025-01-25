from setuptools import setup, find_packages

setup(
    name="my_ai_framework",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "transformers",
        "flask"
    ],
    entry_points={
        "console_scripts": [
            "qna_bot=examples.qna_bot:main",
        ]
    },
)
