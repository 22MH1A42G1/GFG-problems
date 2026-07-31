<h2><a href="https://www.geeksforgeeks.org/problems/encapsulation-in-python/1?page=1&category=python&status=unsolved&sortBy=submissions">Encapsulation in Python</a></h2><h3>Difficulty Level : Difficulty: Easy</h3><hr><div class="problems_problem_content__Xm_eO" style="--text-color: var(--problem-text-color);"><p><span style="font-size: 14pt;">Implement a Person class in Python that demonstrates encapsulation. This class should have two "private" attributes:<br></span></p>
<ul>
<li><span style="font-size: 14pt;">name (String) with a default value of "Geeks".</span></li>
<li><span style="font-size: 14pt;">age (int) with a default value of 10.</span></li>
</ul>
<p><span style="font-size: 14pt;">The class should provide public methods to access and modify these private attributes:</span></p>
<ul>
<li><span style="font-size: 14pt;"><strong>Getter Methods</strong>: get_name() and get_age()</span></li>
<li><span style="font-size: 14pt;"><strong>Setter Methods</strong>: set_name(name) and set_age(age)</span></li>
</ul>
<p><strong><span style="font-size: 14pt;">Example:</span></strong></p>
<pre><strong><span style="font-size: 14pt;">Input: </span></strong><span style="font-size: 14pt;">Funtion calls: [Person(), get_name(), set_name("John"), set_age(21), get_name(), get_age()] <br><strong>Output: </strong>Geeks John 21<br><strong>Explanation: <br></strong>person = Person() // Person Object Created<br>person.get_name() // Default value "Geeks" returned<br>person.set_name("John") // name value set to "John"<br>person.set_age(21) // age value set to 21<br>person.get_name() // "John" returned<br>person.get_age() // 21 returned</span></pre></div><br><p><span style=font-size:18px><strong>Topic Tags : </strong><br><code>OOP</code>&nbsp;<code>python</code>&nbsp;