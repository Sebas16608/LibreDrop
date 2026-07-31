(() => {
  const $ = (selector, context = document) => context.querySelector(selector);
  const $$ = (selector, context = document) => [...context.querySelectorAll(selector)];

  const yearEl = $('#footer-year');
  if (yearEl) {
    yearEl.textContent = new Date().getFullYear();
  }

  const navToggle = $('#nav-toggle');
  const mainNav = $('#main-nav');

  if (navToggle && mainNav) {
    const setMenu = (open) => {
      mainNav.classList.toggle('is-open', open);
      navToggle.classList.toggle('is-active', open);
      navToggle.setAttribute('aria-expanded', String(open));
      navToggle.setAttribute('aria-label', open ? 'Cerrar menú' : 'Abrir menú');
    };

    navToggle.addEventListener('click', () => {
      setMenu(!mainNav.classList.contains('is-open'));
    });

    $$('.nav-link', mainNav).forEach((link) => {
      link.addEventListener('click', () => setMenu(false));
    });

    document.addEventListener('keydown', (event) => {
      if (event.key === 'Escape' && mainNav.classList.contains('is-open')) {
        setMenu(false);
        navToggle.focus();
      }
    });
  }

  const header = $('#site-header');
  if (header) {
    const updateHeader = () => {
      header.classList.toggle('is-scrolled', window.scrollY > 8);
    };
    window.addEventListener('scroll', updateHeader, { passive: true });
    updateHeader();
  }

  const faqItems = $$('.faq-item');

  faqItems.forEach((item) => {
    const question = $('.faq-question', item);
    const answer = $('.faq-answer', item);

    question.addEventListener('click', () => {
      const isOpen = item.classList.contains('is-open');

      faqItems.forEach((other) => {
        if (other !== item) {
          other.classList.remove('is-open');
          $('.faq-question', other).setAttribute('aria-expanded', 'false');
          $('.faq-answer', other).setAttribute('aria-hidden', 'true');
        }
      });

      item.classList.toggle('is-open', !isOpen);
      question.setAttribute('aria-expanded', String(!isOpen));
      answer.setAttribute('aria-hidden', String(isOpen));
    });
  });

  const revealEls = $$('[data-reveal]');

  if ('IntersectionObserver' in window) {
    const observer = new IntersectionObserver(
      (entries) => {
        entries.forEach((entry) => {
          if (entry.isIntersecting) {
            entry.target.classList.add('is-visible');
            observer.unobserve(entry.target);
          }
        });
      },
      { threshold: 0.12, rootMargin: '0px 0px -40px 0px' }
    );

    revealEls.forEach((el) => observer.observe(el));
  } else {
    revealEls.forEach((el) => el.classList.add('is-visible'));
  }
})();
