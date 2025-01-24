from setuptools import setup, find_packages

setup(
    name='spaceone-dashboard-gen',
    version='0.0.2',
    packages=find_packages(),
    install_requires=[
        'fastapi',
        'uvicorn',
        'pydantic',
        'pyyaml',
        'jinja2'
    ],
    author='seolmin',
    author_email='seolmin@megazone.com',
    description='A dashboard generator using FastAPI',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/yourusername/spaceone-dashboard-gen',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.8',
    entry_points={
        'console_scripts': [
            'dashboard-gen=spaceone_dashboard_gen.dashboard_generator.main:app',
        ],
    },
)