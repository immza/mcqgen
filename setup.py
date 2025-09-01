from setuptools import setup, find_packages

setup(
    name='mcqgenerator',
    version='0.0.1',
    author='mz ayan',
    author_email='moinuddinzubair26@gmail.com',
    install_requires=["openai","langchain","streamlit","python-dotenv","PyPDF2"],
    packages=find_packages()
)