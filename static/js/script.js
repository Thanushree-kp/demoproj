// script.js
// Simple frontend JavaScript.
// Right now it only handles the "Are you sure?" confirmation
// before deleting a student, so you don't delete someone by accident.

function confirmDelete(studentName) {
    return confirm("Are you sure you want to delete " + studentName + "?");
}
