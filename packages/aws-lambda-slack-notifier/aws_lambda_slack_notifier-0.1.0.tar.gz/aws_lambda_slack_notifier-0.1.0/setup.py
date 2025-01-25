from setuptools import setup, find_packages

setup(
    name="aws_lambda_slack_notifier",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        'boto3>=1.26.0'
    ],
    author="Vikas",
    author_email="vikasingawale16@gmail.com",
    description="A package to send Slack notifications via AWS Lambda",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    #url="https://github.com/yourusername/aws-slack-notifier",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)