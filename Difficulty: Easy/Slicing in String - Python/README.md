<h2><a href="https://www.geeksforgeeks.org/problems/slicing-in-string-python/1?page=1&category=python&sortBy=submissions">Slicing in String - Python</a></h2><h3>Difficulty Level : Difficulty: Easy</h3><hr><div class="problems_problem_content__Xm_eO"><p><span style="font-size:18px">Here we'll talk about the novel and perhaps tantalizing concept of <strong>slicing</strong>. Slicing is the process through which you can extract some continuous part of a string. For example: string is "<strong>python</strong>", let's use slicing in this. Slicing can be done as:</span></p>

<p><span style="font-size:18px"><strong>a.</strong> string<strong>[0:2]</strong> = <strong>py</strong> (Slicing till index 1)<br>
<strong>b.</strong> string<strong>[0:]</strong> = <strong>python</strong> (Slicing till last index)<br>
<strong>c.</strong> string<strong>[0:4]</strong> = <strong>pyth</strong> (Slicing till index 3)<br>
<strong>d.</strong> string<strong>[0:-2]</strong> = <strong>pyth</strong> (Slicing till index -3).<br>
<strong>Note:</strong> <strong>-1</strong> indexing starts from last of any string.</span></p>

<p><span style="font-size:18px">Now, lets look into this through a question. Given a string of braces named <strong>bound_by</strong>, and a string named <strong>tag_name</strong>. The task is to print a new string such that <strong>tag_name </strong>is in the <strong>middle </strong>of <strong>bound_by</strong>.</span></p>

<p><span style="font-size:18px"><strong>Example 1:</strong></span></p>

<pre><span style="font-size:18px"><strong>Input:</strong> </span>
<span style="font-size:18px">bound_by = [[]], tag_name = tag</span>
<span style="font-size:18px"><strong>Output:</strong></span>
<span style="font-size:18px">[[tag]]<strong>
</strong></span></pre>

<p><span style="font-size:18px"><strong>Example 2:</strong></span></p>

<pre><span style="font-size:18px"><strong>Input:</strong> </span>
<span style="font-size:18px">bound_by = &lt;&gt;, tag_name = body</span>
<span style="font-size:18px"><strong>Output:</strong>
&lt;body&gt;</span></pre>

<p><span style="font-size:18px"><strong>Your Task:</strong><br>
Your task is to complete the function&nbsp;<strong>join_middle()</strong> which should <strong>return </strong>the modified string.</span></p>

<p><span style="font-size:18px"><strong>Constraints:</strong><br>
1 &lt;= |tag_name| &lt;= 10<sup>3</sup></span></p>

<p>&nbsp;</p>

<p><iframe frameborder="0" height="315" src="https://www.youtube.com/embed/i5WNg3UOkQk" width="560"></iframe></p>
</div><br><p><span style=font-size:18px><strong>Topic Tags : </strong><br><code>python-strings</code>&nbsp;<code>python</code>&nbsp;