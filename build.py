from setuptools import setup, Extension

# This dummy extension will force a binary wheel
dummy_ext = Extension(
    'lawyer._dummy',
    sources=['src/lawyer/dummy.c'],
)

setup(
    ext_modules=[dummy_ext],
)