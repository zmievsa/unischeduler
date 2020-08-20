from setuptools import setup


requires = [
    'icalendar',
    'bs4',
    'requests'
]

setup(
    name="unischeduler",
    version="0.1.3",
    packages=['unischeduler'],
    install_requires=requires,

    # metadata to display on PyPI
    author="Stanislav Zmiev",
    author_email="szmiev2000@gmail.com",
    description="Converts class schedule from text to an icalendar format to export into any known calendar service (google calendar, apple calendar, outlook calendar, etc)",
    license="MIT",
    project_urls={"Source Code": "https://github.com/Varabe/unischeduler"},
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8'
    ]
)
