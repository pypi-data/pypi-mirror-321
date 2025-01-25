from setuptools import setup, find_packages

setup(
    name='api-dfs-wrapper',
    version='0.1.0',
    packages=find_packages(),
    description='DFS Wrapper to easily access DFS Books API',
    install_requires=[
        "certifi==2024.12.14",
        "charset-normalizer==3.4.1",
        "idna==3.10",
        "requests==2.32.3",
        "urllib3==2.3.0"
    ],
)

