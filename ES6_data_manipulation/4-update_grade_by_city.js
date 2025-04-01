export default function updateStudentGradeByCity(students, city, newGrades) {
  const filtreStudents = students.filter((student) => student.location === city);
  return filtreStudents.map((student) => {
    const gradeObj = newGrades.find((grade) => grade.studentId === student.id);

    let grade;
    if (gradeObj) {
      grade = gradeObj.grade;
    } else {
      grade = 'N/A';
    }
    return { ...student, grade };
  });
}
