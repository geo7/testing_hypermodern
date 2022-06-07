from typeguard import typechecked

@typechecked
def something(a : int) -> None:

    if a > 20:
        print("a is greater than 20")
    else:
        print("a is less than 20")


def main() -> int:
    something(3)
    something("what")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())