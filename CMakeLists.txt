cmake_minimum_required(VERSION 3.12...3.21.4)
project(LANLCMakeModules)

configure_file(${CMAKE_SOURCE_DIR}/config/LANLCMakeModulesConfig.cmake.in
  ${CMAKE_BINARY_DIR}/LANLCMakeModulesConfig.cmake)

install(FILES ${CMAKE_BINARY_DIR}/LANLCMakeModulesConfig.cmake
  DESTINATION ${CMAKE_INSTALL_PREFIX}/share/LANLCMakeModules)
install(
  DIRECTORY ${PROJECT_SOURCE_DIR}/cmake
  DESTINATION ${CMAKE_INSTALL_PREFIX}/share/LANLCMakeModules
  )
