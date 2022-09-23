# SSD Lab Activity 2

## Question 1
- **Execution**: bash   ./q1.sh   file_name.txt
- **Assumption**: Line count is equal to number of newline characters ("\n")
- **Explaination**: 
    - Calculate the line count using wc -l and store in a variable
    - Then middle = (total+1)/2
    - Then seperate the specific line using awk

## Question 2
- **Execution**: bash ./q2.sh
- **Explaination**:
    - Using "/" as field seperator
    - Selecting lines which start with "/usr"
    - Print the last column using $NF