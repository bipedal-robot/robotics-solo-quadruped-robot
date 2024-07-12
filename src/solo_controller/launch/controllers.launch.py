from launch import LaunchDescription
from launch_ros.actions import Node
from launch.event_handlers import OnProcessExit
from launch.actions import RegisterEventHandler

def generate_launch_description():
    joint_state_broadcaster_spawner = Node(
        package="controller_manager",
        executable="spawner",
        arguments=[
            "joint_state_broadcaster",
            "--controller-manager",
            "/controller_manager"
        ]
    )

    solo_controller_spawner = Node(
        package="controller_manager",
        executable="spawner",
        arguments=[
            "solo_controller",
            "--controller-manager",
            "/controller_manager",
        ]
    )

    return LaunchDescription([
        RegisterEventHandler(
            event_handler=OnProcessExit(
                target_action=joint_state_broadcaster_spawner,
                on_exit=[solo_controller_spawner],
            )
        ),
        joint_state_broadcaster_spawner,
    ])