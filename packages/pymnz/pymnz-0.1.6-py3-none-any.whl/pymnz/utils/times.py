import time


def countdown_timer(wait_seconds: int, msg_wait=""):
    """Countdown by seconds"""
    for i in range(wait_seconds, 0, -1):
        print(f"{msg_wait} {i} segundo(s) ...{' '*10}", end='\r')
        time.sleep(1)  # Waits for 1 second
