#define _POSIX_C_SOURCE 199309L
#include <time.h>

int main(void)
{
    const struct timespec delay = { 0, 50000000L };
    return nanosleep(&delay, 0);
}
