cmake_minimum_required(VERSION 3.12...3.21.4)
project(CMakeExtraModules)

configure_file(${CMAKE_SOURCE_DIR}/config/CMakeExtraModulesConfig.cmake.in
  ${CMAKE_BINARY_DIR}/CMakeExtraModulesConfig.cmake)

install(FILES ${CMAKE_BINARY_DIR}/CMakeExtraModulesConfig.cmake
  DESTINATION ${CMAKE_INSTALL_PREFIX}/share/CMakeExtraModules)
install(
  DIRECTORY ${PROJECT_SOURCE_DIR}/cmake
  DESTINATION ${CMAKE_INSTALL_PREFIX}/share/CMakeExtraModules
  )
