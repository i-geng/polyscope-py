# polyscope-py
Python bindings for TetraPolyscope - Chromalab Version. TetraPolyscope is a fork of Nicholas Sharpe's [Polyscope](https://polyscope.run/py).


This library is a python wrapper and deployment system. The core library/C++ backend lives at [this repository](https://github.com/i-geng/polyscope)

### Installation

#### Install from [PyPI](https://pypi.org/project/tetrapolyscope/).

Use this installation method if you just want to use TetraPolyscope and don't need to add new functionality.

```
pip install tetrapolyscope
```

#### Local Installation

This method requires you to build the C++ backend, but is useful for development and rapid testing.

Uninstall current version of tetrapolyscope from current virtual environment:
```
pip uninstall tetrapolyscope
```

Local installation.
```
git clone --recurse-submodules git@github.com:i-geng/polyscope-py.git
```

From the root polyscope-py directory, build the C++ source:
```
mkdir build; cd build
cmake ../
make -j4
```
Back in the root polyscope-py directory:
```
pip install .
```

To use polyscope's functions for writing videos, you will also need FFmpeg.

### Publishing a New Version of TetraPolyscope

Follow documentation [here](https://polyscope.run/about/contributing/#python-bindings) and [here](https://github.com/nmwsharp/polyscope-py/blob/master/README.md) to use Github Workflow Actions.

- 9/16/24: Unit tests for macOS, Windows, and Linux builds under worklow actions are currently broken after renaming polyscope to tetrapolyscope (needed different name for PyPI upload). Can probably fix this by renaming directory names, but it doesn't affect the PyPI upload and publishing process.
```
python -m pip install polyscope
```

or

```
conda install -c conda-forge polyscope
```

polyscope-py should work out-of-the-box on any combination of Python 3.7-3.12 and Linux/macOS/Windows. Your graphics hardware must support OpenGL >= 3.3 core profile.

## For developers

This repo is configured with CI on github actions. 

- By default, all commits to the main branch build & run tests. Use `[ci skip]` to skip this.
- Tagging a commit with `[ci build]` causes it to also build all precompiled wheels on a matrix of platforms to ensure the build scripts succeed.
- Tagging a commit with `[ci publish]` causes it to build all precompiled wheels on a matrix of platforms AND upload them to pypi index

### Deploy a new version

- Commit the desired version to the `master` branch. Use the `[ci build]` string in the commit message to trigger builds, which should take about an hour.
- Watch the github actions builds to ensure all wheels build successfully. The resulting binaries will be saved as artifacts if you want try test with them.
- While you're waiting, update the docs, including the changelog.
- Update the version string in `setup.py` to the new version number. When you commit, include the string `[ci publish]`, which will kick of a publish job to build wheels again AND upload them to PyPI.
- If something goes wrong with the build & publish, you can manually retry by pushing any new commit with "[ci publish]" in the message.
- Create a github release. Tag the release commit with a tag like `v1.2.3`, matching the version in `setup.py`

- Update the conda builds by committing to the [feedstock repository](https://github.com/conda-forge/polyscope-feedstock). This generally just requires bumping the version number and updating the hash in `meta.yml`. Since `meta.yml` is configured to pull source from PyPi, you can't do this until after the source build has been uploaded from the github action.
