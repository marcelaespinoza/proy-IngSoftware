
export const emociones_puntajes = {
    'tristeza': 10,
    'estres': 4,
    'ansiedad': 5,
    'frustracion': 5,
    'enojo': 8,
    'aburrimiento': 2,
    'preocupacion': 3,
    'motivacion': -5,
    'felicidad': -10,
    'satisfaccion': -4,
    'alivio': -2
}
export const numero = 20;

const loadEmotions = (emotions) => {
  let datos_puntajes = {};

  emotions.forEach(obj => {
    let codigo = obj.codigo;
    let emocion = obj.emocion;

    // Calcula el puntaje usando el diccionario de emociones_puntajes
    const puntaje = emociones_puntajes[emocion];
    if (datos_puntajes.hasOwnProperty(codigo.toString()))
      datos_puntajes[codigo.toString()] += puntaje;
    else
      datos_puntajes[codigo.toString()] = puntaje;
  })

  // comvierte de objeto a List[tuple] (codigo, puntaje)
  const tuple_codigos = Object.entries(datos_puntajes)
  // ordena los puntajes de mayor a menor
  const sort_codigos = tuple_codigos.sort((a, b) => b[1] - a[1])

  return sort_codigos.slice(0, numero);
}

export default loadEmotions;