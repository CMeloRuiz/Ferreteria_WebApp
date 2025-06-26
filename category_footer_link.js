window.addEventListener('DOMContentLoaded', () => {
  const urlParams = new URLSearchParams(window.location.search);
  const categoria = urlParams.get('categoria');

  if (!categoria) return;

  const select = document.getElementById('categoryFilter');

  // Esperar hasta que las opciones se hayan cargado dinámicamente
  const interval = setInterval(() => {
    const optionExists = Array.from(select.options).some(opt => opt.value === categoria);

    if (optionExists) {
      select.value = categoria;

      // Lanzar el evento de cambio para activar el filtrado
      const event = new Event('change');
      select.dispatchEvent(event);

      clearInterval(interval); // Detener la espera
    }
  }, 100); // Revisa cada 100ms

  // Opcional: dejar de intentar después de 5 segundos
  setTimeout(() => clearInterval(interval), 5000);
});


