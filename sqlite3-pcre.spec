Name: sqlite3-pcre-extract
Version: 0.1.1
Release: 0

Summary: Perl-compatible regular expression support for the SQLite
License: Public Domain
Group: Databases
URL: http://git.altlinux.org/people/at/packages/?p=sqlite3-pcre.git

Source: %name-%version.tar.gz

Requires: libsqlite3 >= 3.3.8-alt2

# Automatically added by buildreq on Thu Nov 02 2006
BuildRequires: libpcre-devel libsqlite3-devel sqlite3

#%if %{defined suse_version}
#Requires: libsqlite3 >= 3.3.8 libpcre0
#BuildRequires: pcre-devel sqlite3-devel sqlite3
#%endif

#%if %{defined fedora} || %{defined mdkversion}
#Requires: libsqlite >= 3.3.8 libpcre0
#BuildRequires: pcre-devel sqlite-devel sqlite
#%endif

%description
This SQLite loadable extension enables the REGEXP operator,
which is not implemented by default, to call PCRE routines
for regular expression matching.

%prep
%setup -q

%build
make 

#check
sqlite3 >out <<EOF
.load ./pcre.so
SELECT "asdf" REGEXP "(?i)^A";
EOF
grep 1 out

%install
make DESTDIR=%buildroot%_libdir install

%files
%dir %_libdir/sqlite3
%_libdir/sqlite3/pcre.so

%changelog
* Thu Nov 02 2006 Alexey Tourbin <at@altlinux.ru> 0.1-alt1
- initial revision
