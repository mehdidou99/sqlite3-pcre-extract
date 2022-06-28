#!/bin/sh

cc -shared -o pcre.so -I/usr/local/opt/pcre/include  -fPIC -W -Werror pcre.c -L/usr/local/opt/pcre/lib -lpcre
cc -shared -o pcre_extract.so -I/usr/local/opt/pcre/include  -fPIC -W -Werror pcre_extract.c -L/usr/local/opt/pcre/lib -lpcre
