from setuptools import setup, find_packages
setup(
    name='sahani_tts',
    version='1.0.0',
    description='A simple TTS package',
    author='Sahani',
    author_email='sahaniaryan321@gmail.com',
)

packages = find_packages(),

install_requirements = [
    'requests',
    'playsound',
    'typing',
    'sys',
    'time',
    'threading'
]