# turtle_robot: ROS 2 기초 실습

Ubuntu 24.04와 ROS 2 Jazzy용 수업입니다. 이 브랜치에는 완성 코드와
Launch, config, Challenge만 제공합니다.

## 수업 순서

| 단원 | 주제 | 파일 |
| --- | --- | --- |
| 1 | Topic Subscribe | `lesson1_1` ~ `lesson1_4` |
| 2 | Topic Publish | `lesson2_1` ~ `lesson2_4` |
| 3 | Service | `lesson3_1` ~ `lesson3_3` |
| 4 | Parameter | `lesson4_1` |
| 5 | Launch | `lesson5_1` ~ `lesson5_3` |
| Challenge | 두 거북이 거리 안전 제어 | `challenge_01` |

## 환경 준비

Ubuntu 24.04에서 [ROS 2 Jazzy 공식 Ubuntu 설치 안내](https://docs.ros.org/en/jazzy/Installation/Ubuntu-Install-Debs.html)에
따라 locale, Ubuntu Universe, ROS 저장소를 먼저 설정합니다. 저장소 설정 후:

```bash
sudo apt update
sudo apt install ros-jazzy-desktop ros-jazzy-turtlesim ros-dev-tools
source /opt/ros/jazzy/setup.bash
```

`rosdep` 초기화는 컴퓨터에서 최초 한 번만 합니다. 이미 초기화되어 있으면
`sudo rosdep init`을 반복하지 않습니다. `rosdep update`는 일반 사용자로 실행합니다.

```bash
sudo rosdep init  # 최초 한 번만
rosdep update
```

## 빌드와 검사

```bash
source /opt/ros/jazzy/setup.bash
cd ~/ros2_ws
rosdep install --from-paths src --ignore-src -r -y
colcon build --packages-select turtle_robot --symlink-install
source install/setup.bash
colcon test --packages-select turtle_robot
colcon test-result --verbose
python3 -m compileall src/turtle_robot
ament_flake8 src/turtle_robot
ament_pep257 src/turtle_robot
```

일반 테스트는 실행 중인 turtlesim이나 ROS 그래프를 요구하지 않습니다.
ROS 메시지를 import하므로 Jazzy 환경은 먼저 source해야 합니다.
기존 install 폴더에는 예전 실행 파일이 남을 수 있으므로
`ros2 pkg executables turtle_robot`에서 현재 명령을 확인하세요.

## 터미널 구성

새 터미널마다 다음 두 줄을 실행합니다.

```bash
source /opt/ros/jazzy/setup.bash
source ~/ros2_ws/install/setup.bash
```

터미널 A: 시뮬레이터를 실행합니다. 기본 색상 토픽 `/turtle1/color_sensor`를
이번 수업에서 사용하는 `/turtlesim/color_sensor`로 바꿉니다.

```bash
ros2 run turtlesim turtlesim_node --ros-args -r /turtle1/color_sensor:=/turtlesim/color_sensor
```

터미널 B: 키보드로 turtle1을 움직입니다. 방향키를 누를 때 이 터미널에 포커스를 둡니다.

```bash
ros2 run turtlesim turtle_teleop_key
```

터미널 C: 수업에서 안내한 완성 명령을 실행합니다.

`lesson2_1` ~ `lesson2_4`는 turtle1 속도를 자동 발행하므로 터미널 B를 중지하세요.
여러 노드가 `/turtle1/cmd_vel`에 서로 다른 명령을 동시에 보내면 움직임이 충돌합니다.
같은 토픽에 명령을 보내는 완성 예제를 동시에 실행하지 않습니다.

## 완성본 실행 이름

완성 코드는 학생 실행 이름 뒤에 `_solution`을 붙입니다.

```bash
ros2 run turtle_robot lesson2_1_cmd_vel_publisher_solution
ros2 run turtle_robot lesson3_1_teleport_client_solution
ros2 run turtle_robot lesson4_1_cmd_vel_parameters_solution
ros2 launch turtle_robot lesson5_1_turtlesim_teleop.launch.py
```

## core20 / GLIBC_PRIVATE 문제

`libpthread.so.0` 또는 `GLIBC_PRIVATE` 오류와 `/snap/core20/` 경로가 보이면
호스트 또는 Snap 실행 환경의 라이브러리 충돌입니다. 패키지의 Python 코드 오류와
구분해야 합니다. 시스템 라이브러리를 삭제하거나 교체하지 마세요.
Snap IDE의 내장 터미널을 벗어나 일반 Ubuntu 터미널에서 ROS 환경을 source한 뒤
터미널 A 명령으로 turtlesim을 실행하세요. 라이브 검증은 그 환경에서 수행합니다.
