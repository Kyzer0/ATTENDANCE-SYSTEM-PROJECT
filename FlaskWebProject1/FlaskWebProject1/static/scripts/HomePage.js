const loginBtn = document.getElementById("login-btn")

loginBtn.addEventListener('click', (e) => {
    window.open("admin.html", "_blanks")
})

const studentName = document.getElementById('student-name').value
const studentId = document.getElementById('student=id').value
const studentSection = document.getElementById('student-section').value
const clearBtn = document.getElementById('clear-btn')

clearBtn.addEventListener('click', (e) => {
    e.preventDefault()

    studentName.value = ""
    studentId.value = ""
    studentSection.value = ""
})