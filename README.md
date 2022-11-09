# gazebo_world_p109

This package contains Gazebo world of P109 laboratory present at the "Faculty of Electronics and Information Technology" of WUT.

## Building
It acts as a regular ROS2 package. It was tested on ROS2 Humble. After placing it in the "src" directory of your workspace, building it and sourcing the workspace, the package will set the appropriate environment variables. Therefore, Gazebo launched by gazebo_ros package launches will see worlds and models included in this package.

## Contents

### blender_ws/

Contains Blender files for most of the furniture along with exported 3d meshes in ".dae" format.

### models/

Contains 3d models in ".sdf" format readable by Gazebo along with meshes with fixed colors.

### scripts/

Contains single python script used for automation of creating ".sdf" models for Gazebo from ".dae" meshes exported from Blender. The models will also have their colors fixed by adding an ambient tag.

:warning: 

| WARNING: This executable is meant to be run while in "scripts/" directory. Running it will replace all existing models that originate from Blender files included in this package. DO NOT remove the "models/" directory by yourself, the script will do all the work. |
| --- |

### worlds/

Contains 2 Gazebo worlds:
- p109.wold - p109 laboratory
- model_preview.world - world for inspecting furniture