from setuptools import setup, find_packages


setup(
    name = "ca.disposable_email_checker",
    version='1.0',
    packages = find_packages(),
    author = "Giacomo Marinangeli",
    author_email = "giacomo@cloudacademy.com",
    description = "Python class to detect Disposable Emails - Based on "
                  "https://github.com/aaronbassett/DisposableEmailChecker",
    license = "MIT License",
    keywords = "email disposable validation",
    url = "https://github.com/cloudacademy/DisposableEmailChecker",
    
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 2 :: Only',
    ]
)
