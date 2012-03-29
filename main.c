#include "helloworld_provider.h"

#include <unistd.h>

int
main(int argc, char *argv[])
{
	for (;;) {
		sleep(1);
		HELLOWORLD_TICK();
	}

	return (0);
}
