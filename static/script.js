// This file only handles the VISUAL toggle of genre chips as you click them.
// All actual recommendation logic (matching, sorting, filtering) happens
// in Python inside app.py -- this JS does not calculate anything.

document.querySelectorAll('.genre-chip').forEach(chip => {
  chip.addEventListener('click', () => {
    chip.classList.toggle('selected');
  });
});