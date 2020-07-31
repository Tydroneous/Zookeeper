# put your python code here  hours, minutes and seconds
start_hour = int(input())
start_minute = int(input())
start_second = int(input())

finish_hour = int(input())
finish_minute = int(input())
finish_second = int(input())


hour_diff_sec = ((finish_hour - start_hour) * 3600)
minute_diff_sec = ((finish_minute - start_minute) * 60)
second_diff_sec = ((finish_second - start_second))

print(hour_diff_sec + minute_diff_sec + second_diff_sec)
