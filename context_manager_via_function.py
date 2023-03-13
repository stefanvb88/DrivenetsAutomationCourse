from contextlib import contextmanager



@contextmanager

def my_context():
    # all the code above the yield is called the setup and called when entering the context
    print("Entering my context code")
    yield
    # all the code below the yield is called the teardown phase and will be called when existing the context
    print("Exiting my context code")

#we work with context managers via the keyboard: with <name_of_the context_manager)

with my_context():
    print("         now i'm inside the context manager")

