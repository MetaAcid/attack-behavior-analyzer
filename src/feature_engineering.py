def prepare_features(df):
    return df[[
        "requests",
        "failed_logins",
        "unique_paths",
        "time_between_requests"
    ]]