#
# Conditional build:
%bcond_without	indy	# use libraries without invokedynamic support (compatible with JRE 1.5+)
#
Summary:	Dynamic language for the Java Platform
Name:		groovy
Version:	3.0.6
Release:	1
License:	Apache v2.0
Group:		Development/Languages/Java
Source0:	https://dl.bintray.com/groovy/maven/apache-%{name}-binary-%{version}.zip
# Source0-md5:	aa590e6cc8bae924b154ff79d796e18f
URL:		http://groovy-lang.org/
%if %{with indy}
Requires:	jdk >= 1.7
%else
Requires:	jdk >= 1.5
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautoreq_java		ClassDataVersion

%description
Groovy is an agile and dynamic language for the Java Virtual Machine,
built upon Java with features inspired by languages like Python, Ruby
and Smalltalk. It seamlessly integrates with all existing Java objects
and libraries and compiles straight to Java bytecode so you can use it
anywhere you can use Java.

%prep
%setup -q
grep -rl /usr/bin/env bin | xargs sed -i -e '1{
	s,^#!.*bin/env sh,#!%{__sh},
	s,^#!.*bin/env bash,#!%{__bash},
}'

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_datadir}/%{name}/bin}
for b in grape groovy groovyConsole groovyc groovydoc groovysh java2groovy startGroovy; do
	ln -sf %{_datadir}/%{name}/bin/$b $RPM_BUILD_ROOT%{_bindir}/$b
done

install -d $RPM_BUILD_ROOT
cp -a bin conf lib $RPM_BUILD_ROOT%{_datadir}/%{name}

%if %{with indy}
for f in indy/*-indy.jar; do
	targetname=$(basename $f -indy.jar).jar
	%{__cp} -p $f \
		$RPM_BUILD_ROOT%{_datadir}/%{name}/lib/$targetname
done
%endif

rm $RPM_BUILD_ROOT%{_datadir}/%{name}/bin/*.bat

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/grape
%attr(755,root,root) %{_bindir}/groovy
%attr(755,root,root) %{_bindir}/groovyConsole
%attr(755,root,root) %{_bindir}/groovyc
%attr(755,root,root) %{_bindir}/groovydoc
%attr(755,root,root) %{_bindir}/groovysh
%attr(755,root,root) %{_bindir}/java2groovy
%attr(755,root,root) %{_bindir}/startGroovy
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/bin
%attr(755,root,root) %{_datadir}/%{name}/bin/grape
%attr(755,root,root) %{_datadir}/%{name}/bin/groovy
%attr(755,root,root) %{_datadir}/%{name}/bin/groovyConsole
%attr(755,root,root) %{_datadir}/%{name}/bin/groovyc
%attr(755,root,root) %{_datadir}/%{name}/bin/groovydoc
%attr(755,root,root) %{_datadir}/%{name}/bin/groovysh
%attr(755,root,root) %{_datadir}/%{name}/bin/java2groovy
%attr(755,root,root) %{_datadir}/%{name}/bin/startGroovy
%{_datadir}/%{name}/conf
%{_datadir}/%{name}/lib
