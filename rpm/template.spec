Name:           ros-jade-qt-gui-cpp
Version:        0.2.29
Release:        0%{?dist}
Summary:        ROS qt_gui_cpp package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/qt_gui_cpp
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-jade-pluginlib >= 1.9.23
Requires:       ros-jade-qt-gui >= 0.2.18
BuildRequires:  pkgconfig
BuildRequires:  qt-devel
BuildRequires:  ros-jade-catkin
BuildRequires:  ros-jade-pluginlib >= 1.9.23
BuildRequires:  ros-jade-python-qt-binding >= 0.2.11
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
if [ -f "/opt/ros/jade/setup.sh" ]; then . "/opt/ros/jade/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/jade" \
        -DCMAKE_PREFIX_PATH="/opt/ros/jade" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/jade/setup.sh" ]; then . "/opt/ros/jade/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/jade

%changelog
* Sat Sep 19 2015 Dirk Thomas <dthomas@osrfoundation.org> - 0.2.29-0
- Autogenerated by Bloom

* Mon Jun 08 2015 Dirk Thomas <dthomas@osrfoundation.org> - 0.2.28-0
- Autogenerated by Bloom

* Wed Apr 29 2015 Dirk Thomas <dthomas@osrfoundation.org> - 0.2.27-0
- Autogenerated by Bloom

