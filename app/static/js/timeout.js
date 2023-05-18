// Set the date and time to countdown from
const countDownDate = new Date("June 1, 2023 00:00:00").getTime();

// Update the count down every 1 second
const x = setInterval(function() {

  // Get the current date and time
const now = new Date().getTime();

  // Calculate the distance between now and the countdown date
const distance = countDownDate - now;

// Calculate days, hours, minutes and seconds left
const days = Math.floor(distance / (1000 * 60 * 60 * 24));
const hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
const minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
const seconds = Math.floor((distance % (1000 * 60)) / 1000);

// Display the result in the element with id="timer"
document.getElementById("timer").innerHTML = days + "d " + hours + "h " + minutes + "m " + seconds + "s ";

// If the countdown is finished, display "EXPIRED" and clear the interval
if (distance < 0) {
    clearInterval(x);
    document.getElementById("timer").innerHTML = "EXPIRED";
}
}, 1000);
