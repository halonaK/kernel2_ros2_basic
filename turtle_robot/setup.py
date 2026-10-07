"""turtle_robot 패키지 설치 설정입니다."""

from setuptools import find_packages, setup

package_name = 'turtle_robot'

exercise_lessons = [
    'lesson1_1_pose_subscriber',
    'lesson1_2_color_subscriber',
    'lesson1_3_pose_color_subscriber',
    'lesson1_4_pose_color_velocity_subscriber',
    'lesson2_1_cmd_vel_publisher',
    'lesson2_2_growing_circle',
    'lesson2_3_turtle_cmd_and_pose',
    'lesson2_4_multi_thread',
    'lesson3_1_teleport_client',
    'lesson3_2_spawn_client',
    'lesson3_3_region_pen_client',
    'lesson4_1_cmd_vel_parameters',
]

setup(
    name=package_name,
    version='0.1.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        (
            'share/ament_index/resource_index/packages',
            ['resource/' + package_name],
        ),
        ('share/' + package_name, ['package.xml', 'README.md']),
    ],
    install_requires=['setuptools'],
    tests_require=['pytest'],
    zip_safe=True,
    maintainer='Instructor',
    maintainer_email='instructor@example.com',
    description='ROS 2 topic, service, parameter, and launch lessons',
    license='Apache-2.0',
    entry_points={
        'console_scripts': [
            f'{lesson} = turtle_robot.exercises.{lesson}:main'
            for lesson in exercise_lessons
        ],
    },
)
