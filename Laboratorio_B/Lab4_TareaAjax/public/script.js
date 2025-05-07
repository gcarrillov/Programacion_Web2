// Función para cargar los datos del archivo JSON
async function loadData() {
  const response = await fetch('/data.json');
  const data = await response.json();
  return data;
}

// Cargar la lista de ejercicios al iniciar
generateExerciseList();