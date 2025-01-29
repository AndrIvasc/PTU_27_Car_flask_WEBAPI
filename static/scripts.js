// JAVASCRIPT KODAS DINAMIŠKAI GENERUOTI LENTELĘ SU DUOMENIMIS
document.addEventListener('DOMContentLoaded', function() {
    fetch('/api/models')
        .then(response => response.json())
        .then(data => {
            const tbody = document.getElementById('projektai-body');
            tbody.innerHTML = '';

            data.forEach(projectCar => {
                const tr = document.createElement('tr');

                tr.innerHTML = `
                    <td>${projectCar.id:}</td>
                    <td>${projectCar.manufacturer}</td>
                    <td>${projectCar.model}</td>
                    <td>${projectCar.power_output}</td>
                    <td>${projectCar.price}</td>
                    <td>${projectCar.priceVAT}</td>
                    <td>${projectCar.horse_power}</td>
                    <td>${projectCar.created_at}</td>
                `;

                tbody.appendChild(tr);
            });
        })
        .catch(error => console.error('Error fetching data:', error));
});

