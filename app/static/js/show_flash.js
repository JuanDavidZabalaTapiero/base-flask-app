function flashMessage(message, alertClass = "alert-info") {
    const container = document.getElementById("flash-messages")

    const div = document.createElement("div")
    div.className = `alert ${alertClass} fade show`
    div.setAttribute("role", "alert")

    const span = document.createElement("span")
    span.textContent = message

    div.appendChild(span)
    container.appendChild(div)

    // ELIMINAR DESPUÉS DE 2 SEG
    setTimeout(() => {
        div.classList.remove("show");
        div.addEventListener("transitionend", () => div.remove());
    }, 2000);
}