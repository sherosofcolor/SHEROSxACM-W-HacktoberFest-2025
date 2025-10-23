# ⚙️ Bubble Sort: Making the Smallest Bubbles Float Up

### ELI5 Analogy: The Tallest and Shortest Friends

Imagine you and your friends are standing in a line, but you want to organize yourselves from shortest to tallest.

**Bubble Sort is like doing this:**

1.  You look at the first two people in line (Person 1 and Person 2).
2.  If Person 1 is taller than Person 2, you tell them to **swap places!**
3.  Then, you move to the next two people (Person 2 and Person 3) and repeat: if they are in the wrong order, you swap them.
4.  You keep doing this tiny swap all the way to the end of the line.

When you reach the end, the **tallest person will definitely be at the very back**—they "bubbled up" to the end!

The list isn't completely sorted yet, so you have to repeat this entire process (Pass 2, Pass 3, etc.) again and again until nobody swaps places. When no swaps happen on a full pass, it means everyone is finally in the right order!

### 💻 The Code Analogy

In the code, instead of swapping friends, we swap numbers. We use two loops:

* **The Outer Loop:** Makes sure we repeat the entire process many times (like doing all the passes).
* **The Inner Loop:** Compares and swaps the adjacent items.

It's simple, but it takes many, many passes to get a long list sorted!