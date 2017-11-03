Name:           ros-kinetic-qt-gui-py-common
Version:        0.3.8
Release:        0%{?dist}
Summary:        ROS qt_gui_py_common package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/qt_gui_py_common
Source0:        %{name}-%{version}.tar.gz

Requires:       python-rospkg
Requires:       ros-kinetic-python-qt-binding >= 0.3.0
BuildRequires:  ros-kinetic-catkin

%description
qt_gui_py_common provides common functionality for GUI plugins written in
Python.

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
* Fri Nov 03 2017 D. Hood <dhood@osrfoundation.org> - 0.3.8-0
- Autogenerated by Bloom

* Wed Oct 25 2017 D. Hood <dhood@osrfoundation.org> - 0.3.7-0
- Autogenerated by Bloom

* Tue Jan 24 2017 Dorian Scholz <scholz@sim.tu-darmstadt.de> - 0.3.4-0
- Autogenerated by Bloom

* Mon Sep 19 2016 Dorian Scholz <scholz@sim.tu-darmstadt.de> - 0.3.3-0
- Autogenerated by Bloom

* Thu Apr 21 2016 Dorian Scholz <scholz@sim.tu-darmstadt.de> - 0.3.2-0
- Autogenerated by Bloom

* Mon Apr 18 2016 Dorian Scholz <scholz@sim.tu-darmstadt.de> - 0.3.1-0
- Autogenerated by Bloom

* Fri Apr 01 2016 Dorian Scholz <scholz@sim.tu-darmstadt.de> - 0.3.0-0
- Autogenerated by Bloom

