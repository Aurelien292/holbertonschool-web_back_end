export default function getStudentsByLocation(students, city) {
  if (!Array.isArray(students) || typeof city !== 'string') {
    return [];
  }

  return students.filter((students) => students.location === city);
}
