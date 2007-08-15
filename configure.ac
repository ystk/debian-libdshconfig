# Process this file with autoconf to produce a configure script.
m4_define(LIBDSHCONFIGVERSION,0.20.13)
AC_INIT(libdshconfig, LIBDSHCONFIGVERSION, dancer@debian.org)
AM_INIT_AUTOMAKE(libdshconfig, LIBDSHCONFIGVERSION)
AM_CONFIG_HEADER(config.h)
AM_MAINTAINER_MODE

AC_PROG_LIBTOOL

# Checks for programs.
AC_PROG_CC
AC_CHECK_PROGS([DOXYGEN], [doxygen], [false])
# Checks for libraries.

# Checks for header files.
AC_HEADER_STDC
AC_CHECK_HEADERS([stdlib.h string.h])

# Checks for typedefs, structures, and compiler characteristics.
AC_C_CONST

# Checks for library functions.
AC_FUNC_MALLOC
AC_CHECK_FUNCS([strchr strdup getline])

vsymldflags=
AC_MSG_CHECKING([version script options])
AC_ARG_WITH([versioned-symbol],AC_HELP_STRING([--with-versioned-symbol],[Use versioned symbols]),[dnl
vsymldflags="-Wl,--version-script,dsh.ver -Wl,-O1"
])
AC_SUBST(vsymldflags)
AC_MSG_RESULT([${vsymldflags}])

AC_CONFIG_FILES([Makefile
libdshconfig.dox])
AC_OUTPUT
