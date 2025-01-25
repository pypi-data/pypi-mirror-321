from distutils.core import setup
setup(
  name = 'Topsis-Tanisha-102203340',         # How you named your package folder (MyLib)
  packages = ['topsis'],   # Chose the same as "name"
  version = '0.1',      # Start with a small number and increase it with every change you make
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'A Python package to perform TOPSIS analysis',   # Give a short description about your library
  author = 'Tanisha Ahuja',                   # Type in your name
  author_email = 'tanishaahuja666@gmail.com',      # Type in your E-Mail
  url = 'https://github.com/tanisha0016/Topsis-Tanisha-102203340',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/tanisha0016/Topsis-Tanisha-102203340/releases/tag/v_01',    # I explain this later on
  long_description=open("README.md").read(),
  long_description_content_type="text/markdown",
  install_requires=[            # I get to this in a second
          'pandas',
          'numpy',
      ],
  entry_points={
        'console_scripts': [
            'topsis=Topsis.topsis:main',  # Entry point for CLI usage
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
