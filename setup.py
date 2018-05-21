from setuptools import setup, find_packages

setup(
    name="createsend",
    version='6.0.0',
    description="A library which implements the complete functionality of the Campaign Monitor API.",
    author='Campaign Monitor',
    author_email='support@campaignmonitor.com',
    url="http://campaignmonitor.github.io/createsend-python/",
    license="MIT",
    keywords="createsend campaign monitor email",
    install_requires=[
        'six>=1.10',
    ],
    test_suite='test',
    packages=find_packages('lib'),
    package_dir={'': 'lib'},
    package_data={'': ['cacert.pem']},

    classifiers=[
        "Development Status :: 5 - Production/Stable",

        # Who and what the project is for
        "Intended Audience :: Developers",
        "Topic :: Communications",
        "Topic :: Communications :: Email",
        "Topic :: Communications :: Email :: Mailing List Servers",
        "Topic :: Internet",
        "Topic :: Software Development :: Libraries",

        # License classifiers
        "License :: OSI Approved :: MIT License",
        "License :: DFSG approved",
        "License :: OSI Approved",

        # Generally, we support the following.
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",

        # Specifically, we support the following releases.
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.0",
        "Programming Language :: Python :: 3.1",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
    ]
)
