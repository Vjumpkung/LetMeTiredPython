### Counting

จากการนั่งนับเลขเป็นจำนวนมากพบว่า มีเลขที่เป็นจำนวนเต็มบวก และ จำนวนเต็มลบ ปะปนกันไป แล้วปัญหาคือ น้อง Qiqi จำไม่ได้ว่า ที่นับไปมีจำนวนเต็มบวกกี่จำนวน และ จำนวนเต็มบวกกี่จำนวน อยากให้ช่วยเขียนโปรแกรมนับจำนวนเต็มบวกและจำนวนเต็มลบหน่อยนะ 

- input : รับค่าจำนวนเต็มบวก หรือ จำนวนเต็มลบไปเรื่อยๆ จนเจอ 0 แล้วโปรแกรมจะสิ้นสุดการทำงาน
- output : แสดงจำนวนเต็มบวก และ จำนวนเต็มบวก ที่รับค่ามาทั้งหมด

# Example 1
<pre class='output'>
<em>1
2
7
7
7
7
7
-1
-2
-7
-7
-7
0</em>
Total Postitive Number : 7
Total Negative Number : 5
</pre>

# Example 2
<pre class='output'>
<em>9
2
-1
0</em>
Total Postitive Number : 11
Total Negative Number : 1
</pre>

# Example 3
<pre class='output'>
<em>0</em>
Total Postitive Number : 0
Total Negative Number : 0
</pre>


::elab:begincode blank=True
x = -999
neg = 0
pos = 0
zero = 0
while x != 0:
    x = int(input())
    if x > 0:
        pos += 1
    elif x < 0:
        neg += 1
print(f"Total Postitive Number : {pos}")
print(f"Total Negative Number : {neg}")
::elab:endcode


::elab:begintest
7
4
1
-2
-6
2
-3
0
::elab:endtest

::elab:begintest
0
::elab:endtest

::elab:begintest
4
2
6
8
2
7
4
2
6
9
2
-1 
0
::elab:endtest

::elab:begintest
6
2
-1
3
-6
-4
-5
1 
9 
0
::elab:endtest

::elab:begintest
6
9
4
2
0
::elab:endtest

::elab:begintest
6
4 
1
-1
5
-1
4
-1
4
7
0 
::elab:endtest


::elab:begintest
-1
2
5
7
-8
-8
-3
2
7
3
-10
9
10
-8
7
-7
4
-1
1
6
2
1
-4
-2
9
9
9
-6
-8
-9
-1
-8
-2
7
6
10
-3
-9
1
6
-9
1
-5
-5
-5
-4
-8
-5
4
0
::elab:endtest

