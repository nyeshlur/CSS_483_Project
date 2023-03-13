# CSS_483_Project

This project is a continuation of work done by Yangxiao Wang and Dr. Wooyoung Kim at the University of Washington Bothell.

Wang, Y., & Kim, W. (2020). Identification of essential genes with NemoProfile and various machine learning models. Bioinformatics Research and Applications, 319–326. https://doi.org/10.1007/978-3-030-57821-3_30 

1.	To run PreProccesing/PreProcess.py you will need label.txt and networkdata.txt. label.txt contains the list of genes which are either labeled as essential (E) or not essential (N). networkdata.txt contains the protein-protein interaction network from the STRING database. The output of PreProcess.py is NetworkForMotif.txt this is the undirected graph which will be used to determine network motif profile.
2.	 Go to https://bioresearch.uwb.edu/biores/nemo/ and upload the NetworkForMotif.txt file. Parameters are motif size 4, undirected graph, random graph size of 10, and NemoProfile. The output is the subProfile.txt file which contains the netowrk motif profile. Null values in subProfile.txt should be replaced with zeros.
3.	Run NemoProfile/normalize.py to get data.mat which contains the network motif profile as well as the profile with feature vectors normalized using standardization and min-max normalization.
4.	Go to Models/Models.ipynb and run the notebook. This will output the results of the models (CNN, KNN, Logisitic Regression, Decision Tree, and SVM) and results of InterpretML.