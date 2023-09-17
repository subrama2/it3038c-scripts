#!/bin/bash
# This script downloads covid data and displays it


DATA=$(curl https://api.covidtracking.com/v1/us/current.json)
POSITIVE=$(echo $DATA | jq '.[0].positive')
NEGATIVE=$(echo $DATA | jq '.[0].negative')
DEATH=$(echo $DATA | jq '.[0].death')
HOSPITALIZED=$(echo $DATA | jq '.[0].hospitalizedCumulative')
TOTALTESTRESULTS=$(echo $DATA | jq '.[0].totalTestResults')

TODAY=$(date)
echo "On $TODAY, there were $POSITIVE positive COVID cases, $NEGATIVE negative COVID tests, $DEATH deaths and $HOSPITALIZED hospitalized and total of $TOTALTESTRESULTS tests results in total."
