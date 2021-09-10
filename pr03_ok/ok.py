"""Make everythung OK."""

import time


def wants_solving():
    """Prompt the user to make everything OK."""
    while True:
        solve_worries = input("would you like to make everything OK?")
        if solve_worries == "Y":
            print("Let`s go.")
            return True
        elif solve_worries == "N":
            print("Alrighty then.")
            return False
        else:
            print("Sorry, try again.")


def progress_bar(process_name, second):
    """Show the user where the process is."""

    cycle_time = second / 20

    if len(process_name) > 25:
        process_name = process_name[:25]

    for i in range(21):
        print(f"\r[{'|' * i:.<20}] | Process: {process_name!r:.25} {0.05 * i:3.0%}", end='')
        time.sleep(cycle_time)
    print()


def print_ok():
    """Prints that everything is OK."""
    print("Everything is OK now.")


def main():
    solve = wants_solving()
    if solve:
        progress_bar("Making everything OK...", 5)
        print_ok()


if __name__ == "__main__":
    main()
