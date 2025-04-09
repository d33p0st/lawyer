from setuptools import setup, find_packages

setup(
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    package_data={"lawyer": ["*.so", "*.pyd", "*.dylib"]},
    include_package_data=True,
    # Forces platform-specific wheel
    options={
        "bdist_wheel": {
            "universal": False,
            "py_limited_api": False,
        }
    },
)