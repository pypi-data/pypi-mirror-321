from setuptools import setup, find_packages

setup(
    name="azure-genai-utils",
    version="0.0.1",
    description="Azure GenAI utils",
    url="https://github.com/daekeun-ml/azure-genai-utils",
    install_requires=[
        "langchain",
        "langgraph",
    ],
    packages=find_packages(exclude=[]),
    keywords=[
        "langchain",
        "langgraph",
    ],
    python_requires=">=3.8",
    package_data={},
    zip_safe=False,
    classifiers=[
        "Programming Language :: Python :: 3",
    ],
)
