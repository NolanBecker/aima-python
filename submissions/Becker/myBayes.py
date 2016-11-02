from submissions.Becker import medal_of_honor

class DataFrame:
    data = []
    feature_names = []
    target = []
    target_names = []

dataframe = DataFrame()
awardees = medal_of_honor.get_awardees(test=True)