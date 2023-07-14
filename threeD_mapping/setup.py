from setuptools import setup
import os
from glob import glob

package_name = 'threeD_mapping'

setup(

    name=package_name,
    version='0.0.0',
    packages=[package_name],

    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'), glob(os.path.join('launch', '*launch.[pxy][yma]*'))),
    ],
    install_requires=['setuptools'],

    zip_safe=True,

    maintainer='usame_aw',

    maintainer_email='osamasaedawad@gmail.com',

    description='A modified turtlebot3 with some mapping functionalities',

    license='TODO: License declaration',

    tests_require=['pytest'],

    entry_points={
        'console_scripts': [
        
        'rotate_node = threeD_mapping.rotate_node:main'
            
        ],
    },


)
