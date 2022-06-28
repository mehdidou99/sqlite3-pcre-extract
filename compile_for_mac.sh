#!/bin/sh

cc -shared -o pcre.so -I/usr/local/opt/pcre/include  -fPIC -W -Werror pcre.c -L/usr/local/opt/pcre/lib -lpcre
