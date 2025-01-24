from setuptools import setup, find_packages

setup(
    name="SentimentAnalysisDarijaNZ",  
    version="0.3.2",                 
    author="Nawfal BENHAMDANE",
    author_email="benhamdane2003@gmail.com",
    description="C'est une bibliothèque Python modulaire qui fournit des outils pour le calcul de similarité, le filtrage de données, et l'analyse de sentiments.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/Benhamdane/SentimentAnalysisDarijaNZ",  
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
