%global product_family oVirt Node
%define recipe_root %{_datadir}/ovirt-node-recipe
%define dist_ocselected .ocselected.4.1

%global         package_version 0.2.1_ovirt35
%global         package_name ovirt-node-plugin-hosted-engine


Name:           ovirt-node-plugin-hosted-engine
Version:        0.2.1
Release:        2%{?dist_ocselected}
Source0:        http://plain.resources.ovirt.org/pub/ovirt-master-snapshot/src/%{name}/%{name}-%{package_version}.tar.gz
License:        GPLv2+
Group:          Applications/System
Summary:        Hosted Engine plugin for %{product_family} image
BuildRequires:  python2-devel
Requires:       ovirt-hosted-engine-setup
Requires:       screen
Requires:       python-requests

BuildArch:      noarch

%package recipe
Summary:        Kickstarts for building oVirt Node isos including %{name}
Group:          Applications/System
Requires:       ovirt-node-recipe >= 2.6.0


%post
chkconfig ovirt-ha-agent on
chkconfig ovirt-ha-broker on

%description
This package provides a hosted engine plugin for use with%{product_family} image.

%description recipe
Provides kickstart files for generating an oVirt Node ISO image containing
%{name}.


%files
%{python_sitelib}/ovirt/node/setup/hostedengine/__init__.py*
%{python_sitelib}/ovirt/node/setup/hostedengine/hosted_engine_page.py*

%prep
%setup -q -n "%{name}-%{package_version}"


%build
%configure

%install
%{__rm} -rf %{buildroot}
make install DESTDIR=%{buildroot}


%files
%{_sysconfdir}/rwtab.d/hosted-engine
%{python_sitelib}/ovirt/node/setup/hostedengine
#%{_sysconfdir}/ovirt-plugins.d

%files recipe
%{recipe_root}

%changelog
* Sat Dec 20 2014 Zhao Chao <zhaochao1984@gmail.com> 0.2.1-2.ocselected.4.1
- add the first i18n modification.
- change rank to 115.

* Thu Dec 10 2014 Zhao Chao <zhaochao1984@gmail.com> 0.2.1-1.ocselected.4.1
- merge upstream commits, update to 
  806278ea0fdfe331c60cdeb345f1ac0f77f3d6b4.
- recreate patch for OCselected-oVirt Engine Appliance support.

* Tue Nov 26 2014 Zhao Chao <zhaochao1984@gmail.com> 0.2.0-3.ocselected.4.1
- fixes local images support.

* Tue Nov 26 2014 Zhao Chao <zhaochao1984@gmail.com> 0.2.0-2.ocselected.4.1
- rwtab: Add /var/lib/ovirt-hosted-engine-ha.
- add support for local images.

* Tue Nov 25 2014 Zhao Chao <zhaochao1984@gmail.com> 0.2.0-1.ocselected.4.1
- update to commit 038bb9cf4c35d8e268018734ee79ec91ecd8fc37.

* Tue May 27 2014 Joey Boggs <jboggs@redhat.com> 0.0.1
- initial commit
