import re
import joblib
import pandas as pd

model = None
avg_price = None
dummies = None

COMPANIES = [
  'alfa-romero', 'audi', 'bmw', 'chevrolet', 'dodge', 'honda',
  'isuzu', 'jaguar', 'mazda', 'buick', 'mercury', 'mitsubishi',
  'nissan', 'peugeot', 'plymouth', 'porsche', 'renault', 'saab',
  'subaru', 'toyota', 'volkswagen', 'volvo'
]
TRUE_COLUMNS = ['wheelbase', 'curbweight', 'enginesize', 'boreratio', 'horsepower',
       'fueleconomy', 'carlength', 'carwidth', 'fueltype_gas',
       'aspiration_turbo', 'carbody_hardtop', 'carbody_hatchback',
       'carbody_sedan', 'carbody_wagon', 'drivewheel_fwd',
       'drivewheel_rwd', 'enginetype_dohcv', 'enginetype_l',
       'enginetype_ohc', 'enginetype_ohcf', 'enginetype_ohcv',
       'enginetype_rotor', 'cylindernumber_five', 'cylindernumber_four',
       'cylindernumber_six', 'cylindernumber_three',
       'cylindernumber_twelve', 'cylindernumber_two',
       'company_price_medium', 'company_price_high']

def load_artifacts():
    global model
    global avg_price
    global dummies
    model = joblib.load("data/model.pkl")
    avg_price = pd.read_csv("data/avg_price.csv")
    with open("data/dummies_cols.txt", "r") as f:
        dummies = f.read().split(",")

def transform(data):
    global avg_price
    global dummies
    X = data.copy()
    companies = X['CarName'].apply(lambda x : x.split(' ')[0])
    X.insert(3, "companies", companies)
    X.drop(['CarName'], axis=1, inplace=True)

    X.companies = X.companies.str.lower()

    def replace_name(a,b):
        X.companies.replace(a,b,inplace=True)

    # On remplace certaines occurrences identiques
    replace_name('maxda','mazda')
    replace_name('porcshce','porsche')
    replace_name('toyouta','toyota')
    replace_name('vokswagen','volkswagen')
    replace_name('vw','volkswagen')

    X['fueleconomy'] = (0.55 * X['citympg']) + (0.45 * X['highwaympg'])

    temp = X.copy()
    temp = temp.merge(avg_price.reset_index(), how='left', on='companies')

    bins = [0, 10000, 20000, 40000]
    cars_bin = ['cheap', 'medium', 'high']
    X['company_price'] = pd.cut(temp['price_y'], bins, right=False, labels=cars_bin)
    X.head()

    X = X[[
        'price', 'fueltype', 'aspiration','carbody', 'drivewheel','wheelbase',
        'curbweight', 'enginetype', 'cylindernumber', 'enginesize', 'boreratio','horsepower', 
        'fueleconomy', 'carlength','carwidth', 'company_price'
    ]]

    for dummy in dummies:
        X[dummy] = 0

    dummy_cols = [
        "fueltype", "aspiration", "carbody", "drivewheel",
        "enginetype", "cylindernumber", "company_price"
    ]

    def replace_dummies(col, df):
        temp = pd.get_dummies(df[col], prefix=col, drop_first = True)
        #df = pd.concat([df, temp], axis=1)
        # lsuffix nous indique les colonnes à retirer
        df = df.join(temp, lsuffix="_toremove")
        df.drop([col], axis=1, inplace=True)
        for colname in df.columns.values:
            if re.search(r"_toremove", colname):
                df.drop([colname], axis=1, inplace=True)
        return df

    for dummy in dummy_cols:
        X = replace_dummies(dummy, X)

    return X[TRUE_COLUMNS]


def predict(X):
    global model
    if model:  
        return model.predict(transform(X))
    return None