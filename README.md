
[![GitHub pull-requests](https://img.shields.io/github/issues-pr/Naereen/StrapDown.js.svg)](https://GitHub.com/Naereen/StrapDown.js/pull/)
[![Open Source Love svg1](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)

# 2AF_FRAUD_DETECTION
REST API for FRAUD DETECTION

8 steps for Finding Fraud Rings Using Graph Technology

The steps below are just one example. Your approach will vary depending on your goals and the data itself.

Use graph queries to uncover a suspicious pattern, such as multiple users coming from the same IP address. (Some of the techniques used in the first-party fraud example from blog 3 in this series will also apply.)
Use Community Detection algorithms to identify strongly connected communities engaged in known fraud across various accounts using email addresses, phone numbers, authorized users and previously flagged activity.
Use the Louvain Modularity graph algorithm to examine whether hierarchies exist among these communities. Set thresholds to separate petty thieves from fraud rings so that investigators prioritize their efforts.
Use a Centrality algorithm like PageRank to uncover influential individuals and to identify high frequency paths.
After verifying the pattern of one fraud ring, use a Similarity algorithm such as Jaccard to identify other potential fraud participants and rings across your data.
Once the approaches to find fraud rings have been validated by investigators, and a labeled and scored dataset has been created, you can use these graph-based features in a machine learning pipeline.
Extract the calculated node and relationship properties – graph features from the previous step – into your ML environment (e.g., into a Python notebook). Join those properties with any other relevant tabular data. Use variable selection and model-building techniques to pinpoint the most important features and use them to predict future fraudulent activities or entities.
Once you’re satisfied with your results, move your model into production. Write back any relevant findings to the Neo4j Graph Database to support further exploration.
