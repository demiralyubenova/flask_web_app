function addGrade() {
    var grade = document.getElementById("grade-input").value;
    // проверка
    if (grade === "" && grade < 2 && grade > 6) {
        alert("Моля, въведете оценка.");
    }
}

