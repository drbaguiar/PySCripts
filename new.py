
{
 "metadata": {
  "name": "",
  "signature": "sha256:ab7530ae998cec2d0ab14e3a3b88c58cf47c5ddc95388561b846c20b8a7f56bc"
 },
 "nbformat": 3,
 "nbformat_minor": 0,
 "worksheets": [
  {
   "cells": [
    {
     "cell_type": "heading",
     "level": 1,
     "metadata": {},
     "source": [
      "Mining Massive Datasets Homework"
     ]
    },
    {
     "cell_type": "markdown",
     "metadata": {},
     "source": [
      "*by Jure Leskovec, Anand Rajaraman, Jeff Ullman*"
     ]
    },
    {
     "cell_type": "heading",
     "level": 2,
     "metadata": {},
     "source": [
      "Homework 1"
     ]
    },
    {
     "cell_type": "markdown",
     "metadata": {},
     "source": [
      "Due Mon 13 Oct 2014 11:59 PM PDT; Hard Deadline Mon 24 Nov 2014 11:59 PM PST"
     ]
    },
    {
     "cell_type": "heading",
     "level": 3,
     "metadata": {},
     "source": [
      "Question 1 (iPython docs suggest that logical sections be Heading cells, not just HTML markup)"
     ]
    },
    {
     "cell_type": "markdown",
     "metadata": {},
     "source": [
      "Consider three Web pages with the following links:\n",
      "![Three Web Pages](files/otc_pagerank2.gif)\n",
      "\n",
      "Suppose we compute PageRank with a \u03b2 of 0.7, and we introduce the additional constraint that the sum of the PageRanks of the three pages must be 3, to handle the problem that otherwise any multiple of a solution will also be a solution. Compute the PageRanks a, b, and c of the three pages A, B, and C, respectively. Then, identify from the list below, the true statement.\n",
      "\n",
      "b + c = 2.735  \n",
      "\n",
      "a + c = 2.745  \n",
      "\n",
      "a + b = 0.705  \n",
      "\n",
      "a + b = 0.55 \n"
     ]
    },
    {
     "cell_type": "heading",
     "level": 4,
     "metadata": {},
     "source": [
      "Answer 1 (this is just the heading; iPython docs suggest that logical sections be Heading cells, not just HTML markup)"
     ]
    },
    {
     "cell_type": "markdown",
     "metadata": {},
     "source": [
      "Replace this with your answer to question 1. Add cells as necessary.\n",
      "\n",
      "Here's an example of mixed markdown and HTML: r<sub>a</sub> + r<sub>b</sub> + r<sub>c</sub> = ?\n",
      "\n",
      "~~Shift-Enter or click the \"Play\" button to transform this markdown source to HTML display.~~"
     ]
    },
    {
     "cell_type": "heading",
     "level": 3,
     "metadata": {},
     "source": [
      "Question 2"
     ]
    },
    {
     "cell_type": "markdown",
     "metadata": {},
     "source": [
      "Consider three Web pages with the following links:\n",
      "![Three Web Pages](files/otc_pagerank3.gif)\n",
      "\n",
      "Suppose we compute PageRank with \u03b2=0.85. \n",
      "Write the equations for the PageRanks a, b, and c of the three pages A, B, and C, respectively. \n",
      "Then, identify in the list below, one of the equations.\n",
      "\n",
      ".95a = .9c + .05b\n",
      "\n",
      "b = .575a + .15c\n",
      "\n",
      "c = .9b + .475a\n",
      "\n",
      "85b = .575a + .15c\n"
     ]
    },
    {
     "cell_type": "heading",
     "level": 4,
     "metadata": {},
     "source": [
      "Answer 2"
     ]
    },
    {
     "cell_type": "markdown",
     "metadata": {},
     "source": [
      "Replace this with your answer to question 2. Add cells as necessary.\n",
      "\n",
      "Here's an example of markdown and a MathJAX/TeX matrix: $\\left( \\begin{matrix} a & b & c \\\\ d & e & f \\\\ g & h & i \\end{matrix} \\right)$\n",
      "\n",
      "Use vmatrix for vertical bars: $\\begin{vmatrix} a & b & c \\\\ d & e & f \\\\ g & h & i \\end{vmatrix}$\n",
      "\n",
      "~~Shift-Enter or click the \"Play\" button to transform this markdown source to HTML display.~~"
     ]
    },
    {
     "cell_type": "heading",
     "level": 3,
     "metadata": {},
     "source": [
      "Question 3"
     ]
    },
    {
     "cell_type": "markdown",
     "metadata": {},
     "source": [
      "Consider three Web pages with the following links:\n",
      "![Three Web Pages](files/otc_pagerank3.gif)\n",
      "\n",
      "Assuming no \"taxation,\" compute the PageRanks a, b, and c of the three pages A, B, and C, using iteration, starting with the \"0th\" iteration where all three pages have rank a = b = c = 1. Compute as far as the 5th iteration, and also determine what the PageRanks are in the limit. Then, identify the true statement from the list below.\n",
      "\n",
      "After iteration 5, c = 7/4\n",
      "\n",
      "After iteration 5, c = 1\n",
      "\n",
      "In the limit, c = 9/7\n",
      "\n",
      "After iteration 5, a = 5/4\n"
     ]
    },
    {
     "cell_type": "heading",
     "level": 4,
     "metadata": {},
     "source": [
      "Answer 3"
     ]
    },
    {
     "cell_type": "markdown",
     "metadata": {},
     "source": [
      "Replace this with your answer to question 3. Add cells as necessary.\n",
      "\n",
      "~~Shift-Enter or click the \"Play\" button to transform this markdown source to HTML display.~~"
     ]
    },
    {
     "cell_type": "heading",
     "level": 3,
     "metadata": {},
     "source": [
      "Question 4"
     ]
    },
    {
     "cell_type": "markdown",
     "metadata": {},
     "source": [
      "Suppose our input data to a map-reduce operation consists of integer values (the keys are not important). The map function takes an integer i and produces the list of pairs (p,i) such that p is a prime divisor of i. For example, map(12) = [(2,12), (3,12)].\n",
      "\n",
      "The reduce function is addition. That is, reduce(_p_, [_i_<sub>1</sub>, _i_<sub>2</sub>, ...,_i_<sub>_k_</sub>])\n",
      "is (_p_,_i_<sub>1</sub>+_i_<sub>2</sub>+...+_i_<sub>_k_</sub>).\n",
      "\n",
      "Compute the output, if the input is the set of integers 15, 21, 24, 30, 49. Then, identify, in the list below, one of the pairs in the output.\n",
      "\n",
      "(7,119)\n",
      "\n",
      "(6,54)\n",
      "\n",
      "(3,75)\n",
      "\n",
      "(3,90)\n"
     ]
    },
    {
     "cell_type": "heading",
     "level": 4,
     "metadata": {},
     "source": [
      "Answer 4."
     ]
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "#Replace this with your answer to question 4. Add cells as necessary.\n",
      "\n",
      "#Here's an example of inline python\n",
      "\n",
      "def flattenList(twoDList):\n",
      "    return [ i for sublist in twoDList for i in sublist]\n",
      "\n",
      "twoD = [[(1, 1), (2, 2)], [(1, 2), (2, 1)]]\n",
      "\n",
      "print twoD\n",
      "print flattenList(twoD)\n",
      "print sorted(flattenList(twoD))\n",
      "\n",
      "#Shift-Enter or click the \"Play\" button to run this python script."
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "output_type": "stream",
       "stream": "stdout",
       "text": [
        "[[(1, 1), (2, 2)], [(1, 2), (2, 1)]]\n",
        "[(1, 1), (2, 2), (1, 2), (2, 1)]\n",
        "[(1, 1), (1, 2), (2, 1), (2, 2)]\n"
       ]
      }
     ],
     "prompt_number": 5
    },
    {
     "cell_type": "heading",
     "level": 2,
     "metadata": {},
     "source": [
      "Week 2: LSH (Basic) "
     ]
    },
    {
     "cell_type": "markdown",
     "metadata": {},
     "source": [
      "Due Date Mon 20 Oct 2014 11:59 PM PDT; Hard Deadline Mon 17 Nov 2014 11:59 PM PST"
     ]
    },
    {
     "cell_type": "heading",
     "level": 3,
     "metadata": {},
     "source": [
      "Question 1"
     ]
    },
    {
     "cell_type": "markdown",
     "metadata": {},
     "source": [
      "The edit distance is the minimum number of character insertions and character deletions required to turn one string into another. Compute the edit distance between each pair of the strings he, she, his, and hers. Then, identify which of the following is a true statement about the number of pairs at a certain edit distance.\n",
      "\n",
      "There are 2 pairs at distance 3.\n",
      "\n",
      "There is 1 pair at distance 5.\n",
      "\n",
      "There are 2 pairs at distance 2.\n",
      "\n",
      "There is 1 pair at distance 2."
     ]
    },
    {
     "cell_type": "heading",
     "level": 4,
     "metadata": {},
     "source": [
      "Answer 1"
     ]
    },
    {
     "cell_type": "markdown",
     "metadata": {},
     "source": [
      "Compute answer 1 here"
     ]
    },
    {
     "cell_type": "heading",
     "level": 3,
     "metadata": {},
     "source": [
      "Question 2"
     ]
    },
    {
     "cell_type": "markdown",
     "metadata": {},
     "source": [
      "\n",
      "Consider the following matrix:\n",
      "\n",
      "|   |C1 |C2 |C3 |C4|\n",
      "|---|:-|:-|:-|:-|\n",
      "|R1 |0 |1 |1 |0|\n",
      "|R2 |1 |0 |1 |1|\n",
      "|R3 |0 |1 |0 |1|\n",
      "|R4 |0 |0 |1 |0|\n",
      "|R5 |1 |0 |1 |0|\n",
      "|R6 |0 |1 |0 |0|\n",
      "\n",
      "\n",
      "Perform a minhashing of the data, with the order of rows: R4, R6, R1, R3, R5, R2. Which of the following is the correct minhash value of the stated column? **Note:** we give the minhash value in terms of the original name of the row, rather than the order of the row in the permutation. These two schemes are equivalent, since we only care whether hash values for two columns are equal, not what their actual values are.\n",
      "\n",
      "The minhash value for C3 is R5\n",
      "\n",
      "The minhash value for C2 is R6\n",
      "\n",
      "The minhash value for C4 is R5\n",
      "\n",
      "The minhash value for C2 is R3\n"
     ]
    },
    {
     "cell_type": "heading",
     "level": 4,
     "metadata": {},
     "source": [
      "Answer 2"
     ]
    },
    {
     "cell_type": "markdown",
     "metadata": {},
     "source": [
      "Compute answer 2 here"
     ]
    },
    {
     "cell_type": "heading",
     "level": 3,
     "metadata": {},
     "source": [
      "Question 3"
     ]
    },
    {
     "cell_type": "markdown",
     "metadata": {},
     "source": [
      "Here is a matrix representing the signatures of seven columns, C1 through C7. \n",
      "\n",
      "|C1 |C2 |C3 |C4 |C5 |C6 |C7|\n",
      "|:-|:-|:-|:-|:-|:-|:-|\n",
      "|1 |2 |1 |1 |2 |5 |4|\n",
      "|2 |3 |4 |2 |3 |2 |2|\n",
      "|3 |1 |2 |3 |1 |3 |2|\n",
      "|4 |1 |3 |1 |2 |4 |4|\n",
      "|5 |2 |5 |1 |1 |5 |1|\n",
      "|6 |1 |6 |4 |1 |1 |4|\n",
      "\n",
      " Suppose we use locality-sensitive hashing with three bands of two rows each. Assume there are enough buckets available that the hash function for each band can be the identity function (i.e., columns hash to the same bucket if and only if they are identical in the band). Find all the candidate pairs, and then identify one of them in the list below.\n",
      "\n",
      "C4 and C6\n",
      "\n",
      "C2 and C4\n",
      "\n",
      "C1 and C3\n",
      "\n",
      "C3 and C5\n"
     ]
    },
    {
     "cell_type": "heading",
     "level": 4,
     "metadata": {},
     "source": [
      "Answer 3"
     ]
    },
    {
     "cell_type": "markdown",
     "metadata": {},
     "source": [
      "Compute answer 3 here"
     ]
    },
    {
     "cell_type": "heading",
     "level": 3,
     "metadata": {},
     "source": [
      "Question 4"
     ]
    },
    {
     "cell_type": "markdown",
     "metadata": {},
     "source": [
      "Find the set of 2-shingles for the \"document\":\n",
      "\n",
      "<blockquote><font color='blue'>ABRACADABRA</font></blockquote>\n",
      "\n",
      "and also for the \"document\":\n",
      "\n",
      "<blockquote><font color='blue'>BRICABRAC</font></blockquote>\n",
      "\n",
      "Answer the following questions:\n",
      "\n",
      "* How many 2-shingles does ABRACADABRA have?\n",
      "* How many 2-shingles does BRICABRAC have?\n",
      "* How many 2-shingles do they have in common?\n",
      "* What is the Jaccard similarity between the two documents\"?\n",
      "\n",
      "Then, find the true statement in the list below.\n",
      "\n",
      "The Jaccard similarity is 4/7.\n",
      "\n",
      "BRICABRAC has 7 2-shingles.\n",
      "\n",
      "BRICABRAC has 8 2-shingles.\n",
      "\n",
      "There are 4 shingles in common."
     ]
    },
    {
     "cell_type": "heading",
     "level": 4,
     "metadata": {},
     "source": [
      "Answer 4"
     ]
    },
    {
     "cell_type": "markdown",
     "metadata": {},
     "source": [
      "Compute answer 4 here"
     ]
    },
    {
     "cell_type": "heading",
     "level": 3,
     "metadata": {},
     "source": [
      "Question 5"
     ]
    },
    {
     "cell_type": "markdown",
     "metadata": {},
     "source": [
      "<font color='blue'>\n",
      "s<sub>1</sub> = abcef  \n",
      "s<sub>2</sub> = acdeg  \n",
      "s<sub>3</sub> = bcdefg  \n",
      "s<sub>4</sub> = adfg  \n",
      "s<sub>5</sub> = bcdfgh  \n",
      "s<sub>6</sub> = bceg  \n",
      "s<sub>7</sub> = cdfg  \n",
      "s<sub>8</sub> = abcd\n",
      "</font>\n",
      "\n",
      "Suppose our upper limit on Jaccard distance is 0.2, and we use the indexing scheme of Section 3.9.4 based on symbols appearing in the prefix (no position or length information). For each of s<sub>1</sub>, s<sub>3</sub>, and s<sub>6</sub>, determine how many other strings that string will be compared with, if it is used as the probe string. Then, identify the true count from the list below.\n",
      "\n",
      "s3 is compared with 2 other strings.\n",
      "\n",
      "s6 is compared with 3 other strings.\n",
      "\n",
      "s6 is compared with 2 other strings.\n",
      "\n",
      "s6 is compared with 5 other strings."
     ]
    },
    {
     "cell_type": "heading",
     "level": 4,
     "metadata": {},
     "source": [
      "Answer 5"
     ]
    },
    {
     "cell_type": "markdown",
     "metadata": {},
     "source": [
      "Compute answer 5 here"
     ]
    },
    {
     "cell_type": "heading",
     "level": 3,
     "metadata": {},
     "source": [
      "Question 6"
     ]
    },
    {
     "cell_type": "markdown",
     "metadata": {},
     "source": [
      "Suppose we want to assign points to whichever of the points (0,0) or (100,40) is nearer. Depending on whether we use the L<sub>1</sub> or L<sub>2</sub> norm, a point (x,y) could be clustered with a different one of these two points. For this problem, you should work out the conditions under which a point will be assigned to (0,0) when the L<sub>1</sub> norm is used, but assigned to (100,40) when the L<sub>2</sub> norm is used. Identify one of those points from the list below.\n",
      "\n",
      "(58,13)\n",
      "\n",
      "(63,8)\n",
      "\n",
      "(66,5)\n",
      "\n",
      "(61,8)"
     ]
    },
    {
     "cell_type": "heading",
     "level": 4,
     "metadata": {},
     "source": [
      "Answer 6"
     ]
    },
    {
     "cell_type": "markdown",
     "metadata": {},
     "source": [
      "Compute aswer 6 here"
     ]
    },
    {
     "cell_type": "heading",
     "level": 2,
     "metadata": {},
     "source": [
      "Week 2: Frequent Itemsets (Basic) "
     ]
    },
    {
     "cell_type": "markdown",
     "metadata": {},
     "source": [
      "Due Date Mon 20 Oct 2014 11:59 PM PDT; Hard Deadline Mon 17 Nov 2014 11:59 PM PST"
     ]
    },
    {
     "cell_type": "heading",
     "level": 3,
     "metadata": {},
     "source": [
      "Question 1"
     ]
    },
    {
     "cell_type": "markdown",
     "metadata": {},
     "source": [
      "Suppose we have transactions that satisfy the following assumptions:\n",
      "\n",
      "* *s*, the support threshold, is 10,000.\n",
      "* There are one million items, which are represented by the integers 0,1,...,999999.\n",
      "* There are *N* frequent items, that is, items that occur 10,000 times or more.\n",
      "* There are one million pairs that occur 10,000 times or more.\n",
      "* There are *2M* pairs that occur exactly once. *M* of these pairs consist of two frequent items, the other *M* each have at least one nonfrequent item.\n",
      "* No other pairs occur at all.\n",
      "* Integers are always represented by 4 bytes.\n",
      "\n",
      "Suppose we run the a-priori algorithm to find frequent pairs and can choose on the second pass between the triangular-matrix method for counting candidate pairs (a triangular array count[i][j] that holds an integer count for each pair of items (i, j) where i As a function of N and M, what is the minimum number of bytes of main memory needed to execute the a-priori algorithm on this data? Demonstrate that you have the correct formula by selecting, from the choices below, the triple consisting of values for N, M, and the (approximate, i.e., to within 10%) minumum number of bytes of main memory, S, needed for the a-priori algorithm to execute with this data.\n",
      "\n",
      "N = 10,000; M = 40,000,000; S = 200,000,000\n",
      "\n",
      "N = 30,000; M = 100,000,000; S = 500,000,000\n",
      "\n",
      "N = 10,000; M = 50,000,000; S = 600,000,000\n",
      "\n",
      "N = 50,000; M = 80,000,000; S = 1,500,000,000"
     ]
    },
    {
     "cell_type": "heading",
     "level": 4,
     "metadata": {},
     "source": [
      "Answer 1"
     ]
    },
    {
     "cell_type": "markdown",
     "metadata": {},
     "source": [
      "Compute answer 1 here"
     ]
    },
    {
     "cell_type": "heading",
     "level": 3,
     "metadata": {},
     "source": [
      "Question 2"
     ]
    },
    {
     "cell_type": "markdown",
     "metadata": {},
     "source": [
      "Imagine there are 100 baskets, numbered 1,2,...,100, and 100 items, similarly numbered. Item i is in basket j if and only if i divides j evenly. For example, basket 24 is the set of items {1,2,3,4,6,8,12,24}. Describe all the association rules that have 100% confidence. Which of the following rules has 100% confidence?\n",
      "\n",
      "{1} \u2192 2\n",
      "\n",
      "{8,10} \u2192 20\n",
      "\n",
      "{4,10,12} \u2192 80\n",
      "\n",
      "{2,4} \u2192 8"
     ]
    },
    {
     "cell_type": "heading",
     "level": 4,
     "metadata": {},
     "source": [
      "Answer 2"
     ]
    },
    {
     "cell_type": "markdown",
     "metadata": {},
     "source": [
      "Compute answer 2 here"
     ]
    },
    {
     "cell_type": "heading",
     "level": 3,
     "metadata": {},
     "source": [
      "Question 3"
     ]
    },
    {
     "cell_type": "markdown",
     "metadata": {},
     "source": [
      "Suppose ABC is a frequent itemset and BCDE is NOT a frequent itemset. Given this information, we can be sure that certain other itemsets are frequent and sure that certain itemsets are NOT frequent. Other itemsets may be either frequent or not. Which of the following is a correct classification of an itemset?\n",
      "\n",
      "AC can be either frequent or not frequent.\n",
      "\n",
      "ABCF is frequent.\n",
      "\n",
      "ABCD can be either frequent or not frequent.\n",
      "\n",
      "AB can be either frequent or not frequent."
     ]
    },
    {
     "cell_type": "heading",
     "level": 4,
     "metadata": {},
     "source": [
      "Answer 3"
     ]
    },
    {
     "cell_type": "markdown",
     "metadata": {},
     "source": [
      "Compute answer 3 here"
     ]
    },
    {
     "cell_type": "heading",
     "level": 2,
     "metadata": {},
     "source": [
      "Week 2: Frequent Itemsets (Advanced) "
     ]
    },
    {
     "cell_type": "markdown",
     "metadata": {},
     "source": [
      "Due Date \tMon 20 Oct 2014 11:59 PM PDT; Hard Deadline \tMon 17 Nov 2014 11:59 PM PST"
     ]
    },
    {
     "cell_type": "heading",
     "level": 3,
     "metadata": {},
     "source": [
      "Question 1"
     ]
    },
    {
     "cell_type": "markdown",
     "metadata": {},
     "source": [
      " Suppose we perform the PCY algorithm to find frequent pairs, with market-basket data meeting the following specifications:\n",
      "\n",
      "* *s*, the support threshold, is 10,000.\n",
      "* There are one million items, which are represented by the integers 0,1,...,999999.\n",
      "* There are 250,000 frequent items, that is, items that occur 10,000 times or more.\n",
      "* There are one million pairs that occur 10,000 times or more.\n",
      "* There are *P* pairs that occur exactly once and consist of 2 frequent items.\n",
      "* No other pairs occur at all.\n",
      "* Integers are always represented by 4 bytes.\n",
      "* When we hash pairs, they distribute among buckets randomly, but as evenly as possible; \n",
      "i.e., you may assume that each bucket gets exactly its fair share of the *P* pairs that occur once.\n",
      "\n",
      "Suppose there are *S* bytes of main memory. In order to run the PCY algorithm successfully, \n",
      "the number of buckets must be sufficiently large that most buckets are not large. \n",
      "In addition, on the second pass, there must be enough room to count all the candidate pairs. \n",
      "As a function of *S*, what is the largest value of *P* for which we can successfully run the PCY algorithm on this data?\n",
      "Demonstrate that you have the correct formula by indicating which of the following is a value \n",
      "for *S* and a value for *P* that is approximately (i.e., to within 10%) the largest possible value of *P* for that *S*.\n",
      "\n",
      "S = 300,000,000; P = 750,000,000\n",
      "\n",
      "S = 1,000,000,000; P = 10,000,000,000\n",
      "\n",
      "S = 300,000,000; P = 1,800,000,000\n",
      "\n",
      "S = 500,000,000; P = 10,000,000,000"
     ]
    },
    {
     "cell_type": "heading",
     "level": 4,
     "metadata": {},
     "source": [
      "Answer 1"
     ]
    },
    {
     "cell_type": "markdown",
     "metadata": {},
     "source": [
      "Compute answer 1 here"
     ]
    },
    {
     "cell_type": "heading",
     "level": 3,
     "metadata": {},
     "source": [
      "Question 2"
     ]
    },
    {
     "cell_type": "markdown",
     "metadata": {},
     "source": [
      "During a run of Toivonen's Algorithm with set of items {A,B,C,D,E,F,G,H} a sample is found \n",
      "to have the following maximal frequent itemsets: {A,B}, {A,C}, {A,D}, {B,C}, {E}, {F}. \n",
      "Compute the negative border. Then, identify in the list below the set that is NOT in the negative border.\n",
      "\n",
      "{D,F}\n",
      "\n",
      "{D}\n",
      "\n",
      "{B,E}\n",
      "\n",
      "{A,B,C}"
     ]
    },
    {
     "cell_type": "heading",
     "level": 4,
     "metadata": {},
     "source": [
      "Answer 2"
     ]
    },
    {
     "cell_type": "markdown",
     "metadata": {},
     "source": [
      "Compute answer 2 here"
     ]
    },
    {
     "cell_type": "heading",
     "level": 2,
     "metadata": {},
     "source": [
      "Week3B (Basic) "
     ]
    },
    {
     "cell_type": "markdown",
     "metadata": {},
     "source": [
      "Due Date Mon 27 Oct 2014 11:59 PM PDT; Hard Deadline Mon 17 Nov 2014 11:59 PM PST"
     ]
    },
    {
     "cell_type": "heading",
     "level": 3,
     "metadata": {},
     "source": [
      "Question 1"
     ]
    },
    {
     "cell_type": "markdown",
     "metadata": {},
     "source": [
      "<div dir=\"auto\" class=\"course-quiz-question-text\">Suppose we hash the elements of a set S having 20 members, to a bit array of length 99. The array is initially all-0's, and we set a bit to 1 whenever a member of S hashes to it. The hash function is random and uniform in its distribution. What is the expected fraction of 0's in the array after hashing? What is the expected fraction of 1's? You may assume that 99 is large enough that asymptotic limits are reached.\n",
      "</div>\n",
      "<div dir=\"auto\" class=\"course-quiz-options\">\n",
      "<div class=\"course-quiz-option\">\n",
      "<input dir=\"auto\" class=\"course-quiz-input\" name=\"answer[1fede9f10a9af0fb78f1d4a56bcf56c0][]\" id=\"gensym_544fedc056e1d\" value=\"0bc1ac6134c68285b048576907301b43\" type=\"radio\"><label for=\"gensym_544fedc056e1d\" style=\"cursor:pointer;\">The fraction of 0's is 1-e<sup>-79/99</sup>.&nbsp;\n",
      "</label>\n",
      "</div>\n",
      "<div class=\"course-quiz-option\">\n",
      "<input dir=\"auto\" class=\"course-quiz-input\" name=\"answer[1fede9f10a9af0fb78f1d4a56bcf56c0][]\" id=\"gensym_544fedc0574d6\" value=\"a896eeb52d0013b3f3d5d79bb41985e4\" type=\"radio\"><label for=\"gensym_544fedc0574d6\" style=\"cursor:pointer;\">The fraction of 1's is e<sup>-79/99</sup>.&nbsp;\n",
      "</label>\n",
      "</div>\n",
      "<div class=\"course-quiz-option\">\n",
      "<input dir=\"auto\" class=\"course-quiz-input\" name=\"answer[1fede9f10a9af0fb78f1d4a56bcf56c0][]\" id=\"gensym_544fedc057b14\" value=\"4d0a85d8883d9867aa5a0de9e827a1d7\" type=\"radio\"><label for=\"gensym_544fedc057b14\" style=\"cursor:pointer;\">The fraction of 1's is 1-e<sup>-20/99</sup>.&nbsp;\n",
      "</label>\n",
      "</div>\n",
      "<div class=\"course-quiz-option\">\n",
      "<input dir=\"auto\" class=\"course-quiz-input\" name=\"answer[1fede9f10a9af0fb78f1d4a56bcf56c0][]\" id=\"gensym_544fedc05818e\" value=\"b0f760c9581a5511875818537ca21b46\" type=\"radio\"><label for=\"gensym_544fedc05818e\" style=\"cursor:pointer;\">The fraction of 1's is 20/99. \n",
      "</label>\n",
      "</div>"
     ]
    },
    {
     "cell_type": "heading",
     "level": 4,
     "metadata": {},
     "source": [
      "Answer 1"
     ]
    },
    {
     "cell_type": "markdown",
     "metadata": {},
     "source": [
      "Compute answer here"
     ]
    },
    {
     "cell_type": "heading",
     "level": 3,
     "metadata": {},
     "source": [
      "Question 2"
     ]
    },
    {
     "cell_type": "markdown",
     "metadata": {},
     "source": [
      "A certain Web mail service (like gmail, e.g.) has 10<sup>8</sup>\n",
      "users, and wishes to create a sample of data about these users,\n",
      "occupying 10<sup>10</sup> bytes.  Activity at the service can\n",
      "be viewed as a stream of elements, each of which is an email.\n",
      "The element contains the ID of the sender, which must be one of the\n",
      "10<sup>8</sup> users of the service, and other information,\n",
      "e.g., the recipient(s), and contents of the message.\n",
      "The plan is to pick a subset of the users and collect in the\n",
      "10<sup>10</sup> bytes records of length 100 bytes about every\n",
      "email sent by the users in the selected set (and nothing about\n",
      "other users).\n",
      "<p>\n",
      "The method of Section 4.2.4 will be used.  User ID's will be\n",
      "hashed to a bucket number, from 0 to 999,999.  At all times, there\n",
      "will be a threshold t such that the 100-byte records for all the users whose\n",
      "ID's hash to t or less will be retained, and other users' records\n",
      "will not be retained.  You may assume that each user generates\n",
      "emails at exactly the same rate as other users.\n",
      "As a function of n, the number of emails in the stream so far,\n",
      "what should the threshold t be in order that the selected records\n",
      "will not exceed the 10<sup>10</sup> bytes available to store records?\n",
      "From the list below, identify the true statement about a value of n\n",
      "and its value of t.</p>\n",
      "</div>\n",
      "<div dir=\"auto\" class=\"course-quiz-options\">\n",
      "<div class=\"course-quiz-option\">\n",
      "<input dir=\"auto\" class=\"course-quiz-input\" name=\"answer[6ada92e77b7a46c4a4a9c23f559e97b1][]\" id=\"gensym_544fedc05b5f2\" value=\"2f09fd2efe405419678760f5cedf12be\" type=\"radio\"><label for=\"gensym_544fedc05b5f2\" style=\"cursor:pointer;\">n = 10<sup>10</sup>; t = 100,000</label>\n",
      "</div>\n",
      "<div class=\"course-quiz-option\">\n",
      "<input dir=\"auto\" class=\"course-quiz-input\" name=\"answer[6ada92e77b7a46c4a4a9c23f559e97b1][]\" id=\"gensym_544fedc05bd57\" value=\"88380dbb45f4699e9ac8c03a72d88e24\" type=\"radio\"><label for=\"gensym_544fedc05bd57\" style=\"cursor:pointer;\">n = 10<sup>13</sup>; t = 99</label>\n",
      "</div>\n",
      "<div class=\"course-quiz-option\">\n",
      "<input dir=\"auto\" class=\"course-quiz-input\" name=\"answer[6ada92e77b7a46c4a4a9c23f559e97b1][]\" id=\"gensym_544fedc05c505\" value=\"3890033a5ccdd456e4350a5353a7c3b5\" type=\"radio\"><label for=\"gensym_544fedc05c505\" style=\"cursor:pointer;\">n = 10<sup>11</sup>; t = 1000</label>\n",
      "</div>\n",
      "<div class=\"course-quiz-option\">\n",
      "<input dir=\"auto\" class=\"course-quiz-input\" name=\"answer[6ada92e77b7a46c4a4a9c23f559e97b1][]\" id=\"gensym_544fedc05cc94\" value=\"afe79946f5b76b85cd66c48c766aa69e\" type=\"radio\"><label for=\"gensym_544fedc05cc94\" style=\"cursor:pointer;\">n = 10<sup>13</sup>; t = 9</label>"
     ]
    },
    {
     "cell_type": "heading",
     "level": 4,
     "metadata": {},
     "source": [
      "Answer 2"
     ]
    },
    {
     "cell_type": "markdown",
     "metadata": {},
     "source": [
      "Compute answer 2 here"
     ]
    },
    {
     "cell_type": "heading",
     "level": 2,
     "metadata": {},
     "source": [
      "Week3A (Advanced) "
     ]
    },
    {
     "cell_type": "markdown",
     "metadata": {},
     "source": [
      "Due Date Mon 27 Oct 2014 11:59 PM PDT; Hard Deadline Mon 17 Nov 2014 11:59 PM PST"
     ]
    },
    {
     "cell_type": "heading",
     "level": 3,
     "metadata": {},
     "source": [
      "Question 1"
     ]
    },
    {
     "cell_type": "markdown",
     "metadata": {},
     "source": [
      "<div dir=\"auto\" class=\"course-quiz-question-text\">For the following graph:\n",
      "<p>\n",
      "</p>\n",
      "<pre>   C -- D -- E\n",
      " / |    |    | \\\n",
      "A  |    |    |  B\n",
      " \\ |    |    | /\n",
      "   F -- G -- H\n",
      "</pre>\n",
      "Write the adjacency matrix A, the degree matrix D, and the Laplacian matrix L.\n",
      "For each, find the sum of all entries and the number of nonzero entries.\n",
      "Then identify the true statement from the list below.</div>\n",
      "<div dir=\"auto\" class=\"course-quiz-options\">\n",
      "<div class=\"course-quiz-option\">\n",
      "<input dir=\"auto\" class=\"course-quiz-input\" name=\"answer[612df37212bc5a4292f4e1c368aa1d72][]\" id=\"gensym_544ff012bd88c\" value=\"49c54d1f2190f33db0577aaefd077daa\" type=\"radio\"><label for=\"gensym_544ff012bd88c\" style=\"cursor:pointer;\">D has 16 nonzero entries. </label>\n",
      "</div>\n",
      "<div class=\"course-quiz-option\">\n",
      "<input dir=\"auto\" class=\"course-quiz-input\" name=\"answer[612df37212bc5a4292f4e1c368aa1d72][]\" id=\"gensym_544ff012be1c0\" value=\"03c8298842f1dc9ce710ede94d1741f6\" type=\"radio\"><label for=\"gensym_544ff012be1c0\" style=\"cursor:pointer;\">A has 11 nonzero entries. </label>\n",
      "</div>\n",
      "<div class=\"course-quiz-option\">\n",
      "<input dir=\"auto\" class=\"course-quiz-input\" name=\"answer[612df37212bc5a4292f4e1c368aa1d72][]\" id=\"gensym_544ff012beb10\" value=\"13023753f5fea7b9fc2d055d1208473a\" type=\"radio\"><label for=\"gensym_544ff012beb10\" style=\"cursor:pointer;\">The sum of the entries of L is 8. </label>\n",
      "</div>\n",
      "<div class=\"course-quiz-option\">\n",
      "<input dir=\"auto\" class=\"course-quiz-input\" name=\"answer[612df37212bc5a4292f4e1c368aa1d72][]\" id=\"gensym_544ff012bf3d2\" value=\"8688193901a1eaeadf9e3c7ec319e7eb\" type=\"radio\"><label for=\"gensym_544ff012bf3d2\" style=\"cursor:pointer;\">D has 8 nonzero entries. </label>\n",
      "</div>\n",
      "</div>\n",
      "</div>"
     ]
    },
    {
     "cell_type": "heading",
     "level": 4,
     "metadata": {},
     "source": [
      "Answer 1"
     ]
    },
    {
     "cell_type": "markdown",
     "metadata": {},
     "source": [
      "Compute answer here"
     ]
    },
    {
     "cell_type": "heading",
     "level": 3,
     "metadata": {},
     "source": [
      "Question 2"
     ]
    },
    {
     "cell_type": "markdown",
     "metadata": {},
     "source": [
      "<div dir=\"auto\" class=\"course-quiz-question-text\">You are given the following graph.\n",
      "<p></p>\n",
      "<pre>   2 ----6\n",
      " /  \\    |\n",
      "1    4   |\n",
      " \\  /  \\ |\n",
      "  3      5 \n",
      "</pre>\n",
      "<p></p>\n",
      "<p>\n",
      "The goal is to find two clusters in this graph using Spectral Clustering on the Laplacian matrix.\n",
      "Compute the Laplacian of this graph. Then compute the second eigen vector of the Laplacian (the one corresponding to the second smallest eigenvalue).\n",
      "</p>\n",
      "<p></p>\n",
      "<p>\n",
      "To cluster the points, we decide to split at the mean value. We say that a node is a tie if its value in the eigen-vector is exactly equal to the mean value. Let's assume that if a point is a tie, we choose its cluster at random.\n",
      "Identify the true statement from the list below.</p>\n",
      "</div>\n",
      "<div dir=\"auto\" class=\"course-quiz-options\">\n",
      "<div class=\"course-quiz-option\">\n",
      "<input dir=\"auto\" class=\"course-quiz-input\" name=\"answer[42a32daa12739584b7266dd1d9500ef4][]\" id=\"gensym_544ff012c256f\" value=\"17aa5207e3e7d57820459f974687ef49\" type=\"radio\"><label for=\"gensym_544ff012c256f\" style=\"cursor:pointer;\">4 and 6 can either be in the same cluster or in different clusters (depending on randomness)</label>\n",
      "</div>\n",
      "<div class=\"course-quiz-option\">\n",
      "<input dir=\"auto\" class=\"course-quiz-input\" name=\"answer[42a32daa12739584b7266dd1d9500ef4][]\" id=\"gensym_544ff012c2cb9\" value=\"c6a552afb0c213b065ce6f296601c8ef\" type=\"radio\"><label for=\"gensym_544ff012c2cb9\" style=\"cursor:pointer;\">4 and 5 are in the same cluster</label>\n",
      "</div>\n",
      "<div class=\"course-quiz-option\">\n",
      "<input dir=\"auto\" class=\"course-quiz-input\" name=\"answer[42a32daa12739584b7266dd1d9500ef4][]\" id=\"gensym_544ff012c3452\" value=\"6f861176b6c48da1a8432100890b59b3\" type=\"radio\"><label for=\"gensym_544ff012c3452\" style=\"cursor:pointer;\">5 and 6 can either be in the same cluster or in different clusters (depending on randomness)</label>\n",
      "</div>\n",
      "<div class=\"course-quiz-option\">\n",
      "<input dir=\"auto\" class=\"course-quiz-input\" name=\"answer[42a32daa12739584b7266dd1d9500ef4][]\" id=\"gensym_544ff012c3bac\" value=\"0a3fd9e33f3f300f7728ac02938705e2\" type=\"radio\"><label for=\"gensym_544ff012c3bac\" style=\"cursor:pointer;\">2 and 5 are in different clusters</label>\n",
      "</div>\n",
      "</div>\n",
      "</div>\n"
     ]
    },
    {
     "cell_type": "heading",
     "level": 4,
     "metadata": {},
     "source": [
      "Answer 2"
     ]
    },
    {
     "cell_type": "markdown",
     "metadata": {},
     "source": [
      "Compute answer here"
     ]
    },
    {
     "cell_type": "heading",
     "level": 3,
     "metadata": {},
     "source": [
      "Question 3"
     ]
    },
    {
     "cell_type": "markdown",
     "metadata": {},
     "source": [
      "<div dir=\"auto\" class=\"course-quiz-question-text\">We wish to estimate the surprise number (2nd moment) of a data stream, using the\n",
      "method of AMS.  It happens that our stream consists of ten different values,\n",
      "which we'll call 1, 2,..., 10, that cycle repeatedly.  That is, at timestamps\n",
      "1 through 10, the element of the stream equals the timestamp, at timestamps\n",
      "11 through 20, the element is the timestamp minus 10, and so on.  It is now timestamp\n",
      "75, and a 5 has just been read from the stream.  As a start, you should calculate\n",
      "the surprise number for this time.\n",
      "<p>\n",
      "For our estimate of the surprise number, we shall choose three timestamps\n",
      "at random, and estimate the surprise number from each, using the AMS approach\n",
      "(length of the stream times 2<i>m</i>-1, where <i>m</i> is the number of occurrences\n",
      "of the element of the stream at that timestamp, considering all times from that\n",
      "timestamp on, to the current time).  Then, our estimate will be the median of the\n",
      "three resulting values.\n",
      "</p>\n",
      "<p>\n",
      "You should discover the simple rules that determine the estimate derived from\n",
      "any given timestamp and from any set of three timestamps.  Then, identify from the\n",
      "list below the set of three \"random\" timestamps that give the closest estimate.</p>\n",
      "</div>\n",
      "<div dir=\"auto\" class=\"course-quiz-options\">\n",
      "<div class=\"course-quiz-option\">\n",
      "<input dir=\"auto\" class=\"course-quiz-input\" name=\"answer[fc0e386e677f123ca23549cc122c90d9][]\" id=\"gensym_544ff012c6f2e\" value=\"da33ac971fac070ec6596d629cf3af8e\" type=\"radio\"><label for=\"gensym_544ff012c6f2e\" style=\"cursor:pointer;\">{22, 42, 62} \n",
      "</label>\n",
      "</div>\n",
      "<div class=\"course-quiz-option\">\n",
      "<input dir=\"auto\" class=\"course-quiz-input\" name=\"answer[fc0e386e677f123ca23549cc122c90d9][]\" id=\"gensym_544ff012c7696\" value=\"c3e23c3ae72f0fc56b0234aad9882a0b\" type=\"radio\"><label for=\"gensym_544ff012c7696\" style=\"cursor:pointer;\">{4, 31, 72} \n",
      "</label>\n",
      "</div>\n",
      "<div class=\"course-quiz-option\">\n",
      "<input dir=\"auto\" class=\"course-quiz-input\" name=\"answer[fc0e386e677f123ca23549cc122c90d9][]\" id=\"gensym_544ff012c7dd1\" value=\"f6f62df97a821925f3fbf7b32655eed5\" type=\"radio\"><label for=\"gensym_544ff012c7dd1\" style=\"cursor:pointer;\">{25, 34, 47} \n",
      "</label>\n",
      "</div>\n",
      "<div class=\"course-quiz-option\">\n",
      "<input dir=\"auto\" class=\"course-quiz-input\" name=\"answer[fc0e386e677f123ca23549cc122c90d9][]\" id=\"gensym_544ff012c84ca\" value=\"0c0ff98799c205e15acb6311ce2fa885\" type=\"radio\"><label for=\"gensym_544ff012c84ca\" style=\"cursor:pointer;\">{14, 35, 42} \n",
      "</label>\n",
      "</div>\n",
      "</div>\n",
      "</div>"
     ]
    },
    {
     "cell_type": "heading",
     "level": 4,
     "metadata": {},
     "source": [
      "Answer 3"
     ]
    },
    {
     "cell_type": "markdown",
     "metadata": {},
     "source": [
      "Compute answer here"
     ]
    },
    {
     "cell_type": "heading",
     "level": 3,
     "metadata": {},
     "source": [
      "Question 4"
     ]
    },
    {
     "cell_type": "markdown",
     "metadata": {},
     "source": [
      "<div dir=\"auto\" class=\"course-quiz-question-text\">We wish to use the Flagolet-Martin lgorithm of Section 4.4\n",
      "to count the number of distinct\n",
      "elements in a stream.\n",
      "Suppose that there ten\n",
      "possible elements, 1, 2,..., 10, that could appear in the stream, but only four of them have\n",
      "actually appeared.  To make our estimate of the count of distinct elements,\n",
      "we hash each element to a 4-bit binary number.  The element <i>x</i> is\n",
      "hashed to 3<i>x</i> + 7 (modulo 11).  For example, element 8 hashes to 3*8+7 = 31, which\n",
      "is 9 modulo 11 (i.e., the remainder of 31/11 is 9).  Thus, the 4-bit string\n",
      "for element 8 is 1001.\n",
      "<p>\n",
      "A set of four of the elements 1 through 10 could give an estimate that is exact\n",
      "(if the estimate is 4), or too high, or too low.  You should figure out under what\n",
      "circumstances a set of four elements falls into each of those categories.\n",
      "Then, identify in the list below the set of four elements that gives the\n",
      "exactly correct estimate.</p>\n",
      "</div>\n",
      "<div dir=\"auto\" class=\"course-quiz-options\">\n",
      "<div class=\"course-quiz-option\">\n",
      "<input dir=\"auto\" class=\"course-quiz-input\" name=\"answer[5f59d5e591c3a2768bef9e0ff4fb11ed][]\" id=\"gensym_544ff012cbc42\" value=\"31f4d517c546d3352d10cfd8c37c5da2\" type=\"radio\"><label for=\"gensym_544ff012cbc42\" style=\"cursor:pointer;\">{ 1, 6, 7, 10} \n",
      "</label>\n",
      "</div>\n",
      "<div class=\"course-quiz-option\">\n",
      "<input dir=\"auto\" class=\"course-quiz-input\" name=\"answer[5f59d5e591c3a2768bef9e0ff4fb11ed][]\" id=\"gensym_544ff012cc37d\" value=\"cdd38adf52b865ffdcb87a6d83e49a65\" type=\"radio\"><label for=\"gensym_544ff012cc37d\" style=\"cursor:pointer;\">{2, 5, 7, 10} \n",
      "</label>\n",
      "</div>\n",
      "<div class=\"course-quiz-option\">\n",
      "<input dir=\"auto\" class=\"course-quiz-input\" name=\"answer[5f59d5e591c3a2768bef9e0ff4fb11ed][]\" id=\"gensym_544ff012cca9c\" value=\"a579af8bfb68bf40a729484b52ff859c\" type=\"radio\"><label for=\"gensym_544ff012cca9c\" style=\"cursor:pointer;\">{1, 3, 6, 8} \n",
      "</label>\n",
      "</div>\n",
      "<div class=\"course-quiz-option\">\n",
      "<input dir=\"auto\" class=\"course-quiz-input\" name=\"answer[5f59d5e591c3a2768bef9e0ff4fb11ed][]\" id=\"gensym_544ff012cd1b2\" value=\"e05a2213dbade921d9ab055477d23a56\" type=\"radio\"><label for=\"gensym_544ff012cd1b2\" style=\"cursor:pointer;\">{2, 6, 8, 9} \n",
      "</label>\n",
      "</div>\n",
      "</div>\n"
     ]
    },
    {
     "cell_type": "heading",
     "level": 4,
     "metadata": {},
     "source": [
      "Answer 4"
     ]
    },
    {
     "cell_type": "markdown",
     "metadata": {},
     "source": [
      "Compute answer here"
     ]
    },
    {
     "cell_type": "heading",
     "level": 3,
     "metadata": {},
     "source": [
      "Question 5"
     ]
    },
    {
     "cell_type": "markdown",
     "metadata": {},
     "source": [
      "<div dir=\"auto\" class=\"course-quiz-question-text\">Suppose we are using the DGIM algorithm of Section 4.6.2\n",
      "to estimate the number of 1's\n",
      "in suffixes of a sliding window of length 40.  The current timestamp is 100,\n",
      "and we have the following buckets stored:\n",
      "<p>\n",
      "</p>\n",
      "<center><table bgcolor=\"palegoldenrod\" border=\"5\">\n",
      "<tbody><tr>\n",
      "<th>End Time</th>\n",
      "<td>100</td>\n",
      "<td>98</td>\n",
      "<td>95</td>\n",
      "<td>92</td>\n",
      "<td>87</td>\n",
      "<td>80</td>\n",
      "<td>65</td>\n",
      "</tr>\n",
      "<tr>\n",
      "<th>Size</th>\n",
      "<td>1</td>\n",
      "<td>1</td>\n",
      "<td>2</td>\n",
      "<td>2</td>\n",
      "<td>4</td>\n",
      "<td>8</td>\n",
      "<td>8</td>\n",
      "</tr>\n",
      "</tbody></table></center>\n",
      "<p>\n",
      "Note: we are showing timestamps as absolute values, rather than modulo the\n",
      "window size, as DGIM would do.\n",
      "</p>\n",
      "<p>\n",
      "Suppose that at times 101 through 105, 1's appear in the stream.  Compute the\n",
      "set of buckets that would exist in the system at time 105.  Then identify\n",
      "one such bucket from the list below.  Buckets are represented by pairs\n",
      "(end-time, size).</p>\n",
      "</div>\n",
      "<div dir=\"auto\" class=\"course-quiz-options\">\n",
      "<div class=\"course-quiz-option\">\n",
      "<input dir=\"auto\" class=\"course-quiz-input\" name=\"answer[d3b78f798b24420f2a08756c7fcbd490][]\" id=\"gensym_544ff012d066b\" value=\"3aa14c4501358ab7d822a9e90985fe53\" type=\"radio\"><label for=\"gensym_544ff012d066b\" style=\"cursor:pointer;\">(102,2) \n",
      "</label>\n",
      "</div>\n",
      "<div class=\"course-quiz-option\">\n",
      "<input dir=\"auto\" class=\"course-quiz-input\" name=\"answer[d3b78f798b24420f2a08756c7fcbd490][]\" id=\"gensym_544ff012d0f10\" value=\"2ab2e0af9b7f2ddfe89f120627d924ee\" type=\"radio\"><label for=\"gensym_544ff012d0f10\" style=\"cursor:pointer;\">(100,2) \n",
      "</label>\n",
      "</div>\n",
      "<div class=\"course-quiz-option\">\n",
      "<input dir=\"auto\" class=\"course-quiz-input\" name=\"answer[d3b78f798b24420f2a08756c7fcbd490][]\" id=\"gensym_544ff012d17a2\" value=\"3d9694fb576c481cd79475e7f41c8b5f\" type=\"radio\"><label for=\"gensym_544ff012d17a2\" style=\"cursor:pointer;\">(87,8) \n",
      "</label>\n",
      "</div>\n",
      "<div class=\"course-quiz-option\">\n",
      "<input dir=\"auto\" class=\"course-quiz-input\" name=\"answer[d3b78f798b24420f2a08756c7fcbd490][]\" id=\"gensym_544ff012d1f1e\" value=\"f053feca51f66dc1a0c0498c3fb3e0cd\" type=\"radio\"><label for=\"gensym_544ff012d1f1e\" style=\"cursor:pointer;\">(104,2) \n",
      "</label>\n",
      "</div>\n",
      "</div>"
     ]
    },
    {
     "cell_type": "heading",
     "level": 4,
     "metadata": {},
     "source": [
      "Answer 5"
     ]
    },
    {
     "cell_type": "markdown",
     "metadata": {},
     "source": [
      "Compute answer here"
     ]
    },
    {
     "cell_type": "heading",
     "level": 2,
     "metadata": {},
     "source": [
      "Week4A (Basic)"
     ]
    },
    {
     "cell_type": "markdown",
     "metadata": {},
     "source": [
      "The due date for this quiz is Mon 3 Nov 2014 11:59 PM PST; Hard Deadline Mon 17 Nov 2014 11:59 PM PST"
     ]
    },
    {
     "cell_type": "heading",
     "level": 3,
     "metadata": {},
     "source": [
      "Question 1"
     ]
    },
    {
     "cell_type": "markdown",
     "metadata": {},
     "source": [
      "<div dir=\"auto\" class=\"course-quiz-question-text\">Here is a table of 1-5 star ratings for five movies (M, N, P. Q. R)\n",
      "by three raters (A, B, C).\n",
      "<p>\n",
      "</p>\n",
      "<center><table bgcolor=\"palegoldenrod\" border=\"5\">\n",
      "<tbody><tr>\n",
      "<th> </th>\n",
      "<th>M</th>\n",
      "<th>N</th>\n",
      "<th>P</th>\n",
      "<th>Q</th>\n",
      "<th>R</th>\n",
      "</tr>\n",
      "<tr>\n",
      "<th>A</th>\n",
      "<td>1</td>\n",
      "<td>2</td>\n",
      "<td>3</td>\n",
      "<td>4</td>\n",
      "<td>5</td>\n",
      "</tr>\n",
      "<tr>\n",
      "<th>B</th>\n",
      "<td>2</td>\n",
      "<td>3</td>\n",
      "<td>2</td>\n",
      "<td>5</td>\n",
      "<td>3</td>\n",
      "</tr>\n",
      "<tr>\n",
      "<th>C</th>\n",
      "<td>5</td>\n",
      "<td>5</td>\n",
      "<td>5</td>\n",
      "<td>3</td>\n",
      "<td>2</td>\n",
      "</tr>\n",
      "</tbody></table></center>\n",
      "<p>\n",
      "Normalize the ratings by subtracting the average for each row and then\n",
      "subtracting the average for each column in the resulting\n",
      "table.  Then, identify the true statement\n",
      "about the normalized table.</p>\n",
      "</div>\n",
      "<div dir=\"auto\" class=\"course-quiz-options\">\n",
      "<div class=\"course-quiz-option\">\n",
      "<input dir=\"auto\" class=\"course-quiz-input\" name=\"answer[6c1ceafc3e5ae80657983cca455e0a57][]\" id=\"gensym_5450acaf3e6bf\" value=\"a9e01857927e855cc62f5ef6c3a2941a\" type=\"radio\"><label for=\"gensym_5450acaf3e6bf\" style=\"cursor:pointer;\">\tThe largest element is (A,R)</label>\n",
      "</div>\n",
      "<div class=\"course-quiz-option\">\n",
      "<input dir=\"auto\" class=\"course-quiz-input\" name=\"answer[6c1ceafc3e5ae80657983cca455e0a57][]\" id=\"gensym_5450acaf3ee12\" value=\"4288ca966a6f8a0a9243b4d2e92bc670\" type=\"radio\"><label for=\"gensym_5450acaf3ee12\" style=\"cursor:pointer;\">\tThe entry (A,Q) is -3. </label>\n",
      "</div>\n",
      "<div class=\"course-quiz-option\">\n",
      "<input dir=\"auto\" class=\"course-quiz-input\" name=\"answer[6c1ceafc3e5ae80657983cca455e0a57][]\" id=\"gensym_5450acaf3f4c7\" value=\"4e89e3841b269e89a493e28b696072ca\" type=\"radio\"><label for=\"gensym_5450acaf3f4c7\" style=\"cursor:pointer;\">The entry (B,N) is -1/3. </label>\n",
      "</div>\n",
      "<div class=\"course-quiz-option\">\n",
      "<input dir=\"auto\" class=\"course-quiz-input\" name=\"answer[6c1ceafc3e5ae80657983cca455e0a57][]\" id=\"gensym_5450acaf3fbba\" value=\"87e46e6948e025433a1c36e2c996222c\" type=\"radio\"><label for=\"gensym_5450acaf3fbba\" style=\"cursor:pointer;\">There are more 1's than 0's. </label>\n",
      "</div>\n",
      "</div>\n",
      "</div>"
     ]
    },
    {
     "cell_type": "heading",
     "level": 4,
     "metadata": {},
     "source": [
      "Answer 1"
     ]
    },
    {
     "cell_type": "markdown",
     "metadata": {},
     "source": [
      "Compute answer here"
     ]
    },
    {
     "cell_type": "heading",
     "level": 3,
     "metadata": {},
     "source": [
      "Question 2"
     ]
    },
    {
     "cell_type": "markdown",
     "metadata": {},
     "source": [
      "<div dir=\"auto\" class=\"course-quiz-question-text\">Below is a table giving the profile of three items.\n",
      "<p>\n",
      "</p>\n",
      "<center><table bgcolor=\"paleturquoise\" border=\"5\">\n",
      "<tbody><tr>\n",
      "<th>A</th>\n",
      "<td>1</td>\n",
      "<td>0</td>\n",
      "<td>1</td>\n",
      "<td>0</td>\n",
      "<td>1</td>\n",
      "<td>2</td>\n",
      "</tr>\n",
      "<tr>\n",
      "<th>B</th>\n",
      "<td>1</td>\n",
      "<td>1</td>\n",
      "<td>0</td>\n",
      "<td>0</td>\n",
      "<td>1</td>\n",
      "<td>6</td>\n",
      "</tr>\n",
      "<tr>\n",
      "<th>C</th>\n",
      "<td>0</td>\n",
      "<td>1</td>\n",
      "<td>0</td>\n",
      "<td>1</td>\n",
      "<td>0</td>\n",
      "<td>2</td>\n",
      "</tr>\n",
      "</tbody></table></center>\n",
      "<p>\n",
      "The first five attributes are Boolean, and the last is\n",
      "an integer \"rating.\"  Assume that the scale factor for the\n",
      "rating is \u03b1.  Compute, as a function of \u03b1, the\n",
      "cosine distances between each pair of profiles.\n",
      "For each of \u03b1 = 0, 0.5, 1, and 2, determine the cosine\n",
      "of the angle between each pair of vectors.\n",
      "Which of the following is FALSE?</p>\n",
      "</div>\n",
      "<div dir=\"auto\" class=\"course-quiz-options\">\n",
      "<div class=\"course-quiz-option\">\n",
      "<input dir=\"auto\" class=\"course-quiz-input\" name=\"answer[1c84f130dfe4274699c361a1b1f22aac][]\" id=\"gensym_5450acaf43d14\" value=\"fa04b865833c4924cc3394b46080de5b\" type=\"radio\"><label for=\"gensym_5450acaf43d14\" style=\"cursor:pointer;\">For \u03b1 = 1, B is closer to C than A is. </label>\n",
      "</div>\n",
      "<div class=\"course-quiz-option\">\n",
      "<input dir=\"auto\" class=\"course-quiz-input\" name=\"answer[1c84f130dfe4274699c361a1b1f22aac][]\" id=\"gensym_5450acaf44548\" value=\"b170cca95a2e90f809f957ffa5f73585\" type=\"radio\"><label for=\"gensym_5450acaf44548\" style=\"cursor:pointer;\">For \u03b1 = 2, A is closer to C than B is. </label>\n",
      "</div>\n",
      "<div class=\"course-quiz-option\">\n",
      "<input dir=\"auto\" class=\"course-quiz-input\" name=\"answer[1c84f130dfe4274699c361a1b1f22aac][]\" id=\"gensym_5450acaf44d41\" value=\"f1e4467cf63180a50a875ee93425a4ff\" type=\"radio\"><label for=\"gensym_5450acaf44d41\" style=\"cursor:pointer;\">\tFor \u03b1 = 2, C is closer to B than A is. </label>\n",
      "</div>\n",
      "<div class=\"course-quiz-option\">\n",
      "<input dir=\"auto\" class=\"course-quiz-input\" name=\"answer[1c84f130dfe4274699c361a1b1f22aac][]\" id=\"gensym_5450acaf453b4\" value=\"048da89f7f15826658973afe880abd06\" type=\"radio\"><label for=\"gensym_5450acaf453b4\" style=\"cursor:pointer;\">\tFor \u03b1 = 0, B is closer to C than A is. </label>\n",
      "</div>\n",
      "</div>\n",
      "</div>"
     ]
    },
    {
     "cell_type": "heading",
     "level": 4,
     "metadata": {},
     "source": [
      "Answer 2"
     ]
    },
    {
     "cell_type": "markdown",
     "metadata": {},
     "source": [
      "Compute answer here"
     ]
    },
    {
     "cell_type": "heading",
     "level": 2,
     "metadata": {},
     "source": [
      "Week4B (Basic) "
     ]
    },
    {
     "cell_type": "markdown",
     "metadata": {},
     "source": [
      "The due date for this quiz is Mon 3 Nov 2014 11:59 PM PST; Hard Deadline Mon 17 Nov 2014 11:59 PM PST"
     ]
    },
    {
     "cell_type": "heading",
     "level": 3,
     "metadata": {},
     "source": [
      "Question 1"
     ]
    },
    {
     "cell_type": "markdown",
     "metadata": {},
     "source": [
      "<div dir=\"auto\" class=\"course-quiz-question-text\">Note: In this question, all columns will be written in their transposed form, as rows, to make the typography simpler. Matrix M has three rows and two columns, and the columns form an orthonormal basis. One of the columns is [2/7,3/7,6/7]. There are many options for the second column [x,y,z]. Write down those constraints on x, y, and z. Then, identi fy in the list below the one column that could be [x,y,z]. All components are computed to three decimal places, so the constraints may be satisfied only to a close approximation.</div>\n",
      "<div dir=\"auto\" class=\"course-quiz-options\">\n",
      "<div class=\"course-quiz-option\">\n",
      "<input dir=\"auto\" class=\"course-quiz-input\" name=\"answer[d28687344374244c8352382ba42c08ee][]\" id=\"gensym_5450b2ed24fe1\" value=\"ba38899654c9c8b4f5bed39068d8b8c0\" type=\"radio\"><label for=\"gensym_5450b2ed24fe1\" style=\"cursor:pointer;\">[.429, .857, .286] </label>\n",
      "</div>\n",
      "<div class=\"course-quiz-option\">\n",
      "<input dir=\"auto\" class=\"course-quiz-input\" name=\"answer[d28687344374244c8352382ba42c08ee][]\" id=\"gensym_5450b2ed2587e\" value=\"3b9aa9c8645ac84cd8011c5016b8d33e\" type=\"radio\"><label for=\"gensym_5450b2ed2587e\" style=\"cursor:pointer;\">\t[-.548, .401, .273] </label>\n",
      "</div>\n",
      "<div class=\"course-quiz-option\">\n",
      "<input dir=\"auto\" class=\"course-quiz-input\" name=\"answer[d28687344374244c8352382ba42c08ee][]\" id=\"gensym_5450b2ed2609b\" value=\"81a92d5a0ca4d02ba0269bf90e5dc479\" type=\"radio\"><label for=\"gensym_5450b2ed2609b\" style=\"cursor:pointer;\">\t[.975, .700, -.675] </label>\n",
      "</div>\n",
      "<div class=\"course-quiz-option\">\n",
      "<input dir=\"auto\" class=\"course-quiz-input\" name=\"answer[d28687344374244c8352382ba42c08ee][]\" id=\"gensym_5450b2ed267bb\" value=\"af8a4a7cc6f1e7426299d4c1cf14e846\" type=\"radio\"><label for=\"gensym_5450b2ed267bb\" style=\"cursor:pointer;\">\t[.702, -.702, .117] </label>\n",
      "</div>\n"
     ]
    },
    {
     "cell_type": "heading",
     "level": 4,
     "metadata": {},
     "source": [
      "Answer 1"
     ]
    },
    {
     "cell_type": "markdown",
     "metadata": {},
     "source": [
      "Compute answer here"
     ]
    },
    {
     "cell_type": "heading",
     "level": 3,
     "metadata": {},
     "source": [
      "Question 2"
     ]
    },
    {
     "cell_type": "markdown",
     "metadata": {},
     "source": [
      "<div dir=\"auto\" class=\"course-quiz-question-text\">Note: In this question, all columns will be written\n",
      "in their transposed form, as rows, to make the typography simpler.\n",
      "Matrix M has three rows and three columns, and the columns form an\n",
      "orthonormal basis.  One of the columns is [2/7,3/7,6/7], and another\n",
      "is [6/7, 2/7, -3/7].\n",
      "Let the third column be [x,y,z].\n",
      "Since the length of the vector [x,y,z] must be 1, there is\n",
      "a constraint that x<sup>2</sup>+y<sup>2</sup>+z<sup>2</sup> = 1.\n",
      "However, there are other constraints, and these other constraints\n",
      "can be used to deduce facts about the ratios among x, y, and z.\n",
      "Compute these ratios, and then identify one of them in the list below.</div>\n",
      "<div dir=\"auto\" class=\"course-quiz-options\">\n",
      "<div class=\"course-quiz-option\">\n",
      "<input dir=\"auto\" class=\"course-quiz-input\" name=\"answer[05593e4f265f27593487c12881f26fd9][]\" id=\"gensym_5450b2ed29f1a\" value=\"349eb0aecc75276d66372cd783fc03e2\" type=\"radio\"><label for=\"gensym_5450b2ed29f1a\" style=\"cursor:pointer;\">\t2z = -3x </label>\n",
      "</div>\n",
      "<div class=\"course-quiz-option\">\n",
      "<input dir=\"auto\" class=\"course-quiz-input\" name=\"answer[05593e4f265f27593487c12881f26fd9][]\" id=\"gensym_5450b2ed2a7a8\" value=\"3189cbf2b1f7b87ee0c2f6f6decec0ae\" type=\"radio\"><label for=\"gensym_5450b2ed2a7a8\" style=\"cursor:pointer;\">y = 3z </label>\n",
      "</div>\n",
      "<div class=\"course-quiz-option\">\n",
      "<input dir=\"auto\" class=\"course-quiz-input\" name=\"answer[05593e4f265f27593487c12881f26fd9][]\" id=\"gensym_5450b2ed2afee\" value=\"564c69b551ccb70cd37a4f05f214f68f\" type=\"radio\"><label for=\"gensym_5450b2ed2afee\" style=\"cursor:pointer;\">z = -3y </label>\n",
      "</div>\n",
      "<div class=\"course-quiz-option\">\n",
      "<input dir=\"auto\" class=\"course-quiz-input\" name=\"answer[05593e4f265f27593487c12881f26fd9][]\" id=\"gensym_5450b2ed2b73d\" value=\"133d220b864edbdaac43702e1163f345\" type=\"radio\"><label for=\"gensym_5450b2ed2b73d\" style=\"cursor:pointer;\">2x = 3z </label>\n",
      "</div>\n",
      "</div>\n"
     ]
    },
    {
     "cell_type": "heading",
     "level": 4,
     "metadata": {},
     "source": [
      "Answer 2"
     ]
    },
    {
     "cell_type": "markdown",
     "metadata": {},
     "source": [
      "Compute answer here"
     ]
    },
    {
     "cell_type": "heading",
     "level": 3,
     "metadata": {},
     "source": [
      "Question 3"
     ]
    },
    {
     "cell_type": "markdown",
     "metadata": {},
     "source": [
      "<div dir=\"auto\" class=\"course-quiz-question-text\">Suppose we have three points in a two dimensional space: (1,1), (2,2), and (3,4). We want to perform PCA on these points, so we construct a 2-by-2 matrix whose eigenvectors are the directions that best represent these three points. Construct this matrix and identify, in the list below, one of its elements.</div>\n",
      "<div dir=\"auto\" class=\"course-quiz-options\">\n",
      "<div class=\"course-quiz-option\">\n",
      "<input dir=\"auto\" class=\"course-quiz-input\" name=\"answer[4b80292cadc33cfcb0113301e0d58023][]\" id=\"gensym_5450b2ed2e7b5\" value=\"9208063bd18d163523bbed2654bc6118\" type=\"radio\"><label for=\"gensym_5450b2ed2e7b5\" style=\"cursor:pointer;\">18</label>\n",
      "</div>\n",
      "<div class=\"course-quiz-option\">\n",
      "<input dir=\"auto\" class=\"course-quiz-input\" name=\"answer[4b80292cadc33cfcb0113301e0d58023][]\" id=\"gensym_5450b2ed2f0d5\" value=\"843c9459b28547b404ebdac1d7012553\" type=\"radio\"><label for=\"gensym_5450b2ed2f0d5\" style=\"cursor:pointer;\">21</label>\n",
      "</div>\n",
      "<div class=\"course-quiz-option\">\n",
      "<input dir=\"auto\" class=\"course-quiz-input\" name=\"answer[4b80292cadc33cfcb0113301e0d58023][]\" id=\"gensym_5450b2ed2f7f1\" value=\"419b19ae72c5657379d58e4458b7be6e\" type=\"radio\"><label for=\"gensym_5450b2ed2f7f1\" style=\"cursor:pointer;\">16</label>\n",
      "</div>\n",
      "<div class=\"course-quiz-option\">\n",
      "<input dir=\"auto\" class=\"course-quiz-input\" name=\"answer[4b80292cadc33cfcb0113301e0d58023][]\" id=\"gensym_5450b2ed2ffb9\" value=\"75f873bfb205fde523ae5de1ba948c07\" type=\"radio\"><label for=\"gensym_5450b2ed2ffb9\" style=\"cursor:pointer;\">19</label>\n",
      "</div>\n",
      "</div>"
     ]
    },
    {
     "cell_type": "heading",
     "level": 4,
     "metadata": {},
     "source": [
      "Answer 3"
     ]
    },
    {
     "cell_type": "markdown",
     "metadata": {},
     "source": [
      "Compute answer here"
     ]
    },
    {
     "cell_type": "heading",
     "level": 3,
     "metadata": {},
     "source": [
      "Question 4"
     ]
    },
    {
     "cell_type": "markdown",
     "metadata": {},
     "source": [
      "<div dir=\"auto\" class=\"course-quiz-question-text\">Find, in the list below, the vector that is orthogonal to the vector [1,2,3]. Note: the interesting concept regarding eigenvectors is \"orthonormal,\" that is unit vectors that are orthogonal. However, this question avoids using unit vectors to make the calculations simpler.</div>\n",
      "<div dir=\"auto\" class=\"course-quiz-options\">\n",
      "<div class=\"course-quiz-option\">\n",
      "<input dir=\"auto\" class=\"course-quiz-input\" name=\"answer[c0d2313750b14ff6a45c5b3e10660f9f][]\" id=\"gensym_5450b2ed33116\" value=\"bde5f701ea164f959e9c111226013fa8\" type=\"radio\"><label for=\"gensym_5450b2ed33116\" style=\"cursor:pointer;\">\t[1, 1/2, 1/3] </label>\n",
      "</div>\n",
      "<div class=\"course-quiz-option\">\n",
      "<input dir=\"auto\" class=\"course-quiz-input\" name=\"answer[c0d2313750b14ff6a45c5b3e10660f9f][]\" id=\"gensym_5450b2ed338f9\" value=\"b2f7cc48fa446c18ded3b49973d7c10b\" type=\"radio\"><label for=\"gensym_5450b2ed338f9\" style=\"cursor:pointer;\">\t[-3, -2, 5] </label>\n",
      "</div>\n",
      "<div class=\"course-quiz-option\">\n",
      "<input dir=\"auto\" class=\"course-quiz-input\" name=\"answer[c0d2313750b14ff6a45c5b3e10660f9f][]\" id=\"gensym_5450b2ed342c2\" value=\"f9361214ac21c1ff432bea46b14e6c88\" type=\"radio\"><label for=\"gensym_5450b2ed342c2\" style=\"cursor:pointer;\">\t[-1, -1, 1] </label>\n",
      "</div>\n",
      "<div class=\"course-quiz-option\">\n",
      "<input dir=\"auto\" class=\"course-quiz-input\" name=\"answer[c0d2313750b14ff6a45c5b3e10660f9f][]\" id=\"gensym_5450b2ed34ac1\" value=\"a9ceaa3012e41e85707c5ddd6a822064\" type=\"radio\"><label for=\"gensym_5450b2ed34ac1\" style=\"cursor:pointer;\">[-1, 1, -1] </label>\n",
      "</div>\n",
      "</div>"
     ]
    },
    {
     "cell_type": "heading",
     "level": 4,
     "metadata": {},
     "source": [
      "Answer 4 "
     ]
    },
    {
     "cell_type": "markdown",
     "metadata": {},
     "source": [
      "Compute answer here"
     ]
    },
    {
     "cell_type": "heading",
     "level": 2,
     "metadata": {},
     "source": [
      "Week5A (Advanced) "
     ]
    },
    {
     "cell_type": "markdown",
     "metadata": {},
     "source": [
      "The due date for this quiz is Mon 10 Nov 2014 11:59 PM PST; Hard Deadline Mon 17 Nov 2014 11:59 PM PST"
     ]
    },
    {
     "cell_type": "heading",
     "level": 3,
     "metadata": {},
     "source": [
      "Question 1"
     ]
    },
    {
     "cell_type": "markdown",
     "metadata": {},
     "source": [
      "Consider the diagonal matrix M =\n",
      "<table bgcolor=\"floralwhite\" border=\"\"><tbody>\n",
      "<tr>\n",
      "<td>1</td>\n",
      "<td>0</td>\n",
      "<td>0</td>\n",
      "</tr>\n",
      "<tr>\n",
      "<td>0</td>\n",
      "<td>2</td>\n",
      "<td>0</td>\n",
      "</tr>\n",
      "<tr>\n",
      "<td>0</td>\n",
      "<td>0</td>\n",
      "<td>0</td>\n",
      "</tr>\n",
      "</tbody></table>.\n",
      "Compute its Moore-Penrose pseudoinverse, and then identify, in the list below, the true statement about the elements of the pseudoinverse.</div>\n",
      "<div dir=\"auto\" class=\"course-quiz-options\">\n",
      "<div class=\"course-quiz-option\">\n",
      "<input dir=\"auto\" class=\"course-quiz-input\" name=\"answer[d5fb70e3a9d9dc6b250f8b65fe361dfa][]\" id=\"gensym_546163368f100\" value=\"c05f3ec5232587998613dbc3ff004e3e\" type=\"radio\"><label for=\"gensym_546163368f100\" style=\"cursor:pointer;\">There is one element with value -2. </label>\n",
      "</div>\n",
      "<div class=\"course-quiz-option\">\n",
      "<input dir=\"auto\" class=\"course-quiz-input\" name=\"answer[d5fb70e3a9d9dc6b250f8b65fe361dfa][]\" id=\"gensym_546163368f7da\" value=\"6f6fb393c93c5a9850d09bc0bc96d987\" type=\"radio\"><label for=\"gensym_546163368f7da\" style=\"cursor:pointer;\">There are seven elements with value 0. </label>\n",
      "</div>\n",
      "<div class=\"course-quiz-option\">\n",
      "<input dir=\"auto\" class=\"course-quiz-input\" name=\"answer[d5fb70e3a9d9dc6b250f8b65fe361dfa][]\" id=\"gensym_546163368fe70\" value=\"a4b8cf3774da9b4a587f17e6b576ccf3\" type=\"radio\"><label for=\"gensym_546163368fe70\" style=\"cursor:pointer;\">There are seven elements with value infinity. </label>\n",
      "</div>\n",
      "<div class=\"course-quiz-option\">\n",
      "<input dir=\"auto\" class=\"course-quiz-input\" name=\"answer[d5fb70e3a9d9dc6b250f8b65fe361dfa][]\" id=\"gensym_546163369050f\" value=\"5d14ac6a5ea358d8beb877daa6d295b5\" type=\"radio\"><label for=\"gensym_546163369050f\" style=\"cursor:pointer;\">\tThere is one element with value -1. </label>\n",
      "</div>\n",
      "</div>"
     ]
    },
    {
     "cell_type": "heading",
     "level": 4,
     "metadata": {},
     "source": [
      "Answer 1"
     ]
    },
    {
     "cell_type": "markdown",
     "metadata": {},
     "source": [
      "Compute answer here"
     ]
    },
    {
     "cell_type": "heading",
     "level": 3,
     "metadata": {},
     "source": [
      "Question 2"
     ]
    },
    {
     "cell_type": "markdown",
     "metadata": {},
     "source": [
      "An ad publisher selects three ads to place on each page, in order\n",
      "from the top.  Click-through rates (CTR's) at each position differ for\n",
      "each advertiser, and each advertiser has a different CTR\n",
      "for each position.  Each advertiser bids for click-throughs, and each\n",
      "advertiser has a daily budget, which may not be exceeded.  When a click-through\n",
      "occurs, the advertiser pays the amount they bid.\n",
      "In one day, there are 101 click-throughs to be auctioned.\n",
      "<p>\n",
      "Here is a table of\n",
      "the bids, CTR's for positions 1, 2, and 3, and budget for\n",
      "each advertiser.\n",
      "</p>\n",
      "<p>\n",
      "</p>\n",
      "<center><table bgcolor=\"paleturquoise\" border=\"5\">\n",
      "<tbody><tr>\n",
      "<th>Advertiser</th>\n",
      "<th>Bid</th>\n",
      "<th>CTR1</th>\n",
      "<th>CTR2</th>\n",
      "<th>CTR3</th>\n",
      "<th>Budget</th>\n",
      "</tr>\n",
      "<tr>\n",
      "<td>A</td>\n",
      "<td>\\$.10</td>\n",
      "<td>.015</td>\n",
      "<td>.010</td>\n",
      "<td>.005</td>\n",
      "<td>\\$1</td>\n",
      "</tr>\n",
      "<tr>\n",
      "<td>B</td>\n",
      "<td>\\$.09</td>\n",
      "<td>.016</td>\n",
      "<td>.012</td>\n",
      "<td>.006</td>\n",
      "<td>\\$2</td>\n",
      "</tr>\n",
      "<tr>\n",
      "<td>C</td>\n",
      "<td>\\$.08</td>\n",
      "<td>.017</td>\n",
      "<td>.014</td>\n",
      "<td>.007</td>\n",
      "<td>\\$3</td>\n",
      "</tr>\n",
      "<tr>\n",
      "<td>D</td>\n",
      "<td>\\$.07</td>\n",
      "<td>.018</td>\n",
      "<td>.015</td>\n",
      "<td>.008</td>\n",
      "<td>\\$4</td>\n",
      "</tr>\n",
      "<tr>\n",
      "<td>E</td>\n",
      "<td>\\$.06</td>\n",
      "<td>.019</td>\n",
      "<td>.016</td>\n",
      "<td>.010</td>\n",
      "<td>\\$5</td>\n",
      "</tr>\n",
      "</tbody></table></center>\n",
      "<p>\n",
      "The publisher uses the following strategy to allocate the three ad slots:\n",
      "</p>\n",
      "<p>\n",
      "</p>\n",
      "<ol>\n",
      "<li>Any advertiser whose budget is spent is ignored in what follows.\n",
      "</li>\n",
      "<li>The first slot goes to the advertiser whose expected yield for the first slot\n",
      "(product of the bid and the CTR for the first slot) is the greatest.  This advertiser\n",
      "is ignored in what follows.\n",
      "</li>\n",
      "<li>The second slot goes to the advertiser whose expected yield for the second slot\n",
      "(product of the bid and the CTR for the second slot) is the greatest.  This advertiser\n",
      "is ignored in what follows.\n",
      "</li>\n",
      "<li>The third slot goes to the advertiser whose expected yield for the third slot\n",
      "(product of the bid and the CTR for the third slot) is the greatest.\n",
      "</li>\n",
      "</ol>\n",
      "<p>\n",
      "The same three advertisers get the three ad positions until one of two things happens:\n",
      "</p>\n",
      "<p>\n",
      "</p>\n",
      "<ol>\n",
      "<li>An advertiser runs out of budget, or\n",
      "</li>\n",
      "<li>All 101 click-throughs have been obtained.\n",
      "</li>\n",
      "</ol>\n",
      "<p>\n",
      "Either of these events ends one <em>phase</em> of the allocation.\n",
      "If a phase ends because an advertiser ran out of budget, then they are\n",
      "assumed to get all the clicks their budget buys.  During the same phase,\n",
      "we calculate the number of click-throughs received by the other two\n",
      "advertisers by assuming that all three received click-throughs in\n",
      "proportion to their respective CTR's for their positions (round to the\n",
      "nearest integer).  If click-throughs remain, the publisher reallocates all three\n",
      "slots and starts a new phase.\n",
      "</p>\n",
      "<p>\n",
      "If the phase ends because all click-throughs have been allocated, assume that\n",
      "the three advertisers received click-throughs in proportion to their respective\n",
      "CTR's (again, rounding if necessary).\n",
      "</p>\n",
      "<p>\n",
      "Your task is to simulate the allocation of slots and to determine how many\n",
      "click-throughs each of the five advertisers get.</p>\n",
      "</div>\n",
      "<div dir=\"auto\" class=\"course-quiz-options\">\n",
      "<div class=\"course-quiz-option\">\n",
      "<input dir=\"auto\" class=\"course-quiz-input\" name=\"answer[7326fb2c54f6cb89128d7f015612eb47][]\" id=\"gensym_54616336938cd\" value=\"19b5ba91bfe107c58c33fdd6bd1ff7f4\" type=\"radio\"><label for=\"gensym_54616336938cd\" style=\"cursor:pointer;\">D gets 0 click-throughs.</label>\n",
      "</div>\n",
      "<div class=\"course-quiz-option\">\n",
      "<input dir=\"auto\" class=\"course-quiz-input\" name=\"answer[7326fb2c54f6cb89128d7f015612eb47][]\" id=\"gensym_5461633693fa9\" value=\"b55f888c1d0b88e4ac5946299c020262\" type=\"radio\"><label for=\"gensym_5461633693fa9\" style=\"cursor:pointer;\">B gets 14 click-throughs. </label>\n",
      "</div>\n",
      "<div class=\"course-quiz-option\">\n",
      "<input dir=\"auto\" class=\"course-quiz-input\" name=\"answer[7326fb2c54f6cb89128d7f015612eb47][]\" id=\"gensym_5461633694661\" value=\"466fff0a8ba6826d4e7abd0d1a1b2073\" type=\"radio\"><label for=\"gensym_5461633694661\" style=\"cursor:pointer;\">\tD gets 7 click-throughs.</label>\n",
      "</div>\n",
      "<div class=\"course-quiz-option\">\n",
      "<input dir=\"auto\" class=\"course-quiz-input\" name=\"answer[7326fb2c54f6cb89128d7f015612eb47][]\" id=\"gensym_5461633694d07\" value=\"2a43e80d18c8367c302c0523df67ebc0\" type=\"radio\"><label for=\"gensym_5461633694d07\" style=\"cursor:pointer;\">A gets 5 click-throughs.</label>\n",
      "</div>\n",
      "</div>"
     ]
    },
    {
     "cell_type": "heading",
     "level": 4,
     "metadata": {},
     "source": [
      "Answer 2"
     ]
    },
    {
     "cell_type": "markdown",
     "metadata": {},
     "source": [
      "Compute answer here"
     ]
    },
    {
     "cell_type": "heading",
     "level": 3,
     "metadata": {},
     "source": [
      "Question 3"
     ]
    },
    {
     "cell_type": "markdown",
     "metadata": {},
     "source": [
      "In certain clustering algorithms, such as CURE,\n",
      "we need to pick a representative set of points in a supposed cluster, and these points should be as far away from each other as possible.  That is, begin with the two furthest points, and at each step add the point whose minimum distance to any of the previously selected points is maximum.\n",
      "<p>\n",
      "Suppose you are given the following points in two-dimensional Euclidean space: x = (0,0); y = (10,10), a = (1,6); b = (3,7); c = (4,3); d = (7,7), e = (8,2); f = (9,5).  Obviously, x and y are furthest apart, so start with these.  You must add five more points, which we shall refer to as the first, second,..., fifth points in what follows.  The distance measure is the normal Euclidean <i>L</i><sub>2</sub>-norm.  Which of the following is true about the order in which the five points are added?</p>\n",
      "</div>\n",
      "<div dir=\"auto\" class=\"course-quiz-options\">\n",
      "<div class=\"course-quiz-option\">\n",
      "<input dir=\"auto\" class=\"course-quiz-input\" name=\"answer[b01940ea155bb55d3f4077e1d8dc5ef8][]\" id=\"gensym_5461633698256\" value=\"9161b3abfaed007b9ee8ec4d6d6d08e9\" type=\"radio\"><label for=\"gensym_5461633698256\" style=\"cursor:pointer;\">c is added first</label>\n",
      "</div>\n",
      "<div class=\"course-quiz-option\">\n",
      "<input dir=\"auto\" class=\"course-quiz-input\" name=\"answer[b01940ea155bb55d3f4077e1d8dc5ef8][]\" id=\"gensym_5461633698924\" value=\"85f7d3628d13c0d34551f2c17f80c997\" type=\"radio\"><label for=\"gensym_5461633698924\" style=\"cursor:pointer;\">b is added fourth</label>\n",
      "</div>\n",
      "<div class=\"course-quiz-option\">\n",
      "<input dir=\"auto\" class=\"course-quiz-input\" name=\"answer[b01940ea155bb55d3f4077e1d8dc5ef8][]\" id=\"gensym_5461633699070\" value=\"73232a4427277ba861faa2c5b5020a74\" type=\"radio\"><label for=\"gensym_5461633699070\" style=\"cursor:pointer;\">b is added third</label>\n",
      "</div>\n",
      "<div class=\"course-quiz-option\">\n",
      "<input dir=\"auto\" class=\"course-quiz-input\" name=\"answer[b01940ea155bb55d3f4077e1d8dc5ef8][]\" id=\"gensym_5461633699783\" value=\"9535d0f34d9a56e300d529e4a1f93295\" type=\"radio\"><label for=\"gensym_5461633699783\" style=\"cursor:pointer;\">c is added third</label>\n",
      "</div>\n",
      "</div>"
     ]
    },
    {
     "cell_type": "heading",
     "level": 4,
     "metadata": {},
     "source": [
      "Answer 3"
     ]
    },
    {
     "cell_type": "markdown",
     "metadata": {},
     "source": [
      "Compute answer here"
     ]
    },
    {
     "cell_type": "heading",
     "level": 3,
     "metadata": {},
     "source": [
      "Week5B (Basic) "
     ]
    },
    {
     "cell_type": "markdown",
     "metadata": {},
     "source": [
      "We wish to cluster the following set of points:\n",
      "<p>\n",
      "<img src=\"files/otc_gold.gif\"></p>\n",
      "<p>\n",
      "into 10 clusters.  We initially choose each of the green points (25,125), (44,105), (29,97), (35,63), (55,63), (42,57), (23,40), (64,37), (33,22), and (55,20) as a\n",
      "centroid.  Assign each of the gold points to their nearest centroid.\n",
      "(Note: the scales of the horizontal and vertical axes differ, so you\n",
      "really need to apply the formula for distance of points; you can't just\n",
      "\"eyeball\" it.)\n",
      "Then, recompute the centroids of each of the clusters.\n",
      "Do any of the points then get reassigned to a new cluster on the next round?\n",
      "Identify the true statement in the list below.  Each statement\n",
      "refers either to a centroid AFTER recomputation of centroids (precise\n",
      "to one decimal place) or to a\n",
      "point that gets reclassified.</p>\n",
      "</div>\n",
      "<div dir=\"auto\" class=\"course-quiz-options\">\n",
      "<div class=\"course-quiz-option\">\n",
      "<input dir=\"auto\" class=\"course-quiz-input\" name=\"answer[245af0cad5d79758caa1762602d79da5][]\" id=\"gensym_54616510b196e\" value=\"0a9d03ac542a6239cf0f9ea79583f771\" type=\"radio\"><label for=\"gensym_54616510b196e\" style=\"cursor:pointer;\">There is a centroid after recomputation at (54.5,111.8) </label>\n",
      "</div>\n",
      "<div class=\"course-quiz-option\">\n",
      "<input dir=\"auto\" class=\"course-quiz-input\" name=\"answer[245af0cad5d79758caa1762602d79da5][]\" id=\"gensym_54616510b2069\" value=\"020b4b92f9f88f241df0dce6f987e30e\" type=\"radio\"><label for=\"gensym_54616510b2069\" style=\"cursor:pointer;\">There is a centroid after recomputation at (50.3,116.3) </label>\n",
      "</div>\n",
      "<div class=\"course-quiz-option\">\n",
      "<input dir=\"auto\" class=\"course-quiz-input\" name=\"answer[245af0cad5d79758caa1762602d79da5][]\" id=\"gensym_54616510b273d\" value=\"d8253fc5d186990dacd1c5bd156b05b4\" type=\"radio\"><label for=\"gensym_54616510b273d\" style=\"cursor:pointer;\">There is a centroid after recomputation at (34.3,133.3)</label>\n",
      "</div>\n",
      "<div class=\"course-quiz-option\">\n",
      "<input dir=\"auto\" class=\"course-quiz-input\" name=\"answer[245af0cad5d79758caa1762602d79da5][]\" id=\"gensym_54616510b2e7c\" value=\"12b08f3287072547f1fd7268769ad17f\" type=\"radio\"><label for=\"gensym_54616510b2e7c\" style=\"cursor:pointer;\">The point (38,115) is reassigned after computation of centroids. </label>\n",
      "</div>\n",
      "</div>\n"
     ]
    },
    {
     "cell_type": "heading",
     "level": 4,
     "metadata": {},
     "source": [
      "Answer 1"
     ]
    },
    {
     "cell_type": "markdown",
     "metadata": {},
     "source": [
      "Compute answer 1 here"
     ]
    },
    {
     "cell_type": "heading",
     "level": 3,
     "metadata": {},
     "source": [
      "Question 2"
     ]
    },
    {
     "cell_type": "markdown",
     "metadata": {},
     "source": [
      "When performing a k-means clustering, success\n",
      "depends very much on the initially chosen points.  Suppose that we\n",
      "choose two centroids (a,b) = (5,10) and (c,d) = (20,5),\n",
      "and the data truly belongs to two\n",
      "rectangular clusters, as suggested by the following diagram:\n",
      "<p>\n",
      "<img src=\"files/otc_sq-clust.gif\"></p>\n",
      "<p>\n",
      "Under what circumstances will the initial clustering be successful?\n",
      "That is, under what conditions will all the yellow points be assigned\n",
      "to the centroid (5,10), while all of the blue points are assigned to\n",
      "cluster (20,5))?  Identify in the list below, a pair of rectangles (described by\n",
      "their upper left corner, UL, and their lower-right corner LR) that are\n",
      "successfully clustered.</p>\n",
      "</div>\n",
      "<div dir=\"auto\" class=\"course-quiz-options\">\n",
      "<div class=\"course-quiz-option\">\n",
      "<input dir=\"auto\" class=\"course-quiz-input\" name=\"answer[8d2ebafd292f0c9ae7590a4bae2d449f][]\" id=\"gensym_54616510b629b\" value=\"77c17d348c93f6176023b378cfa0d034\" type=\"radio\"><label for=\"gensym_54616510b629b\" style=\"cursor:pointer;\">Yellow: UL=(3,15) and LR=(13,7); Blue: UL=(11,5) and LR=(17,2) </label>\n",
      "</div>\n",
      "<div class=\"course-quiz-option\">\n",
      "<input dir=\"auto\" class=\"course-quiz-input\" name=\"answer[8d2ebafd292f0c9ae7590a4bae2d449f][]\" id=\"gensym_54616510b6bf9\" value=\"33130e919464f4df783bc4c338a19ade\" type=\"radio\"><label for=\"gensym_54616510b6bf9\" style=\"cursor:pointer;\">\tYellow: UL=(7,8) and LR=(12,5); Blue: UL=(15,14) and LR=(20,10) </label>\n",
      "</div>\n",
      "<div class=\"course-quiz-option\">\n",
      "<input dir=\"auto\" class=\"course-quiz-input\" name=\"answer[8d2ebafd292f0c9ae7590a4bae2d449f][]\" id=\"gensym_54616510b7477\" value=\"09b736448ab5cdfb595060d1b92c445a\" type=\"radio\"><label for=\"gensym_54616510b7477\" style=\"cursor:pointer;\">\tYellow: UL=(6,7) and LR=(11,4); Blue: UL=(14,10) and LR=(23,6) </label>\n",
      "</div>\n",
      "<div class=\"course-quiz-option\">\n",
      "<input dir=\"auto\" class=\"course-quiz-input\" name=\"answer[8d2ebafd292f0c9ae7590a4bae2d449f][]\" id=\"gensym_54616510b7b69\" value=\"c81b8d456126ff2c76c1bcfa509f6c60\" type=\"radio\"><label for=\"gensym_54616510b7b69\" style=\"cursor:pointer;\">Yellow: UL=(7,12) and LR=(12,8); Blue: UL=(16,19) and LR=(25,12) </label>\n",
      "</div>\n",
      "</div>\n"
     ]
    },
    {
     "cell_type": "heading",
     "level": 4,
     "metadata": {},
     "source": [
      "Answer 2"
     ]
    },
    {
     "cell_type": "markdown",
     "metadata": {},
     "source": [
      "Compute answer here"
     ]
    },
    {
     "cell_type": "heading",
     "level": 3,
     "metadata": {},
     "source": [
      "Question 3"
     ]
    },
    {
     "cell_type": "markdown",
     "metadata": {},
     "source": [
      "<div dir=\"auto\" class=\"course-quiz-question-text\">Suppose we apply the BALANCE algorithm with bids of 0 or 1 only, to a situation where advertiser A bids on query words x and y, while advertiser B bids on query words x and z. Both have a budget of $2. Identify in the list below a sequence of four queries that will certainly be handled optimally by the algorithm.</div>\n",
      "<div dir=\"auto\" class=\"course-quiz-options\">\n",
      "<div class=\"course-quiz-option\">\n",
      "<input dir=\"auto\" class=\"course-quiz-input\" name=\"answer[10010845046d07a042b636dd10667241][]\" id=\"gensym_54616510baeb4\" value=\"4f25b2828cf203492b719e14fb39df2f\" type=\"radio\"><label for=\"gensym_54616510baeb4\" style=\"cursor:pointer;\">xzzx</label>\n",
      "</div>\n",
      "<div class=\"course-quiz-option\">\n",
      "<input dir=\"auto\" class=\"course-quiz-input\" name=\"answer[10010845046d07a042b636dd10667241][]\" id=\"gensym_54616510bb5c8\" value=\"aff3d433915c10a895a7494509e37ac0\" type=\"radio\"><label for=\"gensym_54616510bb5c8\" style=\"cursor:pointer;\">yxzz</label>\n",
      "</div>\n",
      "<div class=\"course-quiz-option\">\n",
      "<input dir=\"auto\" class=\"course-quiz-input\" name=\"answer[10010845046d07a042b636dd10667241][]\" id=\"gensym_54616510bbca7\" value=\"fa958ca4b5cb5b8245d08a711d07adec\" type=\"radio\"><label for=\"gensym_54616510bbca7\" style=\"cursor:pointer;\">yyxx</label>\n",
      "</div>\n",
      "<div class=\"course-quiz-option\">\n",
      "<input dir=\"auto\" class=\"course-quiz-input\" name=\"answer[10010845046d07a042b636dd10667241][]\" id=\"gensym_54616510bc37a\" value=\"763871c8dd965361245eb1bae14e41bd\" type=\"radio\"><label for=\"gensym_54616510bc37a\" style=\"cursor:pointer;\">zxyy</label>\n",
      "</div>\n",
      "</div>"
     ]
    },
    {
     "cell_type": "heading",
     "level": 4,
     "metadata": {},
     "source": [
      "Answer 3"
     ]
    },
    {
     "cell_type": "markdown",
     "metadata": {},
     "source": [
      "Compute answer here"
     ]
    },
    {
     "cell_type": "heading",
     "level": 3,
     "metadata": {},
     "source": [
      "Question 4"
     ]
    },
    {
     "cell_type": "markdown",
     "metadata": {},
     "source": [
      "<div dir=\"auto\" class=\"course-quiz-question-text\">The set cover problem is: given a list of sets, find a smallest collection of these sets such that every element in any of the sets is in at least one set of the collection. As we form a collection, we say an element is covered if it is in at least one set of the collection.\n",
      "Note: In this problem, we shall represent sets by concatenating their elements, without brackets or commas. For example, {A,B} will be represented simply as AB.\n",
      "\n",
      "There are many greedy algorithms that could be used to pick a collection of sets that is close to as small as possible. Here are some that you will consider in this problem.\n",
      "\n",
      "Dumb: Select sets for the collection in the order in which they appear on the list. Stop when all elements are covered.\n",
      "\n",
      "Simple: Consider sets in the order in which they appear on the list. When it is considered, select a set if it has at least one element that is not already covered. Stop when all elements are covered.\n",
      "\n",
      "Largest-First: Consider sets in order of their size. If there are ties, break the tie in favor of the one that appears first on the list. When it is considered, select a set if it has at least one element that is not already covered. Stop when all elements are covered.\n",
      "\n",
      "Most-Help: Consider sets in order of the number of elements they contain that are not already covered. If there are ties, break the tie in favor of the one that appears first on the list. Stop when all elements are covered.\n",
      "\n",
      "Here is a list of sets:\n",
      "\n",
      "AB, BC, CD, DE, EF, FG, GH, AH, ADG, ADF\n",
      "First, determine the optimum solution, that is, the fewest sets that can be selected for a collection that covers all eight elements A,B,...,H. Then, determine the sizes of the collections that will be constructed by each of the four algorithms mentioned above. Compute the ratio of the size returned by the algorithm to the optimum size, and identify one of these ratios in the list below, correct to two decimal places.</div>\n",
      "<div dir=\"auto\" class=\"course-quiz-options\">\n",
      "<div class=\"course-quiz-option\">\n",
      "<input dir=\"auto\" class=\"course-quiz-input\" name=\"answer[f4a9cab189c71f59d195de1d45b6c19d][]\" id=\"gensym_54616510c0276\" value=\"1cd84ff79b97582f439eba0f245ad79e\" type=\"radio\"><label for=\"gensym_54616510c0276\" style=\"cursor:pointer;\">The ratio for Dumb is 2.33 \n",
      "</label>\n",
      "</div>\n",
      "<div class=\"course-quiz-option\">\n",
      "<input dir=\"auto\" class=\"course-quiz-input\" name=\"answer[f4a9cab189c71f59d195de1d45b6c19d][]\" id=\"gensym_54616510c099b\" value=\"dcb28916c336aeade042c5ff08e9573c\" type=\"radio\"><label for=\"gensym_54616510c099b\" style=\"cursor:pointer;\">The ratio for Simple is 1.50 \n",
      "</label>\n",
      "</div>\n",
      "<div class=\"course-quiz-option\">\n",
      "<input dir=\"auto\" class=\"course-quiz-input\" name=\"answer[f4a9cab189c71f59d195de1d45b6c19d][]\" id=\"gensym_54616510c10f8\" value=\"358db303351288ce6b12d85b2de1cc92\" type=\"radio\"><label for=\"gensym_54616510c10f8\" style=\"cursor:pointer;\">The ratio for Simple is 1.75 </label>\n",
      "</div>\n",
      "<div class=\"course-quiz-option\">\n",
      "<input dir=\"auto\" class=\"course-quiz-input\" name=\"answer[f4a9cab189c71f59d195de1d45b6c19d][]\" id=\"gensym_54616510c1818\" value=\"d30cd4c27887d26ecbf0be9943c6536a\" type=\"radio\"><label for=\"gensym_54616510c1818\" style=\"cursor:pointer;\">The ratio for Largest-First is 2.00 \n",
      "</label>\n",
      "</div>\n",
      "</div>"
     ]
    },
    {
     "cell_type": "heading",
     "level": 4,
     "metadata": {},
     "source": [
      "Answer 4"
     ]
    },
    {
     "cell_type": "markdown",
     "metadata": {},
     "source": [
      "Compute answer here"
     ]
    },
    {
     "cell_type": "heading",
     "level": 3,
     "metadata": {},
     "source": [
      "Question 5"
     ]
    },
    {
     "cell_type": "markdown",
     "metadata": {},
     "source": [
      "This bipartite graph:\n",
      "<p>\n",
      "<img src=\"https://d396qusza40orc.cloudfront.net/mmds/images/otc.gif\"></p>\n",
      "<p>\n",
      "Has several perfect matchings.  Find all the perfect matchings and\n",
      "then identify, in the list below, a pair of edges that can appear together\n",
      "in a perfect matching.</p>\n",
      "</div>\n",
      "<div dir=\"auto\" class=\"course-quiz-options\">\n",
      "<div class=\"course-quiz-option\">\n",
      "<input dir=\"auto\" class=\"course-quiz-input\" name=\"answer[2c5443eac202b29e4162f8ec56148e6a][]\" id=\"gensym_54616510c4bd4\" value=\"b6ed3b4df466aff545ac3ce0c5595492\" type=\"radio\"><label for=\"gensym_54616510c4bd4\" style=\"cursor:pointer;\">a<sub>4</sub>-b<sub>3</sub> and a<sub>3</sub>-b<sub>1</sub></label>\n",
      "</div>\n",
      "<div class=\"course-quiz-option\">\n",
      "<input dir=\"auto\" class=\"course-quiz-input\" name=\"answer[2c5443eac202b29e4162f8ec56148e6a][]\" id=\"gensym_54616510c5316\" value=\"51ca8e2ab2c770c1b9367ab8f08a4d56\" type=\"radio\"><label for=\"gensym_54616510c5316\" style=\"cursor:pointer;\">a<sub>1</sub>-b<sub>2</sub> and a<sub>4</sub>-b<sub>4</sub></label>\n",
      "</div>\n",
      "<div class=\"course-quiz-option\">\n",
      "<input dir=\"auto\" class=\"course-quiz-input\" name=\"answer[2c5443eac202b29e4162f8ec56148e6a][]\" id=\"gensym_54616510c5acf\" value=\"5ba7049c4bdb0ba42c98eff4754002f0\" type=\"radio\"><label for=\"gensym_54616510c5acf\" style=\"cursor:pointer;\">a<sub>0</sub>-b<sub>0</sub> and a<sub>0</sub>-b<sub>1</sub></label>\n",
      "</div>\n",
      "<div class=\"course-quiz-option\">\n",
      "<input dir=\"auto\" class=\"course-quiz-input\" name=\"answer[2c5443eac202b29e4162f8ec56148e6a][]\" id=\"gensym_54616510c626d\" value=\"f7bc614cb0bd58512174bd8ffabaf786\" type=\"radio\"><label for=\"gensym_54616510c626d\" style=\"cursor:pointer;\">a<sub>4</sub>-b<sub>4</sub> and a<sub>0</sub>-b<sub>0</sub></label>\n",
      "</div>\n",
      "</div>"
     ]
    },
    {
     "cell_type": "heading",
     "level": 4,
     "metadata": {},
     "source": [
      "Answer 5"
     ]
    },
    {
     "cell_type": "markdown",
     "metadata": {},
     "source": [
      "Compute answer here"
     ]
    },
    {
     "cell_type": "heading",
     "level": 2,
     "metadata": {},
     "source": [
      "Week 6B"
     ]
    },
    {
     "cell_type": "markdown",
     "metadata": {},
     "source": [
      "The due date for this quiz is Mon 17 Nov 2014 7:49 PM PST; Hard Deadline Mon 17 Nov 2014 7:49 PM PST"
     ]
    },
    {
     "cell_type": "heading",
     "level": 3,
     "metadata": {},
     "source": [
      "Question 1"
     ]
    },
    {
     "cell_type": "markdown",
     "metadata": {},
     "source": [
      "<div dir=\"auto\" class=\"course-quiz-question-text\">The figure below shows two positive points (purple squares) and two negative points (green circles):\n",
      "<br><img src=\"files/otc_svm1.gif\"><p>\n",
      "\n",
      "That is, the training data set consists of:\n",
      "\n",
      "</p>\n",
      "<p>\n",
      "\n",
      "(<b>x</b><sub>1</sub>,y<sub>1</sub>) = ((5,4),+1)<br>\n",
      "\n",
      "(<b>x</b><sub>2</sub>,y<sub>2</sub>) = ((8,3),+1)<br>\n",
      "\n",
      "(<b>x</b><sub>3</sub>,y<sub>3</sub>) = ((7,2),-1)<br>\n",
      "\n",
      "(<b>x</b><sub>4</sub>,y<sub>4</sub>) = ((3,3),-1)\n",
      "\n",
      "</p>\n",
      "<p>\n",
      "\n",
      "Our goal is to find the maximum-margin linear classifier for this data.\n",
      "\n",
      "In easy cases, the shortest line between a positive and negative point has\n",
      "\n",
      "a perpendicular bisector that separates the points.  If so, the perpendicular\n",
      "\n",
      "bisector is surely the maximum-margin separator.\n",
      "\n",
      "Alas, in this case, the closest pair of positive and negative points,\n",
      "\n",
      "<b>x</b><sub>2</sub> and <b>x</b><sub>3</sub>, have a perpendicular bisector that misclassifies <b>x</b><sub>1</sub> as\n",
      "\n",
      "negative, so that won't work.\n",
      "\n",
      "</p>\n",
      "<p>\n",
      "\n",
      "The next-best possibility is that we can find a pair of points on one side\n",
      "\n",
      "(i.e., either two positive or two negative points) such that a line parallel\n",
      "\n",
      "to the line through these points is the maximum-margin separator.\n",
      "\n",
      "In these cases, the limit to how far from the two points the parallel line can\n",
      "\n",
      "get is determined by the closest (to the line between the two points)\n",
      "\n",
      "of the points on the other side.  For our simple data set, this situation holds.\n",
      "\n",
      "</p>\n",
      "<p>\n",
      "\n",
      "Consider all possibilities for boundaries of this type, and express the boundary\n",
      "\n",
      "as <b>w</b>.<b>x</b>+<i>b</i>=0, such that\n",
      "\n",
      "<b>w</b>.<b>x</b>+<i>b</i>\u22651 for positive points <b>x</b> and\n",
      "\n",
      "<b>w</b>.<b>x</b>+<i>b</i>\u2264-1 for negative points <b>x</b>.\n",
      "\n",
      "Assuming that <b>w</b> = (<i>w</i><sub>1</sub>,<i>w</i><sub>2</sub>), identify in the list below the true\n",
      "\n",
      "statement about one of <i>w</i><sub>1</sub>, <i>w</i><sub>2</sub>, and <i>b</i>.</p>\n",
      "</div>\n",
      "<div dir=\"auto\" class=\"course-quiz-options\">\n",
      "<div class=\"course-quiz-option\">\n",
      "<input dir=\"auto\" class=\"course-quiz-input\" name=\"answer[e1a99f7b4fa8abf0bcfc487686964783][]\" id=\"gensym_546ade0d17e67\" value=\"10e75af88248d06c12a932740ef6a329\" type=\"radio\"><label for=\"gensym_546ade0d17e67\" style=\"cursor:pointer;\"><i>w</i><sub>1</sub> = 1/3</label>\n",
      "</div>\n",
      "<div class=\"course-quiz-option\">\n",
      "<input dir=\"auto\" class=\"course-quiz-input\" name=\"answer[e1a99f7b4fa8abf0bcfc487686964783][]\" id=\"gensym_546ade0d1856d\" value=\"b6335cec9fd6039be982a4d25728f24a\" type=\"radio\"><label for=\"gensym_546ade0d1856d\" style=\"cursor:pointer;\"><i>w</i><sub>2</sub> = 3/2</label>\n",
      "</div>\n",
      "<div class=\"course-quiz-option\">\n",
      "<input dir=\"auto\" class=\"course-quiz-input\" name=\"answer[e1a99f7b4fa8abf0bcfc487686964783][]\" id=\"gensym_546ade0d19099\" value=\"2d5ec0dd96f0c3c525bd53269b5ffd69\" type=\"radio\"><label for=\"gensym_546ade0d19099\" style=\"cursor:pointer;\"><i>w</i><sub>1</sub> = 2/5</label>\n",
      "</div>\n",
      "<div class=\"course-quiz-option\">\n",
      "<input dir=\"auto\" class=\"course-quiz-input\" name=\"answer[e1a99f7b4fa8abf0bcfc487686964783][]\" id=\"gensym_546ade0d197e2\" value=\"7ee1f1b8689f1dcc9ac202e834547ec4\" type=\"radio\"><label for=\"gensym_546ade0d197e2\" style=\"cursor:pointer;\"><i>w</i><sub>1</sub> = 1</label>\n",
      "</div>\n",
      "</div>\n",
      "</div>"
     ]
    },
    {
     "cell_type": "heading",
     "level": 4,
     "metadata": {},
     "source": [
      "Answer 1"
     ]
    },
    {
     "cell_type": "markdown",
     "metadata": {},
     "source": [
      "Compute answer here"
     ]
    },
    {
     "cell_type": "heading",
     "level": 3,
     "metadata": {},
     "source": [
      "Question 2"
     ]
    },
    {
     "cell_type": "markdown",
     "metadata": {},
     "source": [
      "<div dir=\"auto\" class=\"course-quiz-question-text\">Consider the following training set of 16 points.  The eight purple squares are\n",
      "positive examples, and the eight green circles are negative examples.\n",
      "<p>\n",
      "<img src=\"files/newsvm4.gif\"></p>\n",
      "<p>\n",
      "We propose to use the diagonal line with slope +1 and intercept +2 as a decision\n",
      "boundary, with positive examples above and negative examples below.\n",
      "However, like any linear boundary for this training set, some examples are\n",
      "misclassified.\n",
      "We can measure the goodness of the boundary by computing all the slack variables\n",
      "that exceed 0, and then using them in one of several objective functions.\n",
      "In this problem, we shall only concern ourselves with computing the slack variables,\n",
      "not an objective function.\n",
      "</p>\n",
      "<p>\n",
      "To be specific, suppose the boundary is written in the form <b>w</b>.<b>x</b>+<i>b</i>=0, where\n",
      "<b>w</b> = (-1,1) and <i>b</i> = -2.  Note that we can scale the three numbers involved\n",
      "as we wish, and so doing changes the margin around the boundary.  However,\n",
      "we want to consider this specific boundary and margin.\n",
      "</p>\n",
      "<p>\n",
      "Determine the slack for each of the 16 points.  Then, identify the correct\n",
      "statement in the list below.</p>\n",
      "</div>\n",
      "<div dir=\"auto\" class=\"course-quiz-options\">\n",
      "<div class=\"course-quiz-option\">\n",
      "<input dir=\"auto\" class=\"course-quiz-input\" name=\"answer[09b1c5ebe11fcc0408d1414529138c02][]\" id=\"gensym_546ade0d1d027\" value=\"d7528266d531105c0d2a4646d7d91978\" type=\"radio\"><label for=\"gensym_546ade0d1d027\" style=\"cursor:pointer;\">The slack for (7,10) is 2. </label>\n",
      "</div>\n",
      "<div class=\"course-quiz-option\">\n",
      "<input dir=\"auto\" class=\"course-quiz-input\" name=\"answer[09b1c5ebe11fcc0408d1414529138c02][]\" id=\"gensym_546ade0d1d994\" value=\"5439113f66b8e6b82887863f41ffe5da\" type=\"radio\"><label for=\"gensym_546ade0d1d994\" style=\"cursor:pointer;\">The slack for (3,6) is 2. </label>\n",
      "</div>\n",
      "<div class=\"course-quiz-option\">\n",
      "<input dir=\"auto\" class=\"course-quiz-input\" name=\"answer[09b1c5ebe11fcc0408d1414529138c02][]\" id=\"gensym_546ade0d1e1ea\" value=\"5ebf0fb7c6d3a8d4d8718606162316f0\" type=\"radio\"><label for=\"gensym_546ade0d1e1ea\" style=\"cursor:pointer;\">The slack for (5,6) is 0.</label>\n",
      "</div>\n",
      "<div class=\"course-quiz-option\">\n",
      "<input dir=\"auto\" class=\"course-quiz-input\" name=\"answer[09b1c5ebe11fcc0408d1414529138c02][]\" id=\"gensym_546ade0d1e8a0\" value=\"1a9739d2c3fd993a8ff90455223ac0d1\" type=\"radio\"><label for=\"gensym_546ade0d1e8a0\" style=\"cursor:pointer;\">The slack for (3,4) is 0.</label>\n",
      "</div>\n",
      "</div>\n",
      "</div><div class=\"course-quiz-question-body\">\n"
     ]
    },
    {
     "cell_type": "heading",
     "level": 4,
     "metadata": {},
     "source": [
      "Answer 2"
     ]
    },
    {
     "cell_type": "markdown",
     "metadata": {},
     "source": [
      "Compute answer here"
     ]
    },
    {
     "cell_type": "heading",
     "level": 3,
     "metadata": {},
     "source": [
      "Question 3"
     ]
    },
    {
     "cell_type": "markdown",
     "metadata": {},
     "source": [
      "<div dir=\"auto\" class=\"course-quiz-question-text\">Below we see a set of 20 points and a decision tree for classifying the points.\n",
      "<p>\n",
      "</p>\n",
      "<center><table><tbody><tr>\n",
      "<td>\n",
      "<img src=\"files/otc_gold-small.gif\">\n",
      "</td>\n",
      "<td>\n",
      "<img src=\"files/otc_dectree1.gif\">\n",
      "</td>\n",
      "</tr></tbody></table></center>\n",
      "<p>\n",
      "To be precise, the 20 points represent (Age,Salary) pairs of people who do or do not buy gold jewelry.  Age (appreviated A in the decision tree) is the x-axis, and Salary (S in the tree) is the y-axis.  Those that do are represented by gold points, and those that do not by green points.  The 10 points of gold-jewelry buyers are:\n",
      "</p>\n",
      "<p>\n",
      "(28,145), (38,115), (43,83), (50,130), (50,90), (50,60), (50,30), (55,118), (63,88), and (65,140).\n",
      "</p>\n",
      "<p>\n",
      "The 10 points of those that do not buy gold jewelry are:\n",
      "</p>\n",
      "<p>\n",
      "(23,40), (25,125), (29,97), (33,22), (35,63), (42,57), (44, 105), (55,63), (55,20), and (64,37).\n",
      "</p>\n",
      "<p>\n",
      "Some of these points are correctly classified by the decision tree and some are not.  Determine the classification of each point, and then indicate in the list below the point that is misclassified.</p>\n",
      "</div>\n",
      "<div dir=\"auto\" class=\"course-quiz-options\">\n",
      "<div class=\"course-quiz-option\">\n",
      "<input dir=\"auto\" class=\"course-quiz-input\" name=\"answer[e6f7c8a066652f41fa096991a39ceb94][]\" id=\"gensym_546ade0d21c3a\" value=\"d47bd9c613230249eefe49630af3c303\" type=\"radio\"><label for=\"gensym_546ade0d21c3a\" style=\"cursor:pointer;\">(50,90) </label>\n",
      "</div>\n",
      "<div class=\"course-quiz-option\">\n",
      "<input dir=\"auto\" class=\"course-quiz-input\" name=\"answer[e6f7c8a066652f41fa096991a39ceb94][]\" id=\"gensym_546ade0d22457\" value=\"110ee918248115c5d4a9624f73557e71\" type=\"radio\"><label for=\"gensym_546ade0d22457\" style=\"cursor:pointer;\">(50,130) </label>\n",
      "</div>\n",
      "<div class=\"course-quiz-option\">\n",
      "<input dir=\"auto\" class=\"course-quiz-input\" name=\"answer[e6f7c8a066652f41fa096991a39ceb94][]\" id=\"gensym_546ade0d22d50\" value=\"6d8e0f347adb6417523bf81586b26f28\" type=\"radio\"><label for=\"gensym_546ade0d22d50\" style=\"cursor:pointer;\">\t(42,57) </label>\n",
      "</div>\n",
      "<div class=\"course-quiz-option\">\n",
      "<input dir=\"auto\" class=\"course-quiz-input\" name=\"answer[e6f7c8a066652f41fa096991a39ceb94][]\" id=\"gensym_546ade0d233f5\" value=\"53f83875e3cb08a64e7bda65f98800a7\" type=\"radio\"><label for=\"gensym_546ade0d233f5\" style=\"cursor:pointer;\">\t(50,60) </label>\n",
      "</div>\n",
      "</div>\n",
      "</div>"
     ]
    },
    {
     "cell_type": "heading",
     "level": 4,
     "metadata": {},
     "source": [
      "Answer 3"
     ]
    },
    {
     "cell_type": "markdown",
     "metadata": {},
     "source": [
      "Compute answer here"
     ]
    },
    {
     "cell_type": "heading",
     "level": 2,
     "metadata": {},
     "source": [
      "Week6A (Advanced) "
     ]
    },
    {
     "cell_type": "markdown",
     "metadata": {},
     "source": [
      "The due date for this quiz is Mon 17 Nov 2014 7:49 PM PST; Hard Deadline Mon 17 Nov 2014 7:49 PM PST"
     ]
    },
    {
     "cell_type": "heading",
     "level": 2,
     "metadata": {},
     "source": [
      "Question 1"
     ]
    },
    {
     "cell_type": "markdown",
     "metadata": {},
     "source": [
      "<div dir=\"auto\" class=\"course-quiz-question-text\">Using the matrix-vector multiplication described in Section 2.3.1,\n",
      "applied to the matrix and vector:\n",
      "<p>\n",
      "</p>\n",
      "<center><table><tbody><tr>\n",
      "<td>\n",
      "<table bgcolor=\"floralwhite\" border=\"5\">\n",
      "<tbody><tr>\n",
      "<td>1</td>\n",
      "<td>2</td>\n",
      "<td>3</td>\n",
      "<td>4</td>\n",
      "</tr>\n",
      "<tr>\n",
      "<td>5</td>\n",
      "<td>6</td>\n",
      "<td>7</td>\n",
      "<td>8</td>\n",
      "</tr>\n",
      "<tr>\n",
      "<td>9</td>\n",
      "<td>10</td>\n",
      "<td>11</td>\n",
      "<td>12</td>\n",
      "</tr>\n",
      "<tr>\n",
      "<td>13</td>\n",
      "<td>14</td>\n",
      "<td>15</td>\n",
      "<td>16</td>\n",
      "</tr>\n",
      "</tbody></table>\n",
      "</td>\n",
      "<td>\n",
      "<table bgcolor=\"floralwhite\" border=\"5\">\n",
      "<tbody><tr><td>1</td></tr>\n",
      "<tr><td>2</td></tr>\n",
      "<tr><td>3</td></tr>\n",
      "<tr><td>4</td></tr>\n",
      "</tbody></table>\n",
      "</td>\n",
      "</tr></tbody></table></center>\n",
      "<p>\n",
      "apply the Map function to this matrix and vector.\n",
      "Then, identify in the list below,\n",
      "one of the key-value pairs that are output of Map.</p>\n",
      "</div>\n",
      "<div dir=\"auto\" class=\"course-quiz-options\">\n",
      "<div class=\"course-quiz-option\">\n",
      "<input dir=\"auto\" class=\"course-quiz-input\" name=\"answer[de624db1388d9dd361ac2f473ae1e88f][]\" id=\"gensym_5470df7235cc1\" value=\"9f0f4fcdde01c90af89e8a0c2e99457f\" type=\"radio\"><label for=\"gensym_5470df7235cc1\" style=\"cursor:pointer;\">(4,28) </label>\n",
      "</div>\n",
      "<div class=\"course-quiz-option\">\n",
      "<input dir=\"auto\" class=\"course-quiz-input\" name=\"answer[de624db1388d9dd361ac2f473ae1e88f][]\" id=\"gensym_5470df7236618\" value=\"d1b08d610ae525080a0aba87905b795b\" type=\"radio\"><label for=\"gensym_5470df7236618\" style=\"cursor:pointer;\">\t(4,150) </label>\n",
      "</div>\n",
      "<div class=\"course-quiz-option\">\n",
      "<input dir=\"auto\" class=\"course-quiz-input\" name=\"answer[de624db1388d9dd361ac2f473ae1e88f][]\" id=\"gensym_5470df7236dc3\" value=\"01ddfec81d0aaf5d1373b0b4c3e6339a\" type=\"radio\"><label for=\"gensym_5470df7236dc3\" style=\"cursor:pointer;\">\t(3,11) </label>\n",
      "</div>\n",
      "<div class=\"course-quiz-option\">\n",
      "<input dir=\"auto\" class=\"course-quiz-input\" name=\"answer[de624db1388d9dd361ac2f473ae1e88f][]\" id=\"gensym_5470df7237594\" value=\"568128f87295aedbc44af1e03d1a54ae\" type=\"radio\"><label for=\"gensym_5470df7237594\" style=\"cursor:pointer;\">\t(4,48) </label>\n",
      "</div>\n",
      "</div>\n",
      "</div>"
     ]
    },
    {
     "cell_type": "heading",
     "level": 4,
     "metadata": {},
     "source": [
      "Answer 1"
     ]
    },
    {
     "cell_type": "markdown",
     "metadata": {},
     "source": [
      "Compute answer here"
     ]
    },
    {
     "cell_type": "heading",
     "level": 2,
     "metadata": {},
     "source": [
      "Question 2"
     ]
    },
    {
     "cell_type": "markdown",
     "metadata": {},
     "source": [
      "<div dir=\"auto\" class=\"course-quiz-question-text\">Suppose we use the algorithm of Section 2.3.10\n",
      "to compute the product of matrices M and N.\n",
      "Let M have x rows and y columns, while N has y rows and z\n",
      "columns.  As a function of x, y, and z, express the answers\n",
      "to the following questions:\n",
      "<p>\n",
      "</p>\n",
      "<ol>\n",
      "<li>The output of the Map function has how many different keys?\n",
      "How many key-value pairs are there with each key?\n",
      "How many key-value pairs are there in all?\n",
      "<p>\n",
      "</p>\n",
      "</li>\n",
      "<li>The input to the Reduce function has how many keys?\n",
      "What is the length of the value (a list) associated with each key?\n",
      "</li>\n",
      "</ol>\n",
      "<p>\n",
      "Then, identify the true statement in the list below.</p>\n",
      "</div>\n",
      "<div dir=\"auto\" class=\"course-quiz-options\">\n",
      "<div class=\"course-quiz-option\">\n",
      "<input dir=\"auto\" class=\"course-quiz-input\" name=\"answer[85c874b6f304d1de11a53e3ebf63a3f8][]\" id=\"gensym_5470df723ada7\" value=\"9380095c156a349ef9d4a7008bf3d3c8\" type=\"radio\"><label for=\"gensym_5470df723ada7\" style=\"cursor:pointer;\">The output of the Map function has xz different keys. \n",
      "</label>\n",
      "</div>\n",
      "<div class=\"course-quiz-option\">\n",
      "<input dir=\"auto\" class=\"course-quiz-input\" name=\"answer[85c874b6f304d1de11a53e3ebf63a3f8][]\" id=\"gensym_5470df723b6ab\" value=\"bac7d77fb7d7486cacd158cfc7c8aabf\" type=\"radio\"><label for=\"gensym_5470df723b6ab\" style=\"cursor:pointer;\">The input to the Reduce function has pairs with lists of length y. </label>\n",
      "</div>\n",
      "<div class=\"course-quiz-option\">\n",
      "<input dir=\"auto\" class=\"course-quiz-input\" name=\"answer[85c874b6f304d1de11a53e3ebf63a3f8][]\" id=\"gensym_5470df723bf1f\" value=\"baa0eed766b7510aa245be618abe5a07\" type=\"radio\"><label for=\"gensym_5470df723bf1f\" style=\"cursor:pointer;\">\tThe output of the Map function has x+z pairs with each key. </label>\n",
      "</div>\n",
      "<div class=\"course-quiz-option\">\n",
      "<input dir=\"auto\" class=\"course-quiz-input\" name=\"answer[85c874b6f304d1de11a53e3ebf63a3f8][]\" id=\"gensym_5470df723c62f\" value=\"bab26e6808f8c4381fb44150801871a2\" type=\"radio\"><label for=\"gensym_5470df723c62f\" style=\"cursor:pointer;\">The output of the Map function has x+z different keys. </label>\n",
      "</div>\n",
      "</div>\n",
      "</div>"
     ]
    },
    {
     "cell_type": "heading",
     "level": 4,
     "metadata": {},
     "source": [
      "Answer 2"
     ]
    },
    {
     "cell_type": "markdown",
     "metadata": {},
     "source": [
      "Compute answer here"
     ]
    },
    {
     "cell_type": "heading",
     "level": 3,
     "metadata": {},
     "source": [
      "Question 3"
     ]
    },
    {
     "cell_type": "markdown",
     "metadata": {},
     "source": [
      "<div dir=\"auto\" class=\"course-quiz-question-text\">Suppose we use the two-stage algorithm of Section 2.3.9\n",
      "to compute the product of matrices M and N.\n",
      "Let M have x rows and y columns, while N has y rows and z\n",
      "columns.  As a function of x, y, and z, express the answers\n",
      "to the following questions:\n",
      "<p>\n",
      "</p>\n",
      "<ol>\n",
      "<li>The output of the first Map function has how many different keys?\n",
      "How many key-value pairs are there with each key?\n",
      "How many key-value pairs are there in all?\n",
      "<p>\n",
      "</p>\n",
      "</li>\n",
      "<li>The output of the first Reduce function has how many keys?\n",
      "What is the length of the value (a list) associated with each key?\n",
      "<p>\n",
      "</p>\n",
      "</li>\n",
      "<li>The output of the second Map function has how many different keys?\n",
      "How many key-value pairs are there with each key?\n",
      "How many key-value pairs are there in all?\n",
      "</li>\n",
      "</ol>\n",
      "<p>\n",
      "Then, identify the true statement in the list below.</p>\n",
      "</div>\n",
      "<div dir=\"auto\" class=\"course-quiz-options\">\n",
      "<div class=\"course-quiz-option\">\n",
      "<input dir=\"auto\" class=\"course-quiz-input\" name=\"answer[5a16a0a4d9fb4f61270a2a92c9a1d3ad][]\" id=\"gensym_5470df723f574\" value=\"fe7c71bf5cbbb456eb05ea6c07cb1e68\" type=\"radio\"><label for=\"gensym_5470df723f574\" style=\"cursor:pointer;\">\t The output of the first Map function has y(x+z) pairs. </label>\n",
      "</div>\n",
      "<div class=\"course-quiz-option\">\n",
      "<input dir=\"auto\" class=\"course-quiz-input\" name=\"answer[5a16a0a4d9fb4f61270a2a92c9a1d3ad][]\" id=\"gensym_5470df723fe4b\" value=\"7b05a25a783c432a06c3979230f5b9f1\" type=\"radio\"><label for=\"gensym_5470df723fe4b\" style=\"cursor:pointer;\">The output of the first Map function has xy pairs. </label>\n",
      "</div>\n",
      "<div class=\"course-quiz-option\">\n",
      "<input dir=\"auto\" class=\"course-quiz-input\" name=\"answer[5a16a0a4d9fb4f61270a2a92c9a1d3ad][]\" id=\"gensym_5470df72405bc\" value=\"2ecb9c777cf3d82f6b562038b8a88007\" type=\"radio\"><label for=\"gensym_5470df72405bc\" style=\"cursor:pointer;\">The output of the first Map function has x(y+z) pairs. </label>\n",
      "</div>\n",
      "<div class=\"course-quiz-option\">\n",
      "<input dir=\"auto\" class=\"course-quiz-input\" name=\"answer[5a16a0a4d9fb4f61270a2a92c9a1d3ad][]\" id=\"gensym_5470df724130f\" value=\"43b1238c323472c82f84c11589c6fc97\" type=\"radio\"><label for=\"gensym_5470df724130f\" style=\"cursor:pointer;\">The output of the first Map function has z pairs with each key.</label>\n",
      "</div>\n",
      "</div>"
     ]
    },
    {
     "cell_type": "heading",
     "level": 4,
     "metadata": {},
     "source": [
      "Answer 3"
     ]
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "Compute answer here"
     ],
     "language": "python",
     "metadata": {},
     "outputs": []
    },
    {
     "cell_type": "heading",
     "level": 3,
     "metadata": {},
     "source": [
      "Question 4"
     ]
    },
    {
     "cell_type": "markdown",
     "metadata": {},
     "source": [
      "<div dir=\"auto\" class=\"course-quiz-question-text\">Suppose we have the following relations:\n",
      "<p>\n",
      "</p>\n",
      "<center><table><tbody><tr>\n",
      "<td>\n",
      "<table bgcolor=\"paleturquoise\">\n",
      "<tbody><tr>\n",
      "<td></td>\n",
      "<td>R</td>\n",
      "<td></td>\n",
      "</tr>\n",
      "<tr>\n",
      "<th>A</th>\n",
      "<th></th>\n",
      "<th>B</th>\n",
      "</tr>\n",
      "<tr>\n",
      "<td>0</td>\n",
      "<td></td>\n",
      "<td>1</td>\n",
      "</tr>\n",
      "<tr>\n",
      "<td>1</td>\n",
      "<td></td>\n",
      "<td>2</td>\n",
      "</tr>\n",
      "<tr>\n",
      "<td>2</td>\n",
      "<td></td>\n",
      "<td>3</td>\n",
      "</tr>\n",
      "</tbody></table>\n",
      "</td>\n",
      "<td width=\"30\"></td>\n",
      "<td>\n",
      "<table bgcolor=\"blue\">\n",
      "<tbody><tr>\n",
      "<td></td>\n",
      "<td>S</td>\n",
      "<td></td>\n",
      "</tr>\n",
      "<tr>\n",
      "<th>B</th>\n",
      "<th></th>\n",
      "<th>C</th>\n",
      "</tr>\n",
      "<tr>\n",
      "<td>0</td>\n",
      "<td></td>\n",
      "<td>1</td>\n",
      "</tr>\n",
      "<tr>\n",
      "<td>1</td>\n",
      "<td></td>\n",
      "<td>2</td>\n",
      "</tr>\n",
      "<tr>\n",
      "<td>2</td>\n",
      "<td></td>\n",
      "<td>3</td>\n",
      "</tr>\n",
      "</tbody></table>\n",
      "</td>\n",
      "</tr></tbody></table></center>\n",
      "<p>\n",
      "and we take their natural join by the algorithm of Section 2.3.7.\n",
      "Apply the Map function to the tuples of these relations.\n",
      "Then, construct the elements that are input to the Reduce function.\n",
      "Identify one of these elements in the list below.</p>\n",
      "</div>\n",
      "<div dir=\"auto\" class=\"course-quiz-options\">\n",
      "<div class=\"course-quiz-option\">\n",
      "<input dir=\"auto\" class=\"course-quiz-input\" name=\"answer[b88409ab41e2f6f89a5381c28fe9decb][]\" id=\"gensym_5470df72450fc\" value=\"0424585bff6ccd78bfc4cad5bb722a52\" type=\"radio\"><label for=\"gensym_5470df72450fc\" style=\"cursor:pointer;\">\t (3, [(R,2)]) </label>\n",
      "</div>\n",
      "<div class=\"course-quiz-option\">\n",
      "<input dir=\"auto\" class=\"course-quiz-input\" name=\"answer[b88409ab41e2f6f89a5381c28fe9decb][]\" id=\"gensym_5470df72458f6\" value=\"dea3d09c6e9a80b788c0719cb5ae6db6\" type=\"radio\"><label for=\"gensym_5470df72458f6\" style=\"cursor:pointer;\">(2,(R,1)) </label>\n",
      "</div>\n",
      "<div class=\"course-quiz-option\">\n",
      "<input dir=\"auto\" class=\"course-quiz-input\" name=\"answer[b88409ab41e2f6f89a5381c28fe9decb][]\" id=\"gensym_5470df72460af\" value=\"d716f497d20e846f7ffc9d7dc48ef78c\" type=\"radio\"><label for=\"gensym_5470df72460af\" style=\"cursor:pointer;\">\t(1, [(S,2)]) </label>\n",
      "</div>\n",
      "<div class=\"course-quiz-option\">\n",
      "<input dir=\"auto\" class=\"course-quiz-input\" name=\"answer[b88409ab41e2f6f89a5381c28fe9decb][]\" id=\"gensym_5470df724683d\" value=\"c4c388053e4301168b030b27cde6b9e0\" type=\"radio\"><label for=\"gensym_5470df724683d\" style=\"cursor:pointer;\">\t(2, [(2,(R,1)), (2,(S,1))]) </label>\n",
      "</div>\n",
      "</div>"
     ]
    },
    {
     "cell_type": "heading",
     "level": 4,
     "metadata": {},
     "source": [
      "Answer 4"
     ]
    },
    {
     "cell_type": "markdown",
     "metadata": {},
     "source": [
      "Compute answer here"
     ]
    },
    {
     "cell_type": "heading",
     "level": 2,
     "metadata": {},
     "source": [
      "Week7B Basic "
     ]
    },
    {
     "cell_type": "markdown",
     "metadata": {},
     "source": [
      "The due date for this quiz is Sun 23 Nov 2014 11:59 PM PST."
     ]
    },
    {
     "cell_type": "heading",
     "level": 3,
     "metadata": {},
     "source": [
      "Question 1"
     ]
    },
    {
     "cell_type": "markdown",
     "metadata": {},
     "source": [
      "Compute the Topic-Specific PageRank for the following link topology. Assume that pages selected for the teleport set are nodes 1 and 2 and that in the teleport set, the weight assigned for node 1 is twice that of node 2. Assume further that the teleport probability, (1 - beta), is 0.3. Which of the following statements is correct?\n",
      "<p>\n",
      "<img src=\"files/otc_pagerank4.gif\"></p>\n",
      "</div>\n",
      "<div dir=\"auto\" class=\"course-quiz-options\">\n",
      "<div class=\"course-quiz-option\">\n",
      "<input dir=\"auto\" class=\"course-quiz-input\" name=\"answer[6c027c80912a34d461a1f19f58259020][]\" id=\"gensym_5470e21f6abcb\" value=\"ce681f86e9be99af6b2bc4fbec524992\" type=\"radio\"><label for=\"gensym_5470e21f6abcb\" style=\"cursor:pointer;\">TSPR(1) = .3576 </label>\n",
      "</div>\n",
      "<div class=\"course-quiz-option\">\n",
      "<input dir=\"auto\" class=\"course-quiz-input\" name=\"answer[6c027c80912a34d461a1f19f58259020][]\" id=\"gensym_5470e21f6b2c9\" value=\"c73b399f8bc90c5617dbbbd92e29dcd6\" type=\"radio\"><label for=\"gensym_5470e21f6b2c9\" style=\"cursor:pointer;\">TSPR(4) = .4787 </label>\n",
      "</div>\n",
      "<div class=\"course-quiz-option\">\n",
      "<input dir=\"auto\" class=\"course-quiz-input\" name=\"answer[6c027c80912a34d461a1f19f58259020][]\" id=\"gensym_5470e21f6bcec\" value=\"8d55c46aa3c51fa871c517fb88992f56\" type=\"radio\"><label for=\"gensym_5470e21f6bcec\" style=\"cursor:pointer;\">TSPR(3) = .9097 </label>\n",
      "</div>\n",
      "<div class=\"course-quiz-option\">\n",
      "<input dir=\"auto\" class=\"course-quiz-input\" name=\"answer[6c027c80912a34d461a1f19f58259020][]\" id=\"gensym_5470e21f6c71b\" value=\"687cdb8653e70a0f01f94d68846feaae\" type=\"radio\"><label for=\"gensym_5470e21f6c71b\" style=\"cursor:pointer;\">TSPR(2) = .8998 </label>\n",
      "</div>\n",
      "</div>\n"
     ]
    },
    {
     "cell_type": "heading",
     "level": 4,
     "metadata": {},
     "source": [
      "Answer 1"
     ]
    },
    {
     "cell_type": "markdown",
     "metadata": {},
     "source": [
      "Compute answer here"
     ]
    },
    {
     "cell_type": "heading",
     "level": 3,
     "metadata": {},
     "source": [
      "Question 2"
     ]
    },
    {
     "cell_type": "markdown",
     "metadata": {},
     "source": [
      "The spam-farm architecture described in Section 5.4.1 suffers from\n",
      "the problem that the target page has many links --- one to each supporting page.\n",
      "To avoid that problem, the spammer could use the architecture shown below:\n",
      "<p>\n",
      "<img src=\"files/otc_spamfarm1.gif\"></p>\n",
      "<p>\n",
      "There, k \"second-tier\" nodes act as intermediaries.  The target page t has only\n",
      "to link to the k second-tier pages, and each of those pages links to m/k of the\n",
      "m supporting pages.\n",
      "Each of the supporting pages links only to t (although most of these links are\n",
      "not shown).\n",
      "Suppose the taxation parameter is \u03b2 = 0.85, and x is the amount of PageRank\n",
      "supplied from outside to the target page.  Let n be the total number of pages\n",
      "in the Web.  Finally, let y be the PageRank of target page t.\n",
      "If we compute the formula for y in terms of k, m, and n, we get a formula with the form\n",
      "</p>\n",
      "<p>\n",
      "</p>\n",
      "<center>\n",
      "y = ax + bm/n + ck/n\n",
      "</center>\n",
      "<p>\n",
      "Note: To arrive at this form, it is necessary at the last step\n",
      "to drop a low-order term that is a fraction of 1/n.\n",
      "Determine coefficients a, b, and c, remembering that \u03b2 is fixed at 0.85.\n",
      "Then, identify the value, correct to two decimal places, for one of these coefficients.</p>\n",
      "</div>\n",
      "<div dir=\"auto\" class=\"course-quiz-options\">\n",
      "<div class=\"course-quiz-option\">\n",
      "<input dir=\"auto\" class=\"course-quiz-input\" name=\"answer[b51dfcbbcf7f59e1573842f5bf31c9eb][]\" id=\"gensym_5470e21f70681\" value=\"fdd23337b7a9059fd2d15612d8e0f9db\" type=\"radio\"><label for=\"gensym_5470e21f70681\" style=\"cursor:pointer;\">b = 0.46 </label>\n",
      "</div>\n",
      "<div class=\"course-quiz-option\">\n",
      "<input dir=\"auto\" class=\"course-quiz-input\" name=\"answer[b51dfcbbcf7f59e1573842f5bf31c9eb][]\" id=\"gensym_5470e21f70e7e\" value=\"e3b486a7583821f81812464677a70440\" type=\"radio\"><label for=\"gensym_5470e21f70e7e\" style=\"cursor:pointer;\">b = 0.33 </label>\n",
      "</div>\n",
      "<div class=\"course-quiz-option\">\n",
      "<input dir=\"auto\" class=\"course-quiz-input\" name=\"answer[b51dfcbbcf7f59e1573842f5bf31c9eb][]\" id=\"gensym_5470e21f7153f\" value=\"75dca3294c5301d69fbdaa780e07a752\" type=\"radio\"><label for=\"gensym_5470e21f7153f\" style=\"cursor:pointer;\">\tc = 0.46 </label>\n",
      "</div>\n",
      "<div class=\"course-quiz-option\">\n",
      "<input dir=\"auto\" class=\"course-quiz-input\" name=\"answer[b51dfcbbcf7f59e1573842f5bf31c9eb][]\" id=\"gensym_5470e21f71b7a\" value=\"8560aff200a77a360fec8878bd338843\" type=\"radio\"><label for=\"gensym_5470e21f71b7a\" style=\"cursor:pointer;\">\tb = 0.21 </label>\n",
      "</div>\n",
      "</div>\n",
      "</div>\n"
     ]
    },
    {
     "cell_type": "heading",
     "level": 4,
     "metadata": {},
     "source": [
      "Answer 2"
     ]
    },
    {
     "cell_type": "markdown",
     "metadata": {},
     "source": [
      "Compute answer here"
     ]
    },
    {
     "cell_type": "heading",
     "level": 2,
     "metadata": {},
     "source": [
      "Week7A Advanced "
     ]
    },
    {
     "cell_type": "markdown",
     "metadata": {},
     "source": [
      "The due date for this quiz is Sun 23 Nov 2014 11:59 PM PST."
     ]
    },
    {
     "cell_type": "heading",
     "level": 2,
     "metadata": {},
     "source": [
      "Question 1"
     ]
    },
    {
     "cell_type": "markdown",
     "metadata": {},
     "source": [
      "Suppose we have an LSH family <i>h</i> of (<i>d</i><sub>1</sub>,<i>d</i><sub>2</sub>,.6,.4) hash functions.\n",
      "We can use three functions from <i>h</i> and the AND-construction to\n",
      "form a (<i>d</i><sub>1</sub>,<i>d</i><sub>2</sub>,<i>w</i>,<i>x</i>) family, and we can use two functions\n",
      "from <i>h</i> and the OR-construction to form a (<i>d</i><sub>1</sub>,<i>d</i><sub>2</sub>,<i>y</i>,<i>z</i>) family.\n",
      "Calculate <i>w</i>, <i>x</i>, <i>y</i>, and <i>z</i>, and then identify\n",
      "the correct value of one of these in the list below.\n",
      "\n",
      "\n",
      "</div>\n",
      "<div dir=\"auto\" class=\"course-quiz-options\">\n",
      "<div class=\"course-quiz-option\">\n",
      "<input dir=\"auto\" class=\"course-quiz-input\" name=\"answer[762c185cffce854b49de7d9cf9407694][]\" id=\"gensym_5470e37c7b225\" value=\"3f62d5414d671afdb6b18bfb705d2616\" type=\"radio\"><label for=\"gensym_5470e37c7b225\" style=\"cursor:pointer;\">x=.16 \n",
      "</label>\n",
      "</div>\n",
      "<div class=\"course-quiz-option\">\n",
      "<input dir=\"auto\" class=\"course-quiz-input\" name=\"answer[762c185cffce854b49de7d9cf9407694][]\" id=\"gensym_5470e37c7b9ed\" value=\"0255e903c43fe9d016549ac73384a4e2\" type=\"radio\"><label for=\"gensym_5470e37c7b9ed\" style=\"cursor:pointer;\">z=.84 \n",
      "</label>\n",
      "</div>\n",
      "<div class=\"course-quiz-option\">\n",
      "<input dir=\"auto\" class=\"course-quiz-input\" name=\"answer[762c185cffce854b49de7d9cf9407694][]\" id=\"gensym_5470e37c7c2c1\" value=\"ad200f4d805bc693b48f5361757cd3ec\" type=\"radio\"><label for=\"gensym_5470e37c7c2c1\" style=\"cursor:pointer;\">x=..064 \n",
      "</label>\n",
      "</div>\n",
      "<div class=\"course-quiz-option\">\n",
      "<input dir=\"auto\" class=\"course-quiz-input\" name=\"answer[762c185cffce854b49de7d9cf9407694][]\" id=\"gensym_5470e37c7cbcf\" value=\"756a66b0bc16789c886dbe962110cf7b\" type=\"radio\"><label for=\"gensym_5470e37c7cbcf\" style=\"cursor:pointer;\">y=.64 \n",
      "</label>"
     ]
    },
    {
     "cell_type": "heading",
     "level": 4,
     "metadata": {},
     "source": [
      "Answer 1"
     ]
    },
    {
     "cell_type": "markdown",
     "metadata": {},
     "source": [
      "Compute answer here"
     ]
    },
    {
     "cell_type": "heading",
     "level": 3,
     "metadata": {},
     "source": [
      "Question 2"
     ]
    },
    {
     "cell_type": "markdown",
     "metadata": {},
     "source": [
      "Here are eight strings that represent sets:\n",
      "<p>\n",
      "<font color=\"blue\">\n",
      "s<sub>1</sub> = abcef<br>\n",
      "s<sub>2</sub> = acdeg<br>\n",
      "s<sub>3</sub> = bcdefg<br>\n",
      "s<sub>4</sub> = adfg<br>\n",
      "s<sub>5</sub> = bcdfgh<br>\n",
      "s<sub>6</sub> = bceg<br>\n",
      "s<sub>7</sub> = cdfg<br>\n",
      "s<sub>8</sub> = abcd\n",
      "</font>\n",
      "</p>\n",
      "<p>\n",
      "Suppose our upper limit on Jaccard distance is 0.2, and we use the\n",
      "indexing scheme of Section 3.9.4\n",
      "based on symbols appearing in the prefix (no position\n",
      "or length information).  For each of s<sub>1</sub>, s<sub>3</sub>, and s<sub>6</sub>, determine\n",
      "how many <i>other</i> strings that string will be compared with, if it is\n",
      "used as the probe string.  Then, identify the true count from the\n",
      "list below.\n",
      "\n",
      "</p>\n",
      "\n",
      "</div>\n",
      "<div dir=\"auto\" class=\"course-quiz-options\">\n",
      "<div class=\"course-quiz-option\">\n",
      "<input dir=\"auto\" class=\"course-quiz-input\" name=\"answer[8c6549c4c55e91be32a3fe4491685d55][]\" id=\"gensym_5470e37c80a59\" value=\"0908a174983913a8184bc3af0f37b7fd\" type=\"radio\"><label for=\"gensym_5470e37c80a59\" style=\"cursor:pointer;\">s3 is compared with 4 other strings. \n",
      "</label>\n",
      "</div>\n",
      "<div class=\"course-quiz-option\">\n",
      "<input dir=\"auto\" class=\"course-quiz-input\" name=\"answer[8c6549c4c55e91be32a3fe4491685d55][]\" id=\"gensym_5470e37c81317\" value=\"998c0099a8433bf417659113d09f1fc6\" type=\"radio\"><label for=\"gensym_5470e37c81317\" style=\"cursor:pointer;\">s1 is compared with 7 other strings. \n",
      "</label>\n",
      "</div>\n",
      "<div class=\"course-quiz-option\">\n",
      "<input dir=\"auto\" class=\"course-quiz-input\" name=\"answer[8c6549c4c55e91be32a3fe4491685d55][]\" id=\"gensym_5470e37c81a0f\" value=\"e6a3d7e77d26fd84f65ec67e2ac1f496\" type=\"radio\"><label for=\"gensym_5470e37c81a0f\" style=\"cursor:pointer;\">s1 is compared with 6 other strings. \n",
      "</label>\n",
      "</div>\n",
      "<div class=\"course-quiz-option\">\n",
      "<input dir=\"auto\" class=\"course-quiz-input\" name=\"answer[8c6549c4c55e91be32a3fe4491685d55][]\" id=\"gensym_5470e37c82f58\" value=\"d65d977e738a31e187fe1c8cbb82d3e4\" type=\"radio\"><label for=\"gensym_5470e37c82f58\" style=\"cursor:pointer;\">s6 is compared with 2 other strings. \n",
      "</label>"
     ]
    },
    {
     "cell_type": "heading",
     "level": 4,
     "metadata": {},
     "source": [
      "Answer 2"
     ]
    },
    {
     "cell_type": "markdown",
     "metadata": {},
     "source": [
      "Compute answer here"
     ]
    },
    {
     "cell_type": "heading",
     "level": 3,
     "metadata": {},
     "source": [
      "Question 3"
     ]
    },
    {
     "cell_type": "markdown",
     "metadata": {},
     "source": [
      "Consider the link graph\n",
      "<p>\n",
      "<img src=\"files/otc_pagerank4.gif\"></p>\n",
      "<p>\n",
      "First, construct the L, the link matrix, as discussed in Section 5.5\n",
      "on the HITS algorithm.\n",
      "Then do the following:\n",
      "</p>\n",
      "<p>\n",
      "</p>\n",
      "<ol>\n",
      "<li>Start by assuming the hubbiness of each node is 1; that is,\n",
      "the vector h is (the transpose of) [1,1,1,1].\n",
      "</li>\n",
      "<li>Compute an estimate of the authority vector <b>a</b>=L<sup>T</sup><b>h</b>.\n",
      "</li>\n",
      "<li>Normalize <b>a</b> by dividing all values so\n",
      "the largest value is 1.\n",
      "</li>\n",
      "<li>Compute an estimate of the hubbiness vector <b>h</b>=L<b>a</b>.\n",
      "</li>\n",
      "<li>Normalize <b>h</b> by dividing all values so\n",
      "the largest value is 1.\n",
      "</li>\n",
      "<li>Repeat steps 2-5.\n",
      "</li>\n",
      "</ol>\n",
      "<p>\n",
      "Now, identify in the list below the true statement about the final\n",
      "estimates.</p>\n",
      "</div>\n",
      "<div dir=\"auto\" class=\"course-quiz-options\">\n",
      "<div class=\"course-quiz-option\">\n",
      "<input dir=\"auto\" class=\"course-quiz-input\" name=\"answer[9cc332d04790bfc24d447080ba6e7004][]\" id=\"gensym_5470e37c86c9b\" value=\"d79425a094449987c794ae485921f308\" type=\"radio\"><label for=\"gensym_5470e37c86c9b\" style=\"cursor:pointer;\">The final estimate of the authority of 4 is 1/8. </label>\n",
      "</div>\n",
      "<div class=\"course-quiz-option\">\n",
      "<input dir=\"auto\" class=\"course-quiz-input\" name=\"answer[9cc332d04790bfc24d447080ba6e7004][]\" id=\"gensym_5470e37c87404\" value=\"2b26b6f699082f007260470a57650cd7\" type=\"radio\"><label for=\"gensym_5470e37c87404\" style=\"cursor:pointer;\">The final estimate of the hubbiness of 3 is 3/5. </label>\n",
      "</div>\n",
      "<div class=\"course-quiz-option\">\n",
      "<input dir=\"auto\" class=\"course-quiz-input\" name=\"answer[9cc332d04790bfc24d447080ba6e7004][]\" id=\"gensym_5470e37c87b57\" value=\"ac6ba29bda0b93f0765f092f38174bce\" type=\"radio\"><label for=\"gensym_5470e37c87b57\" style=\"cursor:pointer;\">The final estimate of the hubbiness of 3 is 1/5. </label>\n",
      "</div>\n",
      "<div class=\"course-quiz-option\">\n",
      "<input dir=\"auto\" class=\"course-quiz-input\" name=\"answer[9cc332d04790bfc24d447080ba6e7004][]\" id=\"gensym_5470e37c883c5\" value=\"5c36da02dce3e872beb46adafec29c39\" type=\"radio\"><label for=\"gensym_5470e37c883c5\" style=\"cursor:pointer;\">The final estimate of the hubbiness of 3 is 1/8. </label>"
     ]
    },
    {
     "cell_type": "heading",
     "level": 4,
     "metadata": {},
     "source": [
      "Answer 3"
     ]
    },
    {
     "cell_type": "markdown",
     "metadata": {},
     "source": [
      "Compute answer here"
     ]
    },
    {
     "cell_type": "heading",
     "level": 3,
     "metadata": {},
     "source": [
      "Question 4"
     ]
    },
    {
     "cell_type": "markdown",
     "metadata": {},
     "source": [
      "Consider an implementation of the Block-Stripe Algorithm discussed in Section 5.2 to compute page rank on a graph of N nodes (i.e., Web pages). Suppose each page has, on average, 20 links, and we divide the new rank vector into k blocks (and correspondingly, the matrix M into k stripes). Each stripe of M has one line per \"source\" web page, in the format:\n",
      "<p>\n",
      "</p>\n",
      "<center>[source_id, degree, m, dest_1, ...., dest_m] </center>\n",
      "<p>\n",
      "Notice that we had to add an additional entry, m, to denote the number of destination nodes in this stripe, which of course is no more than the degree of the node. Assume that all entries (scores, degrees, identifiers,...) are encoded using 4 bytes.\n",
      "</p>\n",
      "<p>\n",
      "There is an additional detail we need to account for, namely, <b>locality</b> of links. As a very simple model, assume that we divide web pages into two disjoint sets:\n",
      "</p>\n",
      "<ol>\n",
      "<li> <b>Introvert</b> pages, which link only to other pages within the same host as themselves.\n",
      "</li>\n",
      "<li> <b>Extrovert</b> pages, which have links to pages across several hosts.\n",
      "</li>\n",
      "</ol>\n",
      "Assume a fraction x of pages (0 \n",
      "Construct a formula that counts the amount of I/O per page rank iteration in terms of N, x, and k. The 4-tuples below list combinations of N, k, x, and I/O (in bytes). Pick the correct combination.\n",
      "<p>\n",
      "<b>Note.</b> There are some additional optimizations one can think of, such as striping the old score vector, encoding introvert and extrovert pages using different schemes, etc. For the purposes of working this problem, assume we don't do any optimizations beyond the block-stripe algorithm discussed in class.</p>\n",
      "</div>\n",
      "<div dir=\"auto\" class=\"course-quiz-options\">\n",
      "<div class=\"course-quiz-option\">\n",
      "<input dir=\"auto\" class=\"course-quiz-input\" name=\"answer[078f9721a198e974e3429102882b80e8][]\" id=\"gensym_5470e37c8ba5d\" value=\"76f008beb7c691453fa7e3f9f1235324\" type=\"radio\"><label for=\"gensym_5470e37c8ba5d\" style=\"cursor:pointer;\">N = 1 billion, k = 3, x = 0.5, 132GB </label>\n",
      "</div>\n",
      "<div class=\"course-quiz-option\">\n",
      "<input dir=\"auto\" class=\"course-quiz-input\" name=\"answer[078f9721a198e974e3429102882b80e8][]\" id=\"gensym_5470e37c8c12b\" value=\"6ab5012514dcae76f5649f6793c8b7cb\" type=\"radio\"><label for=\"gensym_5470e37c8c12b\" style=\"cursor:pointer;\">\tN = 1 billion, k = 3, x = 0.75, 132GB </label>\n",
      "</div>\n",
      "<div class=\"course-quiz-option\">\n",
      "<input dir=\"auto\" class=\"course-quiz-input\" name=\"answer[078f9721a198e974e3429102882b80e8][]\" id=\"gensym_5470e37c8c74b\" value=\"6ccff7a651efb7edb9601bf74121bf89\" type=\"radio\"><label for=\"gensym_5470e37c8c74b\" style=\"cursor:pointer;\">N = 1 billion, k = 3, x = 0.75, 114GB </label>\n",
      "</div>\n",
      "<div class=\"course-quiz-option\">\n",
      "<input dir=\"auto\" class=\"course-quiz-input\" name=\"answer[078f9721a198e974e3429102882b80e8][]\" id=\"gensym_5470e37c8d085\" value=\"5f884fc88778436495471026178a980e\" type=\"radio\"><label for=\"gensym_5470e37c8d085\" style=\"cursor:pointer;\">\tN = 1 billion, k = 3, x = 0.75, 124GB </label>"
     ]
    },
    {
     "cell_type": "heading",
     "level": 4,
     "metadata": {},
     "source": [
      "Answer 4"
     ]
    },
    {
     "cell_type": "markdown",
     "metadata": {},
     "source": [
      "Compute answer here"
     ]
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [],
     "language": "python",
     "metadata": {},
     "outputs": []
    }
   ],
   "metadata": {}
  }
 ]
}