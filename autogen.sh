#!/bin/bash

libtoolize -f -c && aclocal && autoheader && automake --foreign -a -c && autoconf

