Info:
---------------------
Zipcode distance calculator. Saw a Postcodes repo in jedberg's for Canadian post codes and wanted to try building my own.

Haversine formula from Wayne Dick:
[http://www.platoscave.net/blog/2009/oct/5/calculate-distance-latitude-longitude-python/](http://www.platoscave.net/blog/2009/oct/5/calculate-distance-latitude-longitude-python/)

3963.1676 mile radius of earth from google.

Data Info:
---------------------
Zip code database acquired from [http://www.boutell.com/zipcodes/](http://www.boutell.com/zipcodes/) which is covered under a Creative Commons Attribution-ShareAlike license by CivicSpace Labs. Full text of the original readme for the data set is at the end of this readme. The data was converted to a sqlite 'zipcodes.db' database & the table create statement is in the .sql file.


CivicSpace US ZIP Code Database:
---------------------
 written by Schuyler Erle <schuyler@geocoder.us>
 5 August 2004 

 The ZIP code database contained in 'zipcode.csv' contains 43204 ZIP codes for the continental United States, Alaska, Hawaii, Puerto Rico, and American Samoa. The database is in comma separated value format, with columns for ZIP code, city, state, latitude, longitude, timezone (offset from GMT), and daylight savings time flag (1 if DST is observed in this ZIP code and 0 if not). 

 This database was composed using ZIP code gazetteers from the US Census Bureau from 1999 and 2000, augmented with additional ZIP code information The database is believed to contain over 98% of the ZIP Codes in current use in the United States. The remaining ZIP Codes absent from this database are entirely PO Box or Firm ZIP codes added in the last five years, which are no longer published by the Census Bureau, but in any event serve a very small minority of the population (probably on the order of .1% or less). Although every attempt has been made to filter them out, this data set may contain up to .5% false positives, that is, ZIP codes that do not exist or are no longer in use but are included due to erroneous data sources. The latitude and longitude given for each ZIP code is typically (though not always) the geographic centroid of the ZIP code; in any event, the location given can generally be expected to lie somewhere within the ZIP code's "boundaries". 

 The database andthis README are copyright 2004 CivicSpace Labs, Inc., and are published under a Creative Commons Attribution-ShareAlike license, which requires that all updates must be released under the same license. See http://creativecommons.org/licenses/by-sa/2.0/ for more details. Please contact schuyler@geocoder.us if you are interested in receiving updates to this database as they become available.