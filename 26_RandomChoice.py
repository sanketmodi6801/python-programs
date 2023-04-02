import random

letsDo = ["Introduction to Cyber Security", " Machine Learning/Deep Learning in Cyber security",
          " Machine Learning/ Deep Learning for Anomaly Detection",
          "Machine Learning/ Deep Learning for Hybrid Detection",
          "Machine Learning/ Deep Learning for Scam Detection",
          " Machine Learning for Profiling Network Traffic",
          "Learning Methods for Misuse/Signature Detection",
          "Security of Machine Learning Systems", " Knowledge Representation of Network Semantics",
          "Artificial Intelligence Methods to Network Attack Detection",
          "Machine Learning for Network Intrusion Detection",
          "Network Data Collection, Fusion, Mining and Analytics for Cyber Security",
          "Machine Learning/Deep Learning Techniques for Privacy-Preserving",
          "Neural Language Modeling for Cyber security",
          "Data-Driven Android Malware Intelligence",
          "Interpretable Encrypted Searchable Neural Networks",
          "Deception in the Cyber-World",
          "Cyber Security and Protection of ICS Systems",
          "Network Information Security Technology Using Big data",
          "Emerging Challenges in Cyber security",
          "Case Studies related to Cyber security"]

i = 0
while i < 10:
    List = [random.choice(letsDo)]
    print(List)
    i = i+1
