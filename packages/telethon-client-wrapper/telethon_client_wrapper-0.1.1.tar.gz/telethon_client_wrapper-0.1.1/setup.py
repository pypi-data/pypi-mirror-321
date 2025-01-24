from setuptools import setup, find_packages

setup(
    name='telethon_client_wrapper',
    version='0.1.1',
    packages=find_packages(),
    install_requires=[
        'telethon',
    ],
    entry_points={
        'console_scripts': [
            'telegram_client_wrapper=telegram_client_wrapper.client:create_client',
        ],
    },
    author='Ray',
    description='A simple Telegram (telethon) client wrapper',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/Rerowros/telethon_client_wrapper',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)