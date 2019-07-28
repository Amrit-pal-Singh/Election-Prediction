# Election prediction

## About the files

### Data
1. statewise.txt -> State wise exit/opinion polls of 2019.
2. statewise2014.txt -> State wise exit/opinion poll of 2014.
3. temp_2009 -> Nation wise exit polls of 2009.
4. temp_2014 -> Nation wise exit polls of 2014.
5. temp_2019 -> Nation wise exit polls of 2019.
6. actual_result.txt -> State wise actual result of 2014.

### Code

1. election_state.py -> This is to predict the number of seats that NDA UPA or OTHERS will get using the state wise data of polls
2. election.py -> This predict the number of seats that NDA UPA or OTHERS will get using the nation wise polls.



## How to run

In the collected data of state wise seats we have that only few polls are given and not all.
So we first run `election_state.py` and then run the `election.py` to fine tune it with few of the polls
who didn't contibute in state wise result.

Commands
```bash
python election_state.py
```
After this command run

```bash
python election.py
```

## Approch
We combine different poles using weighted average. 
In normal average, each data contribute equally to the result, 
but taking this weighted average approach we have that the polls with less bias and more accuracy in previous year will have more weight or have more effect on the output.
To calculate the weight of every poll we use the previous year result. 
We take the absolute difference of its predicted and actual result, then we take the inverse square of it. This is the weight of that poll. 
In case of state wise approch we first take the average of difference of that poll's prediction and actual result in various states, 
and then take the inverse square.
Then using these weights and the predicted values of polls of this time we take the weighted average and we get the result.









