from setuptools import setup

setup(name='selendroid_app_ui',
      version='0.1',
      description='selendroid app ui wrapper',
      author='Vladimir Tsyuman',
      author_email='vladimir.tsyuman@gmail.com',
      install_requires=['Appium-Python-Client', 'inject', 'pytest', 'waiting', 'allure-pytest'],
      packages=['selendroid_app_ui'],
      entry_points={"pytest11": ["selendroid_app_ui = selendroid_app_ui.pytest_plugin"]},
      # custom PyPI classifier for pytest plugins
      classifiers=["Framework :: Pytest"],
      )
