# Set the minimum required version of CMake
cmake_minimum_required(VERSION 3.12)

# Set the project name
project(LinkedList)

# Add the executable target
add_executable(LinkedList linked_list.cpp)
add_executable(SingleLinkedList singly_linked_list.cpp)
add_executable(DoubleLinkedList doubly_linked_list.cpp)