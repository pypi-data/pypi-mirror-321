from distutils.core import setup

setup(
    # How you named your package folder (MyLib)
    name='Topsis-Ashmit-102203790',
    packages=['Topsis-Ashmit-102203790'],   # Chose the same as "name"
    version='0.1',      # Start with a small number and increase it with every change you make
    # Chose a license from here: https://help.github.com/articles/licensing-a-repository
    license='MIT',
    # Give a short description about your library
    description='A python class to implement Topsis',
    author='Ashmit Thawait',                   # Type in your name
    author_email='ashmitthawait2@gmail.com',      # Type in your E-Mail
    # Provide either the link to your github or to your website
    url='https://github.com/ashmit0920/Topsis-Ashmit-102203790',
    download_url='https://github.com/ashmit0920/Topsis-Ashmit-102203790/archive/refs/tags/v0.1.tar.gz',
    keywords=['Topsis', 'CLI tool'],   # Keywords that define your package best
    install_requires=[
        'validators',
        'pandas',
        'numpy',
        'sys',
    ],
    classifiers=[
        # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
        'Development Status :: 3 - Alpha',
        # Define that your audience are developers
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',   # Again, pick a license
        # Specify which pyhton versions that you want to support
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Programming Language :: Python :: 3.13',
    ],
)
