export default function getStudentIdsSum(students) {
  if (!Array.isArray(students)) return 0;

  return students.reduce((sumId, students) => sumId + students.id, 0);
}
