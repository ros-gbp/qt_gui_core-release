Name:           ros-lunar-qt-gui-core
Version:        0.3.4
Release:        2%{?dist}
Summary:        ROS qt_gui_core package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/qt_gui_core
Source0:        %{name}-%{version}.tar.gz

BuildArch:      noarch

Requires:       ros-lunar-qt-dotgraph >= 0.3.0
Requires:       ros-lunar-qt-gui >= 0.3.0
Requires:       ros-lunar-qt-gui-app >= 0.3.0
Requires:       ros-lunar-qt-gui-cpp >= 0.3.0
Requires:       ros-lunar-qt-gui-py-common >= 0.3.0
BuildRequires:  ros-lunar-catkin

%description
Integration of the ROS package system and ROS-specific plugins for a Qt-based
GUI.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/lunar/setup.sh" ]; then . "/opt/ros/lunar/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/lunar" \
        -DCMAKE_PREFIX_PATH="/opt/ros/lunar" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/lunar/setup.sh" ]; then . "/opt/ros/lunar/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/lunar

%changelog
* Wed Mar 15 2017 Dirk Thomas <dthomas@osrfoundation.org> - 0.3.4-2
- Autogenerated by Bloom

* Wed Mar 15 2017 Dirk Thomas <dthomas@osrfoundation.org> - 0.3.4-1
- Autogenerated by Bloom

* Fri Feb 24 2017 Dirk Thomas <dthomas@osrfoundation.org> - 0.3.4-0
- Autogenerated by Bloom

