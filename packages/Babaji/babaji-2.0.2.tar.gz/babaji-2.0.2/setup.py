from setuptools import setup, find_packages

setup(
    name='Babaji',
    version='2.0.2',
    author='Nachiket Shinde',
    author_email='nachiketshinde@gmail.com',
    description='A package in which various of Pretrain models are implemented.',
    long_description='Babaji is a lightweight Python library designed to simplify predictions using pre-trained machine learning models. With its user-friendly interface, Babaji enables developers and enthusiasts to integrate predictive analytics into projects with minimal effort.',
    url='https://github.com/PyBabaji',  # Replace with your GitHub repo link
    packages=find_packages(),
    install_requires=[
        'scikit-learn',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
