Summary:	Dynamic language for the Java Platform
Name:		groovy
Version:	2.4.1
Release:	1
License:	Apache v2.0
Group:		Development/Languages/Java
Source0:	https://dl.bintray.com/groovy/maven/%{name}-binary-%{version}.zip
# Source0-md5:	31e7e691a8aeb2d07360d448d4fa8b47
URL:		http://groovy.codehaus.org/
Requires:	jdk
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Groovy is an agile and dynamic language for the Java Virtual Machine,
built upon Java with features inspired by languages like Python, Ruby
and Smalltalk. It seamlessly integrates with all existing Java objects
and libraries and compiles straight to Java bytecode so you can use it
anywhere you can use Java.

%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_datadir}/%{name}/bin}
for b in grape groovy groovyConsole groovyc groovydoc groovysh java2groovy startGroovy; do
	ln -sf %{_datadir}/%{name}/bin/$b $RPM_BUILD_ROOT%{_bindir}/$b
done

install -d $RPM_BUILD_ROOT
cp -a bin conf indy lib $RPM_BUILD_ROOT%{_datadir}/%{name}

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
%{_datadir}/%{name}/indy
%{_datadir}/%{name}/lib
