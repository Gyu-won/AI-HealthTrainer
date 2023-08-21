let startDateInput = document.getElementById("start-date");
let endDateInput = document.getElementById("end-date");
let hoursInput = document.getElementById("hours");
let minutesInput = document.getElementById("minutes");

// 오늘 날짜 설정
let today = new Date();
let dd = String(today.getDate()).padStart(2, '0');
let mm = String(today.getMonth() + 1).padStart(2, '0');
let yyyy = today.getFullYear();

today = yyyy + '-' + mm + '-' + dd;
startDateInput.min = today;

// startDate의 값이 변경될 때마다 endDate의 min 값을 업데이트
startDateInput.addEventListener("change", function() {
    endDateInput.min = startDateInput.value;
});

// 시간 및 분이 변경될 때 제약 사항 확인
hoursInput.addEventListener("change", validateTime);
minutesInput.addEventListener("change", validateTime);

function validateTime() {
    if (parseInt(hoursInput.value) === 0 && parseInt(minutesInput.value) < 1) {
        alert("Goal 시간은 1시간 이상이어야 합니다.");
        hoursInput.value = 1;
        minutesInput.value = 0;
    }
}