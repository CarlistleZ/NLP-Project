# Speech Tagger - Machine Learning - NLP

The project objective is to build taggers for the ATIS (Air Travel Information System) domain. We use Python and TensorFlow to build the ML models.

Two different taggers have to be implemented : the first one should be based on CRF (Conditional Random Fields), the second tagger uses a LSTM classification algorithm.

## Provided data
2 files are provided at the beginning of the project:

1. atis.train is a collection of about 5000 dialog utterances whose aim to train and tune your systems ;

2. evaluation.pl is the script to compute the performances of your systems, it provides concepts error statistics as well as the global statictics (measure to tune is global FB1).

## Output

We provide the predictions of the two systems applied on the test corpus. The test corpus look like the training corpus except that the last column of the ground truth is missing, thus it contains only one column : the words. We provide predictions files that contains the tag predicted by your system, these file must contains the same number of lines as the test file. the following table illustrates the two files.

```
test file - prediction file 

I - O
want - O 
to - O 
go - O 
to - O
Chicago - arrival.city_name 
from - O
Atlanta - departure.city_name
The - O
... - ...
```

## Input transformation

For a system that destructure sequences : one training sample for one position in a sequence, you will need to create as many training samples as words (nb utterances*average length of an utterance). The observation have to be encoded as a 2D numpy scalar matrix (nbsamples*sizeofrepresentation). In atis.train you will have 52170 samples. If you choose to use as observations words inside a win- dows [−1, 1] (3 words : current word, previous word and next word), and if you represent each word by an embedding of size 100, then the representation will be of size 300.
The predictions (groundtruth) needed to train the network have to be encoded as a vector of tag index.

## Deep learning tagger

The observation have to be encoded as a 3D numpy scalar matrix (nbsamples*sizeof longuestse- quence*representationofthecurrentobservation). In ATIS you would have :
1. nbsamples is 4978 (number of utterances)
2. the longest sequence is size 86 (you must pad the shorter sequences with 0)
3. the representation is the vector coding the current observation in the sequence (in general the word itself at least)
* you can create your own representation vector encoding the information you want and use it as third dimension (use zeros vector to pad)
* if you plan to use an embedding layer (to compute a word embedding together with the full network), you can just use a 2D numpy matrix (nbsamples*sizeof longuestsequence) fulled with the words (coded as an integer), use integer 0 to pad : the embedding layer will produce the third dimension.

## Produced Results
```
i	O
would	O
like	O
to	O
find	O
a	O
flight	O
from	O
city	B-fromloc.city_name
to	O
las-vegas	B-fromloc.city_name
that	O
makes	O
a	O
stop	O
statecode	O
st.-louis	B-toloc.city_name

on	O
april	B-depart_date.month_name
first	B-depart_date.day_number
i	O
need	O
a	O
ticket	O
from	O
city	B-fromloc.city_name
to	O
san-jose	B-toloc.city_name
departing	O
before	B-depart_time.time_relative
7am	B-depart_time.time

on	O
april	B-depart_date.month_name
first	B-depart_date.day_number
i	O
need	O
a	O
flight	O
going	O
from	O
city	B-fromloc.city_name
to	O
san-diego	B-toloc.city_name

i	O
would	O
like	O
a	O
flight	O
traveling	O
one-way	B-round_trip
from	O
city	B-fromloc.city_name
to	O
san-diego	B-toloc.city_name
on	O
april	B-depart_date.month_name
first	B-depart_date.day_number

i	O
would	O
like	O
a	O
flight	O
from	O
city	B-fromloc.city_name
to	O
salt-lake-city	B-toloc.city_name
for	O
april	B-depart_date.month_name
first	B-depart_date.day_number
on	O
delta-airlines	B-airline_name

i	O
need	O
a	O
flight	O
from	O
toronto	B-fromloc.city_name
to	O
city	B-toloc.city_name
one-way	B-round_trip
leaving	O
wednesday	B-depart_date.day_name
evening	B-depart_time.period_of_day
statecode	O
thursday	B-depart_date.day_name
morning	B-depart_time.period_of_day

monday	B-depart_date.day_name
morning	B-depart_time.period_of_day
i	O
would	O
like	O
to	O
fly	O
from	O
city	B-fromloc.city_name
to	O
city	B-fromloc.city_name

on	O
wednesday	B-depart_date.day_name
april	B-depart_date.month_name
sixth	B-depart_date.day_number
i	O
would	O
like	O
to	O
fly	O
from	O
long-beach	B-fromloc.city_name
to	O
city	B-toloc.city_name
after	B-depart_time.time_relative
3pm	B-depart_time.time

after	B-depart_time.time_relative
12pm	B-depart_time.time
on	O
wednesday	B-depart_date.day_name
april	B-depart_date.month_name
sixth	B-depart_date.day_number
i	O
would	O
like	O
to	O
fly	O
from	O
long-beach	B-fromloc.city_name
to	O
city	B-toloc.city_name
```