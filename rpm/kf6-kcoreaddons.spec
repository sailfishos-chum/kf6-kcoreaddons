%global  kf_version 6.6.0

Name:		kf6-kcoreaddons
Version: 6.6.0
Release:	0%{?dist}
Summary:	KDE Frameworks 6 Tier 1 addon with various classes on top of QtCore
License:	BSD-2-Clause AND BSD-3-Clause AND CC0-1.0 AND GPL-2.0-or-later AND MPL-1.1 AND LGPL-2.0-only AND LGPL-2.1-or-later AND LGPL-3.0-only AND LGPL-2.1-only WITH Qt-LGPL-exception-1.1
URL:		https://invent.kde.org/frameworks/kcoreaddons
Source0:    %{name}-%{version}.tar.bz2

BuildRequires:  cmake
BuildRequires:  clang
BuildRequires:  make
BuildRequires:  kf6-extra-cmake-modules >= %{kf_version}
BuildRequires:  kf6-rpm-macros
BuildRequires:	qt6-qtbase-devel
BuildRequires:	qt6-qttools-devel
BuildRequires:	qt6-qtdeclarative-devel
BuildRequires:  systemd-devel

%description
KCoreAddons provides classes built on top of QtCore to perform various tasks
such as manipulating mime types, autosaving files, creating backup files,
generating random sequences, performing text manipulations such as macro
replacement, accessing user information and many more.

%package    devel
Summary:    Development files for %{name}
Requires:   %{name} = %{version}-%{release}
Requires:   qt6-qtbase-devel
%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package        doc
Summary:        Developer Documentation files for %{name}
BuildArch:      noarch

%description    doc
Developer Documentation files for %{name} for use with KDevelop or QtCreator.

%prep
%autosetup -n %{name}-%{version}/upstream -p1

%build
%cmake_kf6
%cmake_build

%install
%cmake_install

%find_lang_kf6 kcoreaddons6_qt
%find_lang_kf6 kde6_xml_mimetypes
cat *.lang > all.lang

%files -f all.lang
%doc README.md
%{_kf6_datadir}/mime/packages/kde6.xml
%{_kf6_datadir}/qlogging-categories6/kcoreaddons.*
%{_kf6_libdir}/libKF6CoreAddons.so.*
%{_kf6_libdir}/qt6/qml/org/kde/coreaddons/libkcoreaddonsplugin.so
%{_kf6_libdir}/qt6/qml/org/kde/coreaddons/qmldir
%{_datadir}/kf6/jsonschema/kpluginmetadata.schema.json
%{_libdir}/qt6/qml/org/kde/coreaddons/kcoreaddonsplugin.qmltypes
%{_libdir}/qt6/qml/org/kde/coreaddons/kde-qmlmodule.version

%files devel
%{_kf6_includedir}/KCoreAddons/
%{_kf6_libdir}/cmake/KF6CoreAddons/
%{_kf6_libdir}/libKF6CoreAddons.so
%{_qt6_docdir}/*.tags

%files doc
%{_qt6_docdir}/*.qch
