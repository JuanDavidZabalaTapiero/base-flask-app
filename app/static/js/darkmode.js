document.addEventListener("DOMContentLoaded", () => {
    const html = document.documentElement;
    const btn = document.getElementById("theme-toggle");
    const icon = document.getElementById("theme-icon");

    // Aplicar tema guardado
    const savedTheme = localStorage.getItem("theme") || "light";
    html.setAttribute("data-bs-theme", savedTheme);
    icon.className = savedTheme === "dark" ? "bi bi-sun-fill" : "bi bi-moon-fill";

    btn.addEventListener("click", () => {
        const current = html.getAttribute("data-bs-theme");
        const next = current === "light" ? "dark" : "light";
        html.setAttribute("data-bs-theme", next);

        // Guardar en localStorage
        localStorage.setItem("theme", next);

        // Cambiar icono
        icon.className = next === "dark" ? "bi bi-sun-fill" : "bi bi-moon-fill";
    });
});
