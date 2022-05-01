from Flask import flask, render_template, request
import numpy as np
import pickle


app = flask(__name__)
model = pickle.load(open('maquina_preditiva.pkl', 'rb'))

@app.route('/',methods=['GET'])
def Home():
    return render_template('index.html')

@app.route("/predict", methods=['POST'])
def predict():
    if request.method == 'POST':
        NR_PARTIDO = float(request.form['NR_PARTIDO'])
        NR_IDADE_DATA_POSSE = float(request.form['NR_IDADE_DATA_POSSE'])
        CD_GENERO = float(request.form['CD_GENERO'])
        CD_GRAU_INSTRUCAO = float(request.form['CD_GRAU_INSTRUCAO'])
        CD_ESTADO_CIVIL = float(request.form['CD_ESTADO_CIVIL'])
        CD_COR_RACA = float(request.form['CD_COR_RACA'])
        CD_OCUPACAO = float(request.form['CD_OCUPACAO'])
        ST_REELEICAO = float(request.form['ST_REELEICAO'])
        VR_DESPESA_CONTRATADA = float(request.form['VR_DESPESA_CONTRATADA'])
        VR_BEM_CANDIDATO = float(request.form['VR_BEM_CANDIDATO'])
        QT_VOTOS_NOMINAIS = float(request.form['QT_VOTOS_NOMINAIS'])
       


       
        values = np.array([[NR_PARTIDO, NR_IDADE_DATA_POSSE, CD_GENERO, CD_GRAU_INSTRUCAO,
                        CD_ESTADO_CIVIL, CD_COR_RACA, CD_OCUPACAO, ST_REELEICAO, VR_DESPESA_CONTRATADA, 
                        VR_BEM_CANDIDATO,QT_VOTOS_NOMINAIS]])
        prediction = model.predict(values)

        return render_template('result.html', prediction=prediction)


if __name__ == "__main__":
    app.run(debug=True)

