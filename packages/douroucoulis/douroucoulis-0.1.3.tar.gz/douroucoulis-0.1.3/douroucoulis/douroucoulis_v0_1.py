import random
import pandas as pd
import numpy as np
from sklearn.datasets import make_classification, make_regression
import sweetviz as sv
from douroucoulisay import douroucoulisay, tonal_hoot, gruff_hoot, whoop
from sklearn.impute import SimpleImputer
import math
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.metrics import accuracy_score, mean_absolute_error
from sklearn.linear_model import (LinearRegression, LogisticRegression, RidgeCV, ElasticNetCV, 
                                   Lasso, LassoCV, BayesianRidge)
from sklearn.naive_bayes import MultinomialNB, GaussianNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import (RandomForestClassifier, RandomForestRegressor, ExtraTreesRegressor, 
                              GradientBoostingClassifier, GradientBoostingRegressor, 
                              AdaBoostClassifier, AdaBoostRegressor)
from sklearn.svm import SVC, SVR
from sklearn.tree import DecisionTreeClassifier, DecisionTreeRegressor
from sklearn.preprocessing import OrdinalEncoder, StandardScaler
from xgboost import XGBClassifier, XGBRegressor

np.seterr(under='ignore')


class ModSelection:
    def __init__(self,):
        """
        Initialize the ModSelection class with optional dinosaur and behavior lists.
        """
        self.readme = self._generate_readme()

    def _generate_readme(self) -> str:
        """
        Generates the README text for the library.
        """
        return """
        It is a HOOT to have you here!!

        douroucoulis.mod_selection() is a small library meant to aid in model selection,
        using an Information-Theoretic framework, and building predictive models using the latest
        machine learning algorithms. All in the same place.

        The most important aspect about using this library, and about AIC-based model selection,
        is building a solid a priori model set based on your knowledge and expertise on the study
        system/species. Read and think deeply on the subject, then think some more and seek inspiration 
        in order to produce many relevant competing models/hypotheses!

        The overall pipeline used throughout is: data cleaning, data exploration, model/feature selection,
        cross-validation, model hyperparameterization, and making predictions. Always look for grouping 
        variables and fit mixed models (e.g., LMM, GLMM) to produce more accurate estimates for your 
        explanatory parameters of interest, especially if your goal is to explain rather than predict.

        The main functions and their arguments are:

        - douroucoulis.instructions() -> produces step-by-step instructions. Douroucoulis are cool, don't lie.

        - douroucoulis.test_dataset(n_samples, n_features, n_informative, random_state, regression) -> produces
        a test dataset for exercises. For regression exercises set the "regression" argument to True. Same as 
        sklearn make_classification() and make_regression()

        - douroucoulis.check_data(data) -> takes one argument, which is the dataframe object where the data is stored.
        Checks for any missing values in the dataset.

        - douroucoulis.impute_data(strategy) -> imputes missing data using the SimpleImputer(). For categorical, 
        try 'most_frequent', if you only have numerical values try mean, median, etc.

        - douroucoulis.explore(data, cmap) -> returns a heatmap of the different explanatory variables (features) 
        with your outcome variable (target). It takes two arguments: the dataframe where the data are stored and the 
        color map (try 'rainbow', 'seismic', 'hsv' or 'plasma').

        - douroucoulis.aictable(model_set, model_names) -> returns a dataframe showing each model ranked from best 
        to worst. The function takes 2 arguments: a list containing each model (e.g., model_set = [sex, age]) and a 
        list containing the names of each model in model_set (e.g., model_names = ['sex', 'age']).

        - douroucoulis.best_fit() -> returns the name and corresponding statistics for a single best-fit model 
        (i.e., AIC weight > 0.90). If no single model is identified, use douroucoulis.best_ranked() for multi-model inference.

        - douroucoulis.best_ranked() -> returns the name and corresponding statistics for the best-ranked models 
        (i.e., AIC cumulative weight > 0.95). Use douroucoulis.mod_avg() to return model-averaged estimates for 
        each parameter in the best-ranked models.

        - douroucoulis.mod_avg() -> returns model-averaged estimates for each parameter in the best-ranked models.

        - douroucoulis.cross_val(X, y, classification) -> takes 3 arguments and returns the accuracy of the model 
        containing the explanatory variables (features) provided in the X argument) to the outcome variable in the 
        y argument (target), as well as the best hyperparameters. If your outcome variable is a categorical variable, 
        make sure to set the classification argument to True.

        - douroucoulis.hyper(model) -> takes the name of the most accurate model from the list provided by 
        douroucoulis.cross_val() (e.g., 'ExtraTreeRegressor()') and tunes its hyperparameters with GridSearchCV.

        - douroucoulis.best_predictions(new_data) -> uses best-fit and best-hyperparameterized (most accurate) model 
        to the dataset (new_data dataframe) provided and adds predictions to new_data.

        - douroucoulis.tonalhoot(reps) -> produces a tonal hoot, repreated reps times. Usefil for keeping track of model fitting and cross validations, and for debugging as well.

        - douroucoulis.gruffhoot(reps) -> produces a gruff hoot, repreated reps times. Usefil for keeping track of model fitting and cross validations, and for debugging as well.

        - douroucoulis.rwhoop(reps) -> produces a resonant whoop, repreated reps times. Usefil for keeping track of model fitting and cross validations, and for debugging as well.

        """

    def read_me(self):
        """
        Prints the README text.
        """
        print(self.readme)

    def tonalhoot(self, reps):
        tonal_hoot(reps)

    def gruffhoot(self, reps):
        gruff_hoot(reps)

    def rwhoop(self, reps):
        whoop(reps)

    def instructions(self):
        """
        Provides step-by-step instructions for using the library, 
        printed with a random dinosaur and behavior theme.
        """
        steps = [
            "FIRST: you must clean the data and make sure\nthat there are no missing values.\nUse douroucoulis.check_data() for a quick check\nand douroucoulis.impute_data() to impute missing data.",
            "SECOND: you must create a model set based on your\nknowledge of the study system/species.\nUse douroucoulis.explore() to help build your model set.\nThen create a list with each model\n(e.g., model_set = [sex, temperature, age_sex])\nand a similar list with the names\n(e.g., model_names = ['Sex', 'Temp', 'Age_and_sex']).",
            "THIRD: use douroucoulis.aictable() for AIC-based model selection. douroucoulis.best_fit()\nreturns the single best model if one is identified,\notherwise use douroucoulis.best_ranked() for multi-model inferences.",
            "FOURTH: use douroucoulis.cross_val() to test\nthe accuracy of the best-fit models\nand douroucoulis.hyper() to tune their hyperparameters.\ndouroucoulis.mod_avg() will allow you to get model-averaged estimates for the best predictive parameters.",
            "FINALLY: use douroucoulis.best_predictions()\nto predict new data with the best-fit\nand best-hyperparametrized models."
        ]
        
        for step in steps:
            message = f"{step}"
            douroucoulisay(message)

    def test_dataset(self, n_samples: int, n_features: int, n_informative: int, random_state: int, regression: bool) -> pd.DataFrame:
        """
        Generates a test dataset for classification or regression tasks and returns it as a DataFrame.

        Args:
            n_samples (int): The number of samples to generate.
            n_features (int): The number of features to generate.
            n_informative (int): The number of informative features.
            random_state (int): The seed used by the random number generator.
            regression (bool): If True, generate a regression dataset; otherwise, generate a classification dataset.

        Returns:
            pd.DataFrame: A DataFrame containing the generated dataset, with features and target.
        """
        if regression:
            X, y = make_regression(n_samples=n_samples, n_features=n_features, n_informative=n_informative, random_state=random_state)
        else:
            X, y = make_classification(n_samples=n_samples, n_features=n_features, n_informative=n_informative, random_state=random_state)
        
        # Convert to DataFrame
        df = pd.DataFrame(X, columns=["F" + str(i) for i in range(1, n_features + 1)])
        df['target'] = y
        
        # Print summary statistics
        print(df.describe())
        return df
    
    def check_data(self, data: pd.DataFrame):
        """
        Checks for missing values in the dataset and provides feedback.

        Args:
            data (pd.DataFrame): The dataset to check for missing values.

        Returns:
            None
        """
        self.df = data
        self.describe = self.df.describe()
        self.counts = self.describe.loc['count']
        self.drop = self.counts.sort_values(ascending=True)
        self.balanced = (self.counts == self.counts.iloc[0]).all()
        self.to_drop = self.drop.index[0]
        
        if self.balanced:
            message = (
                'Well done! Your dataset has no missing values.\nTo continue the model-selection process print\n'
                'the douroucoulis.aictable(). You can use douroucoulis.best_fit() to print\nthe single best-fit model, '
                'if one is identified, or use douroucoulis.best_ranked() to use the 95% best-ranked models.\n'
            )
        else:
            message = (
                f"Your sample is not balanced.\nPlease consider dropping rows and columns with missing data.\n"
                f"For example, {self.to_drop} has the lowest sample size.\nIf this is an important parameter, keep all "
                f"columns but drop the necessary rows with missing data. Otherwise drop the {self.to_drop} column completely.\n"
                "Alternatively, try imputing the missing data with douroucoulis.impute_data()."
            )
        
        douroucoulisay(f"{message}")

    def explore(self, df: pd.DataFrame, name: str):
        """
        Generates an exploratory data analysis report using sweetviz.

        Args:
            df (pd.DataFrame): The dataset to analyze.
            name (str): The title of the report.

        Returns:
            HTML: An HTML representation of the report suitable for Jupyter Notebooks.
        """
        self.df = df
        report = sv.analyze(self.df)
    # Save the report as an HTML file and display it inline
        report_html = report.show_html(name + "_report.html", open_browser=False)
        # To display the report in a Jupyter Notebook:
        report.show_notebook()

    def impute(self, data: pd.DataFrame, strategy: str) -> pd.DataFrame:
        """
        Imputes missing values in the dataset using the specified strategy and returns the imputed dataset.

        Args:
            data (pd.DataFrame): The dataset with missing values.
            strategy (str): The imputation strategy to use ('mean', 'median', 'most_frequent', etc.).

        Returns:
            pd.DataFrame: The imputed dataset.
        """
        self.df = data
        self.imp_most = SimpleImputer(missing_values=np.nan, strategy=strategy)
        self.imp_data = pd.DataFrame(self.imp_most.fit_transform(self.df), columns=self.df.columns)
        
        # Display the imputed data summary
        message = f"Imputation completed using strategy '{strategy}'.\n"
        message += "Summary of the imputed dataset:\n"
        message += self.imp_data.describe(include='all').to_string()
        douroucoulisay(message)
        
        return self.imp_data
    
    def drop_missing(self, data):
        self.df = data
        self.drop_data = self.df.dropna(axis = 0)
        print(self.drop_data.describe(include = 'all'))
        return self.drop_data
	
    def template(self, model_type):
        if model_type.lower() == "ols":
            code = """
	import statsmodels.api as sm

	# Assuming you have your predictors in X and target in y
	X = sm.add_constant(X)  # Adds a constant term to the predictors
	model = sm.OLS(y, X).fit()
	print(model.summary())
	print(f'AIC: {model.aic}')
	"""
        elif model_type.lower() == "logistic regression":
            code = """
	import statsmodels.api as sm

	# Assuming you have your predictors in X and target in y
	X = sm.add_constant(X)  # Adds a constant term to the predictors
	model = sm.Logit(y, X).fit()
	print(model.summary())
	print(f'AIC: {model.aic}')
	"""
        elif model_type.lower() == "linear mixed models":
            code = """
	import statsmodels.formula.api as smf

	# Assuming you have your formula and data ready
	# Replace 'formula' with the actual formula and 'data' with your DataFrame
	model = smf.mixedlm('formula', data, groups=data["group_var"]).fit(reml=False)
	print(model.summary())
	print(f'AIC: {model.aic}')
	"""
        elif model_type.lower() == "generalized mixed models":
            code = """
	import statsmodels.formula.api as smf

	# Assuming you have your formula and data ready
	# Replace 'formula' with the actual formula, 'data' with your DataFrame, and specify the family
	model = smf.mixedlm('formula', data, groups=data["group_var"], family=sm.families.Binomial()).fit(reml=False)
	print(model.summary())
	print(f'AIC: {model.aic}')
	"""
        else:
            code = "Model type not recognized. Please choose from: ols, logistic regression, linear mixed models, generalized mixed models."

        print(code)

    def aictable(self, model_set, data, model_names=None, criterion='AIC'):
        """
        Generates a table of model selection criteria including AIC, BIC, AICc, and their respective weights.

        Args:
            model_set (list): List of fitted model objects.
            data (pd.DataFrame): The dataset used for modeling.
            model_names (list): Optional list of model names. If None, default names are generated.
            criterion (str): The criterion to use for model selection. Options are 'BIC', 'AIC', 'AICc'.

        Returns:
            pd.DataFrame: A DataFrame containing the selected criterion, its delta, weights, and related metrics for each model.
        """
        self.df = data
        self.model_set = model_set
        self.criterion_user = criterion
        
        # Generate default model names if not provided
        if model_names is None:
            model_names = [f'Model_{i+1}' for i in range(len(model_set))]
        
        # Extract metrics from models
        self.bic = [model.bic for model in model_set] 
        self.aic = [model.aic for model in model_set] 
        self.log_likelihood = [model.llf for model in model_set]
        self.k = [len(model.params) - 1 for model in model_set]  # Number of parameters
        self.n = len(data)  # Number of observations
        
        # Calculate AICc
        self.aicc = [aic + (2 * k * (k + 1)) / (self.n - k - 1) for aic, k in zip(self.aic, self.k)]
        
        # Select the criterion
        if criterion == 'BIC':
            self.selected_criterion = self.bic
            delta_criterion = [x - min(self.bic) for x in self.bic]
            exp_delta_criterion = [math.exp(-0.5 * x) for x in delta_criterion]
        elif criterion == 'AICc':
            self.selected_criterion = self.aicc
            delta_criterion = [x - min(self.aicc) for x in self.aicc]
            exp_delta_criterion = [math.exp(-0.5 * x) for x in delta_criterion]
        else:  # Default to 'AIC'
            self.selected_criterion = self.aic
            delta_criterion = [x - min(self.aic) for x in self.aic]
            exp_delta_criterion = [math.exp(-0.5 * x) for x in delta_criterion]
        
        # Handle potential zero values in exp_delta_criterion
        exp_delta_criterion_sum = np.nansum(exp_delta_criterion)
        if exp_delta_criterion_sum == 0:
            exp_delta_criterion_sum = 1e-10  # Small value to avoid division by zero
        
        # Calculate weights and evidence ratios
        criterion_weight = [x / exp_delta_criterion_sum for x in exp_delta_criterion]
        ev_ratio = [max(criterion_weight) / x if x != 0 else np.nan for x in criterion_weight]
        
        # Create DataFrame
        self.aictab = pd.DataFrame(index=model_names)
        self.aictab['Model_Name'] = model_names
        self.aictab['K'] = self.k
        self.aictab[f'{criterion}'] = self.selected_criterion
        self.aictab[f'Δ_{criterion}'] = delta_criterion
        self.aictab[f'exp(-0.5 * Δ_{criterion})'] = exp_delta_criterion
        self.aictab[f'{criterion}_Weight'] = criterion_weight
        self.aictab[f'{criterion}_Evidence_Ratios'] = ev_ratio
        self.aictab['Log_Likelihood'] = self.log_likelihood
        
        # Sort by the selected criterion
        self.aictab = self.aictab.sort_values(by=[f'Δ_{criterion}'], ascending=True)
        
        # Cumulative Weights
        self.aictab[f'{criterion}_Cum_Weight'] = self.aictab[f'{criterion}_Weight'].cumsum()

        self.aictable = self.aictab.reset_index(drop=True)
        
        return self.aictable
 

    def best_fit(self):
        """
        Identifies and provides feedback on the best-fit model based on the weights in the aictab DataFrame.
        If no single model meets the weight criteria, prompts to use best_ranked().
        """
        # Ensure the selected criterion is valid
        if self.criterion_user not in ['AIC', 'AICc', 'BIC']:
            raise ValueError(f"Invalid criterion selected. Please choose from 'AIC', 'AICc', or 'BIC'.")
        
        # Determine the appropriate weight column based on the selected criterion
        if self.criterion_user == 'AIC':
            weight_column = 'AIC_Weight'
        elif self.criterion_user == 'AICc':
            weight_column = 'AICc_Weight'
        elif self.criterion_user == 'BIC':
            weight_column = 'BIC_Weight'
        
        # Filter models with weight >= 0.90 based on the selected criterion
        best_models = self.aictab[self.aictab[weight_column] >= 0.90].sort_values(by=weight_column, ascending=False).reset_index(drop=True)
        
        if best_models.empty:
            # No single model has a weight >= 0.90
            douroucoulisay(
                'Several models in your set best explained the data.\n'
                'You can print douroucoulis.best_ranked() to identify the 95% best-ranked models and then\n'
                'use douroucoulis.model_averaging() to produce model-averaged parameter estimates.\n'
            )
        else:
            # Single best model identified
            best_model = best_models.loc[0]
            bestname = best_model['Model_Name']  # Extract model name
            douroucoulisay(
                f'{bestname} was identified as being the single best-fit model.\n'
                f'Print the model summary ({bestname}.summary()) and\n'
                'use the estimates to make inferences.\n'
            )
    def best_ranked(self):
        """
        Identifies models with cumulative weights up to 0.95 based on the selected criterion in the aictab DataFrame.
        Includes all models up to and including the first model that exceeds 0.95.

        Returns:
            pd.DataFrame: DataFrame containing models with cumulative weights up to 0.95 if any are found.
        """
        # Determine the correct column name for cumulative weight based on the selected criterion
        criterion_column = {
            'AIC': 'AIC_Cum_Weight',
            'AICc': 'AICc_Cum_Weight',
            'BIC': 'BIC_Cum_Weight'
        }.get(self.criterion_user, 'AIC_Cum_Weight')  # Default to 'AIC_Cum_Weight' if not found

        # Identify rows where cumulative weight <= 0.95
        cumulative_weights = self.aictab[criterion_column]
        self.best_95 = self.aictab.loc[cumulative_weights <= 0.95]

        # If there are no such rows, show feedback
        if self.best_95.empty:
            douroucoulisay(
                'A single model in your set best explained the data.\n'
                'You can print douroucoulis.best_fit() to\n'
                'identify the model and print the model.summary() for more details.'
            )
        else:
            # Include the first row that exceeds 0.95 if the DataFrame isn't already empty
            exceeding_row = self.aictab.loc[cumulative_weights > 0.95].head(1)
            if not exceeding_row.empty:
                self.best_95 = pd.concat([self.best_95, exceeding_row])

            # Return models with cumulative weight up to and including the first one exceeding 0.95
            return self.best_95

        
    def model_averaging(self):
        """
        Averages the parameter estimates of the best-ranked models with cumulative weights <= 0.95.
        Computes means and standard errors (SE) for shared parameters.

        Returns:
            pd.DataFrame: DataFrame with averaged parameter estimates and standard errors.
        """
        # Get the best-ranked models
        best_ranked_models = self.best_ranked()

        # Check if there are models to average
        if best_ranked_models.empty:
            douroucoulisay(
                'No models with cumulative weights <= 0.95 found for model averaging. '
                'Please ensure you have run best_ranked() with appropriate settings.'
            )
            return None

        # Extract model names from the best-ranked DataFrame
        best_model_names = best_ranked_models['Model_Name']  # Replace 'Model' with the actual column for model names

        # List to store parameter data for averaging
        parameter_data = []

        # Iterate through the model_set to extract parameters for the best-ranked models
        for idx, model_object in enumerate(self.model_set):
            # Dynamically infer model name based on index or class name
            model_name = f"Model_{idx+1}"  # You could also use model_object.__class__.__name__ for type-based names

            if model_name in best_model_names.values:
                # Print model params and BSE to inspect
                print(f"Inspecting model: {model_name}")
                print("Params:", model_object.params)  # Check the parameters
                print("BSE:", model_object.bse)  # Check the standard errors

                # Check if the model has params and bse attributes
                if hasattr(model_object, 'params') and hasattr(model_object, 'bse'):
                    # Extract parameters and their estimates
                    for param, estimate in model_object.params.items():  # Replace `.params` with how parameters are stored
                        if param in model_object.bse:  # Ensure standard error is available for each parameter
                            se = model_object.bse[param]  # Replace `.bse` with how standard errors are stored
                            
                            # Add the parameter data to the list
                            parameter_data.append({
                                'param': param,
                                'estimate': estimate,
                                'se': se
                            })
                        else:
                            print(f"Warning: No standard error available for parameter '{param}' in model '{model_name}'.")

        # Create a DataFrame for parameter data
        param_df = pd.DataFrame(parameter_data)

        if param_df.empty:
            print("Warning: No parameters were found to average.")
            return None

        # Calculate mean and SE for each parameter
        averaged_params = param_df.groupby('param').agg(
            average_estimate=('estimate', 'mean'),
            average_se=('se', 'mean')
        ).reset_index()

        return averaged_params


    def cross_val(self, X, y, regression):
        """
        Performs cross-validation for classification or regression models and displays accuracy results.

        Args:
            X (list of str): List of feature column names.
            y (str): Target column name.
            regression (bool): True if regression models, False if classification models.

        Returns:
            pd.DataFrame: DataFrame containing accuracy scores or mean absolute errors of the models.
        """
        douroucoulisay('Cross-validations are happening!\nMeanwhile, pet your pet!')

        self.regression = regression
        self.X = self.df.loc[:, X]
        self.y = self.df.loc[:, y]

        # Preprocessing the features (categorical -> Ordinal Encoding, numerical -> Scaling)
        self.enc = OrdinalEncoder()
        self.scaler = StandardScaler()

        # Separate categorical and numerical columns
        categorical_cols = self.X.select_dtypes(include=['object', 'category']).columns
        numerical_cols = self.X.select_dtypes(exclude=['object', 'category']).columns

        # Encode categorical columns and scale numerical columns
        if not categorical_cols.empty:
            self.X[categorical_cols] = self.enc.fit_transform(self.X[categorical_cols])
        if not numerical_cols.empty:
            self.X[numerical_cols] = self.scaler.fit_transform(self.X[numerical_cols])

        # Convert `self.y` to a Series (in case it's a DataFrame) to check its dtype
        if isinstance(self.y, pd.DataFrame):
            self.y = self.y.squeeze()  # Convert DataFrame to Series if necessary

        # Train-test split
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(self.X, self.y, test_size=0.2, random_state=0)

        if not self.regression:
            # Classification models
            classifiers = {
                'LogisticRegression': LogisticRegression(random_state=0, solver='lbfgs', max_iter=1000, C=1.0),
                'KNeighborsClassifier': KNeighborsClassifier(n_neighbors=5, metric='minkowski', p=2),
                'SVC': SVC(),
                'XGBoostClassifier': XGBClassifier(learning_rate=0.1, min_child_weight=1),
                'RandomForestClassifier': RandomForestClassifier(random_state=0),
                'GradientBoostingClassifier': GradientBoostingClassifier(random_state=0),
                'AdaBoostClassifier': AdaBoostClassifier(random_state=0),
                'GaussianNB': GaussianNB(),
                'DecisionTreeClassifier': DecisionTreeClassifier(random_state=0)
            }

            # If the target is categorical, encode it
            if self.y.dtype == 'object' or isinstance(self.y.iloc[0], str):
                self.y_train = self.enc.fit_transform(self.y_train.values.reshape(-1, 1)).ravel()
                self.y_test = self.enc.transform(self.y_test.values.reshape(-1, 1)).ravel()

            # Run classification models and calculate accuracy
            accuracies = {}
            for name, clf in classifiers.items():
                model = clf.fit(self.X_train, self.y_train)
                predictions = model.predict(self.X_test)
                accuracy = accuracy_score(self.y_test, predictions)
                accuracies[name] = accuracy
                print(f"{name}: {accuracy:.3f}")

            self.accuracy = pd.DataFrame({"Model": list(accuracies.keys()), "Accuracy Score": list(accuracies.values())})
            self.accuracy = self.accuracy.sort_values(by='Accuracy Score', ascending=False).reset_index(drop=True)
        
        else:
            # Regression models
            regressors = {
                'LinearRegression': LinearRegression(),
                'RidgeCV': RidgeCV(),
                'ElasticNetCV': ElasticNetCV(),
                'Lasso': Lasso(),
                'LassoCV': LassoCV(),
                'BayesianRidge': BayesianRidge(),
                'ExtraTreesRegressor': ExtraTreesRegressor(),
                'SVR': SVR(),
                'XGBoostRegressor': XGBRegressor(learning_rate=0.1, min_child_weight=1),
                'RandomForestRegressor': RandomForestRegressor(random_state=0),
                'GradientBoostingRegressor': GradientBoostingRegressor(random_state=0),
                'AdaBoostRegressor': AdaBoostRegressor(random_state=0),
                'DecisionTreeRegressor': DecisionTreeRegressor(random_state=0)
            }

            # Ensure the target variable remains numerical for regression
            self.y_train = self.y_train.astype(float)
            self.y_test = self.y_test.astype(float)

            # Run regression models and calculate MAE (Mean Absolute Error)
            mae_scores = {}
            for name, reg in regressors.items():
                model = reg.fit(self.X_train, self.y_train)
                predictions = model.predict(self.X_test)
                mae = mean_absolute_error(self.y_test, predictions)
                mae_scores[name] = mae
                print(f"{name}: {mae:.3f}")

            self.accuracy = pd.DataFrame({"Model": list(mae_scores.keys()), "MAE": list(mae_scores.values())})
            self.accuracy = self.accuracy.sort_values(by='MAE', ascending=True).reset_index(drop=True)

        return self.accuracy
        
    def hyper(self, model):
        """
        Tunes hyperparameters for a specified model and logs the results.

        Args:
            model (str): The name of the model to tune.

        Returns:
            The best model after hyperparameter tuning.
        """
        douroucoulisay('Tuning {} to increase accuracy!\nGo get some coffee/tea and call your mom.'.format(model))

        if model == 'ExtraTreesRegressor':
            etr = ExtraTreesRegressor(n_jobs=-1)
            parameters = {'n_estimators': [100, 200, 300], 'max_depth': range(1, 10, 1), 'max_features': range(10, 150, 10)}
            self.grid_search = GridSearchCV(estimator=etr, param_grid=parameters, verbose=1, n_jobs=-1)
            self.grid_search.fit(self.X, np.ravel(self.y))
            self.best_model = self.grid_search.best_estimator_
            self.score = self.grid_search.best_score_.round(2)
            douroucoulisay('The MAE for the {} with\ntuned hyperparameters (shown above) is {}.'.format(model, self.score))

        elif model == 'XGBRegressor':
            xgb1 = XGBRegressor()
            parameters = {
                'objective': ['reg:squarederror'],
                'learning_rate': [0.03, 0.05, 0.07],
                'max_depth': [5, 6, 7],
                'min_child_weight': [4],
                'subsample': [0.7],
                'colsample_bytree': [0.7],
                'n_estimators': [10, 50, 200, 500]
            }
            self.grid_search = GridSearchCV(xgb1, parameters, cv=2, n_jobs=-1, verbose=1)
            self.grid_search.fit(self.X, np.ravel(self.y))
            self.best_model = self.grid_search.best_estimator_
            self.score = self.grid_search.best_score_.round(2)
            douroucoulisay('The MAE for the {} with\ntuned hyperparameters (shown above) is {}.'.format(model, self.score))

        elif model == 'LinearRegression':
            douroucoulisay('{} has no hyperparameters to tune. If this is the most accurate model you can use to make predictions\nby providing new data to douroucoulisay.best_predictions()'.format(model))
            self.best_model = LinearRegression()

        elif model == 'RidgeCV':
            ridge = RidgeCV()
            ridge_params = {'alphas': [550, 580, 600, 620, 650]}
            self.grid_search = GridSearchCV(ridge, ridge_params, cv=2, n_jobs=-1, verbose=1)
            self.grid_search.fit(self.X, np.ravel(self.y))
            self.best_model = self.grid_search.best_estimator_
            self.score = self.grid_search.best_score_.round(2)
            douroucoulisay('The MAE for the {} with\ntuned hyperparameters (shown above) is {}.'.format(model, self.score))

        elif model == 'Lasso':
            lasso = Lasso()
            lasso_params = {'alpha': [0.005, 0.02, 0.03, 0.05, 0.06]}
            self.grid_search = GridSearchCV(lasso, lasso_params, cv=2, n_jobs=-1, verbose=1)
            self.grid_search.fit(self.X, np.ravel(self.y))
            self.best_model = self.grid_search.best_estimator_
            self.score = self.grid_search.best_score_.round(2)
            douroucoulisay('The MAE for the {} with\ntuned hyperparameters (shown above) is {}.'.format(model, self.score))

        elif model == 'ElasticNetCV':
            en = ElasticNetCV()
            en_params = {"alphas": [0.0001, 0.001, 0.01, 0.1, 1, 10, 100]}
            self.grid_search = GridSearchCV(en, en_params, cv=2, n_jobs=-1, verbose=1)
            self.grid_search.fit(self.X, np.ravel(self.y))
            self.best_model = self.grid_search.best_estimator_
            self.score = self.grid_search.best_score_.round(2)
            douroucoulisay('The MAE for the {} with\ntuned hyperparameters (shown above) is {}.'.format(model, self.score))

        elif model == 'SVR':
            svr = SVR()
            c_range = np.logspace(-0, 4, 8)
            gamma_range = np.logspace(-4, 0, 8)
            tuned_parameters = {'C': c_range, 'gamma': gamma_range}
            self.grid_search = GridSearchCV(svr, param_grid=tuned_parameters, scoring='explained_variance', cv=2, n_jobs=-1, verbose=1)
            self.grid_search.fit(self.X, np.ravel(self.y))
            self.best_model = self.grid_search.best_estimator_
            self.score = self.grid_search.best_score_.round(2)
            douroucoulisay('The MAE for the {} with\ntuned hyperparameters (shown above) is {}.'.format(model, self.score))

        elif model == 'LogisticRegression':
            logreg = LogisticRegression()
            grid_values = {'penalty': ['l1', 'l2'], 'C': [0.001, 0.01, 0.1, 1, 10, 100, 1000]}
            self.grid_search = GridSearchCV(logreg, param_grid=grid_values, cv=2, n_jobs=-1, verbose=1)
            self.grid_search.fit(self.X, np.ravel(self.y))
            self.best_model = self.grid_search.best_estimator_
            self.score = self.grid_search.best_score_.round(2)
            douroucoulisay('The accuracy score for the {} with\ntuned hyperparameters (shown above) is {}.'.format(model, self.score))

        elif model == 'SVC':
            svc = SVC()
            param_grid = {'C': [0.1, 1, 10, 100, 200], 'gamma': [1, 0.1, 0.01, 0.001]}
            self.grid_search = GridSearchCV(svc, param_grid=param_grid, cv=2, n_jobs=-1, verbose=1)
            self.grid_search.fit(self.X, np.ravel(self.y))
            self.best_model = self.grid_search.best_estimator_
            self.score = self.grid_search.best_score_.round(2)
            douroucoulisay('The accuracy score for the {} with\ntuned hyperparameters (shown above) is {}.'.format(model, self.score))

        elif model == 'RandomForestClassifier':
            rantree = RandomForestClassifier()
            param_grid = {'n_estimators': [10, 50, 100, 200, 500],
                        'criterion': ['gini', 'entropy'],
                        'min_samples_split': [2, 4],
                        'min_samples_leaf': [1, 2]}
            self.grid_search = GridSearchCV(rantree, param_grid=param_grid, cv=2, n_jobs=-1, verbose=1)
            self.grid_search.fit(self.X, np.ravel(self.y))
            self.best_model = self.grid_search.best_estimator_
            self.score = self.grid_search.best_score_.round(2)
            douroucoulisay('The accuracy score for the {} with\ntuned hyperparameters (shown above) is {}.'.format(model, self.score))

        elif model == 'KNeighborsClassifier':
            knn = KNeighborsClassifier()
            param_grid = {'n_neighbors': [3, 5, 7, 10], 'weights': ['uniform', 'distance']}
            self.grid_search = GridSearchCV(knn, param_grid=param_grid, cv=2, n_jobs=-1, verbose=1)
            self.grid_search.fit(self.X, np.ravel(self.y))
            self.best_model = self.grid_search.best_estimator_
            self.score = self.grid_search.best_score_.round(2)
            douroucoulisay('The accuracy score for the {} with\ntuned hyperparameters (shown above) is {}.'.format(model, self.score))

        elif model == 'MultinomialNB':
            mnb = MultinomialNB()
            param_grid = {'alpha': [0.1, 0.5, 1.0, 2.0]}
            self.grid_search = GridSearchCV(mnb, param_grid=param_grid, cv=2, n_jobs=-1, verbose=1)
            self.grid_search.fit(self.X, np.ravel(self.y))
            self.best_model = self.grid_search.best_estimator_
            self.score = self.grid_search.best_score_.round(2)
            douroucoulisay('The accuracy score for the {} with\ntuned hyperparameters (shown above) is {}.'.format(model, self.score))

        elif model == 'XGBClassifier':
            xgbc = XGBClassifier()
            parameters = {
                'objective': ['binary:logistic'],
                'learning_rate': [0.03, 0.05, 0.07],
                'max_depth': [5, 6, 7],
                'min_child_weight': [4],
                'subsample': [0.7],
                'colsample_bytree': [0.7],
                'n_estimators': [10, 50, 200, 500]
            }
            self.grid_search = GridSearchCV(xgbc, parameters, cv=2, n_jobs=-1, verbose=1)
            self.grid_search.fit(self.X, np.ravel(self.y))
            self.best_model = self.grid_search.best_estimator_
            self.score = self.grid_search.best_score_.round(2)
            douroucoulisay('The accuracy score for the {} with\ntuned hyperparameters (shown above) is {}.'.format(model, self.score))

        elif model == 'RandomForestRegressor':
            rfr = RandomForestRegressor()
            param_grid = {'n_estimators': [10, 50, 100, 200, 500],
                        'criterion': ['squared_error', 'absolute_error'],
                        'min_samples_split': [2, 4],
                        'min_samples_leaf': [1, 2]}
            self.grid_search = GridSearchCV(rfr, param_grid=param_grid, cv=2, n_jobs=-1, verbose=1)
            self.grid_search.fit(self.X, np.ravel(self.y))
            self.best_model = self.grid_search.best_estimator_
            self.score = self.grid_search.best_score_.round(2)
            douroucoulisay('The MAE for the {} with\ntuned hyperparameters (shown above) is {}.'.format(model, self.score))

        elif model == 'GradientBoostingClassifier':
            gbc = GradientBoostingClassifier()
            param_grid = {'n_estimators': [50, 100, 200], 'learning_rate': [0.01, 0.1, 1.0], 'max_depth': [3, 4, 5]}
            self.grid_search = GridSearchCV(gbc, param_grid=param_grid, cv=2, n_jobs=-1, verbose=1)
            self.grid_search.fit(self.X, np.ravel(self.y))
            self.best_model = self.grid_search.best_estimator_
            self.score = self.grid_search.best_score_.round(2)
            douroucoulisay('The accuracy score for the {} with\ntuned hyperparameters (shown above) is {}.'.format(model, self.score))

        elif model == 'GradientBoostingRegressor':
            gbr = GradientBoostingRegressor()
            param_grid = {'n_estimators': [50, 100, 200], 'learning_rate': [0.01, 0.1, 1.0], 'max_depth': [3, 4, 5]}
            self.grid_search = GridSearchCV(gbr, param_grid=param_grid, cv=2, n_jobs=-1, verbose=1)
            self.grid_search.fit(self.X, np.ravel(self.y))
            self.best_model = self.grid_search.best_estimator_
            self.score = self.grid_search.best_score_.round(2)
            douroucoulisay('The MAE for the {} with\ntuned hyperparameters (shown above) is {}.'.format(model, self.score))

        elif model == 'AdaBoostClassifier':
            ada = AdaBoostClassifier()
            param_grid = {'n_estimators': [50, 100, 200], 'learning_rate': [0.01, 0.1, 1.0]}
            self.grid_search = GridSearchCV(ada, param_grid=param_grid, cv=2, n_jobs=-1, verbose=1)
            self.grid_search.fit(self.X, np.ravel(self.y))
            self.best_model = self.grid_search.best_estimator_
            self.score = self.grid_search.best_score_.round(2)
            douroucoulisay('The accuracy score for the {} with\ntuned hyperparameters (shown above) is {}.'.format(model, self.score))

        elif model == 'AdaBoostRegressor':
            ada_reg = AdaBoostRegressor()
            param_grid = {'n_estimators': [50, 100, 200], 'learning_rate': [0.01, 0.1, 1.0]}
            self.grid_search = GridSearchCV(ada_reg, param_grid=param_grid, cv=2, n_jobs=-1, verbose=1)
            self.grid_search.fit(self.X, np.ravel(self.y))
            self.best_model = self.grid_search.best_estimator_
            self.score = self.grid_search.best_score_.round(2)
            douroucoulisay('The MAE for the {} with\ntuned hyperparameters (shown above) is {}.'.format(model, self.score))

        elif model == 'DecisionTreeClassifier':
            dtc = DecisionTreeClassifier()
            param_grid = {'max_depth': [None, 10, 20, 30], 'min_samples_split': [2, 5, 10], 'criterion': ['gini', 'entropy']}
            self.grid_search = GridSearchCV(dtc, param_grid=param_grid, cv=2, n_jobs=-1, verbose=1)
            self.grid_search.fit(self.X, np.ravel(self.y))
            self.best_model = self.grid_search.best_estimator_
            self.score = self.grid_search.best_score_.round(2)
            douroucoulisay('The accuracy score for the {} with\ntuned hyperparameters (shown above) is {}.'.format(model, self.score))

        elif model == 'DecisionTreeRegressor':
            dtr = DecisionTreeRegressor()
            param_grid = {'max_depth': [None, 10, 20, 30], 'min_samples_split': [2, 5, 10], 'criterion': ['squared_error', 'absolute_error']}
            self.grid_search = GridSearchCV(dtr, param_grid=param_grid, cv=2, n_jobs=-1, verbose=1)
            self.grid_search.fit(self.X, np.ravel(self.y))
            self.best_model = self.grid_search.best_estimator_
            self.score = self.grid_search.best_score_.round(2)
            douroucoulisay('The MAE for the {} with\ntuned hyperparameters (shown above) is {}.'.format(model, self.score))

        else:
            douroucoulisay('Model {} is not recognized or is not supported for hyperparameter tuning.'.format(model))
            self.best_model = None

        return self.best_model
