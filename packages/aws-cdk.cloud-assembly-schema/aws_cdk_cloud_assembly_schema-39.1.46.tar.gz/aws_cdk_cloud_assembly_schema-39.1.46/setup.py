import json
import setuptools

kwargs = json.loads(
    """
{
    "name": "aws-cdk.cloud-assembly-schema",
    "version": "39.1.46",
    "description": "Cloud Assembly Schema",
    "license": "Apache-2.0",
    "url": "https://github.com/cdklabs/cloud-assembly-schema",
    "long_description_content_type": "text/markdown",
    "author": "Amazon Web Services",
    "bdist_wheel": {
        "universal": true
    },
    "project_urls": {
        "Source": "https://github.com/cdklabs/cloud-assembly-schema.git"
    },
    "package_dir": {
        "": "src"
    },
    "packages": [
        "aws_cdk.cloud_assembly_schema",
        "aws_cdk.cloud_assembly_schema._jsii"
    ],
    "package_data": {
        "aws_cdk.cloud_assembly_schema._jsii": [
            "cloud-assembly-schema@39.1.46.jsii.tgz"
        ],
        "aws_cdk.cloud_assembly_schema": [
            "py.typed"
        ]
    },
    "python_requires": "~=3.8",
    "install_requires": [
        "jsii>=1.106.0, <2.0.0",
        "publication>=0.0.3",
        "typeguard>=2.13.3,<4.3.0"
    ],
    "classifiers": [
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Programming Language :: JavaScript",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Typing :: Typed",
        "Development Status :: 5 - Production/Stable",
        "License :: OSI Approved",
        "Framework :: AWS CDK",
        "Framework :: AWS CDK :: 2"
    ],
    "scripts": []
}
"""
)

with open("README.md", encoding="utf8") as fp:
    kwargs["long_description"] = fp.read()


setuptools.setup(**kwargs)
