from setuptools import setup, find_packages

setup(
    name="testliblockingcdt",
    version="0.1.10",
    description="Custom library to support table locking",
    author="Javad Javadzade",
    author_email="JavadJavadzade@LiveNation.com",
    packages=find_packages(where="testliblockingcdt"),
    include_package_data=True,
    zip_safe=False,
)