Name:           ros-kinetic-qt-gui-cpp
Version:        0.3.2
Release:        0%{?dist}
Summary:        ROS qt_gui_cpp package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/qt_gui_cpp
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-kinetic-pluginlib >= 1.9.23
Requires:       ros-kinetic-qt-gui >= 0.3.0
BuildRequires:  pkgconfig
BuildRequires:  qt5-qtbase-devel
BuildRequires:  ros-kinetic-catkin
BuildRequires:  ros-kinetic-pluginlib >= 1.9.23
BuildRequires:  ros-kinetic-python-qt-binding >= 0.3.0
BuildRequires:  tinyxml-devel

%description
qt_gui_cpp provides the foundation for C++-bindings for qt_gui and creates
bindings for every generator available. At least one specific binding must be
available in order to use C++-plugins.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kinetic/setup.sh" ]; then . "/opt/ros/kinetic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/kinetic" \
        -DCMAKE_PREFIX_PATH="/opt/ros/kinetic" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kinetic/setup.sh" ]; then . "/opt/ros/kinetic/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/kinetic

%changelog
* Thu Apr 21 2016 Dirk Thomas <dthomas@osrfoundation.org> - 0.3.2-0
- Autogenerated by Bloom

* Mon Apr 18 2016 Dirk Thomas <dthomas@osrfoundation.org> - 0.3.1-0
- Autogenerated by Bloom

* Fri Apr 01 2016 Dirk Thomas <dthomas@osrfoundation.org> - 0.3.0-0
- Autogenerated by Bloom

