# turtle_robot: ROS 2 기초 실습

Ubuntu 24.04와 ROS 2 Jazzy용 수업입니다. 
현재 `main` 브랜치에는 학생이 직접 완성할 실습 파일만 있습니다. 
정답과 Challenge는 `solutions` 브랜치에 있습니다.

## 수업 순서

| 단원 | 주제 | 파일 |
| --- | --- | --- |
| 1 | Topic Subscribe | `lesson1_1` ~ `lesson1_4` |
| 2 | Topic Publish | `lesson2_1` ~ `lesson2_4` |
| 3 | Service | `lesson3_1` ~ `lesson3_3` |
| 4 | Parameter | `lesson4_1` |
| 5 | Launch(수업 중 생성) | `lesson5_1` ~ `lesson5_3` |
| Challenge(`solutions` 전용) | 두 거북이 거리 안전 제어 | `challenge_01` |

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



