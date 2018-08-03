Name:           ros-melodic-qt-gui
Version:        0.3.9
Release:        0%{?dist}
Summary:        ROS qt_gui package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/qt_gui
Source0:        %{name}-%{version}.tar.gz

Requires:       python-rospkg
Requires:       ros-melodic-python-qt-binding >= 0.3.0
Requires:       tango-icon-theme
BuildRequires:  python-qt5
BuildRequires:  qt5-qtbase-devel
BuildRequires:  ros-melodic-catkin
BuildRequires:  sip

%description
qt_gui provides the infrastructure for an integrated graphical user interface
based on Qt. It is extensible with Python- and C++-based plugins (implemented in
separate packages) which can contribute arbitrary widgets. It requires either
PyQt or PySide bindings.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/melodic/setup.sh" ]; then . "/opt/ros/melodic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/melodic" \
        -DCMAKE_PREFIX_PATH="/opt/ros/melodic" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/melodic/setup.sh" ]; then . "/opt/ros/melodic/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/melodic

%changelog
* Fri Aug 03 2018 D. Hood <dhood@osrfoundation.org> - 0.3.9-0
- Autogenerated by Bloom

* Wed Mar 21 2018 D. Hood <dhood@osrfoundation.org> - 0.3.8-0
- Autogenerated by Bloom

