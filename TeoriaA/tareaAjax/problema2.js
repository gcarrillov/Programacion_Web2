document.addEventListener("DOMContentLoaded", function () {
    const ctx = document.getElementById("chart2").getContext("2d");
  
    fetch("data.json")
      .then(res => res.json())
      .then(data => {
        const regionesFiltradas = data.filter(d => d.region !== "Lima" && d.region !== "Callao");
        const regiones = [...new Set(regionesFiltradas.map(d => d.region))];
        const fechas = [...new Set(regionesFiltradas.map(d => d.fecha))].sort();
  
        const datasets = regiones.map(region => {
          const datos = fechas.map(fecha => {
            const entrada = regionesFiltradas.find(d => d.region === region && d.fecha === fecha);
            return entrada ? parseInt(entrada.confirmados) : 0;
          });
  
          return {
            label: region,
            data: datos,
            borderWidth: 2,
            fill: false
          };
        });
  
        new Chart(ctx, {
          type: 'line',
          data: {
            labels: fechas,
            datasets: datasets
          },
          options: {
            responsive: true,
            plugins: {
              legend: { position: 'top' },
              title: { display: true, text: 'Crecimiento de Confirmados (sin Lima y Callao)' }
            }
          }
        });
      });
  });
  