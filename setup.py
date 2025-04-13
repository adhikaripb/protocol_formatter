from setuptools import setup, find_packages

setup(
    name="protocol_formatter",
    version="0.1.3",
    packages=find_packages(),
    entry_points={"console_scripts": ["protocol_formatter=protocol_formatter.__main__:main"]},
    include_package_data=True,
    install_requires=[
        "python-docx",
        "fpdf",
        "svgwrite",
        "cairosvg",
    ],
    package_data={
        "protocol_formatter": ["*.png"],
    },
)
