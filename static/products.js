let productsList = [];

fetch('/api/products') 
  .then(response => {
    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }
    return response.json();
  }) 
  .then(data => {
    productsList = unifyProducts(data); 
    populateCategories(productsList);   
    displayProducts(1);                 
  })
  .catch(error => {
    console.error('Error al cargar productos desde la API de Flask:', error);
  });


function unifyProducts(arr) {
	const productosUnificados = [];

	arr.forEach(producto => {
		const claveBase = producto.name
			.replace(/\b\d+(W|W)?\b/gi, '')
			.replace(/\b(3000K|4000K|6500K|LUZ DIA|DESIGN)\b/gi, '')
			.replace(/\b[0-9]+\*?[0-9]*\b/g, '')
			.replace(/\s+/g, ' ')
			.trim();

		const existente = productosUnificados.find(p => p.clave === claveBase);

		if (existente) {
			existente.variantes.push(producto.name);
		} else {
			productosUnificados.push({
					clave: claveBase,
					cat: producto.cat,
					img: producto.img,
					variantes: [producto.name]
			});
		}
	});

	return productosUnificados;
}