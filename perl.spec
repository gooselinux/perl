%define perl_version    5.10.1
%define perl_epoch      4
%define perl_arch_stem -thread-multi
%define perl_archname %{_arch}-%{_os}%{perl_arch_stem}

%define multilib_64_archs x86_64 s390x ppc64 sparc64

Name:           perl
Version:        %{perl_version}
Release:        115%{?dist}
Epoch:          %{perl_epoch}
Summary:        Practical Extraction and Report Language
Group:          Development/Languages
# Modules Tie::File and Getopt::Long are licenced under "GPLv2+ or Artistic,"
# we have to reflect that in the sub-package containing them.
# under UCD are unicode tables
# Public domain: ext/SDBM_File/sdbm/*, ext/Compress-Raw-Bzip2/bzip2-src/dlltest.c 
# MIT: ext/MIME-Base64/Base64.xs 
# Copyright Only: for example ext/Text-Soundex/Soundex.xs 
License:        (GPL+ or Artistic) and (GPLv2+ or Artistic) and Copyright Only and MIT and Public Domain and UCD
Url:            http://www.perl.org/
Source0:        http://www.cpan.org/src/5.0/perl-%{perl_version}.tar.bz2
Source1:        filter-requires.sh
Source2:        perl-5.8.0-libnet.cfg
Source3:        macros.perl
# image (binary) for CGI testing
Source4:        upload_post_text.txt

# overload.pm is looking into wrong directories if perl was already installed
# http://www.gossamer-threads.com/lists/perl/porters/242181
Patch0:         perl-5.10.1-fix_local_build.patch
# Specific to Fedora/RHEL
Patch1:         perl-suid-noroot.patch

# Removes date check, Fedora/RHEL specific
Patch2:         perl-perlbug-tag.patch

# work around annoying rpath issue
# This is only relevant for Fedora, as it is unlikely
# that upstream will assume the existence of a libperl.so
Patch3:         perl-5.8.8-rpath-make.patch

# Fedora/RHEL only (64bit only)
Patch4:         perl-5.8.0-libdir64.patch

# Fedora/RHEL specific (use libresolv instead of libbind)
Patch5:         perl-5.10.0-libresolv.patch

# FIXME: May need the "Fedora" references removed before upstreaming
# patches ExtUtils-MakeMaker
Patch6:         perl-USE_MM_LD_RUN_PATH.patch

# Skip hostname tests, since hostname lookup isn't available in Fedora
# buildroots by design.
# patches Net::Config from libnet
Patch7:         perl-5.10.0-disable_test_hosts.patch

# The Fedora builders started randomly failing this futime test
# only on x86_64, so we just don't run it. Works fine on normal
# systems.
Patch8:        perl-5.10.0-x86_64-io-test-failure.patch

# Reorder @INC: Based on: http://github.com/rafl/perl/commit/b9ba2fadb18b54e35e5de54f945111a56cbcb249
# and remove duplicates rhbz#594768
Patch9:        perl-5.10.1_INC.patch

# http://rt.perl.org/rt3/Ticket/Display.html?id=39060 (#221113)
Patch10:       perl-perlio-incorrect-errno.patch

# much better swap logic to support reentrancy and fix assert failure
# http://perl5.git.perl.org/perl.git/commitdiff/e9105d30edfbaa7f444bc7984c9bafc8e991ad12
# RT #60508
Patch11:       perl-much-better-swap-logic.patch

# temporarily export debug symbols even though DEBUGGING is not set:
Patch12:       perl-add-symbols.patch

# CVE_2009_3626 rhbz#547656 
Patch13:       perl-5.10.1-CVE_2009_3626.patch

# 554666 -  Wrong man pages location specified in perl manual page
Patch14:        perl-5.10.1-man_reference.patch
# 554654 -  "perldoc perlvar" renders incorrectly in C and en_US.UTF-8 locales.
Patch15:        perl-5.10.1-perlvar.patch
# 594768 - cpan rewrite by default rpm installation, set installation path into "site"
Patch16:        perl_CPAN.patch

# rpm vs cpan evaluate "bigger" release number differenty. Sometimes we need to
# change version according to rpm update (macro _rpm vs _real).
%define                     Archive_Extract_version 0.38
%define                     Archive_Tar_version 1.58
%define                     Compress_Raw_Zlib_version 2.023
%define                     Compress_Zlib_version 2.020
%define                     CPAN_version 1.9402
%define                     CPANPLUS_version 0.88
%define                     CGI_version 3.49
%define                     Digest_SHA_version 5.47
%define                     ExtUtils_CBuilder_version 0.27
%define                     ExtUtils_Embed_version 1.28
# It's really 6.55_02, but we drop the _02.
%define                     ExtUtils_MakeMaker_version 6.55
# It's really 2.2203, but we add .0 for update from previous version
%define                     ExtUtils_ParseXS_version 2.2003.0
%define                     File_Fetch_version 0.26
%define                     File_Path_version 2.08
%define                     File_Temp_version 0.22
%define                     IO_Compress_Base_version 2.020
%define                     IO_Compress_Zlib_version 2.020
%define                     IO_Zlib_version 1.09
%define                     IPC_Cmd_version 0.56
%define                     Locale_Maketext_Simple_version 0.18
%define                     Log_Message_version 0.02
%define                     Log_Message_Simple_version 0.04
%define                     Module_Build_version 0.35
# For Module-Build-0.x, the second component has to have four digits.
%define                     Module_Build_rpm_version  0.3500
%define                     Module_CoreList_version 2.18
%define                     Module_Load_version 0.16
%define                     Module_Load_Conditional_version 0.30
%define                     Module_Loaded_version 0.02
# has to be 3.x0, not 3.x
%define                     Module_Pluggable_version 3.90
%define                     Object_Accessor_version 0.34
%define                     Package_Constants_version 0.02
%define                     Params_Check_version 0.26
%define                     Parse_CPAN_Meta_version 1.40
%define                     Pod_Escapes_version 1.04
%define                     Pod_Simple_version 3.13
%define                     Safe_version 2.27
%define                     Term_UI_version 0.20
%define                     Test_Harness_version 3.17
%define                     Test_Simple_version 0.92
%define                     Time_Piece_version 1.15
%define                     Time_HiRes_version 1.9721
%define                     parent_version 0.221
%define                     version_version 0.77

# Update some of the bundled modules
# see http://fedoraproject.org/wiki/Perl/perl.spec for instructions
# and sometimes is needed change manifest
Patch99:        perl-manifest.patch
Patch100:       perl-update-ExtUtils-CBuilder.patch
Patch101:       perl-update-File-Path.patch
Patch102:       perl-update-Module-Build.patch
Patch103:       perl-update-Parse-CPAN-Meta.patch
Patch104:       perl-update-Archive-Extract.patch
Patch105:       perl-update-Archive-Tar.patch
Patch106:       perl-update-ExtUtils-ParseXS.patch
Patch107:       perl-update-File-Fetch.patch
Patch108:       perl-update-IPC-Cmd.patch
Patch109:       perl-update-Pod-Simple.patch
Patch110:       perl-update_Safe.patch
Patch111:       perl-update_CGI.patch
Patch112:       perl-update_Time-HiRes.patch

# Fix bundled modules
# Non-true return value on failed extraction
# https://rt.cpan.org/Public/Bug/Display.html?id=58636
Patch201:       perl-fix-Archive-Tar-failed_extract_code.patch

BuildRoot:      %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
BuildRequires:  tcsh, dos2unix, man, groff
BuildRequires:  gdbm-devel, db4-devel, zlib-devel
# For tests
BuildRequires:  procps, rsyslog

# The long line of Perl provides.

# These provides are needed by the perl pkg itself with auto-generated perl.req
Provides: perl(VMS::Filespec)
Provides: perl(VMS::Stdio)

# Compat provides which helps to future changes to new versions
Provides: perl(:MODULE_COMPAT_5.10.1)
Provides: perl(:MODULE_COMPAT_5.10.0)

# Threading provides
Provides: perl(:WITH_ITHREADS)
Provides: perl(:WITH_THREADS)
# Largefile provides
Provides: perl(:WITH_LARGEFILES)
# PerlIO provides
Provides: perl(:WITH_PERLIO)
# File provides
Provides: perl(abbrev.pl)
Provides: perl(assert.pl)
Provides: perl(bigfloat.pl)
Provides: perl(bigint.pl)
Provides: perl(bigrat.pl)
Provides: perl(bytes_heavy.pl)
Provides: perl(cacheout.pl)
Provides: perl(complete.pl)
Provides: perl(ctime.pl)
Provides: perl(dotsh.pl)
Provides: perl(dumpvar.pl)
Provides: perl(exceptions.pl)
Provides: perl(fastcwd.pl)
Provides: perl(find.pl)
Provides: perl(finddepth.pl)
Provides: perl(flush.pl)
Provides: perl(ftp.pl)
Provides: perl(getcwd.pl)
Provides: perl(getopt.pl)
Provides: perl(getopts.pl)
Provides: perl(hostname.pl)
Provides: perl(importenv.pl)
Provides: perl(look.pl)
Provides: perl(newgetopt.pl)
Provides: perl(open2.pl)
Provides: perl(open3.pl)
Provides: perl(perl5db.pl)
Provides: perl(pwd.pl)
Provides: perl(shellwords.pl)
Provides: perl(stat.pl)
Provides: perl(syslog.pl)
Provides: perl(tainted.pl)
Provides: perl(termcap.pl)
Provides: perl(timelocal.pl)
Provides: perl(utf8_heavy.pl)
Provides: perl(validate.pl)
Provides: perl(Carp::Heavy)

# Parse_CPAN_Meta
Provides: perl-Parse-CPAN-Meta = %{Parse_CPAN_Meta_version}
Obsoletes: perl-Parse-CPAN-Meta < 1.40

# Long history in 3rd-party repositories:
Provides: perl-File-Temp = %{File_Temp_version}
Obsoletes: perl-File-Temp < 0.20

# Use new testing module perl-Test-Harness, obsolete it outside of this package
Provides: perl-TAP-Harness = %{Test_Harness_version}
Obsoletes: perl-TAP-Harness < 3.10

Requires: perl-libs = %{perl_epoch}:%{perl_version}-%{release}

# We need this to break the dependency loop, and ensure that perl-libs 
# gets installed before perl.
Requires(post): perl-libs

# Filter the automatically generated dependencies.
#
# The original script might be /usr/lib/rpm/perl.req or
# /usr/lib/rpm/redhat/perl.req, better use the original value of the macro:
%{expand:%%define prev__perl_requires %{__perl_requires}}
%define __perl_requires %{SOURCE1} %{prev__perl_requires}

# When _use_internal_dependency_generator is 0, the perl.req script is
# called from /usr/lib/rpm{,/redhat}/find-requires.sh
# Likewise:
%{expand:%%define prev__find_requires %{__find_requires}}
%define __find_requires %{SOURCE1} %{prev__find_requires}


%description
Perl is a high-level programming language with roots in C, sed, awk
and shell scripting.  Perl is good at handling processes and files,
and is especially good at handling text.  Perl's hallmarks are
practicality and efficiency.  While it is used to do a lot of
different things, Perl's most common applications are system
administration utilities and web programming.  A large proportion of
the CGI scripts on the web are written in Perl.  You need the perl
package installed on your system so that your system can handle Perl
scripts.

Install this package if you want to program in Perl or enable your
system to handle Perl scripts.

%package libs
Summary:        The libraries for the perl runtime
Group:          Development/Languages
License:        GPL+ or Artistic
Requires:       perl = %{perl_epoch}:%{perl_version}-%{release}

%description libs
The libraries for the perl runtime


%package devel
Summary:        Header files for use in perl development
Group:          Development/Languages
License:        GPL+ or Artistic
Requires:       perl = %{perl_epoch}:%{perl_version}-%{release}

%description devel
This package contains header files and development modules.
Most perl packages will need to install perl-devel to build.


%package suidperl
Summary:        Suidperl, for use with setuid perl scripts
Group:          Development/Languages
License:        GPL+ or Artistic
Requires:       perl = %{perl_epoch}:%{perl_version}-%{release}

%description suidperl
Suidperl is a setuid binary copy of perl that allows for (hopefully)
more secure running of setuid perl scripts.


%package Archive-Extract
Summary:        Generic archive extracting mechanism
Group:          Development/Libraries
License:        GPL+ or Artistic
# Epoch bump for clean upgrade over old standalone package
Epoch:          1
Version:        %{Archive_Extract_version}
Requires:       perl = %{perl_epoch}:%{perl_version}-%{release}

%description Archive-Extract
Archive::Extract is a generic archive extraction mechanism.


%package Archive-Tar
Summary:        A module for Perl manipulation of .tar files
Group:          Development/Libraries
License:        GPL+ or Artistic
Epoch:          0
Version:        %{Archive_Tar_version}
Requires:       perl = %{perl_epoch}:%{perl_version}-%{release}
Requires:       perl(Compress::Zlib), perl(IO::Zlib)

%description Archive-Tar
Archive::Tar provides an object oriented mechanism for handling tar
files.  It provides class methods for quick and easy files handling
while also allowing for the creation of tar file objects for custom
manipulation.  If you have the IO::Zlib module installed, Archive::Tar
will also support compressed or gzipped tar files.


%package Compress-Raw-Zlib
Summary:        Low-Level Interface to the zlib compression library
Group:          Development/Libraries
License:        GPL+ or Artistic
Epoch:          0
Version:        %{Compress_Raw_Zlib_version}
Requires:       perl = %{perl_epoch}:%{perl_version}-%{release}

%description Compress-Raw-Zlib
This module provides a Perl interface to the zlib compression library.
It is used by IO::Compress::Zlib.


%package Compress-Zlib
Summary:        A module providing Perl interfaces to the zlib compression library
Group:          Development/Libraries
License:        GPL+ or Artistic
Epoch:          0
Version:        %{Compress_Zlib_version}
Requires:       perl = %{perl_epoch}:%{perl_version}-%{release}

%description Compress-Zlib
The Compress::Zlib module provides a Perl interface to the zlib
compression library. Most of the functionality provided by zlib is
available in Compress::Zlib.

The module can be split into two general areas of functionality,
namely in-memory compression/decompression and read/write access to
gzip files.


%package CPAN
Summary:        Query, download and build perl modules from CPAN sites
Group:          Development/Languages
License:        GPL+ or Artistic
Epoch:          0
Version:        %{CPAN_version}
Requires:       perl = %{perl_epoch}:%{perl_version}-%{release}
Provides:       cpan = %{version}

%description CPAN
Query, download and build perl modules from CPAN sites.


%package CPANPLUS
Summary:        API & CLI access to the CPAN mirrors
Group:          Development/Libraries
License:        GPL+ or Artistic
Epoch:          0
Version:        %{CPANPLUS_version}
Requires:       perl(Module::Pluggable) >= 2.4
Requires:       perl(Module::CoreList)
Requires:       perl = %{perl_epoch}:%{perl_version}-%{release}
Provides:       perl-CPANPLUS-Dist-Build = 0.06
Obsoletes:      perl-CPANPLUS-Dist-Build <= 0.05

%description CPANPLUS
The CPANPLUS library is an API to the CPAN mirrors and a collection of
interactive shells, commandline programs, etc, that use this API.

%package CGI
Summary:        Handle Common Gateway Interface requests and responses
Group:          Development/Libraries
License:        GPL+ or Artistic
Epoch:          0
Version:        %{CGI_version}
# not provided in RHEL, shouldn't be needed anyway
#Requires:      perl-FCGI
Requires:       perl = %{perl_epoch}:%{perl_version}-%{release}

%description CGI
CGI.pm is a stable, complete and mature solution for processing and 
preparing HTTP requests and responses. Major features including processing 
form submissions, file uploads, reading and writing cookies, query string 
generation and manipulation, and processing and preparing HTTP headers. 
Some HTML generation utilities are included as well.


%package Digest-SHA
Summary:        Perl extension for SHA-1/224/256/384/512
Group:          Development/Libraries
License:        GPL+ or Artistic
# Epoch bump for clean upgrade over old standalone package
Epoch:          1
Version:        %{Digest_SHA_version}
Requires:       perl = %{perl_epoch}:%{perl_version}-%{release}

%description Digest-SHA
Digest::SHA is a complete implementation of the NIST Secure Hash
Standard.  It gives Perl programmers a convenient way to calculate
SHA-1, SHA-224, SHA-256, SHA-384, and SHA-512 message digests.  The
module can handle all types of input, including partial-byte data.


%package ExtUtils-CBuilder
Summary:        Compile and link C code for Perl modules
Group:          Development/Libraries
License:        GPL+ or Artistic
# Epoch bump for clean upgrade over old standalone package
Epoch:          1
Version:        %{ExtUtils_CBuilder_version}
Requires:       perl-devel
Requires:       perl = %{perl_epoch}:%{perl_version}-%{release}

%description ExtUtils-CBuilder
This module can build the C portions of Perl modules by invoking the
appropriate compilers and linkers in a cross-platform manner. It was
motivated by the Module::Build project, but may be useful for other
purposes as well.


%package ExtUtils-Embed
Summary:        Utilities for embedding Perl in C/C++ applications
Group:          Development/Languages
License:        GPL+ or Artistic
Epoch:          0
Version:        %{ExtUtils_Embed_version}
Requires:       perl-devel
Requires:       perl = %{perl_epoch}:%{perl_version}-%{release}

%description ExtUtils-Embed
Utilities for embedding Perl in C/C++ applications.


%package ExtUtils-MakeMaker
Summary:        Create a module Makefile
Group:          Development/Languages
License:        GPL+ or Artistic
Epoch:          0
# It's really 6.55_02, but we drop the _02.
Version:        %{ExtUtils_MakeMaker_version}
Requires:       perl-devel
Requires:       perl = %{perl_epoch}:%{perl_version}-%{release}
Requires:       perl(Test::Harness)

%description ExtUtils-MakeMaker
Create a module Makefile.


%package ExtUtils-ParseXS
Summary:        Module and a script for converting Perl XS code into C code
Group:          Development/Libraries
License:        GPL+ or Artistic
# Epoch bump for clean upgrade over old standalone package
Epoch:          1
Version:        %{ExtUtils_ParseXS_version}
Requires:       perl-devel
Requires:       perl = %{perl_epoch}:%{perl_version}-%{release}

%description ExtUtils-ParseXS
ExtUtils::ParseXS will compile XS code into C code by embedding the
constructs necessary to let C functions manipulate Perl values and
creates the glue necessary to let Perl access those functions.


%package File-Fetch
Summary:        Generic file fetching mechanism
Group:          Development/Libraries
License:        GPL+ or Artistic
Epoch:          0
Version:        %{File_Fetch_version}
Requires:       perl(IPC::Cmd) >= 0.36
Requires:       perl(Module::Load::Conditional) >= 0.04
Requires:       perl(Params::Check) >= 0.07
Requires:       perl = %{perl_epoch}:%{perl_version}-%{release}

%description File-Fetch
File::Fetch is a generic file fetching mechanism.


%package IO-Compress-Base
Summary:        Base Class for IO::Compress modules
Group:          Development/Libraries
License:        GPL+ or Artistic
Epoch:          0
Version:        %{IO_Compress_Base_version}
Requires:       perl = %{perl_epoch}:%{perl_version}-%{release}

%description IO-Compress-Base
This module is the base class for all IO::Compress and IO::Uncompress
modules. This module is not intended for direct use in application
code. Its sole purpose is to to be sub-classed by IO::Compress
modules.


%package IO-Compress-Zlib
Summary:        Perl interface to allow reading and writing of gzip and zip data
Group:          Development/Libraries
License:        GPL+ or Artistic
Epoch:          0
Version:        %{IO_Compress_Zlib_version}
Requires:       perl = %{perl_epoch}:%{perl_version}-%{release}

%description IO-Compress-Zlib
This module provides an "IO::"-style Perl interface to "Compress::Zlib"


%package IO-Zlib
Summary:        Perl IO:: style interface to Compress::Zlib
Group:          Development/Libraries
License:        GPL+ or Artistic
# Epoch bump for clean upgrade over old standalone package
Epoch:          1
Version:        %{IO_Zlib_version}
Requires:       perl(Compress::Zlib)
Requires:       perl = %{perl_epoch}:%{perl_version}-%{release}

%description IO-Zlib
This modules provides an IO:: style interface to the Compress::Zlib
package. The main advantage is that you can use an IO::Zlib object in
much the same way as an IO::File object so you can have common code
that doesn't know which sort of file it is using.


%package IPC-Cmd
Summary:        Finding and running system commands made easy
Group:          Development/Libraries
License:        GPL+ or Artistic
# Epoch bump for clean upgrade over old standalone package
Epoch:          1
# do not upgrade in the future to _something version. They are testing!
Version:        %{IPC_Cmd_version}
Requires:       perl = %{perl_epoch}:%{perl_version}-%{release}

%description IPC-Cmd
IPC::Cmd allows you to run commands, interactively if desired, in a
platform independent way, but have them still work.


%package Locale-Maketext-Simple
Summary:        Simple interface to Locale::Maketext::Lexicon
Group:          Development/Libraries
License:        MIT
# Epoch bump for clean upgrade over old standalone package
Epoch:          1
Version:        %{Locale_Maketext_Simple_version}
Requires:       perl = %{perl_epoch}:%{perl_version}-%{release}

%description Locale-Maketext-Simple
This module is a simple wrapper around Locale::Maketext::Lexicon, designed
to alleviate the need of creating Language Classes for module authors.


%package Log-Message
Summary:        Generic message storage mechanism
Group:          Development/Libraries
License:        GPL+ or Artistic
# Epoch bump for clean upgrade over old standalone package
Epoch:          1
Version:        %{Log_Message_version}
Requires:       perl = %{perl_epoch}:%{perl_version}-%{release}
# Add a versioned provides, since we pull the unversioned one out.
Provides:       perl(Log::Message::Handlers) = %{version}

%description Log-Message
Log::Message is a generic message storage mechanism. It allows you to 
store messages on a stack -- either shared or private -- and assign meta-data 
to it. Some meta-data will automatically be added for you, like a timestamp
and a stack trace, but some can be filled in by the user, like a tag by
which to identify it or group it, and a level at which to handle the
message (for example, log it, or die with it).


%package Log-Message-Simple
Summary:        Simplified frontend to Log::Message
Group:          Development/Libraries
License:        GPL+ or Artistic
Epoch:          0
Version:        %{Log_Message_Simple_version}
Requires:       perl = %{perl_epoch}:%{perl_version}-%{release}

%description Log-Message-Simple
This module provides standardized logging facilities using the
Log::Message module.


%package Module-Build
Summary:        Perl module for building and installing Perl modules
Group:          Development/Libraries
License:        GPL+ or Artistic
# Epoch bump for clean upgrade over old standalone package
Epoch:          1
Version:        %{Module_Build_rpm_version}
Requires:       perl(Archive::Tar) >= 1.08
Requires:       perl(ExtUtils::CBuilder) >= 0.15
Requires:       perl(ExtUtils::ParseXS) >= 1.02
Requires:       perl = %{perl_epoch}:%{perl_version}-%{release}

%description Module-Build
Module::Build is a system for building, testing, and installing Perl
modules. It is meant to be an alternative to ExtUtils::MakeMaker.
Developers may alter the behavior of the module through subclassing in a
much more straightforward way than with MakeMaker. It also does not 
require a make on your system - most of the Module::Build code is pure-perl and
written in a very cross-platform way. In fact, you don't even need a 
shell, so even platforms like MacOS (traditional) can use it fairly easily. Its
only prerequisites are modules that are included with perl 5.6.0, and it
works fine on perl 5.005 if you can install a few additional modules.


%package Module-CoreList
Summary:        Perl core modules indexed by perl versions
Group:          Development/Languages
License:        GPL+ or Artistic
Epoch:          0
Version:        %{Module_CoreList_version}
Requires:       perl = %{perl_epoch}:%{perl_version}-%{release}
Requires:       perl(version)

%description Module-CoreList
Module::CoreList contains the hash of hashes %Module::CoreList::version,
this is keyed on perl version as indicated in $].  The second level hash
is module => version pairs.


%package Module-Load
Summary:        Runtime require of both modules and files
Group:          Development/Libraries
License:        GPL+ or Artistic
# Epoch bump for clean upgrade over old standalone package
Epoch:          1
Version:        %{Module_Load_version}
Requires:       perl = %{perl_epoch}:%{perl_version}-%{release}

%description Module-Load
Module::Load eliminates the need to know whether you are trying to
require either a file or a module.


%package Module-Load-Conditional
Summary:        Looking up module information / loading at runtime
Group:          Development/Libraries
License:        GPL+ or Artistic
Epoch:          0
Version:        %{Module_Load_Conditional_version}
Requires:       perl = %{perl_epoch}:%{perl_version}-%{release}

%description Module-Load-Conditional
Module::Load::Conditional provides simple ways to query and possibly 
load
any of the modules you have installed on your system during runtime.


%package Module-Loaded
Summary:        Mark modules as loaded or unloaded
Group:          Development/Libraries
License:        GPL+ or Artistic
# Epoch bump for clean upgrade over old standalone package
Epoch:          1
Version:        %{Module_Loaded_version}
Requires:       perl = %{perl_epoch}:%{perl_version}-%{release}

%description Module-Loaded
When testing applications, often you find yourself needing to provide
functionality in your test environment that would usually be provided by
external modules. Rather than munging the %INC by hand to mark these
external modules as loaded, so they are not attempted to be loaded by
perl, this module offers you a very simple way to mark modules as loaded
and/or unloaded.


%package Module-Pluggable
Summary:        Automatically give your module the ability to have plugins
Group:          Development/Libraries
License:        GPL+ or Artistic
# Epoch bump for clean upgrade over old standalone package
Epoch:          1
Version:        %{Module_Pluggable_version} 
Requires:       perl = %{perl_epoch}:%{perl_version}-%{release}

%description Module-Pluggable
Provides a simple but, hopefully, extensible way of having 'plugins' for
your module.


%package Object-Accessor
Summary:        Perl module that allows per object accessors
Group:          Development/Libraries
License:        GPL+ or Artistic
# Epoch bump for clean upgrade over old standalone package
Epoch:          1
Version:        %{Object_Accessor_version}
Requires:       perl = %{perl_epoch}:%{perl_version}-%{release}

%description Object-Accessor
Object::Accessor provides an interface to create per object accessors 
(as opposed to per Class accessors, as, for example, Class::Accessor 
provides).


%package Package-Constants
Summary:        List all constants declared in a package
Group:          Development/Libraries
License:        GPL+ or Artistic
# Epoch bump for clean upgrade over old standalone package
Epoch:          1
Version:        %{Package_Constants_version}
Requires:       perl = %{perl_epoch}:%{perl_version}-%{release}

%description Package-Constants
Package::Constants lists all the constants defined in a certain package.
This can be useful for, among others, setting up an autogenerated
@EXPORT/@EXPORT_OK for a Constants.pm file.


%package Params-Check
Summary:        Generic input parsing/checking mechanism
Group:          Development/Libraries
License:        GPL+ or Artistic
# Epoch bump for clean upgrade over old standalone package
Epoch:          1
Version:        %{Params_Check_version}
Requires:       perl = %{perl_epoch}:%{perl_version}-%{release}

%description Params-Check
Params::Check is a generic input parsing/checking mechanism.


%package Parse-CPAN-Meta
Summary:        Parse META.yml and other similar CPAN metadata files
Group:          Development/Libraries
License:        GPL+ or Artistic
# Epoch bump for clean upgrade over old standalone package
Epoch:          1
Version:        %{Parse_CPAN_Meta_version}
Requires:       perl = %{perl_epoch}:%{perl_version}-%{release}

%description Parse-CPAN-Meta 
Parse::CPAN::Meta is a parser for META.yml files, based on the parser half
of YAML::Tiny.


%package Pod-Escapes
Summary:        Perl module for resolving POD escape sequences
Group:          Development/Libraries
License:        GPL+ or Artistic
# Epoch bump for clean upgrade over old standalone package
Epoch:          1
Version:        %{Pod_Escapes_version}
Requires:       perl = %{perl_epoch}:%{perl_version}-%{release}

%description Pod-Escapes
This module provides things that are useful in decoding Pod E<...>
sequences. Presumably, it should be used only by Pod parsers and/or
formatters.


%package Pod-Simple
Summary:        Framework for parsing POD documentation
Group:          Development/Libraries
License:        GPL+ or Artistic
# Epoch bump for clean upgrade over old standalone package
Epoch:          1
Version:        %{Pod_Simple_version}
Requires:       perl = %{perl_epoch}:%{perl_version}-%{release}

%description Pod-Simple
Pod::Simple is a Perl library for parsing text in the Pod ("plain old
documentation") markup language that is typically used for writing
documentation for Perl and for Perl modules.


%package Term-UI
Summary:        Term::ReadLine UI made easy
Group:          Development/Libraries
License:        GPL+ or Artistic
Epoch:          0
Version:        %{Term_UI_version}
Requires:       perl = %{perl_epoch}:%{perl_version}-%{release}
Requires:       perl(Log::Message::Simple)

%description Term-UI
Term::UI is a transparent way of eliminating the overhead of having to
format a question and then validate the reply, informing the user if the
answer was not proper and re-issuing the question.


%package Test-Harness
Summary:        Run Perl standard test scripts with statistics
Group:          Development/Languages
License:        GPL+ or Artistic
Epoch:          0
Version:        %{Test_Harness_version}
Requires:       perl-devel
Requires:       perl = %{perl_epoch}:%{perl_version}-%{release}

%description Test-Harness
Run Perl standard test scripts with statistics.
Use TAP::Parser, Test::Harness package was whole rewritten.

%package Test-Simple
Summary:        Basic utilities for writing tests
Group:          Development/Languages
License:        GPL+ or Artistic
Epoch:          0
Version:        %{Test_Simple_version}
Requires:       perl-devel
Requires:       perl = %{perl_epoch}:%{perl_version}-%{release}

%description Test-Simple
Basic utilities for writing tests.


%package Time-Piece
Summary:        Time objects from localtime and gmtime
Group:          Development/Libraries
License:        GPL+ or Artistic
Epoch:          0
Version:        %{Time_Piece_version}
Requires:       perl = %{perl_epoch}:%{perl_version}-%{release}

%description Time-Piece
The Time::Piece module replaces the standard localtime and gmtime functions
with implementations that return objects.  It does so in a backwards
compatible manner, so that using localtime or gmtime as documented in
perlfunc still behave as expected.


%package Time-HiRes
Summary:        High resolution alarm, sleep, gettimeofday, interval timers
Group:          Development/Libraries
License:        GPL+ or Artistic
Version:        %{Time_HiRes_version}
Requires:       perl = %{perl_epoch}:%{perl_version}-%{release}

%description Time-HiRes
The Time::HiRes module implements a Perl interface to the usleep, nanosleep, 
ualarm, gettimeofday, and setitimer/getitimer system calls, in other words, 
high resolution time and timers. See the "EXAMPLES" section below and the test 
scripts for usage; see your system documentation for the description of the 
underlying nanosleep or usleep, ualarm, gettimeofday, and setitimer/getitimer
calls.


%package parent
Summary:        Establish an ISA relationship with base classes at compile time
Group:          Development/Libraries
License:        GPL+ or Artistic
# Epoch bump for clean upgrade over old standalone package
Epoch:          1
Version:        %{parent_version}
Requires:       perl = %{perl_epoch}:%{perl_version}-%{release}

%description parent
parent allows you to both load one or more modules, while setting up 
inheritance from those modules at the same time. Mostly similar in 
effect to:

    package Baz;

    BEGIN {
        require Foo;
        require Bar; 
        
        push @ISA, qw(Foo Bar); 
    }

%package version
Summary:        Perl extension for Version Objects
Group:          Development/Libraries
License:        GPL+ or Artistic
# Epoch bump for clean upgrade over old standalone package
Epoch:          3
Version:        %{version_version}
Requires:       perl = %{perl_epoch}:%{perl_version}-%{release}

%description version
Perl extension for Version Objects


%package core
Summary:        Base perl metapackage
Group:          Development/Languages
# This rpm doesn't contain any copyrightable material.
# Nevertheless, it needs a License tag, so we'll use the generic
# "perl" license.
License:        GPL+ or Artistic
Epoch:          0
Version:        %{perl_version}
Requires:       perl = %{perl_epoch}:%{perl_version}-%{release}
Requires:       perl-libs = %{perl_epoch}:%{perl_version}-%{release}
Requires:       perl-devel = %{perl_epoch}:%{perl_version}-%{release}

Requires:       perl-Archive-Extract, perl-Archive-Tar, perl-Compress-Raw-Zlib, perl-Compress-Zlib, perl-CPAN,
Requires:       perl-CPANPLUS, perl-Digest-SHA, perl-ExtUtils-CBuilder,
Requires:       perl-ExtUtils-Embed, perl-ExtUtils-MakeMaker, perl-ExtUtils-ParseXS,
Requires:       perl-File-Fetch, perl-IO-Compress-Base, perl-IO-Compress-Zlib, perl-IO-Zlib,
Requires:       perl-IPC-Cmd, perl-Locale-Maketext-Simple, perl-Log-Message, perl-Log-Message-Simple,
Requires:       perl-Module-Build, perl-Module-CoreList, perl-Module-Load,
Requires:       perl-Module-Load-Conditional, perl-Module-Loaded,
Requires:       perl-Module-Pluggable, perl-Object-Accessor, perl-Package-Constants,
Requires:       perl-Params-Check, perl-Pod-Escapes, perl-Pod-Simple, perl-Term-UI, 
Requires:       perl-Test-Harness, perl-Test-Simple, perl-Time-Piece, perl-Time-HiRes, perl-version
Requires:       perl-parent, perl-Parse-CPAN-Meta
# Note: perl-suidperl has always been an independent subpackage
# We don't want perl-core to drag it in.

%description core
A metapackage which requires all of the perl bits and modules in the
upstream tarball from perl.org.


%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
# This patch breaks sparc64 compilation
# We should probably consider removing it for all arches.
%ifnarch sparc64
%patch3 -p1
%endif
%ifarch %{multilib_64_archs}
%patch4 -p1
%endif
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1
%patch10 -p1
%patch11 -p1
%patch12 -p1
%patch13 -p1
%patch14 -p1
%patch15 -p1
%patch16 -p1

%patch99 -p1
%patch100 -p1
%patch101 -p1
%patch102 -p1
%patch103 -p1
%patch104 -p1
%patch105 -p1
%patch106 -p1
%patch107 -p1
%patch108 -p1
# E stands for removal of one test in patch
%patch109 -p1 -E
%patch110 -p1
%patch111 -p1
%patch112 -p1

%patch201 -p1

#
# Candidates for doc recoding (need case by case review):
# find . -name "*.pod" -o -name "README*" -o -name "*.pm" | xargs file -i | grep charset= | grep -v '\(us-ascii\|utf-8\)'
recode()
{
        iconv -f "${2:-iso-8859-1}" -t utf-8 < "$1" > "${1}_"
        touch -r "$1" "${1}_"
        mv -f "${1}_" "$1"
}
recode README.cn euc-cn
recode README.jp euc-jp
recode README.ko euc-kr
recode README.tw big5
recode pod/perlebcdic.pod
recode pod/perlhack.pod
recode pod/perlhist.pod
recode pod/perlothrtut.pod
recode pod/perlthrtut.pod
recode lib/Unicode/Collate.pm
recode AUTHORS

find . -name \*.orig -exec rm -fv {} \;

# replace local perl with installed for test files
#cd lib/CGI/t/
#for i in apache can carp cookie form function html no_tabindex pretty push request \
#start_end_asterisk start_end_end start_end_start switch uploadInfo upload util-58 util
#do
#    sed -i -e 's/\/usr\/local\/bin\/perl/\/usr\/bin\/perl/' $i.t
#done
#cd ../../..

# Oh, the irony. Perl generates some non-versioned provides we don't need.
# Each of these has a versioned provide, which we keep.
cat << EOF > perl-prov
#!/bin/sh
%{__perl_provides} $* |\
    sed -e '/^perl(Carp)$/d' |\
    sed -e '/^perl(DynaLoader)$/d' |\
    sed -e '/^perl(Locale::Maketext)$/d' |\
    sed -e '/^perl(Log::Message::Handlers)$/d' |\
    sed -e '/^perl(Math::BigInt)$/d' |\
    sed -e '/^perl(Net::Config)$/d' |\
    sed -e '/^perl(Tie::Hash)$/d' |\
    sed -e '/^perl(bigint)$/d' |\
    sed -e '/^perl(bigrat)$/d' |\
    sed -e '/^perl(bytes)$/d' |\
    sed -e '/^perl(utf8)$/d' |\
    sed -e '/^perl(DB)$/d'
EOF
%define __perl_provides %{_builddir}/%{name}-%{perl_version}/perl-prov
chmod +x %{__perl_provides}

# Configure Compress::Zlib to use system zlib
sed -i 's|BUILD_ZLIB      = True|BUILD_ZLIB      = False|
        s|INCLUDE         = ./zlib-src|INCLUDE         = %{_includedir}|
        s|LIB             = ./zlib-src|LIB             = %{_libdir}|' \
        ext/Compress-Raw-Zlib/config.in

%build
echo "RPM Build arch: %{_arch}"

# use "lib", not %{_lib}, for privlib, sitelib, and vendorlib
# To build production version, we would need -DDEBUGGING=-g

# Perl INC path (perl -V) in search order:
# - /usr/local/share/perl5            -- for CPAN     (site lib)
# - /usr/local/lib[64]/perl5          -- for CPAN     (site arch)
# - /usr/share/perl5/vendor_perl      -- 3rd party    (vendor lib)
# - /usr/lib[64]/perl5/vendor_perl    -- 3rd party    (vendor arch)
# - /usr/share/perl5                  -- RHEL         (priv lib)
# - /usr/lib[64]/perl5                -- RHEL         (arch lib)

%define privlib         %{_prefix}/share/perl5
%define archlib         %{_libdir}/perl5

/bin/sh Configure -des -Doptimize="$RPM_OPT_FLAGS" \
        -DDEBUGGING=-g \
        -Dversion=%{perl_version} \
        -Dmyhostname=localhost \
        -Dperladmin=root@localhost \
        -Dcc='%{__cc}' \
        -Dcf_by='Red Hat, Inc.' \
        -Dprefix=%{_prefix} \
        -Dvendorprefix=%{_prefix} \
        -Dsiteprefix=%{_prefix}/local \
        -Dsitelib="%{_prefix}/local/share/perl5" \
        -Dsitearch="%{_prefix}/local/%{_lib}/perl5" \
        -Dprivlib="%{privlib}" \
        -Darchlib="%{archlib}" \
        -Dvendorlib="%{privlib}/vendor_perl" \
        -Dvendorarch="%{archlib}/vendor_perl" \
%if 1
        -Dinc_version_list="5.10.0" \
%endif
        -Darchname=%{perl_archname} \
%ifarch %{multilib_64_archs}
        -Dlibpth="/usr/local/lib64 /lib64 %{_prefix}/lib64" \
%endif
%ifarch sparc sparcv9
        -Ud_longdbl \
%endif
        -Duseshrplib \
        -Dusethreads \
        -Duseithreads \
        -Duselargefiles \
        -Dd_dosuid \
        -Dd_semctl_semun \
        -Di_db \
        -Ui_ndbm \
        -Di_gdbm \
        -Di_shadow \
        -Di_syslog \
        -Dman3ext=3pm \
        -Duseperlio \
        -Dinstallusrbinperl=n \
        -Ubincompat5005 \
        -Uversiononly \
        -Dpager='/usr/bin/less -isr' \
        -Dd_gethostent_r_proto -Ud_endhostent_r_proto -Ud_sethostent_r_proto \
        -Ud_endprotoent_r_proto -Ud_setprotoent_r_proto \
        -Ud_endservent_r_proto -Ud_setservent_r_proto \
        -Dscriptdir='%{_bindir}'


%ifarch sparc64
make
%else
make %{?_smp_mflags}
%endif

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

%define build_archlib $RPM_BUILD_ROOT%{archlib}
%define build_privlib $RPM_BUILD_ROOT%{privlib}
%define build_bindir  $RPM_BUILD_ROOT%{_bindir}
%define new_perl LD_PRELOAD="%{build_archlib}/CORE/libperl.so" \\\
        LD_LIBRARY_PATH="%{build_archlib}/CORE" \\\
        PERL5LIB="%{build_archlib}:%{build_privlib}" \\\
        %{build_bindir}/perl

# perl doesn't create the auto subdirectory, but modules put things in it,
# so we need to own it.
mkdir -p -m 755 %{build_archlib}/auto

install -p -m 755 utils/pl2pm %{build_bindir}/pl2pm

for i in asm/termios.h syscall.h syslimits.h syslog.h \
        sys/ioctl.h sys/socket.h sys/time.h wait.h
do
        %{new_perl} %{build_bindir}/h2ph -a -d %{build_archlib} $i || true
done

# vendor directories (in this case for third party rpms)
mkdir -p $RPM_BUILD_ROOT%{archlib}/vendor_perl
mkdir -p $RPM_BUILD_ROOT%{privlib}/vendor_perl

#
# libnet configuration file
#
install -p -m 644 %{SOURCE2} %{build_privlib}/Net/libnet.cfg

#
# perl RPM macros
#
mkdir -p ${RPM_BUILD_ROOT}%{_sysconfdir}/rpm
install -p -m 644 %{SOURCE3} ${RPM_BUILD_ROOT}%{_sysconfdir}/rpm/


#
# Core modules removal
#
find $RPM_BUILD_ROOT -name '*NDBM*' | xargs rm -rfv
find $RPM_BUILD_ROOT -type f -name '*.bs' -empty | xargs rm -f 

chmod -R u+w $RPM_BUILD_ROOT/*

# miniperl? As an interpreter? How odd. Anyway, a symlink does it:
rm %{build_privlib}/ExtUtils/xsubpp
ln -s ../../../bin/xsubpp %{build_privlib}/ExtUtils/

# Don't need the .packlist
rm %{build_archlib}/.packlist

# Fix some manpages to be UTF-8
pushd $RPM_BUILD_ROOT%{_mandir}/man1/
  for i in perl588delta.1 perldelta.1 ; do
    iconv -f MS-ANSI -t UTF-8 $i --output new-$i
    rm $i
    mv new-$i $i
  done
popd

# Local patch tracking
pushd %{build_archlib}/CORE/
%{new_perl} -x patchlevel.h \
       'RHEL Patch0: Sys-Syslog has wrong path (build failure) ' \
       'RHEL Patch1: Permit suidperl to install as nonroot' \
       'RHEL Patch2: Removes date check, Fedora/RHEL specific' \
%ifnarch sparc64 \
       'RHEL Patch3: Work around annoying rpath issue' \
%endif \
%ifarch %{multilib_64_archs} \
       'RHEL Patch4: support for libdir64' \
%endif \
       'RHEL Patch5: use libresolv instead of libbind' \
       'RHEL Patch6: USE_MM_LD_RUN_PATH' \
       'RHEL Patch7: Skip hostname tests, due to builders not being network capable' \
       'RHEL Patch8: Dont run one io test due to random builder failures' \
       'RHEL Patch9: Reorder @INC and remove duplicates' \
       'RHEL Patch10: fix RT 39060, errno incorrectly set in perlio' \
       'RHEL Patch11: much better swap logic to support reentrancy and fix assert failure' \
       'RHEL Patch12: backward compatibility for the trasition' \
       'RHEL Patch13: CVE_2009_3626' \
       'RHEL Patch14: man page location in /usr/share' \
       'RHEL Patch15: perlvar pod rendered correctly' \
       'RHEL Patch16: set default CPAN install into site' \
       'RHEL Patch100: Update ExtUtils::CBuilder to %{ExtUtils_CBuilder_version}' \
       'RHEL Patch101: Update File::Path to %{File_Path_version}' \
       'RHEL Patch102: Update Module::Build to %{Module_Build_version}' \
       'RHEL Patch103: Update Parse::CPAN::Meta::version to %{Parse_CPAN_Meta_version}' \
       'RHEL Patch104: Update Archive::Extract to %{Archive_Extract_version}' \
       'RHEL Patch105: Update Archive::Tar to %{Archive_Tar_version}' \
       'RHEL Patch106: Update ExtUtils::ParseXS to %{ExtUtils_ParseXS_version}' \
       'RHEL Patch107: Update File::Fetch to %{File_Fetch_version}' \
       'RHEL Patch108: Update IPC::Cmd to %{IPC_Cmd_version}' \
       'RHEL Patch109: Update Pod::Simple to %{Pod_Simple_version}' \
       'RHEL Patch110: Update Safe to %{Safe_version}' \
       'RHEL Patch111: Update CGI to %{CGI_version}' \
       'RHEL Patch112: Update Time::HiRes to %{Time_HiRes_version}' \
       'RHEL Patch201: Fix Archive::Tar to return correct code on error' \
       %{nil}

rm patchlevel.bak
popd

# compatibility directory: for perl(:MODULE_COMPAT_5.10.0)
mkdir -p $RPM_BUILD_ROOT%{_libdir}/perl5/5.10.0/%{perl_archname}/CORE
ln -s ../../../CORE/libperl.so $RPM_BUILD_ROOT%{_libdir}/perl5/5.10.0/%{perl_archname}/CORE/libperl.so

# for now, remove Bzip2:
find $RPM_BUILD_ROOT -name Bzip2 | xargs rm -r
find $RPM_BUILD_ROOT -name '*B*zip2*'| xargs rm

%clean
rm -rf $RPM_BUILD_ROOT

%check
# this file is binary which can't be attach into patch
cp %{SOURCE4} lib/CGI/t/
sed -i -e 's|\(t\/upload_post_text\.txt\)|../lib/CGI/\1|' lib/CGI/t/*.t
# some updated modules check whether module is built from cpan or core
%ifnarch ppc64 s390 s390x
#ext/threads-shared/t/stress test fails on z10
export PERL_CORE=1
make test
%endif

%post libs -p /sbin/ldconfig

%postun libs -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%doc Artistic AUTHORS Copying README Changes
%{_mandir}/man1/*.1*
%{_mandir}/man3/*.3*
%{_bindir}/*
%{privlib}
%{archlib}/*
%{privlib}/vendor_perl
%exclude %{archlib}/vendor_perl
%{_prefix}/local/share/perl5

# libs
%exclude %{archlib}/CORE/libperl.so
%exclude %{_libdir}/perl5/5.10.0/%{perl_archname}/CORE/libperl.so

# devel
%exclude %{_bindir}/enc2xs
%exclude %{_mandir}/man1/enc2xs*
%exclude %{privlib}/Encode/
%exclude %{_bindir}/h2xs
%exclude %{_mandir}/man1/h2xs*
%exclude %{_bindir}/libnetcfg
%exclude %{_mandir}/man1/libnetcfg*
%exclude %{_bindir}/perlivp
%exclude %{_mandir}/man1/perlivp*
%exclude %{archlib}/CORE/*.h
%exclude %{_bindir}/xsubpp
%exclude %{_mandir}/man1/xsubpp*

# suidperl
%exclude %{_bindir}/suidperl
%exclude %{_bindir}/sperl%{perl_version}

# Archive-Extract
%exclude %{privlib}/Archive/Extract.pm
%exclude %{_mandir}/man3/Archive::Extract.3*

# Archive-Tar
%exclude %{_bindir}/ptar
%exclude %{_bindir}/ptardiff
%exclude %{privlib}/Archive/Tar/
%exclude %{privlib}/Archive/Tar.pm
%exclude %{_mandir}/man1/ptar.1*
%exclude %{_mandir}/man1/ptardiff.1*
%exclude %{_mandir}/man3/Archive::Tar*

# CPAN
%exclude %{_bindir}/cpan
%exclude %{privlib}/CPAN/
%exclude %{privlib}/CPAN.pm
%exclude %{_mandir}/man1/cpan.1*
%exclude %{_mandir}/man3/CPAN.*
%exclude %{_mandir}/man3/CPAN:*

# Parse-CPAN-Meta
%exclude %dir %{privlib}/Parse/
%exclude %dir %{privlib}/Parse/CPAN/
%exclude %{privlib}/Parse/CPAN/Meta.pm
%exclude %{_mandir}/man3/Parse::CPAN::Meta.3*

# CPANPLUS
%exclude %{_bindir}/cpan2dist
%exclude %{_bindir}/cpanp
%exclude %{_bindir}/cpanp-run-perl
%exclude %{privlib}/CPANPLUS/
%exclude %{privlib}/CPANPLUS.pm
%exclude %{_mandir}/man1/cpan2dist.1*
%exclude %{_mandir}/man1/cpanp.1*
%exclude %{_mandir}/man3/CPANPLUS*

#CGI
%exclude %{privlib}/CGI/
%exclude %{privlib}/CGI.pm
%exclude %{_mandir}/man3/CGI*

# Compress::Raw::Zlib
%exclude %{archlib}/Compress
%exclude %{archlib}/Compress/Raw/
%exclude %{archlib}/auto/Compress
%exclude %{archlib}/auto/Compress/Raw/
%exclude %{_mandir}/man3/Compress::Raw::Zlib*

# Compress::Zlib
%exclude %{archlib}/Compress/Zlib.pm
%exclude %{archlib}/auto/Compress/Zlib/
%exclude %{_mandir}/man3/Compress::Zlib*

# Digest::SHA
%exclude %{_bindir}/shasum
%exclude %{archlib}/Digest/SHA.pm
%exclude %{archlib}/auto/Digest/SHA/
%exclude %{_mandir}/man1/shasum.1*
%exclude %{_mandir}/man3/Digest::SHA.3*

# ExtUtils::CBuilder
%exclude %{privlib}/ExtUtils/CBuilder/
%exclude %{privlib}/ExtUtils/CBuilder.pm
%exclude %{_mandir}/man3/ExtUtils::CBuilder*

# ExtUtils::Embed
%exclude %{privlib}/ExtUtils/Embed.pm
%exclude %{_mandir}/man3/ExtUtils::Embed*

# ExtUtils::MakeMaker
%exclude %{_bindir}/instmodsh
%exclude %{privlib}/ExtUtils/Command/
%exclude %{privlib}/ExtUtils/Install.pm
%exclude %{privlib}/ExtUtils/Installed.pm
%exclude %{privlib}/ExtUtils/Liblist/
%exclude %{privlib}/ExtUtils/Liblist.pm
%exclude %{privlib}/ExtUtils/MakeMaker/
%exclude %{privlib}/ExtUtils/MakeMaker.pm
%exclude %{privlib}/ExtUtils/MANIFEST.SKIP
%exclude %{privlib}/ExtUtils/MM*.pm
%exclude %{privlib}/ExtUtils/MY.pm
%exclude %{privlib}/ExtUtils/Manifest.pm
%exclude %{privlib}/ExtUtils/Mkbootstrap.pm
%exclude %{privlib}/ExtUtils/Mksymlists.pm
%exclude %{privlib}/ExtUtils/Packlist.pm
%exclude %{privlib}/ExtUtils/testlib.pm
%exclude %{_mandir}/man1/instmodsh.1*
%exclude %{_mandir}/man3/ExtUtils::Command::MM*
%exclude %{_mandir}/man3/ExtUtils::Install.3*
%exclude %{_mandir}/man3/ExtUtils::Installed.3*
%exclude %{_mandir}/man3/ExtUtils::Liblist.3*
%exclude %{_mandir}/man3/ExtUtils::MM*
%exclude %{_mandir}/man3/ExtUtils::MY.3*
%exclude %{_mandir}/man3/ExtUtils::MakeMaker*
%exclude %{_mandir}/man3/ExtUtils::Manifest.3*
%exclude %{_mandir}/man3/ExtUtils::Mkbootstrap.3*
%exclude %{_mandir}/man3/ExtUtils::Mksymlists.3*
%exclude %{_mandir}/man3/ExtUtils::Packlist.3*
%exclude %{_mandir}/man3/ExtUtils::testlib.3*

# ExtUtils::ParseXS
%exclude %{privlib}/ExtUtils/ParseXS.pm
%exclude %{privlib}/ExtUtils/xsubpp
%exclude %{_mandir}/man3/ExtUtils::ParseXS.3*

# File::Fetch
%exclude %{privlib}/File/Fetch.pm
%exclude %{_mandir}/man3/File::Fetch.3*

# IO::Compress::Base
%exclude %{archlib}/File/GlobMapper.pm
%exclude %{archlib}/IO/Compress/Base/
%exclude %{archlib}/IO/Compress/Base.pm
%exclude %{archlib}/IO/Uncompress/AnyUncompress.pm
%exclude %{archlib}/IO/Uncompress/Base.pm
%exclude %{_mandir}/man3/File::GlobMapper.*
%exclude %{_mandir}/man3/IO::Compress::Base.*
%exclude %{_mandir}/man3/IO::Uncompress::AnyUncompress.*
%exclude %{_mandir}/man3/IO::Uncompress::Base.*

# IO::Compress::Zlib
%exclude %{archlib}/IO/Compress/Adapter/
%exclude %{archlib}/IO/Compress/Deflate.pm
%exclude %{archlib}/IO/Compress/Gzip/
%exclude %{archlib}/IO/Compress/Gzip.pm
%exclude %{archlib}/IO/Compress/RawDeflate.pm
%exclude %{archlib}/IO/Compress/Zip/
%exclude %{archlib}/IO/Compress/Zip.pm
%exclude %{archlib}/IO/Compress/Zlib/
%exclude %{archlib}/IO/Uncompress/Adapter/
%exclude %{archlib}/IO/Uncompress/AnyInflate.pm
%exclude %{archlib}/IO/Uncompress/Gunzip.pm
%exclude %{archlib}/IO/Uncompress/Inflate.pm
%exclude %{archlib}/IO/Uncompress/RawInflate.pm
%exclude %{archlib}/IO/Uncompress/Unzip.pm
%exclude %{_mandir}/man3/IO::Compress::Deflate*
%exclude %{_mandir}/man3/IO::Compress::Gzip*
%exclude %{_mandir}/man3/IO::Compress::RawDeflate*
%exclude %{_mandir}/man3/IO::Compress::Zip*
%exclude %{_mandir}/man3/IO::Uncompress::AnyInflate*
%exclude %{_mandir}/man3/IO::Uncompress::Gunzip*
%exclude %{_mandir}/man3/IO::Uncompress::Inflate*
%exclude %{_mandir}/man3/IO::Uncompress::RawInflate*
%exclude %{_mandir}/man3/IO::Uncompress::Unzip*

# IO::Zlib
%exclude %{privlib}/IO/Zlib.pm
%exclude %{_mandir}/man3/IO::Zlib.*

# IPC::Cmd
%exclude %{privlib}/IPC/Cmd.pm
%exclude %{_mandir}/man3/IPC::Cmd.3*

# Locale::Maketext::Simple
%exclude %{privlib}/Locale/Maketext/Simple.pm
%exclude %{_mandir}/man3/Locale::Maketext::Simple.*

# Log::Message
%exclude %{privlib}/Log/Message.pm
%exclude %{privlib}/Log/Message/Config.pm
%exclude %{privlib}/Log/Message/Handlers.pm
%exclude %{privlib}/Log/Message/Item.pm
%exclude %{_mandir}/man3/Log::Message.3*
%exclude %{_mandir}/man3/Log::Message::Config.3*
%exclude %{_mandir}/man3/Log::Message::Handlers.3*
%exclude %{_mandir}/man3/Log::Message::Item.3*

# Log::Message::Simple
%exclude %{privlib}/Log/Message/Simple.pm
%exclude %{_mandir}/man3/Log::Message::Simple.3*

# Module::Build
%exclude %{_bindir}/config_data
%exclude %{privlib}/Module/Build/
%exclude %{privlib}/Module/Build.pm
%exclude %{_mandir}/man1/config_data.1*
%exclude %{_mandir}/man3/Module::Build*

# Module-CoreList
%exclude %{_bindir}/corelist
%exclude %{privlib}/Module/CoreList.pm
%exclude %{_mandir}/man1/corelist*
%exclude %{_mandir}/man3/Module::CoreList*

# Module-Load
%exclude %{privlib}/Module/Load.pm
%exclude %{_mandir}/man3/Module::Load.*

# Module-Load-Conditional
%exclude %{privlib}/Module/Load/
%exclude %{_mandir}/man3/Module::Load::Conditional*

# Module-Loaded
%exclude %{privlib}/Module/Loaded.pm
%exclude %{_mandir}/man3/Module::Loaded*

# Module-Pluggable
%exclude %{privlib}/Devel/InnerPackage.pm
%exclude %{privlib}/Module/Pluggable/
%exclude %{privlib}/Module/Pluggable.pm
%exclude %{_mandir}/man3/Devel::InnerPackage*
%exclude %{_mandir}/man3/Module::Pluggable*

# Object-Accessor
%exclude %{privlib}/Object/
%exclude %{_mandir}/man3/Object::Accessor*

# Package-Constants
%exclude %{privlib}/Package/
%exclude %{_mandir}/man3/Package::Constants*

# Params-Check
%exclude %{privlib}/Params/
%exclude %{_mandir}/man3/Params::Check*

# parent
%exclude %{privlib}/parent.pm
%exclude %{_mandir}/man3/parent.3*

# Pod-Escapes
%exclude %{privlib}/Pod/Escapes.pm
%exclude %{_mandir}/man3/Pod::Escapes.*

# Pod-Simple
%exclude %{privlib}/Pod/Simple/
%exclude %{privlib}/Pod/Simple.pm
%exclude %{privlib}/Pod/Simple.pod
%exclude %{_mandir}/man3/Pod::Simple*

# Term-UI
%exclude %{privlib}/Term/UI.pm
%exclude %{privlib}/Term/UI/
%exclude %{_mandir}/man3/Term::UI*

# Test::Harness
%exclude %{_bindir}/prove
%exclude %{privlib}/App*
%exclude %{privlib}/TAP*
%exclude %{privlib}/Test/Harness*
%exclude %{_mandir}/man1/prove.1*
%exclude %{_mandir}/man3/App*
%exclude %{_mandir}/man3/TAP*
%exclude %{_mandir}/man3/Test::Harness*

# Test::Simple
%exclude %{privlib}/Test/More*
%exclude %{privlib}/Test/Builder*
%exclude %{privlib}/Test/Simple*
%exclude %{privlib}/Test/Tutorial*
%exclude %{_mandir}/man3/Test::More*
%exclude %{_mandir}/man3/Test::Builder*
%exclude %{_mandir}/man3/Test::Simple*
%exclude %{_mandir}/man3/Test::Tutorial*

# Time::HiRes
%exclude %{archlib}/Time/HiRes.pm
%exclude %{archlib}/auto/Time/HiRes/HiRes.so
%exclude %{_mandir}/man3/Time::HiRes.3*

# Time::Piece
%exclude %{archlib}/Time/Piece.pm
%exclude %{archlib}/Time/Seconds.pm
%exclude %{archlib}/auto/Time/Piece/
%exclude %{_mandir}/man3/Time::Piece.3*
%exclude %{_mandir}/man3/Time::Seconds.3*

# version
%exclude %{privlib}/version.pm
%exclude %{privlib}/version.pod
%exclude %{privlib}/version/
%exclude %{_mandir}/man3/version.3*
%exclude %{_mandir}/man3/version::Internals.3*

%files libs
%defattr(-,root,root)
%{archlib}/CORE/libperl.so
%{_libdir}/perl5/5.10.0/%{perl_archname}/CORE/libperl.so
%dir %{archlib}
%dir %{archlib}/vendor_perl
%dir %{_prefix}/local/%{_lib}/perl5

%files devel
%defattr(-,root,root,-)
%{_bindir}/enc2xs
%{_mandir}/man1/enc2xs*
%{privlib}/Encode/
%{_bindir}/h2xs
%{_mandir}/man1/h2xs*
%{_bindir}/libnetcfg
%{_mandir}/man1/libnetcfg*
%{_bindir}/perlivp
%{_mandir}/man1/perlivp*
%{archlib}/CORE/*.h
%{_bindir}/xsubpp
%{_mandir}/man1/xsubpp*
%{_sysconfdir}/rpm/macros.perl

%files suidperl
%defattr(-,root,root,-)
%{_bindir}/suidperl
%{_bindir}/sperl%{perl_version}

%files Archive-Extract
%defattr(-,root,root,-)
%{privlib}/Archive/Extract.pm
%{_mandir}/man3/Archive::Extract.3*

%files Archive-Tar
%defattr(-,root,root,-)
%{_bindir}/ptar
%{_bindir}/ptardiff
%{privlib}/Archive/Tar/ 
%{privlib}/Archive/Tar.pm
%{_mandir}/man1/ptar.1*
%{_mandir}/man1/ptardiff.1*
%{_mandir}/man3/Archive::Tar* 

%files Compress-Raw-Zlib
%defattr(-,root,root,-)
%dir %{archlib}/Compress
%{archlib}/Compress/Raw/
%dir %{archlib}/auto/Compress/
%{archlib}/auto/Compress/Raw/
%{_mandir}/man3/Compress::Raw::Zlib*

%files Compress-Zlib
%defattr(-,root,root,-)
%{archlib}/Compress/Zlib.pm
%{archlib}/auto/Compress/Zlib/
%{_mandir}/man3/Compress::Zlib*

%files CPAN
%defattr(-,root,root,-)
%{_bindir}/cpan
%{privlib}/CPAN/
%{privlib}/CPAN.pm
%{_mandir}/man1/cpan.1*
%{_mandir}/man3/CPAN.*
%{_mandir}/man3/CPAN:*

%files CPANPLUS
%defattr(-,root,root,-)
%{_bindir}/cpan2dist
%{_bindir}/cpanp
%{_bindir}/cpanp-run-perl
%{privlib}/CPANPLUS/
%{privlib}/CPANPLUS.pm
%{_mandir}/man1/cpan2dist.1*
%{_mandir}/man1/cpanp.1*
%{_mandir}/man3/CPANPLUS*

%files CGI
%defattr(-,root,root,-)
%{privlib}/CGI/
%{privlib}/CGI.pm
%{_mandir}/man3/CGI*

%files Digest-SHA
%defattr(-,root,root,-)
%{_bindir}/shasum
%dir %{archlib}/Digest/
%{archlib}/Digest/SHA.pm
%{archlib}/auto/Digest/SHA/
%{_mandir}/man1/shasum.1*
%{_mandir}/man3/Digest::SHA.3*

%files ExtUtils-CBuilder
%defattr(-,root,root,-)
%{privlib}/ExtUtils/CBuilder/
%{privlib}/ExtUtils/CBuilder.pm
%{_mandir}/man3/ExtUtils::CBuilder*

%files ExtUtils-Embed
%defattr(-,root,root,-)
%{privlib}/ExtUtils/Embed.pm
%{_mandir}/man3/ExtUtils::Embed*

%files ExtUtils-MakeMaker
%defattr(-,root,root,-)
%{_bindir}/instmodsh
%{privlib}/ExtUtils/Command/
%{privlib}/ExtUtils/Install.pm
%{privlib}/ExtUtils/Installed.pm
%{privlib}/ExtUtils/Liblist/
%{privlib}/ExtUtils/Liblist.pm
%{privlib}/ExtUtils/MakeMaker/
%{privlib}/ExtUtils/MakeMaker.pm
%{privlib}/ExtUtils/MANIFEST.SKIP
%{privlib}/ExtUtils/MM*.pm
%{privlib}/ExtUtils/MY.pm
%{privlib}/ExtUtils/Manifest.pm
%{privlib}/ExtUtils/Mkbootstrap.pm
%{privlib}/ExtUtils/Mksymlists.pm
%{privlib}/ExtUtils/Packlist.pm
%{privlib}/ExtUtils/testlib.pm
%{_mandir}/man1/instmodsh.1*
%{_mandir}/man3/ExtUtils::Command::MM*
%{_mandir}/man3/ExtUtils::Install.3*
%{_mandir}/man3/ExtUtils::Installed.3*
%{_mandir}/man3/ExtUtils::Liblist.3*
%{_mandir}/man3/ExtUtils::MM*
%{_mandir}/man3/ExtUtils::MY.3*
%{_mandir}/man3/ExtUtils::MakeMaker*
%{_mandir}/man3/ExtUtils::Manifest.3*
%{_mandir}/man3/ExtUtils::Mkbootstrap.3*
%{_mandir}/man3/ExtUtils::Mksymlists.3*
%{_mandir}/man3/ExtUtils::Packlist.3*
%{_mandir}/man3/ExtUtils::testlib.3*

%files ExtUtils-ParseXS
%defattr(-,root,root,-)
%{privlib}/ExtUtils/ParseXS.pm
%{privlib}/ExtUtils/xsubpp
%{_mandir}/man3/ExtUtils::ParseXS.3*

%files File-Fetch
%defattr(-,root,root,-)
%{privlib}/File/Fetch.pm
%{_mandir}/man3/File::Fetch.3*

%files IO-Compress-Base
%defattr(-,root,root,-)
%{archlib}/File/GlobMapper.pm
%{archlib}/IO/Compress/Base/
%{archlib}/IO/Compress/Base.pm
%{archlib}/IO/Uncompress/AnyUncompress.pm
%{archlib}/IO/Uncompress/Base.pm
%{_mandir}/man3/File::GlobMapper.*
%{_mandir}/man3/IO::Compress::Base.*
%{_mandir}/man3/IO::Uncompress::AnyUncompress.*
%{_mandir}/man3/IO::Uncompress::Base.*

%files IO-Compress-Zlib
%defattr(-,root,root,-)
%{archlib}/IO/Compress/Adapter/
%{archlib}/IO/Compress/Deflate.pm
%{archlib}/IO/Compress/Gzip/
%{archlib}/IO/Compress/Gzip.pm
%{archlib}/IO/Compress/RawDeflate.pm
%{archlib}/IO/Compress/Zip/
%{archlib}/IO/Compress/Zip.pm
%{archlib}/IO/Compress/Zlib/
%{archlib}/IO/Uncompress/Adapter/
%{archlib}/IO/Uncompress/AnyInflate.pm
%{archlib}/IO/Uncompress/Gunzip.pm
%{archlib}/IO/Uncompress/Inflate.pm
%{archlib}/IO/Uncompress/RawInflate.pm
%{archlib}/IO/Uncompress/Unzip.pm
%{_mandir}/man3/IO::Compress::Deflate*
%{_mandir}/man3/IO::Compress::Gzip*
%{_mandir}/man3/IO::Compress::RawDeflate*
%{_mandir}/man3/IO::Compress::Zip*
%{_mandir}/man3/IO::Uncompress::AnyInflate*
%{_mandir}/man3/IO::Uncompress::Gunzip*
%{_mandir}/man3/IO::Uncompress::Inflate*
%{_mandir}/man3/IO::Uncompress::RawInflate*
%{_mandir}/man3/IO::Uncompress::Unzip*

%files IO-Zlib
%defattr(-,root,root,-)
%{privlib}/IO/Zlib.pm
%{_mandir}/man3/IO::Zlib.*

%files IPC-Cmd
%defattr(-,root,root,-)
%{privlib}/IPC/Cmd.pm
%{_mandir}/man3/IPC::Cmd.3*

%files Locale-Maketext-Simple
%defattr(-,root,root,-)
%{privlib}/Locale/Maketext/Simple.pm
%{_mandir}/man3/Locale::Maketext::Simple.*

%files Log-Message
%defattr(-,root,root,-)
%{privlib}/Log/Message.pm
%{privlib}/Log/Message/Config.pm
%{privlib}/Log/Message/Handlers.pm
%{privlib}/Log/Message/Item.pm
%{_mandir}/man3/Log::Message.3*
%{_mandir}/man3/Log::Message::Config.3*
%{_mandir}/man3/Log::Message::Handlers.3*
%{_mandir}/man3/Log::Message::Item.3*

%files Log-Message-Simple
%defattr(-,root,root,-)
%{privlib}/Log/Message/Simple.pm
%{_mandir}/man3/Log::Message::Simple.3*

%files Module-Build
%defattr(-,root,root,-)
%{_bindir}/config_data
%{privlib}/Module/Build/
%{privlib}/Module/Build.pm
%{_mandir}/man1/config_data.1*
%{_mandir}/man3/Module::Build*

%files Module-CoreList
%defattr(-,root,root,-)
%{_bindir}/corelist
%{privlib}/Module/CoreList.pm
%{_mandir}/man1/corelist*
%{_mandir}/man3/Module::CoreList*

%files Module-Load
%defattr(-,root,root,-)
%{privlib}/Module/Load.pm
%{_mandir}/man3/Module::Load.*

%files Module-Load-Conditional
%defattr(-,root,root,-)
%{privlib}/Module/Load/
%{_mandir}/man3/Module::Load::Conditional* 

%files Module-Loaded
%defattr(-,root,root,-)
%dir %{privlib}/Module/
%{privlib}/Module/Loaded.pm
%{_mandir}/man3/Module::Loaded*

%files Module-Pluggable
%defattr(-,root,root,-)
%{privlib}/Devel/InnerPackage.pm
%{privlib}/Module/Pluggable/
%{privlib}/Module/Pluggable.pm
%{_mandir}/man3/Devel::InnerPackage*
%{_mandir}/man3/Module::Pluggable*

%files Object-Accessor
%defattr(-,root,root,-)
%{privlib}/Object/
%{_mandir}/man3/Object::Accessor*

%files Package-Constants
%defattr(-,root,root,-)
%{privlib}/Package/
%{_mandir}/man3/Package::Constants*

%files Params-Check
%defattr(-,root,root,-)
%{privlib}/Params/
%{_mandir}/man3/Params::Check*

%files Parse-CPAN-Meta
%defattr(-,root,root,-)
%dir %{privlib}/Parse/
%dir %{privlib}/Parse/CPAN/
%{privlib}/Parse/CPAN/Meta.pm
%{_mandir}/man3/Parse::CPAN::Meta.3*

%files Pod-Escapes
%defattr(-,root,root,-)
%{privlib}/Pod/Escapes.pm
%{_mandir}/man3/Pod::Escapes.*

%files Pod-Simple
%defattr(-,root,root,-)
%{privlib}/Pod/Simple/ 
%{privlib}/Pod/Simple.pm
%{privlib}/Pod/Simple.pod
%{_mandir}/man3/Pod::Simple*

%files Term-UI
%defattr(-,root,root,-)
%{privlib}/Term/UI/
%{privlib}/Term/UI.pm
%{_mandir}/man3/Term::UI*

%files Test-Harness
%defattr(-,root,root,-)
%{_bindir}/prove
%{privlib}/App*
%{privlib}/TAP*
%{privlib}/Test/Harness*
%{_mandir}/man1/prove.1*
%{_mandir}/man3/App*
%{_mandir}/man3/TAP*
%{_mandir}/man3/Test::Harness*

%files Test-Simple
%defattr(-,root,root,-)
%{privlib}/Test/More*
%{privlib}/Test/Builder*
%{privlib}/Test/Simple*
%{privlib}/Test/Tutorial*
%{_mandir}/man3/Test::More*
%{_mandir}/man3/Test::Builder*
%{_mandir}/man3/Test::Simple*
%{_mandir}/man3/Test::Tutorial*

%files Time-HiRes
%defattr(-,root,root,-)
%{archlib}/Time/HiRes.pm
%{archlib}/auto/Time/HiRes/HiRes.so
%{_mandir}/man3/Time::HiRes.3*

%files Time-Piece
%defattr(-,root,root,-)
%{archlib}/Time/Piece.pm 
%{archlib}/Time/Seconds.pm
%{archlib}/auto/Time/Piece/        
%{_mandir}/man3/Time::Piece.3*
%{_mandir}/man3/Time::Seconds.3*

%files parent 
%defattr(-,root,root,-)
%{privlib}/parent.pm
%{_mandir}/man3/parent.3*

%files version
%defattr(-,root,root,-)
%{privlib}/version.pm
%{privlib}/version.pod
%{privlib}/version/
%{_mandir}/man3/version.3*
%{_mandir}/man3/version::Internals.3*

%files core
# Nothing. Nada. Zilch. Zarro. Uh uh. Nope. Sorry.

# Old changelog entries are preserved in CVS.
%changelog
* Mon Jul 19 2010 Petr Pisar <ppisar@redhat.com> - 4:5.10.1-115
- Resolves: #614917 - Remove trailing slashes from vendor paths

* Thu Jul 16 2010 Petr Pisar <ppisar@redhat.com> - 4:5.10.1-114
- Remove unused @INC paths
- Own all used @INC paths
- Own architecture dependent paths by perl-libs due to multiarch
- Resolves: rhbz#554671

* Wed Jun 30 2010 Petr Pisar <ppisar@redhat.com> - 4:5.10.1-113
- fix CGI test data location to pass internal tests 
- remove CPAN and CPANPLUS sysconfig declarations as they are not provided
- disable tests on s390(x) and ppc64 as multithread stress tests fails
- Related: rhbz#594768

* Wed Jun 30 2010 Petr Pisar <ppisar@redhat.com> - 4:5.10.1-112
- fix Archive::Tar to return correct code on failed extraction
- Resolves: rhbz#606813

* Wed Jun 30 2010 Marcela Mašláňová <mmaslano@redhat.com> - 4:5.10.1-111
- fix conflicts in specfile, upload missing sources, upload patch with
 wrong name
- Related: rhbz# 594768

* Tue Jun  8 2010 Marcela Mašláňová <mmaslano@redhat.com> - 4:5.10.1-110
- set CPAN installation path into "site"
- 'make local' now pass because of Patch0, which removes incorectly set
 dependencies
- Related: rhbz#594768

* Fri Jun  4 2010 Marcela Mašláňová <mmaslano@redhat.com> - 4:5.10.1-110
- 597982 add all version* in -version sub-package
- Resolves: rhbz#597982, rhbz#598397, rhbz#595387, rhbz#595387

* Wed Apr 14 2010 Marcela Mašláňová <mmaslano@redhat.com> - 4:5.10.1-109
- fix macro of Module::Build again
- Resolves: rhbz#580238

* Tue Mar 30 2010 Marcela Mašláňová <mmaslano@redhat.com> - 4:5.10.1-108
- remove DPERL_USE_SAFE_PUTENV from Configure #577229 Use perl internal
 putenv, which doesn't leak memory.
- 580238 wrong version of module
Resolves: rhbz#580238

* Wed Mar  3 2010 Marcela Mašláňová <mmaslano@redhat.com> - 4:5.10.1-107
- clean spec - remove unused patches, rename patches, sources
- add releases macros for all modules
- change license according to legal
- update modules to stable version. e.g. Module-Build can't be updated anymore
  because of API breakage, that's true also for some other modules.
- Related: rhbz#543948

* Tue Jan 19 2010 Marcela Mašláňová <mmaslano@redhat.com> - 4:5.10.1-106
- 554654 -  "perldoc perlvar" renders incorrectly in C and en_US.UTF-8 locales.
- 554666 -  Wrong man pages location specified in perl manual page
- Resolves: rhbz#554654, rhbz#554666

* Tue Dec 22 2009 Marcela Mašláňová <mmaslano@redhat.com> - 4:5.10.1-105
- 547657 CVE-2009-3626 perl: regexp matcher crash on invalid UTF-8 characters  
- 549306 version::Internals should be packaged in perl-version subpackage
- Parse-CPAN-Meta updated and separate package is dead
- subpackage parent and Parse-CPAN-Meta; add them to core's dep list
- exclude "parent".
- exclude Parse-CPAN-Meta.
Resolves: rhbz#547657

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 4:5.10.1-104
- do not pack Bzip2 manpages either (#544582)

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 4:5.10.1-103
- do not pack Bzip2 modules (#544582)
- hack: cheat about Compress::Raw::Zlib version (#544582)

* Thu Dec  3 2009 Stepan Kasal <skasal@redhat.com> - 4:5.10.1-102
- switch off check for ppc64 and s390x
- remove the hack for "make test," it is no longer needed

* Thu Dec  3 2009 Stepan Kasal <skasal@redhat.com> - 4:5.10.1-101
- be more careful with the libperl.so compatibility symlink (#543936)

* Wed Dec  2 2009 Stepan Kasal <skasal@redhat.com> - 4:5.10.1-100
- new upstream version
- release number must be high, because of stale version numbers of some
  of the subpackages
- drop upstreamed patches
- update the versions of bundled modules
- shorten the paths in @INC
- build without DEBUGGING
- implement compatibility measures for the above two changes, for a short
  transition period
- provide perl(:MODULE_COMPAT_5.10.0), for that transition period only

* Tue Dec  1 2009 Stepan Kasal <skasal@redhat.com> - 4:5.10.0-87
- fix patch-update-Compress-Raw-Zlib.patch (did not patch Zlib.pm)
- update Compress::Raw::Zlib to 2.023
- update IO::Compress::Base, and IO::Compress::Zlib to 2.015 (#542645)

* Mon Nov 30 2009 Marcela Mašláňová <mmaslano@redhat.com> - 4:5.10.0-86
- 542645 update IO-Compress-Base

* Tue Nov 24 2009 Stepan Kasal <skasal@redhat.com> - 4:5.10.0-85
- back out perl-5.10.0-spamassassin.patch (#528572)

* Thu Oct 01 2009 Chris Weyl <cweyl@alumni.drew.edu> - 4:5.10.0-84
- add /perl(UNIVERSAL)/d; /perl(DB)/d to perl_default_filter auto-provides
  filtering

* Thu Oct  1 2009 Stepan Kasal <skasal@redhat.com> - 4:5.10.0-83
- update Storable to 2.21

* Mon Aug 31 2009 Chris Weyl <cweyl@alumni.drew.edu> - 4:5.10.0-82
- update our Test-Simple update to 0.92 (patch by Iain Arnell), #519417
- update Module-Pluggable to 3.9

* Thu Aug 27 2009 Chris Weyl <cweyl@alumni.drew.edu> - 4:5.10.0-81
- fix macros.perl *sigh*

* Mon Aug 24 2009 Stepan Kasal <skasal@redhat.com> - 4:5.10.0-80
- Remove -DDEBUGGING=-g, we are not ready yet.

* Fri Aug 21 2009 Chris Weyl <cweyl@alumni.drew.edu> - 4:5.10.0-79
- add helper filtering macros to -devel, for perl-* package invocation
  (#502402)

* Fri Jul 31 2009 Stepan Kasal <skasal@redhat.com> - 4:5.10.0-78
- Add configure option -DDEBUGGING=-g (#156113)

* Tue Jul 28 2009 arcela Mašláňová <mmaslano@redhat.com> - 4:5.10.0-77
- 510127 spam assassin suffer from tainted bug

* Mon Jul 27 2009 Marcela Mašláňová <mmaslano@redhat.com> - 4:5.10.0-76
- 494773 much better swap logic to support reentrancy and fix assert failure (rt #60508)

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4:5.10.0-75
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Fri Jul 10 2009 Stepan Kasal <skasal@redhat.com> - 4:5.10.0-74
- fix generated .ph files so that they no longer cause warnings (#509676)
- remove PREREQ_FATAL from Makefile.PL's processed by miniperl
- update to latest Scalar-List-Utils (#507378)
- perl-skip-prereq.patch: skip more prereq declarations in Makefile.PL files

* Tue Jul  7 2009 Stepan Kasal <skasal@redhat.com> - 4:5.10.0-73
- re-enable tests

* Tue Jul  7 2009 Stepan Kasal <skasal@redhat.com> - 4:5.10.0-72
- move -DPERL_USE_SAFE_PUTENV to ccflags (#508496)

* Mon Jun  8 2009 Marcela Mašláňová <mmaslano@redhat.com> - 4:5.10.0-71
- #504386 update of Compress::Raw::Zlib 2.020

* Thu Jun  4 2009 Marcela Mašláňová <mmaslano@redhat.com> - 4:5.10.0-70
- update File::Spec (PathTools) to 3.30

* Wed Jun  3 2009 Stepan Kasal <skasal@redhat.com> - 4:5.10.0-69
- fix #221113, $! wrongly set when EOF is reached

* Fri Apr 10 2009 Marcela Mašláňová <mmaslano@redhat.com> - 4:5.10.0-68
- do not use quotes in patchlevel.h; it breaks installation from cpan (#495183)

* Tue Apr  7 2009 Stepan Kasal <skasal@redhat.com> - 4:5.10.0-67
- update CGI to 3.43, dropping upstreamed perl-CGI-escape.patch

* Tue Apr  7 2009 Stepan Kasal <skasal@redhat.com> - 4:5.10.0-66
- fix CGI::escape for all strings (#472571)
- perl-CGI-t-util-58.patch: Do not distort lib/CGI/t/util-58.t
  http://rt.perl.org/rt3/Ticket/Display.html?id=64502

* Fri Mar 27 2009 Stepan Kasal <skasal@redhat.com> - 4:5.10.0-65
- Move the gargantuan Changes* collection to -devel (#492605)

* Tue Mar 24 2009 Stepan Kasal <skasal@redhat.com> - 4:5.10.0-64
- update module autodie

* Mon Mar 23 2009 Stepan Kasal <skasal@redhat.com> - 4:5.10.0-63
- update Digest::SHA (fixes 489221)

* Wed Mar 11 2009 Tom "spot" Callaway <tcallawa@redhat.com> - 4:5.10.0-62
- drop 26_fix_pod2man_upgrade (don't need it)
- fix typo in %%define ExtUtils_CBuilder_version

* Wed Mar 11 2009 Tom "spot" Callaway <tcallawa@redhat.com> - 4:5.10.0-61
- apply Change 34507: Fix memory leak in single-char character class optimization
- Reorder @INC, based on b9ba2fadb18b54e35e5de54f945111a56cbcb249
- fix Archive::Extract to fix test failure caused by tar >= 1.21
- Merge useful Debian patches

* Tue Mar 10 2009 Stepan Kasal <skasal@redhat.com> - 4:5.10.0-60
- remove compatibility obsolete sitelib directories
- use a better BuildRoot
- drop a redundant mkdir in %%install
- call patchlevel.h only once; rm patchlevel.bak
- update modules Sys::Syslog, Module::Load::Conditional, Module::CoreList,
  Test::Harness, Test::Simple, CGI.pm (dropping the upstreamed patch),
  File::Path (that includes our perl-5.10.0-CVE-2008-2827.patch),
  constant, Pod::Simple, Archive::Tar, Archive::Extract, File::Fetch,
  File::Temp, IPC::Cmd, Time::HiRes, Module::Build, ExtUtils::CBuilder
- standardize the patches for updating embedded modules
- work around a bug in Module::Build tests bu setting TMPDIR to a directory
  inside the source tree

* Sun Mar 08 2009 Robert Scheck <robert@fedoraproject.org> - 4:5.10.0-59
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Feb 16 2009 Tom "spot" Callaway <tcallawa@redhat.com> - 4:5.10.0-58
- add /usr/lib/perl5/site_perl to otherlibs (bz 484053)

* Mon Feb 16 2009 Dennis Gilmore <dennis@ausil.us> - 4:5.10.0-57
- build sparc64 without _smp_mflags

* Sat Feb 07 2009 Dennis Gilmore <dennis@ausil.us> - 4:5.10.0-56
- limit sparc builds to -j12

* Tue Feb  3 2009 Marcela Mašláňová <mmaslano@redhat.com> - 4:5.10.0-55
- update IPC::Cmd to v 0.42

* Mon Jan 19 2009 Marcela Mašláňová <mmaslano@redhat.com> - 4:5.10.0-54
- 455410 http://rt.perl.org/rt3/Public/Bug/Display.html?id=54934
  Attempt to free unreferenced scalar fiddling with the symbol table
  Keep the refcount of the globs generated by PerlIO::via balanced.

* Mon Dec 22 2008 Marcela Mašláňová <mmaslano@redhat.com> - 4:5.10.0-53
- add missing XHTML.pm into Pod::Simple

* Thu Dec 12 2008 Marcela Mašláňová <mmaslano@redhat.com> - 4:5.10.0-52
- 295021 CVE-2007-4829 perl-Archive-Tar directory traversal flaws
- add another source for binary files, which test untaring links

* Fri Nov 28 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 4:5.10.0-51
- to fix Fedora bz 473223, which is really perl bug #54186 (http://rt.perl.org/rt3//Public/Bug/Display.html?id=54186)
  we apply Changes 33640, 33881, 33896, 33897

* Mon Nov 24 2008 Marcela Mašláňová <mmaslano@redhat.com> - 4:5.10.0-50
- change summary according to RFC fix summary discussion at fedora-devel :)

* Thu Oct 23 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 4:5.10.0-49
- update File::Temp to 0.20

* Sun Oct 12 2008 Lubomir Rintel <lkundrak@v3.sk> - 4:5.10.0-48
- Include fix for rt#52740 to fix a crash when using Devel::Symdump and
  Compress::Zlib together

* Tue Oct 07 2008 Marcela Mašláňová <mmaslano@redhat.com> 4:5.10.0-47.fc10
- rt#33242, rhbz#459918. Segfault after reblessing objects in Storable.
- rhbz#465728 upgrade Simple::Pod to 3.07

* Wed Oct  1 2008 Stepan Kasal <skasal@redhat.com> - 4:5.10.0-46
- also preserve the timestamp of AUTHORS; move the fix to the recode
  function, which is where the stamps go wrong

* Wed Oct  1 2008 Tom "spot" Callaway <tcallawa@redhat.com> 4:5.10.0-45
- give Changes*.gz the same datetime to avoid multilib conflict

* Wed Sep 17 2008 Marcela Maslanova <mmaslano@redhat.com> 4:5.10.0-44.fc10
- remove Tar.pm from Archive-Extract
- fix version of Test::Simple in spec
- update Test::Simple
- update Archive::Tar to 1.38

* Tue Sep 16 2008 Marcela Maslanova <mmaslano@redhat.com> 4:5.10.0-43.fc10
- 462444 update Test::Simple to 0.80

* Thu Aug 14 2008 Stepan Kasal <skasal@redhat.com> - 4:5.10.0-42.fc10
- move libnet to the right directory, along Net/Config.pm

* Wed Aug 13 2008 Stepan Kasal <skasal@redhat.com> - 4:5.10.0-41.fc10
- do not create directory .../%%{version}/auto

* Tue Aug  5 2008 Marcela Maslanova <mmaslano@redhat.com> 4:5.10.0-40.fc10
- 457867 remove required IPC::Run from CPANPLUS - needed only by win32
- 457771 add path

* Fri Aug  1 2008 Stepan Kasal <skasal@redhat.com> 4:5.10.0-39.fc10
- CGI.pm bug in exists() on tied param hash (#457085)
- move the enc2xs templates (../Encode/*.e2x) to -devel, (#456534)

* Mon Jul 21 2008 Marcela Maslanova <mmaslano@redhat.com> 4:5.10.0-38
- 455933 update to CGI-3.38
- fix fuzz problems (patch6)
- 217833 pos() function handle unicode characters correct

* Thu Jul 10 2008 Tom "spot" Callaway <tcallawa@redhat.com> 4:5.10.0-36
- rebuild for new db4 4.7

* Wed Jul  9 2008 Stepan Kasal <skasal@redhat.com> 4:5.10.0-35
- remove db4 require, it is handled automatically

* Thu Jul  3 2008 Stepan Kasal <skasal@redhat.com> 4:5.10.0-34
- 453646 use -DPERL_USE_SAFE_PUTENV. Without fail some modules f.e. readline.

* Tue Jul  1 2008 Marcela Maslanova <mmaslano@redhat.com> 4:5.10.0-33
- 451078 update Test::Harness to 3.12 for more testing. Removed verbose 
test, new Test::Harness has possibly verbose output, but updated package
has a lot of features f.e. TAP::Harness. Carefully watched all new bugs 
related to tests!

* Fri Jun 27 2008 Stepan Kasal <skasal@redhat.com> 4:5.10.0-32
- bump the release number, so that it is not smaller than in F-9

* Tue Jun 24 2008 Marcela Maslanova <mmaslano@redhat.com> 4:5.10.0-28
- CVE-2008-2827 perl: insecure use of chmod in rmtree

* Wed Jun 11 2008 Marcela Maslanova <mmaslano@redhat.com> 4:5.10.0-27
- 447371 wrong access permission rt49003

* Tue Jun 10 2008 Stepan Kasal <skasal@redhat.com> 4:5.10.0-26
- make config parameter list consistent for 32bit and 64bit platforms,
  add config option -Dinc_version_list=none (#448735)
- use perl_archname consistently
- cleanup of usage of *_lib macros in %%install

* Mon Jun  6 2008 Marcela Maslanova <mmaslano@redhat.com> 4:5.10.0-25
- 449577 rebuild for FTBFS

* Mon May 26 2008 Marcela Maslanova <mmaslano@redhat.com> 4:5.10.0-24
- 448392 upstream fix for assertion

* Thu May 22 2008 Tom "spot" Callaway <tcallawa@redhat.com> 4:5.10.0-23
- sparc64 breaks with the rpath hack patch applied

* Mon May 19 2008 Marcela Maslanova <mmaslano@redhat.com>
- 447142 upgrade CGI to 3.37 (this actually happened in -21 in rawhide.)

* Sat May 17 2008 Tom "spot" Callaway <tcallawa@redhat.com> 4:5.10.0-21
- sparc64 fails two tests under mysterious circumstances. we need to get the
  rest of the tree moving, so we temporarily disable the tests on that arch.

* Tue Mar 18 2008 Tom "spot" Callaway <tcallawa@redhat.com> 4:5.10.0-20
- create the vendor_perl/%%{perl_version}/%%{perl_archname}/auto directory 
  in %%{_libdir} so we own it properly

* Tue Mar 18 2008 Tom "spot" Callaway <tcallawa@redhat.com> 4:5.10.0-19
- fix CPANPLUS-Dist-Build Provides/Obsoletes (bz 437615)
- bump version on Module-CoreList subpackage

* Tue Mar 18 2008 Tom "spot" Callaway <tcallawa@redhat.com> 4:5.10.0-18
- forgot to create the auto directory for multilib vendor_perl dirs

* Tue Mar 18 2008 Tom "spot" Callaway <tcallawa@redhat.com> 4:5.10.0-17
- own multilib vendor_perl directories
- mark Module::CoreList patch in patchlevel.h

* Tue Mar 18 2008 Marcela Maslanova <mmaslano@redhat.com> 4:5.10.0-16
- 437817: RFE: Upgrade Module::CoreList to 2.14

* Wed Mar 12 2008 Marcela Maslanova <mmaslano@redhat.com> 4:5.10.0-15
- xsubpp now lives in perl-devel instead of perl.

* Sat Mar  8 2008 Tom "spot" Callaway <tcallawa@redhat.com> 4:5.10.0-14
- back out Archive::Extract patch, causing odd test failure

* Sat Mar  8 2008 Tom "spot" Callaway <tcallawa@redhat.com> 4:5.10.0-13
- add missing lzma test file

* Fri Mar  7 2008 Tom "spot" Callaway <tcallawa@redhat.com> 4:5.10.0-12
- conditionalize multilib patch report in patchlevel.h
- Update Archive::Extract to 0.26
- Update Module::Load::Conditional to 0.24

* Fri Mar  7 2008 Tom "spot" Callaway <tcallawa@redhat.com> 4:5.10.0-11
- only do it once, and do it for all our patches

* Fri Mar  7 2008 Tom "spot" Callaway <tcallawa@redhat.com> 4:5.10.0-10
- note 32891 in patchlevel.h

* Fri Mar  7 2008 Tom "spot" Callaway <tcallawa@redhat.com> 4:5.10.0-9
- get rid of bad conflicts on perl-File-Temp

* Fri Mar  7 2008 Tom "spot" Callaway <tcallawa@redhat.com> 4:5.10.0-8
- use /usr/local for sitelib/sitearch dirs
- patch 32891 for significant performance improvement

* Fri Feb 22 2008 Stepan Kasal <skasal@redhat.com> - 4:5.10.0-7
- Add perl-File-Temp provides/obsoletes/conflicts (#433836),
  reported by Bill McGonigle <bill@bfccomputing.com>
- escape the macros in Jan 30 entry

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 4:5.10.0-6
- Autorebuild for GCC 4.3

* Wed Jan 30 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 4:5.10.0-5
- disable some futime tests in t/io/fs.t because they started failing on x86_64
  in the Fedora builders, and no one can figure out why. :/

* Wed Jan 30 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 4:5.10.0-4
- create %%{_prefix}/lib/perl5/vendor_perl/%%{perl_version}/auto and own it
  in base perl (resolves bugzilla 214580)

* Thu Jan 10 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 4:5.10.0-3
- Update Sys::Syslog to 0.24, to fix test failures

* Wed Jan 9 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 4:5.10.0-2
- add some BR for tests

* Tue Jan 8 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 4:5.10.0-1
- 5.10.0 final
- clear out all the unnecessary patches (down to 8 patches!)
- get rid of super perl debugging mode
- add new subpackages

* Thu Nov 29 2007 Robin Norwood <rnorwood@redhat.com> - 4:5.10.0_RC2-0.1
- first attempt at building 5.10.0


