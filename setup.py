from setuptools import setup, find_packages

setup(
    name='ccip-read-dns-gateway-python',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'Flask',
        'aiohttp',
        'requests',
        'web3',
        'python-dotenv',
        'unittest',
        'dnspython',
    ],
    entry_points={
        'console_scripts': [
            'ccip-read=app:main',
        ],
    },
)
