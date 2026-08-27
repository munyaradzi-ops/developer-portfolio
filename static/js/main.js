document.addEventListener("DOMContentLoaded", () => {
  const mobileMenuButton = document.getElementById("mobileMenuButton");
  const mainNavigation = document.getElementById("mainNavigation");

  // Toggle navigation menu on click or touch
  if (mobileMenuButton && mainNavigation) {
    const toggleMenu = (event) => {
      event.stopPropagation();
      mainNavigation.classList.toggle("active");
      mobileMenuButton.classList.toggle("open");

      // Update accessibility aria attribute
      const isExpanded = mainNavigation.classList.contains("active");
      mobileMenuButton.setAttribute("aria-expanded", isExpanded);
    };

    mobileMenuButton.addEventListener("click", toggleMenu);

    // Ensure touch events respond instantly on mobile browsers
    mobileMenuButton.addEventListener(
      "touchstart",
      (e) => {
        e.preventDefault();
        toggleMenu(e);
      },
      { passive: false },
    );

    // Close menu when clicking outside of the navbar
    document.addEventListener("click", (event) => {
      const isClickInside =
        mainNavigation.contains(event.target) ||
        mobileMenuButton.contains(event.target);
      if (!isClickInside && mainNavigation.classList.contains("active")) {
        mainNavigation.classList.remove("active");
        mobileMenuButton.classList.remove("open");
        mobileMenuButton.setAttribute("aria-expanded", "false");
      }
    });

    // Close mobile menu when a link inside it is clicked
    const navLinks = mainNavigation.querySelectorAll("a");
    navLinks.forEach((link) => {
      link.addEventListener("click", () => {
        mainNavigation.classList.remove("active");
        mobileMenuButton.classList.remove("open");
        mobileMenuButton.setAttribute("aria-expanded", "false");
      });
    });
  }
});
