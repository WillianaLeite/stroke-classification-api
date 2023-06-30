import pandas as pd
import pickle
from sklearn.ensemble import ExtraTreesClassifier
from sklearn.model_selection import train_test_split


def fit(extractor: str):

    '''
    This function trains and save the stroke classification model using features previously extracted from the MGABT {pixel, percent} extractors.

    :param extractor: Type of extractor used: *percent* referring to MGABTD_percent and *pixel* referring to MGABTD_pixel
    :type extractor: str
    '''

    df = pd.read_csv(f'train/dataset_{extractor}.csv', header=0)

    X_train, _, y_train, _ = train_test_split(
            df.drop(['target'], axis=1),
            df['target'],
            train_size=0.7,
            stratify=df['target']
    )
    clf = ExtraTreesClassifier()
    clf.fit(X_train, y_train)

    with open(f'model/extratree_{extractor}.pkl', 'wb') as outp:
        pickle.dump(clf, outp)

    return clf