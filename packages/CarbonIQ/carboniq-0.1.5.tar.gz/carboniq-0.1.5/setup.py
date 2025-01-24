from setuptools import setup, find_packages

setup(
    name="CarbonIQ",
    version="0.1.5",
    author="Md Ashikur Rahman",
    author_email="mdashikur.rafi@gmail.com",
    description="A Python package that monitors and tracks the carbon emissions of scripts and applications. It provides insights into the environmental impact of code by analyzing resource usage such as CPU, memory, disk I/O, network, and GPU utilization.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/ashikrafi/CarbonIQ",
    packages=find_packages(),
    install_requires=[
        "pynvml",
        "psutil"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    entry_points={
        "console_scripts": [
            "carboniq=carboniq.__main__:main",  # CLI entry point (if applicable)
        ],
    },
    include_package_data=True,
)
