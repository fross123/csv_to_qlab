from setuptools import setup, find_packages
from pathlib import Path

# Read the README file
readme_file = Path(__file__).parent / "README.md"
long_description = readme_file.read_text() if readme_file.exists() else ""

# Core dependencies (required for CLI)
install_requires = [
    'python-osc>=1.8.3',
]

# GUI-specific dependencies (optional)
gui_requires = [
    'Flask>=3.0.3',
    'pywebview>=5.1',
]

# Development and testing dependencies
dev_requires = [
    'pytest>=8.0.0',
    'pytest-cov>=4.1.0',
]

setup(
    name='csv-to-qlab',
    version='2025.1',
    description='Send CSV files to QLab via OSC',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Finlay Ross',
    url='https://github.com/fross123/csv_to_qlab',
    packages=['app'],
    package_data={
        'app': [
            'qlab_osc_config.json',
            'static/**/*',
            'templates/**/*',
        ],
    },
    include_package_data=True,
    install_requires=install_requires,
    extras_require={
        'gui': gui_requires,
        'dev': dev_requires,
        'all': gui_requires + dev_requires,
    },
    entry_points={
        'console_scripts': [
            'csv-to-qlab=app.cli:main',
        ],
    },
    python_requires='>=3.8',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Intended Audience :: End Users/Desktop',
        'Topic :: Multimedia :: Sound/Audio',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Programming Language :: Python :: 3.13',
    ],
    keywords='qlab osc csv automation theatre theater sound lighting',
)
