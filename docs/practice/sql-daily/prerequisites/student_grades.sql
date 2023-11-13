CREATE TABLE Students (
    StudentID INT,
    Name VARCHAR(50)
);

INSERT INTO Students (StudentID, Name) VALUES
(1, 'Alice'),
(2, 'Bob'),
(3, 'Charlie');

CREATE TABLE Grades (
    StudentID INT,
    Course VARCHAR(50),
    Grade VARCHAR(2)
);

INSERT INTO Grades (StudentID, Course, Grade) VALUES
(1, 'Math', 'A'),
(2, 'English', 'B'),
(1, 'History', 'C'),
(3, 'Math', 'B'),
(2, 'History', 'A');
