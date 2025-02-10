import setuptools
with open("README.md","r",encoding="utf-8") as f:
    long_description=f.read()
__version__="0.0.0"
REPO_NAME="Text-Summarizer" 
AUTHO_USER_NAME="secretly_Unhinged"
SRC_REPO="textSummarizer"
AUTHOR_EMAIL="jyotirmoyee03@gmail.com"

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHO_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small python package for NLP app",
    Long_description=long_description,
    Long_description_content="text/markdown",
    url=f"https://github.com/secretlyUnhinged/Text-Summarizer",
    project_urls={
        "Bug Tracker":f"https://github.com/secretlyUnhinged/Text-Summarizer/issues",

    },
    package_dir={"":"src"},
    packages=setuptools.find_packages(where="src")


)