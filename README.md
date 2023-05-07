## Music recommendation comparison
Brief introduction:
Bands are recommended to users based on the number of playback times. 
The number of songs played by users represents the user's liking for the band
Model algorithms of User_CF,Item_CF,LFM,BPR and ALS_WR were used for solving and comparing
Measures adopted: Accuracy, recall, coverage, diversity
- Data set (two copies of data):
1. lastfm-360K(small_data.csv) Take the 10000 most active users and 1000 most popular songs
2. Million Song Datasets -- u.data,lable encoded small data
#### 1.User-based collaborative filtering
      The similarity of users is calculated. If two users have behaviors on unpopular items, the two users should have high similarity
#### 2.Item-based collaborative filtering
      To calculate the similarity of items, active users should contribute less to the similarity of items than inactive users
#### 3.Lingo model (LFM)
    Connect users and items through implicit features
      Parameter: The number of implicit features
        Learning rate alph
        The regularization term coefficient lamba
#### 4.BPR: Bayesian Personalized Ranking
    Maximizing a posteriori probability based on Bayesian theory under prior knowledge, realizing training multiple matrices from a user-item matrix,
    And each matrix represents a user's project preferences to obtain the partial order relationship of multiple items for the user to sort the recommendation system

#### 5.ALS_WR：ALS with Weighted--Regularization
        Users do not give clear feedback on their preference for commodities, or score directly. Users' preference for commodities can be inferred through certain behaviors of users
        ALS_WR is measured by confidence
##Result

Result: 
u.data

|menu|user_CF|item_CF|LFM|BPR|ALS_WR|
|:---|:---|:---|:---|:---|:---|
|precision|0.297028|0.296454|0.235244|0.2545068928950159|0.2706256627783669
|recall|0.139218|0.138919|0.110260|0.1234694927461673|0.1312892272867579
|coverage|0.317905|0.230207|0.358709|0.3393829401088929|0.39503932244404116
|popularity|5.245796|5.359162|5.235433|5.121795795790667|5.154377399784349
|s|1.49998675|1.5061855|1.4849115|1.459788779|1.487832902

Result: 
small_data.csv 
bpr:auc mean = 0.86 std = 0.11  
als_wr:auc mean =0.77 std = 0.22     

|menu|user_CF|item_CF|LFM|BPR|ALS_WR|
|:---|:---|:---|:---|:---|:---|
|precision|0.108502|0.115724|0.046713|0.10419407894736842|0.08890830592105263
|recall|0.199219|0.210743|0.085783|0.21724500075015538|0.18537411320916475
|coverage|0.997000|0.813000|0.452000|0.731|0.999
|popularity|5.628611|5.997764|6.883521|6.05680689158381|5.833611415438899
|s|1.733333|1.78430775|1.86700425|1.77730975|1.77672335



        
        

