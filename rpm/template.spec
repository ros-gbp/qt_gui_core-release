%bcond_without weak_deps

%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')
%global __provides_exclude_from ^/opt/ros/noetic/.*$
%global __requires_exclude_from ^/opt/ros/noetic/.*$

Name:           ros-noetic-qt-gui
Version:        0.4.1
Release:        1%{?dist}%{?release_suffix}
Summary:        ROS qt_gui package

License:        BSD
URL:            http://ros.org/wiki/qt_gui
Source0:        %{name}-%{version}.tar.gz

Requires:       python3-rospkg
Requires:       ros-noetic-python-qt-binding >= 0.3.0
Requires:       tango-icon-theme
BuildRequires:  python3-qt5-devel
BuildRequires:  python3-setuptools
BuildRequires:  qt5-qtbase-devel
BuildRequires:  ros-noetic-catkin
BuildRequires:  sip
Provides:       %{name}-devel = %{version}-%{release}
Provides:       %{name}-doc = %{version}-%{release}
Provides:       %{name}-runtime = %{version}-%{release}

%description
qt_gui provides the infrastructure for an integrated graphical user interface
based on Qt. It is extensible with Python- and C++-based plugins (implemented in
separate packages) which can contribute arbitrary widgets. It requires either
PyQt or PySide bindings.

%prep
%autosetup

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/noetic/setup.sh" ]; then . "/opt/ros/noetic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake3 \
    -UINCLUDE_INSTALL_DIR \
    -ULIB_INSTALL_DIR \
    -USYSCONF_INSTALL_DIR \
    -USHARE_INSTALL_PREFIX \
    -ULIB_SUFFIX \
    -DCMAKE_INSTALL_LIBDIR="lib" \
    -DCMAKE_INSTALL_PREFIX="/opt/ros/noetic" \
    -DCMAKE_PREFIX_PATH="/opt/ros/noetic" \
    -DSETUPTOOLS_DEB_LAYOUT=OFF \
    -DCATKIN_BUILD_BINARY_PACKAGE="1" \
    ..

%make_build

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/noetic/setup.sh" ]; then . "/opt/ros/noetic/setup.sh"; fi
%make_install -C obj-%{_target_platform}

%files
/opt/ros/noetic

%changelog
* Thu May 28 2020 Dirk Thomas <dthomas@osrfoundation.org> - 0.4.1-1
- Autogenerated by Bloom

* Fri Feb 28 2020 Dirk Thomas <dthomas@osrfoundation.org> - 0.4.0-1
- Autogenerated by Bloom

