import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn import metrics
from fairlearn.metrics import MetricFrame, selection_rate

class InfluentialInstanceAnalyzer:
    def __init__(self, model, sensitive_features, deletion_percentage=10):
        self.model = model
        self.sensitive_features = sensitive_features
        self.deletion_percentage = deletion_percentage

    def fit(self, X_train, y_train, X_test, y_test):
        self.model.fit(X_train, y_train)
        self.X, self.y = X_train, pd.Series(y_train, index=X_train.index)

        self.y_pred = self.model.predict(X_test)
        self.accuracy = metrics.accuracy_score(y_test, self.y_pred)
        self.fairness_overall, self.fairness_by_group = self.compute_fairness(X_test, y_test, self.y_pred)

        self.evaluate_model(y_test, self.y_pred, "Before Removal")
        self.print_fairness(self.fairness_overall, self.fairness_by_group, "Before Removal")

    def compute_fairness(self, X, y, y_pred):
        metric_frame = MetricFrame(
            metrics={"accuracy": metrics.accuracy_score, "selection_rate": selection_rate},
            y_true=y, y_pred=y_pred, sensitive_features=X[self.sensitive_features]
        )
        return metric_frame.overall, metric_frame.by_group

    def find_influential_instances(self):
        acc_changes = []
        fairness_changes = []
        indices = list(self.X.index)

        for i in indices:
            X_reduced = self.X.drop(i)
            y_reduced = self.y.drop(i)

            model_clone = self.model.__class__(**self.model.get_params())
            model_clone.fit(X_reduced, y_reduced)
            y_pred_reduced = model_clone.predict(X_reduced)

            acc_reduced = metrics.accuracy_score(y_reduced, y_pred_reduced)
            fairness_reduced, _ = self.compute_fairness(X_reduced, y_reduced, y_pred_reduced)

            acc_changes.append(abs(self.accuracy - acc_reduced))
            fairness_changes.append(abs(fairness_reduced['accuracy'] - self.fairness_overall['accuracy']))

        influence_scores = np.array(acc_changes) + np.array(fairness_changes)
        num_to_remove = min(int((self.deletion_percentage / 100) * len(self.X)), len(indices))
        influential_indices = np.array(indices)[np.argsort(influence_scores)[-num_to_remove:]].tolist()

        return influential_indices, influence_scores, acc_changes, fairness_changes

    @staticmethod
    def evaluate_model(y_true, y_pred, stage="Before Removal"):
        accuracy = metrics.accuracy_score(y_true, y_pred)
        print(f"{stage} Accuracy: {accuracy:.4f}")

    @staticmethod
    def print_fairness(overall_fairness, fairness_by_group, stage="Before Removal"):
        print(f"{stage} Fairness Metrics:")
        print("Overall Fairness:")
        print(overall_fairness)
        print("Fairness by Group:")
        print(fairness_by_group)
        print("-----------------------------------")

    def run_analysis(self, showGraph=False):
        influential_indices, influence_scores, acc_changes, fairness_changes = self.find_influential_instances()

        if showGraph:
            plt.figure(figsize=(10, 5))
            sns.barplot(x=influential_indices, y=influence_scores[np.argsort(influence_scores)[-len(influential_indices):]], palette="viridis")
            plt.ylabel("Influence Score")
            plt.title("Most Influential Instances")
            plt.xticks(rotation=90)
            plt.show()

        return influential_indices, influence_scores, acc_changes, fairness_changes
