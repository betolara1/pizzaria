
// Função de inicialização do mapa
function initMap() {
    // Coordenadas do centro do mapa
    var center = [-23.5505, -46.6333];

    // Criar o mapa
    var map = L.map('map').setView(center, 50);

    // Adicionar camada do OpenStreetMap
    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
    }).addTo(map);

    // Adicionar marcador
    L.marker(center).addTo(map)
        .bindPopup('Pizzaria dboa')
        .openPopup();
}

// Chamada da função de inicialização do mapa quando o documento estiver pronto
document.addEventListener('DOMContentLoaded', function() {
    // Verificar se o elemento com ID 'map' está presente no DOM
    var mapElement = document.getElementById('map');
    if (mapElement) {
        // Se o elemento 'map' estiver presente, chame a função initMap
        initMap();
    }
});