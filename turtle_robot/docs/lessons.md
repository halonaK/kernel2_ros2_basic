# 수업 안내

파일은 모두 `turtle_robot/exercises/<명령>.py`와
`turtle_robot/solutions/<명령>.py`에 있습니다.
01, 03, 05는 함께 작성하고, 02와 04는 각각 학생 과제 1, 2입니다.
모든 수업에 학생용 빈칸 세 곳 이상이 있습니다.

아래 명령 앞에 `ros2 run turtle_robot`을 붙입니다.
예: `ros2 run turtle_robot lesson_01_pose_subscriber_solution`.
터미널 A/B/C와 source 방법은 [README](../README.md)를 따릅니다.

| 순서 | 학생 명령 / 파일명(.py) | 완성 명령 | 예상 결과 |
|---|---|---|---|
| 01 | `lesson_01_pose_subscriber` | `lesson_01_pose_subscriber_solution` | 위치 x, y, theta 출력 |
| 02 | `lesson_02_color_subscriber` | `lesson_02_color_subscriber_solution` | RGB 값 출력 |
| 03 | `lesson_03_pose_color_subscriber` | `lesson_03_pose_color_subscriber_solution` | 위치와 색상을 1초마다 출력 |
| 04 | `lesson_04_pose_color_velocity_subscriber` | `lesson_04_pose_color_velocity_subscriber_solution` | 위치·색상·속도 출력 (키보드 입력 후) |
| 05 | `lesson_05_cmd_vel_publisher` | `lesson_05_cmd_vel_publisher_solution` | 10 Hz 전진, 회전 없음 |
| 06 | `lesson_06_turtle_cmd_and_pose` | `lesson_06_turtle_cmd_and_pose_solution` | 한 노드에서 전진 발행과 위치 출력 |
| 07 | `lesson_07_multi_thread` | `lesson_07_multi_thread_solution` | 앞선 두 노드를 멀티스레드 실행 |
| 08 | `lesson_08_region_pen_client` | `lesson_08_region_pen_client_solution` | 왼쪽 노랑, 오른쪽 초록; 영역 변경 때 요청 |
| 09 | `lesson_09_teleport_client` | `lesson_09_teleport_client_solution` | 지정한 x, y, theta로 순간이동 |
| 10 | `lesson_10_spawn_client` | `lesson_10_spawn_client_solution` | turtle2 생성 |
| 11 | `lesson_11_named_turtle_controller` | `lesson_11_named_turtle_controller_solution` | turtle2 전진 및 위치 출력 |
| 12 | `lesson_12_distance_guard` | `lesson_12_distance_guard_solution` | turtle2 자동 이동, 가까우면 정지 후 안전해지면 재개 |

## 수업별 실행 조건

- 01–04: A의 turtlesim과 B의 키보드를 실행하고 C에서 수업을 실행합니다.
  04는 속도 명령을 한 번 받아야 세 값이 모두 출력됩니다.
- 05–07: A와 C를 실행하고 B 및 다른 자동 제어 노드는 중지합니다.
  06은 `rclpy.spin(node)`로 한 노드의 타이머와 구독을 처리합니다.
  07은 01/05의 클래스를 그대로 import하고 두 노드를
  `MultiThreadedExecutor`에 등록하여 `executor.spin()`으로 처리합니다.
- 08: A/B/C를 실행합니다. 가로 중앙 기준은 x=5.5입니다.
  첫 위치에서 색상을 한 번 초기화하고 이후에는 영역을 바꿀 때만 요청합니다.
  요청 대기 중에는 중복 요청을 보내지 않고 실패 시 다음 위치에서 다시 시도합니다.
- 09: A를 실행한 상태에서 C에서 아래 명령을 실행합니다. 각도 단위는 rad입니다.
- 10: A에서 turtle2가 없는 상태로 C에서 생성 명령을 실행합니다.
  같은 이름을 다시 생성하면 서비스가 실패하므로 새 이름을 주거나 시뮬레이터를 재시작합니다.
- 11: 10으로 turtle2를 먼저 만들고 아래 namespace 옵션을 사용합니다.
- 12: 10으로 turtle2를 만들고 11을 중지합니다. A/B/C를 실행합니다.
  키보드 turtle1을 turtle2 가까이 움직이면 turtle2만 멈춥니다.
  turtle1을 멀리 움직이면 turtle2가 다시 이동합니다.

```bash
ros2 run turtle_robot lesson_09_teleport_client_solution --ros-args -p x:=3.0 -p y:=3.0 -p theta:=0.0
ros2 run turtle_robot lesson_10_spawn_client_solution --ros-args -p name:=turtle2 -p x:=8.0 -p y:=8.0
ros2 run turtle_robot lesson_11_named_turtle_controller_solution --ros-args -r __ns:=/turtle2
ros2 run turtle_robot lesson_12_distance_guard_solution --ros-args -p safe_distance:=2.0
```

학생 버전도 같은 옵션을 사용하고 명령의 `_solution`만 뺍니다.
11의 상대 이름 `pose`, `cmd_vel`은 `/turtle2` namespace에서 각각
`/turtle2/pose`, `/turtle2/cmd_vel`로 해석됩니다. 맨 앞에 `/`를 붙인 절대 이름은
namespace를 적용받지 않습니다.

## 05 확장: 완전한 원 그리기

기본 완성 예제는 전진만 합니다. 확장에서는 속도 메시지의 전진 성분과 회전 성분을
함께 설정합니다. 반지름은 `r = |v / ω|`, 한 바퀴 시간은 `T = 2π / |ω|`입니다.
벽에서 충분히 떨어진 위치에서 시작하고 반지름이 화면 안에 들어가도록 선택하세요.
예를 들어 v=1.0 m/s, ω=1.0 rad/s라면 약 6.28초 동안 발행하면 한 바퀴입니다.
계속 발행하면 원을 반복하며, 정확히 한 바퀴만 돌려면 시간 조건과 영속도 발행을 추가합니다.

## 12 거리 계산

`d = sqrt((x1 - x2)^2 + (y1 - y2)^2)`이며 `math.hypot`으로 계산합니다.
거리는 음수가 아닙니다. `d < safe_distance`일 때 turtle2에 영속도를 보내고,
`d >= safe_distance`이면 전진과 주기적으로 바뀌는 회전 명령을 보냅니다.
위치 두 개를 받기 전에는 명령을 보내지 않습니다. 이 예제는 벽 회피나 경로 계획을
구현하지 않으므로 벽에 닿을 수 있습니다. turtle1 속도에는 관여하지 않습니다.
