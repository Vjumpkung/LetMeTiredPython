### Ghost Walking

ผีตัวหนึ่งเริ่มเดินจากจุดเริ่มต้นไปยังจุดใดๆ โดยมีการเคลื่อนที่ตามนี้

- W คือเดินขึ้น
- A คือเดินซ้าย
- S คือเดินลง
- D คือเดินขวา

เมื่อเดินจบแล้วให้คำนวณระยะทางที่ผีเดินไปได้

กำหนดให้จุดเริ่มต้นคือจุด (0,0) และ Distance เป็นทศนิยม 2 ตำแหน่ง

**Hint : ใน operator \*\* (ยกกำลัง) สามารถยกกำลังเป็นทศนิยมได้**

# Example 1
<pre class='output'>
<em>WD</em>
Distance : 1.41
</pre>
# Example 2
<pre class='output'>
<em>WASD</em>
Distance : 0.00
</pre>
# Example 3
<pre class='output'>
<em>DDDSSSWWWDDDDDDAADDWWSS</em>
Distance : 9.00
</pre>

::elab:begincode blank=True
t = input()
x = 0
y = 0
for i in t:
    if i == "W":
        y += 1
    elif i == "A":
        x -= 1
    elif i == "S":
        y -= 1
    elif i == "D":
        x += 1
print(f"Distance : {(x**2 + y**2)**(1/2):.2f}")
::elab:endcode


::elab:begintest
WWWDDDD
::elab:endtest

::elab:begintest
AWSDSDAWAWSDDWSD
::elab:endtest

::elab:begintest
ADWSADSWASDS
::elab:endtest

::elab:begintest
WD
::elab:endtest

::elab:begintest
WDWAASSSSDWW
::elab:endtest

::elab:begintest
SSDSDSSDSDDDDDDDDAA
::elab:endtest

