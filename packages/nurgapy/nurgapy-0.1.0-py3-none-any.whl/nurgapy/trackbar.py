import sys
from datetime import datetime
from datetime import timedelta


def chop_microseconds(delta: timedelta):
    return delta - timedelta(microseconds=delta.microseconds)


def trackbar(it, prefix="", size=80, out=sys.stdout):  # Python3.6+
    count = len(it)

    def show(j, current_time):
        x = int(size * j / count)
        print(
            f"{current_time} {prefix}[{u'█'*x}{('.'*(size-x))}] {j}/{count}",
            end="\r",
            file=out,
            flush=True,
        )

    start_time = datetime.now()
    end_time = datetime.now()
    show(0, chop_microseconds(end_time - start_time))
    for i, item in enumerate(it):
        yield item
        end_time = datetime.now()
        show(i + 1, chop_microseconds(end_time - start_time))
    print("\n", flush=True, file=out)
