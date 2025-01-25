from setuptools import setup, find_packages

desc = '\n'.join(("Универсальная библиотека python для большинства задач", 'A universal python library for most tasks'))
req = '''soundfile==0.13.0
SpeechRecognition==3.14.0
requests>=2.32.3
screeninfo>=0.8.1
psutil>=6.1.1
bs4==0.0.2
beautifulsoup4==4.12.3
pyodbc==5.2.0'''.split('\n')

setup(
    name='hrenpack',
    version='1.0.0',
    author_email='hrenpack@mail.ru',
    author='Маг Ильяс DOMA (MagIlyas_DOMA)',
    description=desc,  # Описание
    long_description=open('README.md', encoding='utf-8').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/MagIlyas-DOMA/hrenpack',
    packages=find_packages(),
    license=open('LICENSE.md').read(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.10',
    install_requires=req,
    package_data={'hrenpack': ['hrenpack/resources/*']},
    include_package_data=True,
)
