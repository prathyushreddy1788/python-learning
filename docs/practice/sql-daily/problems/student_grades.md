## Question: Student Grades

Consider a database with the following tables: `Students` and `Grades`.

### Students Table:

| StudentID | Name     |
| --------- | -------- |
| 1         | Alice    |
| 2         | Bob      |
| 3         | Charlie  |

### Grades Table:

| StudentID | Course    | Grade |
| --------- | --------- | ----- |
| 1         | Math      | A     |
| 2         | English   | B     |
| 1         | History   | C     |
| 3         | Math      | B     |
| 2         | History   | A     |

### Tasks:

1. Find the average grade for each course (grouped by `Course`).
2. Find the names of students who received an 'A' grade in both Math and History courses.
 