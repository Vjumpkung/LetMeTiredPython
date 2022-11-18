### Pyramid

เมื่อผีตัวหนึ่งอยากต่อสัญลักษณ์ชนิดหนึ่งให้เป็นรูปพีระมิด โดยก่อนจะต่อเป็นรูปจริง 

ผีอยากร่างแบบบนก่อน และอยากทราบจำนวนของที่ใช้ด้วย แต่ปัญหาคือ ของที่เอามานั้นจะต้องเอามาพอดี ไม่สามารถเอามาเกินได้

ช่วยผีตัวนี้วาดแบบร่างและคำนวณจำนวนของที่ใช้ทั้งหมด

**Hint** : ลองสังเกตุลำดับของตัวอักษร และ ช่องว่าง

ใช้ string repetition ได้

<pre class='output'>
>>> print('X'*5) # เป็นการ print X 5 ตัว
XXXXX
>>> print('A'*4) # เป็นการ print A 4 ตัว
AAAA
</pre>

# Example 1
<pre class='output'>
symbol : <em>I</em>
size : <em>5</em>
    I
   III
  IIIII
 IIIIIII
IIIIIIIII
Use I 25 items
</pre>

<pre class='output'>
symbol : <em>O</em>
size : <em>3</em>
  O
 OOO
OOOOO
Use O 9 items
</pre>

<pre class='output'>
symbol : <em>*</em>
size : <em>9</em>
        *
       ***
      *****
     *******
    *********
   ***********
  *************
 ***************
*****************
Use * 81 items
</pre>

::elab:begincode blank=True
t = input("symbol : ")
n = int(input("size : "))
c = 0
for i in range(n):
    for j in range(n-i-1):
        print(" ", end="")
    for j in range(2*i+1):
        print(t, end="")
    print()
    c += 2*i+1
print(f"Use {t} {c} items")
::elab:endcode
::elab:begintest
O
3
::elab:endtest
::elab:begintest
*
9
::elab:endtest
::elab:begintest
i
0
::elab:endtest
::elab:begintest
-
13
::elab:endtest
::elab:begintest
T
20
::elab:endtest
::elab:begintest
I
5
::elab:endtest