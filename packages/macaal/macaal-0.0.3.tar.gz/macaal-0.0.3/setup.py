from setuptools import setup, find_packages

setup(
    name="macaal",
    version="0.0.3",
    packages=find_packages(),
        install_requires=[
            # List your dependencies here
        ],
        entry_points={
            'console_scripts': [
                'aal=src.aal:aal',  # Adjust this to your CLI entry point
            ],
        },
        author='Silicon27',
        author_email='yangsilicon@gmail.com',
        description='Auto Assembly Linker - for MacOS M-Series, ARM64',
        long_description=open('README.md').read(),
        long_description_content_type='text/markdown',
        url='https://github.com/Silicon27/aal',
        classifiers=[
            'Programming Language :: Python :: 3',
            'License :: OSI Approved :: MIT License',
            'Operating System :: OS Independent',
        ],
        python_requires='>=3.6',
)