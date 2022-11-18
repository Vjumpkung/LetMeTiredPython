# Court Badminton

คอร์ดแบดมินตัน แห่งหนึ่งคิดราคาดังนี้

<table border="1">
    <tr>
        <td>เวลา (ชั่วโมง)</td>
        <td>ราคา (ชม.ละ)</td>
    </tr>
    <tr>
        <td>1 <= เวลา < 4</td>
        <td><center>100</center></td>
    </tr>
    <tr>
        <td>4 <= เวลา < 7</td>
        <td><center>90</center></td>
    </tr>
    <tr>
        <td>เวลา >= 7</td>
        <td><center>80</center></td>
    </tr>
</table>
<br>
**หมายเหตุ** เศษของชั่วโมงปัดขึ้นเสมอ

แล้วสิ่งที่เจ้าของคอร์ดแบดมินตัน พบปัญหาคือ มีผู้ใช้บริการเป็นจำนวนมาก (ซึ่งไม่ใช่คน) แล้ว ทำให้ไม่สามารถ คำนวณ ค่าใช้จ่ายได้ทัน
จงเขียนโปรแกรมคำนวณค่าเช่า คอร์ดแบดมินตัน โดยเวลาที่รับเข้ามาเป็นหน่วย นาที

# Example 1
<pre class='output'>
Customer name : <em>Player1</em>
Input time (minutes) : <em>784</em>
<span>-------------------------------</span>
Name : Player1
Playtime : 13 hr. 4 min.
Price : 1120 baht
<span>-------------------------------</span>
</pre>

# Example 2
<pre class='output'>
Customer name : <em>vjump</em>
Input time (minutes) : <em>888</em>
<span>-------------------------------</span>
Name : vjump
Playtime : 14 hr. 48 min.
Price : 1200 baht
<span>-------------------------------</span>
</pre>

# Example 3
<pre class='output'>
Customer name : <em>TWICE</em>
Input time (minutes) : <em>-1</em>
Invalid Time
</pre>

::elab:begincode blank=True
customer_name = input("Customer name : ")
total_time = int(input("Input time (minutes) : "))
hours = int(total_time//60)
remain_time = int(total_time % 60)
cost = 0
cal_hours = 0

if(remain_time != 0):
    cal_hours = 1

cal_hours += hours

if 1 <= cal_hours < 4:
    cost = 100 * cal_hours
elif 4 <= cal_hours < 7:
    cost = 90 * cal_hours
elif cal_hours >= 7:
    cost = 80 * cal_hours

if(hours >= 0):
    print("-------------------------------")
    print(f"Name : {customer_name}")
    print(f"Playtime : {hours} hr. {remain_time} min.")
    print(f"Price : {cost} baht")
    print("-------------------------------")
else:
    print("Invalid Time")
::elab:endcode

::elab:begintest
Player1
784
::elab:endtest

::elab:begintest
vjump
888
::elab:endtest

::elab:begintest
TWICE
-1
::elab:endtest

::elab:begintest
ABCDEFG
420
::elab:endtest

::elab:begintest
You and I
-123456789
::elab:endtest

::elab:begintest
Ricciardo
69
::elab:endtest

