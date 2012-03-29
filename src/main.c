#include <unistd.h>

extern void tick(void);

int
main(int argc, char *argv[])
{
	for (;;) {
		sleep(1);
		tick();
	}

	return (0);
}
