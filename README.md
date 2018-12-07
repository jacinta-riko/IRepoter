# IRepoter
Corruption is a huge bane to Africa’s development. African countries must develop novel and localised solutions that will curb this menace, hence the birth of iReporter. iReporter enables any/every citizen to bring any form of corruption to the notice of appropriate authorities and the general public. Users can also report on things that needs government intervention.


[![Build Status](https://travis-ci.com/jacinta-riko/IRepoter.svg?branch=ft-update-comment-location-162363557)](https://travis-ci.com/jacinta-riko/IRepoter)

[![Coverage Status](https://coveralls.io/repos/github/jacinta-riko/IRepoter/badge.svg?branch=ft-update-comment-location-162363557)](https://coveralls.io/github/jacinta-riko/IRepoter?branch=ft-update-comment-location-162363557)

[![Maintainability](https://api.codeclimate.com/v1/badges/2dfe60023dea8cf10443/maintainability)](https://codeclimate.com/github/jacinta-riko/IRepoter/maintainability)

### Postman Link
https://web.postman.co/collections/5993390-de6397dc-79f8-4189-aee0-e0533b6cce47?workspace=4abfb612-6956-4d69-8369-22cc4e921711

## Heroku link
https://young-tundra-12508.herokuapp.com/api/v1/red-flags

## Prerequisites
Things you need to run the appliaction;
- Requirements
- Virtual environment

python3 -m env env
pip intall -r requirements.txt

## installing
Clone my repository;

git clone https://github.com/jacinta-riko/IRepoter


## Running the tests
Run this command on terminal:
pytest

## Endpoints
You can run the urls on postman
<table>
<th>Method</th>
<th>URL</th>
<th>Description</th>
<tr>
<td>POST</td>
<td>api/v1/red-flags</td>
<td>Create red flag</td>
</tr>
<tr>
<td>GET</td>
<td>api/v1/red-flags</td>
<td>View red flags</td>
</tr>
<tr>
<td>GET</td>
<td>api/v1/red-flags/1</td>
<td>View specific red flag</td>
</tr>
<tr>
<td>DELETE</td>
<td>api/v1/red-flags/1</td>
<td>Delete specific red flag</td>
</tr>
<tr>
<td>PATCH</td>
<td>v1/red-flags/1/comment</td>
<td>Edit comment of a red flag</td>
</tr>
<tr>
<td>PATCH</td>
<td>v1/red-flags/1/location</td>
<td>Edit location of a red flag</td>
</tr>
</table>

