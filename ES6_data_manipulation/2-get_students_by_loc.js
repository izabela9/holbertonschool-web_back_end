export default function getStudentsByLocation(studentList, city) {
	return studentList.filter((studentList) => studentList.location === city);
}
