# wthen

Wthen is a simple rule engine in Python, it is allowed to extract rules outside the program, but it's not business oriented. 
That means it is for developer or those whose are able to program with Python
The name came from our daily speaking, when condition matched, then actions will be taken.

It leverages <code>YAML</code> to provide an easy understanding rule format. 
The conditions (When) are evalated by Python <code>eval()</code>. 
The actions (Then) are executed by Python <code>exec()</code>

# Quick Example
* Given scinario:
    * When <code>a (=2) > b (=1)</code>
    * Then <code>2 > 1</code> is printed out
<code:yaml>
rules:
  - rule:
      
</code>
