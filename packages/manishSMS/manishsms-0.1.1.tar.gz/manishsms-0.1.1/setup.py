from setuptools import setup, find_packages

setup(
    name='manishSMS',
    version='0.1.1',
    author='Manish Prasad',
    author_email='m4manishp4prasad@gmail.com.com',
    description='A School Management System',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/Manish-Let-It-Be/manishSMS',  
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'start=manishSMS.sms:main',  
        ],
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',  
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
