// Função animação Contatos
// Selecionar todos os elementos com a classe 'contact-item'
var elements = document.querySelectorAll('.contact-item');

// Animar cada elemento
anime({
    targets: elements,
    opacity: 1, // Definir a opacidade para 1 (totalmente visível)
    translateY: [50, 0], // Deslocar verticalmente de 50 pixels para 0
    delay: anime.stagger(100), // Adicionar um atraso escalonado de 100ms entre cada elemento
    easing: 'easeOutQuad' // Definir a curva de animação
});