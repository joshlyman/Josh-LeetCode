# Write an SQL query to find the number of times each student attended each exam.

# Order the result table by student_id and subject_name.

# The query result format is in the following example:

# Students table:
# +------------+--------------+
# | student_id | student_name |
# +------------+--------------+
# | 1          | Alice        |
# | 2          | Bob          |
# | 13         | John         |
# | 6          | Alex         |
# +------------+--------------+
# Subjects table:
# +--------------+
# | subject_name |
# +--------------+
# | Math         |
# | Physics      |
# | Programming  |
# +--------------+
# Examinations table:
# +------------+--------------+
# | student_id | subject_name |
# +------------+--------------+
# | 1          | Math         |
# | 1          | Physics      |
# | 1          | Programming  |
# | 2          | Programming  |
# | 1          | Physics      |
# | 1          | Math         |
# | 13         | Math         |
# | 13         | Programming  |
# | 13         | Physics      |
# | 2          | Math         |
# | 1          | Math         |
# +------------+--------------+
# Result table:
# +------------+--------------+--------------+----------------+
# | student_id | student_name | subject_name | attended_exams |
# +------------+--------------+--------------+----------------+
# | 1          | Alice        | Math         | 3              |
# | 1          | Alice        | Physics      | 2              |
# | 1          | Alice        | Programming  | 1              |
# | 2          | Bob          | Math         | 1              |
# | 2          | Bob          | Physics      | 0              |
# | 2          | Bob          | Programming  | 1              |
# | 6          | Alex         | Math         | 0              |
# | 6          | Alex         | Physics      | 0              |
# | 6          | Alex         | Programming  | 0              |
# | 13         | John         | Math         | 1              |
# | 13         | John         | Physics      | 1              |
# | 13         | John         | Programming  | 1              |
# +------------+--------------+--------------+----------------+
# The result table should contain all students and all subjects.
# Alice attended Math exam 3 times, Physics exam 2 times and Programming exam 1 time.
# Bob attended Math exam 1 time, Programming exam 1 time and didn't attend the Physics exam.
# Alex didn't attend any exam.
# John attended Math exam 1 time, Physics exam 1 time and Programming exam 1 time.


# Write your MySQL query statement below


SELECT student.student_id,student.student_name,subject.subject_name,COUNT(exam.subject_name) as attended_exams
FROM Students as student
JOIN Subjects as subject
LEFT JOIN Examinations as exam
ON student.student_id=exam.student_id AND subject.subject_name=exam.subject_name
GROUP BY student.student_id,subject.subject_name
ORDER BY student_id,subject_name