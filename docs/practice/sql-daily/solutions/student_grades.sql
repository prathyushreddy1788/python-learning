SELECT
	course,
	avg(grade) AS avg_grade
FROM grades
GROUP BY course;


SELECT StudentID from grades
where Grade = "A" and (Course = "Math"  or Course = "History")
group by StudentID;