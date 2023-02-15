import numpy as np
import pandas as pd
from sklearn import preprocessing

def get_everything(datos, estacion, train_months, variables, dependent, train_test_samples, input_samples, output_samples, number_of_features,
                  step):
    
    # Primero elegimos la estacion que queremos usar 
    # y luego dividimos el dataframe en train y test (12 meses y 3 meses)

    df_estacion = datos[datos['ESTACION'] == estacion]

    df_estacion = df_estacion.reset_index(drop = True)

    last_train_set_date = df_estacion.FECHAHORA.min() + train_months

    df_train = df_estacion[df_estacion['FECHAHORA'] <= last_train_set_date ].copy()

    df_test = df_estacion[df_estacion['FECHAHORA'] > last_train_set_date].copy()

    # Elegimos las variables que van a estar en cada set

    df_train = df_train[variables]
    df_test = df_test[variables]

    # Normalizamos train
    AQI_train = df_train['AQI_MP2_5']
    df_train = df_train.drop(dependent, axis = 1)

    df_train = (df_train-df_train.min())/(df_train.max()-df_train.min())


    df_train = pd.concat([df_train, AQI_train.rename('AQI_MP2_5')], axis=1)

    # Normalizamos test
    AQI_test = df_test['AQI_MP2_5']
    df_test = df_test.drop(dependent, axis = 1)

    df_test = (df_test -df_test.min())/(df_test.max()-df_test.min())

    df_test = pd.concat([df_test, AQI_test.rename('AQI_MP2_5')], axis=1)

    # Dividimos el df_train en batches de entrenamiento
    
    start = 0
    end = len(df_train)
    next_ = 0

    X_train_batches_df = []
    y_train_batches_df = []

    while (start + train_test_samples) <= end:
        next_ = start + input_samples
        X_train_batches_df.append(df_train.loc[start:next_ - 1, :]) # 20
        y_train_batches_df.append(df_train.loc[next_: next_+output_samples -1, dependent])
        start = start + step

    X_train_batches = np.asarray(X_train_batches_df)
    X_train_batches = X_train_batches.reshape(-1, input_samples, number_of_features)

    y_train_batches = np.asarray(y_train_batches_df)
    y_train_batches = y_train_batches.reshape(-1, output_samples, 1)
    
    # Dividimos el df_test en batches de entrenamiento
    
    start = df_test.index[0]
    end = len(df_test) + start
    next_ = 0

    X_test_batches_df = []
    y_test_batches_df = []

    while (start + train_test_samples) <= end:
        next_ = start + input_samples
        X_test_batches_df.append(df_test.loc[start:next_ - 1, :]) # 20
        y_test_batches_df.append(df_test.loc[next_: next_+output_samples -1, dependent])
        start = start + step

    X_test_batches = np.asarray(X_test_batches_df)
    X_test_batches = X_test_batches.reshape(-1, input_samples, number_of_features)

    y_test_batches = np.asarray(y_test_batches_df)
    y_test_batches = y_test_batches.reshape(-1, output_samples, 1)
    
    # Cambiamos ventanas a una sola instancia (TRAIN)
    
    X_train = []

    for i in range(0, len(X_train_batches)):

        hold = []

        for j in range(0, len(X_train_batches[i])):

            if j==(len(X_train_batches[i]) - 1):
                hold = np.concatenate((hold, X_train_batches[i][j][:]), axis = None)

            else:
                hold = np.concatenate((hold, X_train_batches[i][j][-1]), axis = None)

        X_train.append(hold)
        
    # Cambiamos ventanas a una sola instancia (TEST)

    X_test = []

    for i in range(0, len(X_test_batches)):

        hold = []

        for j in range(0, len(X_test_batches[i])):

            if j==(len(X_test_batches[i]) -1):
                #print('hola')
                hold = np.concatenate((hold, X_test_batches[i][j][:]), axis = None)

            else:
                hold = np.concatenate((hold, X_test_batches[i][j][-1]), axis = None)

        X_test.append(hold)


    X_train = np.nan_to_num(np.reshape(X_train, (len(X_train), len(X_train[0]))))

    y_train = np.nan_to_num(np.reshape(y_train_batches, (len(y_train_batches), output_samples)))

    X_test = np.nan_to_num(np.reshape(X_test, (len(X_test), len(X_test[0]))))

    y_test = np.nan_to_num(np.reshape(y_test_batches, (len(y_test_batches), output_samples)))

    return X_train, y_train, X_test, y_test
    
    