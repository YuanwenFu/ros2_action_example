from setuptools import find_packages, setup

package_name = 'fibonacci_action_demo'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='fuyuanwen',
    maintainer_email='yuanwenfu98@163.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
            'action_server = fibonacci_action_demo.action_server:main',
            'action_client = fibonacci_action_demo.action_client:main'
        ],
    },
)
