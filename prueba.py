from plataforma.similarity import *
#x={1: (4,1) , 2: [(3,3) , (2,2) ],3: (6,1) }
x={'cuestionario': {1: (4,1) , 2: [(3,3) , (2,2) ],3: (6,1) }, 'tipo': 'P'}
print similarity(x,x)
#http://127.0.0.1:8080/afinidad/?pagina=1&cuestionario={%22cuestionarios%22:[{%22id%22:1,%22preguntas%22:[{%22id%22:5,%22pregunta%22:{%22id%22:1,%22opciones%22:[{%22id%22:5,%22respuesta%22:%22Software%22,%22orden%22:1,%22valor%22:2,%22pregunta%22:1,%22dato%22:false},{%22id%22:4,%22respuesta%22:%22Redes%20Sociales%22,%22orden%22:2,%22valor%22:1,%22pregunta%22:1,%22dato%22:false}],%22enunciado%22:%22%C2%BFQu%C3%A9%20necesitas?%22,%22imagen%22:null,%22tipo_pregunta%22:%22U%22,%22dato%22:%224%22},%22orden%22:1,%22cuestionario%22:1,%22dependencia_respuestas%22:[],%22enable%22:true},{%22id%22:6,%22pregunta%22:{%22id%22:2,%22opciones%22:[{%22id%22:3,%22respuesta%22:%22Instagram%22,%22orden%22:1,%22valor%22:3,%22pregunta%22:2,%22dato%22:true},{%22id%22:1,%22respuesta%22:%22Facebook%22,%22orden%22:2,%22valor%22:1,%22pregunta%22:2,%22dato%22:true},{%22id%22:2,%22respuesta%22:%22Twitter%22,%22orden%22:3,%22valor%22:2,%22pregunta%22:2,%22dato%22:true}],%22enunciado%22:%22%C2%BFQu%C3%A9%20redes%20sociales%20necesitas?%22,%22imagen%22:null,%22tipo_pregunta%22:%22M%22,%22dato%22:0},%22orden%22:2,%22cuestionario%22:1,%22dependencia_respuestas%22:[],%22enable%22:true}],%22titulo%22:%22%C2%BFQu%C3%A9%20buscas?%22,%22descripcion%22:null,%22imagen%22:%22boton-que.png%22,%22fecha%22:null,%22enable%22:true},{%22id%22:2,%22preguntas%22:[{%22id%22:7,%22pregunta%22:{%22id%22:3,%22opciones%22:[{%22id%22:6,%22respuesta%22:%22menos%20de%20$500.000%22,%22orden%22:1,%22valor%22:1,%22pregunta%22:3,%22dato%22:false},{%22id%22:7,%22respuesta%22:%22Entre%20$500.000%20a%20$1.0000%22,%22orden%22:2,%22valor%22:2,%22pregunta%22:3,%22dato%22:false},{%22id%22:8,%22respuesta%22:%22Entre%20$1.000.000%20y%20$5.000.000%22,%22orden%22:3,%22valor%22:3,%22pregunta%22:3,%22dato%22:false},{%22id%22:9,%22respuesta%22:%22M%C3%A1s%20de%20$5.000.000%22,%22orden%22:4,%22valor%22:4,%22pregunta%22:3,%22dato%22:false}],%22enunciado%22:%22%C2%BFCu%C3%A1l%20es%20tu%20presupuesto?%22,%22imagen%22:null,%22tipo_pregunta%22:%22U%22,%22dato%22:%226%22},%22orden%22:0,%22cuestionario%22:2,%22dependencia_respuestas%22:[],%22enable%22:true}],%22titulo%22:%22%C2%BFCu%C3%A1l%20es%20tu%20presupuesto?%22,%22descripcion%22:null,%22imagen%22:%22boton-cuanto.png%22,%22fecha%22:null,%22enable%22:true},{%22id%22:3,%22preguntas%22:[{%22id%22:8,%22pregunta%22:{%22id%22:4,%22opciones%22:[{%22id%22:10,%22respuesta%22:%22Ch%C3%ADa%22,%22orden%22:1,%22valor%22:1,%22pregunta%22:4,%22dato%22:false},{%22id%22:11,%22respuesta%22:%22Girardot%22,%22orden%22:2,%22valor%22:2,%22pregunta%22:4,%22dato%22:false},{%22id%22:12,%22respuesta%22:%22Mosquera%22,%22orden%22:3,%22valor%22:3,%22pregunta%22:4,%22dato%22:false}],%22enunciado%22:%22%C2%BFD%C3%B3nde%20est%C3%A1s%20Ubicado?%22,%22imagen%22:null,%22tipo_pregunta%22:%22L%22,%22dato%22:%2212%22},%22orden%22:0,%22cuestionario%22:3,%22dependencia_respuestas%22:[],%22enable%22:true}],%22titulo%22:%22%C2%BFD%C3%B3nde%20te%20encuentras?%22,%22descripcion%22:null,%22imagen%22:%22boton-donde.png%22,%22fecha%22:null,%22enable%22:true}],%22tipo%22:%22P%22}

http://127.0.0.1:8080/afinidad/detalle?id_ps=84&cuestionario={%22cuestionarios%22:[{%22id%22:1,%22preguntas%22:[{%22id%22:5,%22pregunta%22:{%22id%22:1,%22opciones%22:[{%22id%22:5,%22respuesta%22:%22Software%22,%22orden%22:1,%22valor%22:2,%22pregunta%22:1,%22dato%22:false},{%22id%22:4,%22respuesta%22:%22Redes%20Sociales%22,%22orden%22:2,%22valor%22:1,%22pregunta%22:1,%22dato%22:false}],%22enunciado%22:%22%C2%BFQu%C3%A9%20necesitas?%22,%22imagen%22:null,%22tipo_pregunta%22:%22U%22,%22dato%22:%224%22},%22orden%22:1,%22cuestionario%22:1,%22dependencia_respuestas%22:[],%22enable%22:true},{%22id%22:6,%22pregunta%22:{%22id%22:2,%22opciones%22:[{%22id%22:3,%22respuesta%22:%22Instagram%22,%22orden%22:1,%22valor%22:3,%22pregunta%22:2,%22dato%22:true},{%22id%22:1,%22respuesta%22:%22Facebook%22,%22orden%22:2,%22valor%22:1,%22pregunta%22:2,%22dato%22:true},{%22id%22:2,%22respuesta%22:%22Twitter%22,%22orden%22:3,%22valor%22:2,%22pregunta%22:2,%22dato%22:true}],%22enunciado%22:%22%C2%BFQu%C3%A9%20redes%20sociales%20necesitas?%22,%22imagen%22:null,%22tipo_pregunta%22:%22M%22,%22dato%22:0},%22orden%22:2,%22cuestionario%22:1,%22dependencia_respuestas%22:[],%22enable%22:true}],%22titulo%22:%22%C2%BFQu%C3%A9%20buscas?%22,%22descripcion%22:null,%22imagen%22:%22boton-que.png%22,%22fecha%22:null,%22enable%22:true},{%22id%22:2,%22preguntas%22:[{%22id%22:7,%22pregunta%22:{%22id%22:3,%22opciones%22:[{%22id%22:6,%22respuesta%22:%22menos%20de%20$500.000%22,%22orden%22:1,%22valor%22:1,%22pregunta%22:3,%22dato%22:false},{%22id%22:7,%22respuesta%22:%22Entre%20$500.000%20a%20$1.0000%22,%22orden%22:2,%22valor%22:2,%22pregunta%22:3,%22dato%22:false},{%22id%22:8,%22respuesta%22:%22Entre%20$1.000.000%20y%20$5.000.000%22,%22orden%22:3,%22valor%22:3,%22pregunta%22:3,%22dato%22:false},{%22id%22:9,%22respuesta%22:%22M%C3%A1s%20de%20$5.000.000%22,%22orden%22:4,%22valor%22:4,%22pregunta%22:3,%22dato%22:false}],%22enunciado%22:%22%C2%BFCu%C3%A1l%20es%20tu%20presupuesto?%22,%22imagen%22:null,%22tipo_pregunta%22:%22U%22,%22dato%22:%226%22},%22orden%22:0,%22cuestionario%22:2,%22dependencia_respuestas%22:[],%22enable%22:true}],%22titulo%22:%22%C2%BFCu%C3%A1l%20es%20tu%20presupuesto?%22,%22descripcion%22:null,%22imagen%22:%22boton-cuanto.png%22,%22fecha%22:null,%22enable%22:true},{%22id%22:3,%22preguntas%22:[{%22id%22:8,%22pregunta%22:{%22id%22:4,%22opciones%22:[{%22id%22:10,%22respuesta%22:%22Ch%C3%ADa%22,%22orden%22:1,%22valor%22:1,%22pregunta%22:4,%22dato%22:false},{%22id%22:11,%22respuesta%22:%22Girardot%22,%22orden%22:2,%22valor%22:2,%22pregunta%22:4,%22dato%22:false},{%22id%22:12,%22respuesta%22:%22Mosquera%22,%22orden%22:3,%22valor%22:3,%22pregunta%22:4,%22dato%22:false}],%22enunciado%22:%22%C2%BFD%C3%B3nde%20est%C3%A1s%20Ubicado?%22,%22imagen%22:null,%22tipo_pregunta%22:%22L%22,%22dato%22:%2212%22},%22orden%22:0,%22cuestionario%22:3,%22dependencia_respuestas%22:[],%22enable%22:true}],%22titulo%22:%22%C2%BFD%C3%B3nde%20te%20encuentras?%22,%22descripcion%22:null,%22imagen%22:%22boton-donde.png%22,%22fecha%22:null,%22enable%22:true}],%22tipo%22:%22P%22}

