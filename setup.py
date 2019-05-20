import codecs
import io
import os
import re
import sys
import webbrowser
import platform

try:
    from setuptools import setup
except:
    from distutils.core import setup


NAME = "quantaxis_eventbus"
"""
名字，一般放你包的名字即可
"""
PACKAGES = ["QAEventBus"]
"""
包含的包，可以多个，这是一个列表
"""

DESCRIPTION = "QUANTAXIS REALTIME: QUANTAXIS REALTIME RESOLUTION"
KEYWORDS = ["quantaxis", "quant", "finance", "Backtest", 'Framework']
AUTHOR_EMAIL = "yutiansut@qq.com"
AUTHOR = 'yutiansut'
URL = "https://github.com/yutiansut/QUANTAXIS_EVENTBUS"


LICENSE = "MIT"

setup(
    name=NAME,
    version='2.5',
    description=DESCRIPTION,
    long_description='EventBus for publisher/subscriber',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
    ],
    install_requires=['pika>1.0.0', 'quantaxis', 'janus'],
    # entry_points={
    #     'console_scripts': [
    #         'qareal=QAREALTIME.__init__:bat_start',
    #         'qarealx=QAREALTIME.__init__:bat_simnow24',
    #         'qatrade=QAREALTIME.__init__:bat_trade',
    #         'qasim=QAREALTIME.__init__:bat_sim',
    #         'qasimnow=QAREALTIME.__init__:bat_simnow',
    #         'qasimX=QAREALTIME.__init__:single_sim',
    #         'qatradeX=QAREALTIME.__init__:single_trade'
    #     ]
    # },
    keywords=KEYWORDS,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    url=URL,
    license=LICENSE,
    packages=PACKAGES,
    include_package_data=True,
    zip_safe=True
)
