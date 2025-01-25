from setuptools import setup, find_packages

setup(
    name='Topsis-Yuvika-102203800',
    version='0.3',
    author='Yuvika',
    author_email='yuvikasardana@gmail.com',
    long_description=open('README.md').read(),  # Optional: Load description from a README file
    long_description_content_type='text/markdown',  # Or 'text/x-rst' for reStructuredText,
    packages=find_packages(),
    install_requires=['pandas', 'numpy'],
    entry_points={
        'console_scripts': [
            'topsis = Topsis_Yuvika_102203800.cli:main',
        ],
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
