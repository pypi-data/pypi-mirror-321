"""

"""

from setuptools import setup, find_packages  # noqa: H301

NAME = "utf-queue-client"
VERSION = "1.17.2"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = [
    "pika >= 1.2.0",
    "jsonschema >= 3.2.0",
    "msgpack >= 1.0.2",
    "pydantic == 1.*",
    "regex",
    "typing_extensions; python_version < '3.8'",
    "click",
    "ubai-client >= 1.2.0",
    "opentelemetry-distro[otlp]",
    "otel-extensions >= 0.1.2",
    "retry>=0.9.2",
    "requests",
    "ndjson~=0.3",
]

setup(
    name=NAME,
    version=VERSION,
    description="",
    author="Joe Savage",
    author_email="joe.savage@silabs.com",
    url="",
    keywords=["UTF", ""],
    python_requires=">=3.6",
    install_requires=REQUIRES,
    packages=find_packages(exclude=["test", "tests"]),
    package_data={
        "utf_queue_client": [
            "models/schemas/utf_queue_models/models/python/*.py",
            "models/schemas/utf_queue_models/schema/*.json",
        ]
    },
    entry_points={
        "console_scripts": [
            "ubai_upload_cli = utf_queue_client.scripts.ubai_upload_cli:cli_entrypoint",
            "ubai_search_cli = utf_queue_client.scripts.ubai_search_cli:cli_entrypoint",
            "publish_test_results_cli = utf_queue_client.scripts.publish_test_results_cli:cli_entrypoint",
            "ubai_update_retention_cli = utf_queue_client.scripts.ubai_update_retention_cli:cli_entrypoint",
            "publish_release_info_cli = utf_queue_client.scripts.publish_release_info_cli:cli_entrypoint",
            "ubai_copy_cli = utf_queue_client.scripts.ubai_copy_cli:cli_entrypoint",
        ],
    },
    include_package_data=True,
    long_description="""\
    No description provided
    """,
)
