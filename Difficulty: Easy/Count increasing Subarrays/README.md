<h2><a href="https://www.geeksforgeeks.org/problems/count-increasing-subarrays5301/1">Count increasing Subarrays</a></h2><h3>Difficulty Level : Difficulty: Easy</h3><hr><div class="problems_problem_content__Xm_eO"><p><span style="font-size: 18px;">Given an array <strong>arr[]&nbsp;</strong>of integers, count the number of subarrays in <strong>arr[]</strong> which are strictly increasing with size greater or equal to <strong>2</strong>. A subarray is a contiguous part of array. A subarray is strictly increasing if each element is greater then it's previous element if it exists.</span></p>
<p><span style="font-size: 18px;"><strong>Examples:</strong></span></p>
<pre><span style="font-size: 18px;"><strong>Input: </strong>arr[] = [1, 3, 3, 2, 3, 5]
<strong>Output:</strong> 4
<strong>Explanation: </strong>Increasing Subarrays are : arr[0,1], arr[3,4], arr[3,5], arr[4,5].</span></pre>
<pre><span style="font-size: 18px;"><strong>Input: </strong>arr[] = [1, 5] 
<strong>Output:</strong> 1
<strong>Explanation:</strong>The only Increasing Subarray is arr[0,1].</span></pre>
<p><span style="font-size: 18px;"><strong>Expected Time Complexity:</strong> O(n)<br><strong>Expected Auxiliary Space:</strong> O(1)</span></p>
<p><span style="font-size: 18px;"><strong>Constraints:</strong><br>1 &lt;= arr.size() &lt;= 10<sup>6</sup><br>1 &lt;= arr<sub>i</sub> &lt;= 10<sup>7</sup></span></p></div><br><p><span style=font-size:18px><strong>Topic Tags : </strong><br><code>Arrays</code>&nbsp;<code>Data Structures</code>&nbsp;<code>sliding-window</code>&nbsp;<code>two-pointer-algorithm</code>&nbsp;