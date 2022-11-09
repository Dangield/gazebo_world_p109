# License: Apache 2.0. See LICENSE file in root directory.
# Copyright(c) 2022 Intel Corporation. All Rights Reserved.

cmake_minimum_required(VERSION 3.5)
project(gazebo_world_p109)

find_package(ament_cmake REQUIRED)

# Install files
install(DIRECTORY 
        models
        worlds
        DESTINATION share/${PROJECT_NAME})

ament_package()
