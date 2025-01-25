import setuptools
setuptools.setup(
 name='topsis_charu',
 version='0.1',
 author="charu garg",
 author_email="gargcharu59@gmail.com",
 description="topsis package made by charu garg",
 packages=setuptools.find_packages(),
 classifiers=[
 "Programming Language :: Python :: 3",
 "License :: OSI Approved :: MIT License",
 "Operating System :: OS Independent",
 ],
)


# $env:TWINE_USERNAME="_token_"
# $env:TWINE_PASSWORD="pypi-AgEIcHlwaS5vcmcCJGZhNDg5YzY4LWI5ZTktNDM1OC1hMzI1LTNkZThkZjgzYmY3NQACKlszLCI5M2U3MWZlMy03ODYzLTRiZjktODIyNy00NjFlMzNhMGZlYTciXQAABiCdUiBL6gT5EXfD5nDk5Lf0VnzQJM1pueEEBlmgV6g58w"
# twine upload --repository pypi dist/*s