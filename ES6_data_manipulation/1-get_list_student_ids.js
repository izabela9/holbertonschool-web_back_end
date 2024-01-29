/* eslint-disable*/
export default function getListStudentIds(studentArray) {
  if (!Array.isArray(studentArray) {
    return [];
  }
const idsArray = studentArray.map((student) => student.id);
  return idsArray;
}
