from setuptools import setup, find_packages

setup(
    name="createsend",
    version='9.0.2',
    description="A library which implements the complete functionality of the Campaign Monitor API.",
    author='Campaign Monitor',
    author_email='support@campaignmonitor.com',
    url="http://campaignmonitor.github.io/createsend-python/",
    license="MIT",
    keywords="createsend campaign monitor email",
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
        "Programming Language :: Python :: 3",

        # Specifically, we support the following releases.
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
    ]
)
