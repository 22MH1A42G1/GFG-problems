<h2><a href="https://www.geeksforgeeks.org/problems/dictionary-in-python-iii/1?page=2&category=python&sortBy=submissions">Dictionary in Python - III</a></h2><h3>Difficulty Level : Difficulty: Easy</h3><hr><div class="problems_problem_content__Xm_eO"><p><span style="font-size:18px">You are familiar with most of the properties of the dictionary in Python. Add some more info about dictionaries through dictionary <strong>formatting </strong>and <strong>deleting </strong>key-value pairs.</span></p>

<p><span style="font-size:18px"><strong>Formatting</strong>:</span></p>

<pre><span style="font-size:18px">hash = {}</span>
<span style="font-size:18px">hash['Geeks'] = 5</span>
<span style="font-size:18px">hash['geeksforgeeks'] = 13
key = 'Geeks'</span>
<span style="font-size:18px">s = ("Count of characters is " + 
hash[key] + " in " + key)             </span>
<span style="font-size:18px"># results in: Count of characters is 
5 in Geeks.</span></pre>

<p><span style="font-size:18px"><strong>Deleting:</strong></span></p>

<pre><span style="font-size:18px"><strong>dict </strong>= {'a' : 1, 'b': 2, 'c' : 3, 'd' : 4}</span>
<span style="font-size:18px"><strong>del dict</strong>['c']          
# delete entry for 'c'</span></pre>

<p><span style="font-size:18px">Let's get this into the head by solving a question. Given a list of some students in a list and their corresponding marks in another list. The task is to do some operations as described below:<br>
<strong>a.</strong>&nbsp;<strong>i&nbsp;key value</strong>: Iserts key and value in the dictionary, and print 'Inserted'.<br>
<strong>b. d key</strong>: Delete the entry for a given key and print 'Deleted' if the key to be deleted is present, else print '-1'.<br>
<strong>c.</strong> <strong>key</strong>: Print marks of a given key in a statement as "Marks of student name is : marks".</span></p>

<p><span style="font-size:18px"><strong>Example:</strong></span></p>

<pre><span style="font-size:18px"><strong>Input:</strong></span>
<span style="font-size:18px">N = 5</span>
<span style="font-size:18px">i geeks 100</span>
<span style="font-size:18px">i for 200</span>
<span style="font-size:18px">d geeks</span>
<span style="font-size:18px">i geeks 300</span>
<span style="font-size:18px">p geeks</span>
<span style="font-size:18px"><strong>Output:</strong></span>
<span style="font-size:18px">Inserted</span>
<span style="font-size:18px">Inserted</span>
<span style="font-size:18px">Deleted</span>
<span style="font-size:18px">Inserted</span>
<span style="font-size:18px">Marks of geeks is 300</span>
<span style="font-size:18px"><strong>Explanation:</strong></span>
<span style="font-size:18px">For first four queries, insert and del 
operation happens, correspondingly <strong>Inserted 
</strong>And <strong>Deleted </strong>is printed. For the last query, 
marks of geeks is printed.</span></pre>

<p><span style="font-size:18px"><strong>Your Task:</strong><br>
Your task is to complete the function <strong>insert_dict()</strong>, <strong>del_dict()</strong> and <strong>print_dict()</strong> which should perform the operations as required.&nbsp;If nothing is printed for a test case, print "<strong>-1</strong>".</span></p>

<p><span style="font-size:18px"><strong>Constraints:</strong><br>
1 &lt;= N &lt;= 10<sup>4</sup><br>
1 &lt;= marks &lt;= 10<sup>4</sup></span></p>
</div><br><p><span style=font-size:18px><strong>Topic Tags : </strong><br><code>python-dict</code>&nbsp;<code>python</code>&nbsp;