CC		 = gcc

all: build/helloworld

clean:
	-rm -rf build

build:
	mkdir build

#
# The executable combines main.o and dtrace.o (compiled from source) and
# helloworld_provider.o (generated by "dtrace -G").
#
build/helloworld: build/main.o build/dtrace.o build/helloworld_provider.o
	$(CC) -o $@ $^

#
# dtrace.c uses a header file generated by "dtrace -h".
#
build/dtrace.o: build/helloworld_provider.h

build/%.o: src/%.c | build
	$(CC) -Ibuild -c -o $@ $<

build/helloworld_provider.h: src/helloworld_provider.d
	dtrace -xnolibs -h -o $@ -s $<

build/helloworld_provider.o: src/helloworld_provider.d build/dtrace.o
	dtrace -xnolibs -G -o $@ -s $^
