# turtle_robot: ROS 2 기초 실습

Ubuntu 24.04와 ROS 2 Jazzy용 수업입니다. 학생 코드는 `turtle_robot/exercises/`,
완성 코드는 `turtle_robot/solutions/`에 있습니다. 각 폴더의 같은 파일이 한 쌍입니다.

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
예전 명령 대신 `lesson_` 명령을 사용합니다. 기존 install 폴더에는 예전 실행 파일이
남을 수 있으므로 `ros2 pkg executables turtle_robot`에서 확인하세요.

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

터미널 C: 수업에서 안내한 실습 또는 완성 명령을 실행합니다.
학생 코드의 `실습 1~3` 주석을 풀고 빈칸을 완성한 뒤 `main()`의 안내용
`raise SystemExit(...)` 줄을 삭제합니다. `pass`는 삭제해도 됩니다.
실행 전에는 짧은 한국어 안내로 종료합니다. 완성 답은 별도 solutions 파일에 있습니다.
의도적으로 남긴 학생 import의 `# noqa: F401`은 미완성 상태의 미사용 import만 허용합니다.

05, 06, 07은 turtle1 속도를 자동 발행하므로 터미널 B를 중지하세요.
여러 노드가 `/turtle1/cmd_vel`에 서로 다른 명령을 동시에 보내면 움직임이 충돌합니다.
학생 버전과 완성 버전도 동시에 실행하지 않습니다. 11과 12 역시 turtle2 제어를
동시에 실행하지 않습니다. 12에서는 turtle1 키보드 제어를 유지합니다.

## core20 / GLIBC_PRIVATE 문제

`libpthread.so.0` 또는 `GLIBC_PRIVATE` 오류와 `/snap/core20/` 경로가 보이면
호스트 또는 Snap 실행 환경의 라이브러리 충돌입니다. 패키지의 Python 코드 오류와
구분해야 합니다. 시스템 라이브러리를 삭제하거나 교체하지 마세요.
Snap IDE의 내장 터미널을 벗어나 일반 Ubuntu 터미널에서 ROS 환경을 source한 뒤
터미널 A 명령으로 turtlesim을 실행하세요. 라이브 검증은 그 환경에서 수행합니다.
