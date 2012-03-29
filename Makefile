CC		 = gcc
CFLAGS		+= -Wall -Werror

all: helloworld

clean:
	-rm -rf main.o helloworld_provider.o helloworld_provider.h helloworld

#
# The executable combines both main.o (compiled from source) and
# helloworld_provider.o (generated by "dtrace -G").
#
helloworld: main.o helloworld_provider.o
	$(CC) -o $@ $^

#
# The main source file uses a header file generated by "dtrace -h".  We rely on
# the built-in "make" recipe to generate main.o.
#
main.o: helloworld_provider.h

helloworld_provider.h: helloworld_provider.d
	dtrace -xnolibs -h -o $@ -s $<

helloworld_provider.o: helloworld_provider.d main.o
	dtrace -xnolibs -G -o $@ -s $^
