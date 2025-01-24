from setuptools import setup, find_packages

# setup(
#     name="zenduty-api",
#     version="0.2",
#     description="Python SDK wrapper for the Zenduty API",
#     long_description="Python SDK wrapper for the Zenduty API",
#     long_description_content_type="text/x-rst",
#     author="Vishwa Krishnakumar",
#     author_email="vishwa@yellowant.com",
#     packages=find_packages(),
#     install_requires=["urllib3", "six==1.9.0"],
#     scripts=["bin/client.py"],
# )

setup(
    name="zenduty-api",
    version="0.3",
    description="Python SDK wrapper for the Zenduty API",
    long_description="Python SDK wrapper for the Zenduty API",
    long_description_content_type="text/x-rst",
    author="Javeed Yara",
    author_email="javeed@zenduty.com",
    packages=find_packages(),
    install_requires=["urllib3", "six==1.9.0"],
    url="https://github.com/Zenduty/zenduty-python-sdk",
    license="MIT",
    classifiers=[
        "Development Status :: 4 - Beta",  # Update based on your package's status
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",  # Specify Python versions supported
    ],
    python_requires=">=3.6",  # Specify the minimum Python version
    scripts=["bin/client.py"],  # Include any scripts you want to make executable
)
