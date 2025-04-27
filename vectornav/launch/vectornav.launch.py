import launch
from launch_ros.actions import ComposableNodeContainer
from launch_ros.descriptions import ComposableNode


def generate_launch_description():
    
    container = ComposableNodeContainer(
        name='vectornav_container',
        namespace='',
        package='rclcpp_components',
        executable='component_container',
        composable_node_descriptions=[
            ComposableNode(
                package='vectornav',
                plugin='vn_ros::VectorNavNode',
                name='vectornav_node',
                parameters=[{
                        "sensor_port": "/dev/ttyUSB0",
                        "baudrate": 921600,
                        "sample_rate": 200,
                        "topic": "/imu",
                        "frame_id": "imu",
                        "gyroscope_variance": 1e-3,
                        "accelerometer_variance": 1e-3
                }]
            )
        ],
        output='screen',
        emulate_tty=True
    )

    return launch.LaunchDescription([container])
