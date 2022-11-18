# Leap Year

เนื่องจากในความเป็นจริง โลกโคจรรอบดวงอาทิตย์ใช้เวลา 365.256 วัน ซึ่งในวันที่เกินมานั้น จะนำไปชดเชยเป็น ปีอธิกสุรทิน (Leap Year) ซึ่งในการคำนวณปีอธิกสุรทิน มีนิยามดังนี้

- ปีอธิกสุรทิน เป็นปีที่หาร 4 ลงตัวแต่หาร 100 ไม่ลงตัว ยกเว้นปีที่หาร 400 ลงตัว

ซึ่งผีน้อยนั้นหารเลขไม่เป็น และ ไม่รู้ว่าปีที่ผ่านมานั้นมันเป็น "ปีอธิกสุรทิน" หรือไม่ อยากให้น้องช่วยเขียนโปรแกรม ตรวจสอบหน่อยว่าเป็น ปีอธิกสุรทิน หรือไม่

**การันตีว่า input มีค่ามากกว่า 0 แน่นอน**

### Example 1

<pre class='output'>
Input Year : <em>2000</em>
Leap year
</pre>

### Example 2

<pre class='output'>
Input Year : <em>2022</em>
Not Leap year
</pre>

### Example 3

<pre class='output'>
Input Year : <em>1955</em>
Not Leap year
</pre>

::elab:begincode blank=True
y = int(input("Input Year : "))
if (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0):
    print("Leap year")
else:
    print("Not Leap year")
::elab:endcode

::elab:begintest
2000
::elab:endtest

::elab:begintest
2022
::elab:endtest

::elab:begintest
1955
::elab:endtest

::elab:begintest
18293
::elab:endtest

::elab:begintest
1995
::elab:endtest

::elab:begintest
1984
::elab:endtest