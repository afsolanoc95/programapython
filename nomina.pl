docentes(pedro,titular).
docentes(pablo,auxiliar).
docentes(carlos,asistente).
docentes(juan,auxiliar).
docentes(ricardo,titular).
docentes(clara,titular).
docentes(lupe,asistente).
tipoContrato(pablo,mto).
tipoContrato(carlos,catedra).
tipoContrato(pedro,honorario).
tipoContrato(ricardo,catedra).
tipoContrato(juan,tco).
tipoContrato(clara,mto).
tipoContrato(lupe,honorario).
duracionSemestre(pedro,15).
duracionSemestre(pablo,16).
duracionSemestre(carlos,14).
duracionSemestre(juan,17).
duracionSemestre(clara,15).
duracionSemestre(lupe,16).
duracionSemestre(ricardo,12).
sueldodia(X,Y):-docentes(X,Q),tipoContrato(X,Z),Q==titular,Z==catedra,Y is 100000.
sueldodia(X,Y):-docentes(X,Q),tipoContrato(X,Z),Q==asistente,Z==catedra,Y is 70000.
sueldodia(X,Y):-docentes(X,Q),tipoContrato(X,Z),Q==auxiliar,Z==catedra,Y is 50000.
sueldodia(X,Y):-docentes(X,Q),tipoContrato(X,Z),Q==titular,Z==honorario,Y is 90000.
sueldodia(X,Y):-docentes(X,Q),tipoContrato(X,Z),Q==asistente,Z==honorario,Y is 60000.
sueldodia(X,Y):-docentes(X,Q),tipoContrato(X,Z),Q==auxiliar,Z==honorario,Y is 40000.
sueldodia(X,Y):-docentes(X,Q),tipoContrato(X,Z),Q==titular,Z==tco,Y is 80000.
sueldodia(X,Y):-docentes(X,Q),tipoContrato(X,Z),Q==asistente,Z==tco,Y is 50000.
sueldodia(X,Y):-docentes(X,Q),tipoContrato(X,Z),Q==auxiliar,Z==tco,Y is 30000.
sueldodia(X,Y):-docentes(X,Q),tipoContrato(X,Z),Q==titular,Z==mto,Y is 70000.
sueldodia(X,Y):-docentes(X,Q),tipoContrato(X,Z),Q==asistente,Z==mto,Y is 40000.
sueldodia(X,Y):-docentes(X,Q),tipoContrato(X,Z),Q==auxiliar,Z==mto,Y is 20000.
sueldoSemestre(X,Y):-sueldodia(X,Z),duracionSemestre(X,Q),Y is Z*Q.
sueldoTotal(X,Y):-sueldoSemestre(X,Q),tipoContrato(X,Z),Z==tco,Y is Q+Q*0.30.
sueldoTotal(X,Y):-sueldoSemestre(X,Q),tipoContrato(X,Z),Z==mto,Y is Q+Q*0.30.
sueldoTotal(X,Y):-sueldoSemestre(X,Q),tipoContrato(X,Z),Z\=mto,Z\=tco,Y is Q.






