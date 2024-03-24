from setuptools import find_packages, setup

package_name = 'my_robot_controller'

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
    maintainer='AlaikalHamdi',
    maintainer_email='yuan.arib@gmail.com',
    description='Testing',
    license='MIT License',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            "test_node = my_robot_controller.node1:main"
            "draw_circle = my_robot_controller.draw_circle:main"
            "pose_subscriber = my_robot_controller.pose_subcriber:main"
            "twowheels = my_robot_controller.main:main"
        ],
    },
)
