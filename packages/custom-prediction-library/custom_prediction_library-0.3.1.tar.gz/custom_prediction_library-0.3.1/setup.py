from setuptools import setup, find_packages

# Read the README.md file for the long description
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="custom_prediction_library",
    version="0.3.1",
    packages=find_packages(),
    install_requires=[
        "scikit-learn",
        "optuna",
        "bayesian-optimization",
        "numpy",
        "pandas",
        "statsmodels",
        "bokeh",
    ],
    description="A custom prediction library with automated hyperparameter tuning, training utilities, exponential smoothing, and visualisation.",
    long_description=long_description,  # Include the README content
    long_description_content_type="text/markdown",  # Specify the content type
    author="JKEEPS",
    author_email="your.email@example.com",
    license="MIT",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
    python_requires=">=3.6",
)
