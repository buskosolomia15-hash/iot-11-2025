class TimeConverter:
    def __init__(self, hours=0, minutes=0, seconds=0, total_seconds=None):
        if total_seconds is not None:
            self.hours = total_seconds // 3600
            self.minutes = (total_seconds % 3600) // 60
            self.seconds = total_seconds % 60
        else:
            self.hours = hours
            self.minutes = minutes
            self.seconds = seconds

    def __del__(self):
        print("Об'єкт TimeConverter знищено.")

    def to_seconds(self):
        return self.hours * 3600 + self.minutes * 60 + self.seconds

    def from_seconds(self, total_seconds):
        self.hours = total_seconds // 3600
        self.minutes = (total_seconds % 3600) // 60
        self.seconds = total_seconds % 60

    def outputConvertedTime(self):
        print(f"Час: {self.hours:02d}:{self.minutes:02d}:{self.seconds:02d}")
        print(f"У секундах: {self.to_seconds()} секунд")

    def outputConvertedTime(self, format='time'):
        if format == 'time':
            print(f"Час: {self.hours:02d}:{self.minutes:02d}:{self.seconds:02d}")
        elif format == 'seconds':
            print(f"У секундах: {self.to_seconds()} секунд")
        else:
            print("Невідомий формат. Використовуйте 'time' або 'seconds'.")

def main():
    print("=== Конвертація з hh:mm:ss у секунди ===")
    t1 = TimeConverter(1, 30, 15)
    t1.outputConvertedTime('time')
    t1.outputConvertedTime('seconds')

    print("\n=== Конвертація з секунд у hh:mm:ss ===")
    t2 = TimeConverter(total_seconds=5415)
    t2.outputConvertedTime('time')
    t2.outputConvertedTime('seconds')

if __name__ == "__main__":
    main()