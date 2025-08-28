document.querySelectorAll('.switch').forEach(link => {
  link.addEventListener('click', e => {
    e.preventDefault();
    const target = e.target.getAttribute('data-target');
    if (!target) return;

    // nascondi tutti i form
    document.querySelectorAll('.auth-container > div').forEach(div => {
      div.classList.remove('form-visible');
      div.classList.add('form-hidden');
    });

    // mostra quello target
    const formToShow = document.querySelector(`.${target}-form`);
    if (formToShow) {
      formToShow.classList.add('form-visible');
      formToShow.classList.remove('form-hidden');
    }
  });
});

// All’avvio mostra solo il login
window.addEventListener('DOMContentLoaded', () => {
  document.querySelectorAll('.auth-container > div').forEach(div => {
    div.classList.remove('form-visible');
    div.classList.add('form-hidden');
  });
  document.querySelector('.login-form').classList.add('form-visible');
});
