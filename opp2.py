#ex 2.2
import math
r = 5
V = 4/3 * math.pi * r ** 3
print ("The tich cua hinh cau ban kinh 5 la: ", round (V, 2) )

Giabia = 24.95
Sosach = 60
Phivanchuyen = 3 + 59 * 0.75
Tongchiphi = ((Giabia * 0.6) * Sosach + Phivanchuyen )
print ("Tong chi phi nhap sach la: ", round (Tongchiphi, 2), "dollars" )

Start = 6 * 3600 + 52 * 60
Easypace = 8 * 60 + 15
Tempopace = 7 * 60 + 12
Totaltime = Tempopace * 3 + 2 * Easypace
Finish = Start + Totaltime
Finishhour = Finish // 3600
Finishminute = (Finish % 3600) // 60
Finishsecond = Finish % 60
print (f"Finish time is: {Finishhour:02d}:{Finishminute:02d}:{Finishsecond:02d}")


#Think Python, chapter 3
#ex 3.3
print ( "+", "-", "-", "-", "-", "+", "-", "-", "-", "-", "+" )
print ( "|", " ", " ", " ", " ", "|", " ", " ", " ", " ", "|" )
print ( "|", " ", " ", " ", " ", "|", " ", " ", " ", " ", "|" )
print ( "|", " ", " ", " ", " ", "|", " ", " ", " ", " ", "|" )
print ( "|", " ", " ", " ", " ", "|", " ", " ", " ", " ", "|" )
print ( "+", "-", "-", "-", "-", "+", "-", "-", "-", "-", "+" )
print ( "|", " ", " ", " ", " ", "|", " ", " ", " ", " ", "|" )
print ( "|", " ", " ", " ", " ", "|", " ", " ", " ", " ", "|" )
print ( "|", " ", " ", " ", " ", "|", " ", " ", " ", " ", "|" )
print ( "|", " ", " ", " ", " ", "|", " ", " ", " ", " ", "|" )
print ( "+", "-", "-", "-", "-", "+", "-", "-", "-", "-", "+" )


#Think Python, chapter 4
#ex 5.1
import time
Now = time.time ()
Days = Now // (24 *3600)
Remaining = Now % (24 * 3600)
Hours = Remaining // 3600
Remaining = Remaining % 3600
Minutes = Remaining // 60
Seconds = Remaining % 60
print("Days since epoch:", int(Days))
print ("Now is: ", f"{int(Hours):02d}:{int(Minutes):02d}:{int(Seconds):02d}" )