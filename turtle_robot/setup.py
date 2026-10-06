"""turtle_robot 패키지 설치 설정입니다."""

from setuptools import find_packages, setup

package_name = 'turtle_robot'

exercise_lessons = [
    'lesson_01_pose_subscriber',
    'lesson_02_color_subscriber',
    'lesson_03_pose_color_subscriber',
    'lesson_04_pose_color_velocity_subscriber',
    'lesson_05_cmd_vel_publisher',
    'lesson_06_turtle_cmd_and_pose',
    'lesson_08_teleport_client',
    'lesson_09_spawn_client',
    'lesson_10_region_pen_client',
    'lesson_11_named_turtle_controller',
    'lesson_12_distance_guard',
]

solution_lessons = [
    'lesson_01_pose_subscriber',
    'lesson_02_color_subscriber',
    'lesson_03_pose_color_subscriber',
    'lesson_04_pose_color_velocity_subscriber',
    'lesson_05_cmd_vel_publisher',
    'lesson_05_growing_circle',
    'lesson_06_turtle_cmd_and_pose',
    'lesson_07_multi_thread',
    'lesson_08_teleport_client',
    'lesson_09_spawn_client',
    'lesson_10_region_pen_client',
    'lesson_11_named_turtle_controller',
    'lesson_12_distance_guard',
]

setup(
    name=package_name,
    version='0.1.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages', ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml', 'README.md']),
        ('share/' + package_name + '/docs', ['docs/lessons.md']),
    ],
    install_requires=['setuptools'],
    tests_require=['pytest'],
    zip_safe=True,
    maintainer='Instructor',
    maintainer_email='instructor@example.com',
    description='Topic and service exercises with turtlesim',
    license='Apache-2.0',
    entry_points={
        'console_scripts': [
            f'{lesson} = turtle_robot.exercises.{lesson}:main'
            for lesson in exercise_lessons
        ] + [
            f'{lesson}_solution = turtle_robot.solutions.{lesson}:main'
            for lesson in solution_lessons
        ],
    },
)
